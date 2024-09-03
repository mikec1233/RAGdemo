import os
import time
import uuid
from pydantic import BaseModel, Field
from typing import List, Optional
import mysql.connector
from dotenv import load_dotenv

load_dotenv()

DB_CONFIG = {
    "host": "localhost",
    "user": os.environ.get("DB_USER"),
    "password": os.environ.get("DB_PASSWORD"),
    "database": os.environ.get("DB_NAME"),
    
    
    # 'ssl_ca': os.environ.get("CA"),
    # 'ssl_cert': os.environ.get("CLIENT_CERT"),
    # 'ssl_key': os.environ.get("CLIENT_KEY") 
}

TABLE_NAME = os.environ.get("TABLE_NAME", "queries")
TTL_EXPIRE_MONTHS = 6  # Only keep queries for 6 months.
TTL_EXPIRE_TIMESTAMP = 60 * 60 * 24 * 30 * TTL_EXPIRE_MONTHS

class DBQueryModel(BaseModel):
    query_id: str = Field(default_factory=lambda: uuid.uuid4().hex)
    user_id: str 
    create_time: int = Field(default_factory=lambda: int(time.time()))
    ttl: int = Field(default_factory=lambda: int(time.time() + TTL_EXPIRE_TIMESTAMP))
    query_text: str
    answer_text: Optional[str] = None
    sources: List[str] = Field(default_factory=list)
    is_complete: bool = False

    @staticmethod
    def get_connection():
        return mysql.connector.connect(**DB_CONFIG)

    def put_item(self):
        conn = self.get_connection()
        cursor = conn.cursor()
        sql = f"""
            INSERT INTO {TABLE_NAME} (query_id, create_time, query_text, answer_text, sources, is_complete, user_id)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            ON DUPLICATE KEY UPDATE
            create_time = VALUES(create_time),
            query_text = VALUES(query_text),
            answer_text = VALUES(answer_text),
            sources = VALUES(sources),
            is_complete = VALUES(is_complete),
            user_id = VALUES(user_id)
        """
        cursor.execute(sql, (self.query_id, self.create_time, self.query_text, self.answer_text, ','.join(self.sources), self.is_complete, self.user_id))
        conn.commit()
        cursor.close()
        conn.close()

    @classmethod
    def get_item(cls, query_id: str) -> Optional["DBQueryModel"]:
        conn = cls.get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute(f"SELECT * FROM {TABLE_NAME} WHERE query_id = %s", (query_id,))
        result = cursor.fetchone()
        cursor.close()
        conn.close()
        if result:
            # Convert comma-separated sources back to list
            result['sources'] = result['sources'].split(',') if result['sources'] else []
            return cls(**result)
        return None
    
    @classmethod
    def list_queries_by_user(cls, user_id: str, count: int = 5) -> List["DBQueryModel"]:
        conn = cls.get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute(
            f"""
            SELECT * FROM {TABLE_NAME} WHERE user_id = %s
            ORDER BY create_time DESC
            LIMIT %s
            """,
            (user_id, count)
        )
        results = cursor.fetchall()
        cursor.close()
        conn.close()

        #convert response to a list of queries
        queries = []
        for result in results:
            result['sources'] = result['sources'].split(',') if result['sources'] else []
            queries.append(cls(**result))
        return queries
    
    def as_dict(self):
        return {
            "query_id": self.query_id,
            "user_id": self.user_id,
            "create_time": self.create_time,
            "query_text": self.query_text,
            "answer_text": self.answer_text,
            "sources": ','.join(self.sources),
            "is_complete": self.is_complete
        }

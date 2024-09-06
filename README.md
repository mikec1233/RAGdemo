# Demo for Atorus Research to introduce RAG for OpenVal

## 1. Clone repo

```bash
git clone https://github.com/mikec1233/RAGdemo.git
cd RAGdemo
```

## 2. Set up backend
```python
python3 -m venv .venv
source .venv/bin/activate
pip install -r backend/requirements.txt
```

## 3. Set up Chroma DB
```bash
mkdir backend/data
cd backend/data
```
upload a PDF to data directory
cd back to RAGdemo and create a .gitignore file
add the following:
```
.env
.venv
__pycache__
db_test.py
backend/data/
backend/tests/
frontend/rag_frontend/src/api-client/
```
create a .env file
add the following:
```
DATA_PATH=path/to/data/
CHROMA_PATH=path/to/data/Chroma
OPENAI_API_KEY="yourkey"
DB_USER="youruser"
DB_PASSWORD="yourpass"
DB_NAME="yourdb"
```
**You must ensure that .env is in your .gitignore. DO NOT push any key to github.**
     
You can now run the following:
```python
      python -m backend.src.app_logic.store_dox
```
Ensure that your data/Chroma/ directory contains data

## 4. Set up mysql database
In our current stage we are just using a local instance of mysql for testing purposes.
Follow a tutorial to set up mysql. Here is a tutorial for [mac](https://www.youtube.com/watch?v=iQjmY2Q5n3o&t=245s)
Head into your running mysql server and create a new database. Put the name of that database int your .env file.
```sql
CREATE DATABASE your_database_name;
USE your_database_name;
```
Next, create a table called queries:
```sql
   CREATE TABLE queries (
      query_id VARCHAR(255) PRIMARY KEY,
      user_id VARCHAR(255),
      create_time INT,
      ttl INT,
      query_text TEXT,
      answer_text TEXT,
      sources TEXT,
      is_complete BOOLEAN
   );
```

In RAGdemo run the command
```python
python -m backend.src.api.api_handler
```
Verify that the api up at localhost:8000
You can see the api documentation and run calls at localhost:8000/docs
The backend should be up and running

## 5. Set up frontend
```bash
cd frontend/rag_frontend
npm install
```
### To generate our API client based on our backend specification
1. Start the backend
2. Run the command
```bash
npm run generate-api-client
```
3. This will automatically configure our API client, which we will use to call our backend API from client side.
Start the frontend with
```bash
npm run start
```

   


   
   
   

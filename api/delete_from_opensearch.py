import requests
import os
from dotenv import load_dotenv
from requests.auth import HTTPBasicAuth

# Load environment variables from .env file
load_dotenv()

# Get OpenSearch connection details from environment variables
host = "http://localhost:9200"  # Adjust to your OpenSearch host if necessary
index_name = "docdemo"
username = os.getenv("OPENSEARCH_USERNAME")
password = os.getenv("OPENSEARCH_PASSWORD")

# Use POST for _delete_by_query to delete all documents in the specified index
response = requests.post(f"{host}/{index_name}/_delete_by_query",
                         json={"query": {"match_all": {}}},
                         auth=HTTPBasicAuth(username, password))

if response.status_code == 200:
    print("All documents deleted successfully.")
else:
    print(f"Failed to delete documents. Status code: {response.status_code}")
    print(response.json())

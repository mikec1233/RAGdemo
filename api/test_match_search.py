import requests
from requests.auth import HTTPBasicAuth
import os
import json

# Assuming the .env file is loaded and OpenSearch credentials are available
opensearch_url = "http://localhost:9200/docdemo/_search"
query = {
    "query": {
        "match": {
            "content": "ART"
        }
    }
}

response = requests.get(
    opensearch_url,
    json=query,
    auth=HTTPBasicAuth(
        os.getenv("OPENSEARCH_USERNAME"), 
        os.getenv("OPENSEARCH_PASSWORD")
    )
)

# Save JSON response to a text file
output_file_path = "opensearch_query_response.txt"
with open(output_file_path, "w") as file:
    json.dump(response.json(), file, indent=4)

print(f"Response saved to {output_file_path}")
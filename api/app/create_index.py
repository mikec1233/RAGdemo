from opensearchpy import OpenSearch

# Define OpenSearch client connection
client = OpenSearch(
    hosts=[{'host': 'localhost', 'port': 9200}],  # Use 'localhost' since OpenSearch is running locally
    http_auth=('admin', 'admin'),  # Replace with your actual credentials if needed
    use_ssl=False,
    verify_certs=False,
)

# Define the index name
INDEX_NAME = "my-documents-index"

# Create an index with basic settings
def create_index():
    index_body = {
        "settings": {
            "index": {
                "number_of_shards": 1,
                "number_of_replicas": 1
            }
        },
        "mappings": {
            "properties": {
                "title": {"type": "text"},
                "content": {"type": "text"},
                "timestamp": {"type": "date"}
            }
        }
    }

    # Check if the index already exists
    if not client.indices.exists(INDEX_NAME):
        response = client.indices.create(index=INDEX_NAME, body=index_body)
        print(f"Index created: {response}")
    else:
        print(f"Index {INDEX_NAME} already exists.")

if __name__ == "__main__":
    create_index()

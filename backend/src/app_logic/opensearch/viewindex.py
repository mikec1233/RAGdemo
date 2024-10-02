from opensearchpy import OpenSearch

# Set up the OpenSearch client
client = OpenSearch(
    hosts=[{"host": "localhost", "port": 9200}],
    http_compress=True
)

# Query the index and retrieve data
index_name = "gpt-index-demo"
response = client.search(index=index_name, body={"query": {"match_all": {}}}, size=10)

# Print the results
for hit in response["hits"]["hits"]:
    print(f"ID: {hit['_id']}")
    print(f"Source: {hit['_source']}")
    print("---")

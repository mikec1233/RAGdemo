from opensearchpy import OpenSearch

# Define the connection parameters
host = 'localhost'  # Change this to your OpenSearch container's host
port = 9200         # Default OpenSearch port
auth = ('cscrams123', 'cscrams123')  # Default credentials for OpenSearch

# Create a client instance
client = OpenSearch(
    hosts=[{'host': host, 'port': port}],
    http_auth=auth,
    use_ssl=False,
    verify_certs=False,
    ssl_show_warn=False
)

# Verify the connection by getting the cluster health
response = client.cluster.health()
print(response)
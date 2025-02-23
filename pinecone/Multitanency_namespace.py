from pinecone import Pinecone

# Initialize the Pinecone client with your API key
pc = Pinecone(api_key="pcsk_3ZCPFh_9+++++++XGYe")

# Connect to your Pinecone index
index = pc.Index('datacamp-index')

# Example vector sets
vector_set1 = [
    {"id": "1", "values": [0.1] * 1536},
    {"id": "2", "values": [0.2] * 1536},
    # Add more vectors as needed
]

vector_set2 = [
    {"id": "3", "values": [0.3] * 1536},
    {"id": "4", "values": [0.4] * 1536},
    # Add more vectors as needed
]

# Upsert vector_set1 to namespace1
index.upsert(
  items=vector_set1,
  namespace="namespace1"
)

# Upsert vector_set2 to namespace2
index.upsert(
  items=vector_set2,
  namespace="namespace2"
)

# Print the index statistics
index_stats = index.describe_index_stats()
print(index_stats)

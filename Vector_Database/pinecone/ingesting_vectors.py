from pinecone import Pinecone

# Initialize the Pinecone client using your API key
pc = Pinecone(api_key="pcsk_3ZCPFh_+++++++++++++iXGYe")

# Index name
index_name = "datacamp-index"

# Connect to your index
index = pc.Index(index_name)

# Example vectors with metadata
vectors = [
    {
        "id": "0",
        "values": np.random.uniform(-1, 1, 1536).tolist(),  # Generate 1536 dimension values
        "metadata": {"genre": "action", "year": 2024}
    },
    {
        "id": "1",
        "values": np.random.uniform(-1, 1, 1536).tolist(),  # Generate 1536 dimension values
        "metadata": {"genre": "comedy", "year": 2023}
    },
    # More vectors...
]
# Upsert vectors to the index
index.upsert(vectors=vectors)

# Print the index's descriptive statistics
print(index.describe_index_stats())

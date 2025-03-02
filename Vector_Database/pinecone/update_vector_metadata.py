# Initialize the Pinecone client with your API key
pc = Pinecone(api_key="pcsk_3ZCPFh_9+++++++++++++GYe")

index = pc.Index('datacamp-index')

# Update the metadata of vector ID 7
metadata = {
    "genre": "thriller",
    "year": 2024
}
# Update the vector with ID "7" with new metadata
index.upsert(vectors=[{"id": "7","values":[1.0]+[0.0]*1535, "metadata": metadata}])
# Fetch vector ID 7
fetched_vector = index.fetch(ids=["7"])
print(fetched_vector)

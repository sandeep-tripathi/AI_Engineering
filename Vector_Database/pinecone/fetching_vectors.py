# Initialize the Pinecone client with your API key
pc = Pinecone(api_key="pcsk_3ZCPFh_9++++++++++++++++o1UvTStRiXGYe")

index = pc.Index('datacamp-index')
ids = ['2', '5', '8']

# Fetch the vectors from the connected Pinecone index
fetched_vectors = index.fetch(ids=ids)

# Extract the metadata from each result in fetched_vectors
metadatas = [fetched_vectors['vectors'].get(id, {}).get('metadata') for id in ids]
print(metadatas)

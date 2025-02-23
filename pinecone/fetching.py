# Initialize the Pinecone client with your API key
pc = Pinecone(api_key="pcsk_3ZCPFh_9+++XGYe")

index = pc.Index('datacamp-index')
ids = ['2', '5', '8']

# Fetch vectors from the connected Pinecone index
fetched_vectors = index.fetch(ids=ids)
print(fetched_vectors)
# Extract the metadata from each result in fetched_vectors
metadatas = [
    {
        "genre": fetched_vectors['vectors'][id]['metadata']['genre'], 
        "year": fetched_vectors['vectors'][id]['metadata']['year']
    } for id in ids if id in fetched_vectors['vectors'] and 'metadata' in fetched_vectors['vectors'][id]
]

#metadatas = [fetched_vectors['vectors'][id]['metadata'] for id in ids]
print(metadatas)

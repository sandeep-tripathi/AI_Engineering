# Initialize the Pinecone client with your API key
pc = Pinecone(api_key="pcsk_3ZCPFh_9++++++++RiXGYe")

index = pc.Index('datacamp-index')

# Upsert vectors in batches of 100
for chunk in chunks(vectors):
    index.upsert(vectors=chunk)

# Retrieve statistics of the connected Pinecone index
print(index.describe_index_stats())

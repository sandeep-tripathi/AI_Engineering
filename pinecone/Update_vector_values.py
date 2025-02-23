from pinecone import Pinecone,ServerlessSpec

# Initialize the Pinecone client with your API key
pc = Pinecone(api_key="pcsk_3ZCPFh_96++++++++++++XGYe")


index = pc.Index('datacamp-index')

# Update the values of vector ID 7
index.update(
    id="7",
    values=vector
)

# Fetch vector ID 7
fetched_vector = index.fetch(ids=['7'])
print(fetched_vector)

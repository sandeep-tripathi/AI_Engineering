# Initialize the Pinecone client with your API key
pc = Pinecone(api_key="pcsk_3ZCPFh_9+++++++++TStRiXGYe")

# Create an index that uses the dot product distance metric
pc.create_index(
    name="dotproduct-index",
    dimension=1536,
    metric='dotproduct',
    spec=ServerlessSpec(
        cloud='aws',
        region='us-east-1'
    )
)

# Print a list of your indexes
print(pc.list_indexes())

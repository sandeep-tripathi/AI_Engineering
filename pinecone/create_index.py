from pinecone import Pinecone,ServerlessSpec

# Initialize the Pinecone client using your API key
pc = Pinecone(api_key="pcsk_3ZCPFh_9*******************6")

# Create your Pinecone index
pc.create_index(
    name="datacamp-index", 
    dimension=1536, 
    spec=ServerlessSpec(
        cloud='aws', 
        region='us-east-1'
    )
)

# Check that each vector has a dimensionality of 1536
vector_dims = [len(vector['values']) == 1536 for vector in vectors]
print(all(vector_dims))
# Delete index
#pc.delete_index('datacamp-index')

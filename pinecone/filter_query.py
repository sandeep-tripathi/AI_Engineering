from pinecone import Pinecone

# Initialize the Pinecone client with your API key
pc = Pinecone(api_key="pcsk_3ZCPFh_963+++++++++XGYe")

# Connect to your Pinecone index
index = pc.Index('datacamp-index')

# Example query vector (ensure it has the same dimensions as the vectors in your index)
#query_vector = [0.025525547564029694] * 1536  # Replace with your actual query vector

# Define metadata filter to match vectors with metadata where year is 2024
metadata_filter = {"year": 2024}

# Retrieve the MOST similar vector with the year 2024
query_result = index.query(
    vector=vector,
    top_k=1,  # Only retrieve the most similar vector
    filter=metadata_filter
)

# Print the query results
print(query_result)

from pinecone import Pinecone

# Initialize the Pinecone client with your API key
pc = Pinecone(api_key="pcsk_3ZCPFh_9++++++StRiXGYe")

# Connect to your Pinecone index
index = pc.Index('datacamp-index')

# Example query vector (ensure it has the same dimensions as the vectors in your index)
vector = [0.025525547564029694] * 1536  # Example vector; replace with your actual query vector

# Retrieve the top three most similar records
query_result = index.query(vector=vector, top_k=3)

# Print the query results
print(query_result)

# Query namespace1 with the vector provided
#query_result = index.query(
 #   vector=vector,
  #  top_k=3,  # Number of top results to retrieve
   # namespace="namespace1"

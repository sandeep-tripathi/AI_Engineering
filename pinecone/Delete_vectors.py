from pinecone import Pinecone

# Initialize the Pinecone client using your API key
pc = Pinecone(api_key="pcsk_3ZCPFh_963+++++++++++++++++DRo1UvTStRiXGYe")

# Connect to your Pinecone index
index = pc.Index('datacamp-index')

# IDs of vectors to delete
delete_ids = ['3', '4']

# Delete the vectors with IDs "3" and "4"
index.delete(ids=delete_ids)

# Retrieve and print the metrics of the connected Pinecone index
index_stats = index.describe_index_stats()
print(index_stats)

import chromadb
from chromadb.api import OpenAIEmbeddingFunction

# Create a persistent client (if not already created)
client = chromadb.PersistentClient()



collection = client.get_collection(
  name="netflix_titles",
  embedding_function=OpenAIEmbeddingFunction(model_name="text-embedding-3-small", api_key="<OPENAI_API_TOKEN>")
)

reference_ids = ['s999', 's1000']

# Retrieve the documents for the reference_ids
reference_texts = collection.get(ids=reference_ids)['documents']

# Query using reference_texts
result = collection.query(
    query_texts=reference_texts,
    n_results=3
)

print(result['documents'])

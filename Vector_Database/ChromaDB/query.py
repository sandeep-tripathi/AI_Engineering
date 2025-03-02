import chromadb
from chromadb.api import OpenAIEmbeddingFunction

# Create a persistent client 
client = chromadb.PersistentClient()


# Retrieve the netflix_titles collection
collection = client.get_collection(
  name="netflix_titles",
  embedding_function=OpenAIEmbeddingFunction(model_name="text-embedding-3-small", api_key="<OPENAI_API_TOKEN>")
)

# Query the collection for "films about dogs"
result = collection.query(query_texts=["films about dogs"], n_results=3)

print(result)

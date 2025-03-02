
import chromadb
from chromadb.api import OpenAIEmbeddingFunction
import csv

# Provided code to extract ids and documents from netflix_titles.csv
ids = []
documents = []

with open('netflix_titles.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for i, row in enumerate(reader):
        ids.append(row['show_id'])
        text = f"Title: {row['title']} ({row['type']})\nDescription: {row['description']}\nCategories: {row['listed_in']}"
        documents.append(text)

# Create a persistent client
client = chromadb.PersistentClient()

# Recreate the netflix_titles collection
collection = client.create_collection(
  name="netflix_titles",
  embedding_function=OpenAIEmbeddingFunction(model_name="text-embedding-3-small", api_key="<OPENAI_API_TOKEN>")
)

# Add the documents and IDs to the collection
collection.add(ids=ids, documents=documents)

# Print the collection size and first ten items
print(f"No. of documents: {collection.count()}")
print(f"First ten documents: {collection.peek()}")

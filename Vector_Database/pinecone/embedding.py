from pinecone import Pinecone
import numpy as np
from uuid import uuid4


# Define the OpenAI API client which is already available as 'client'
#client = ...  # Assuming 'client' is provided and correctly initialized

# Initialize the Pinecone client
pc = Pinecone(api_key="pcsk_3ZCPFh_9+++RiXGYe")
index = pc.Index('pinecone-datacamp')

batch_limit = 100

for batch in np.array_split(df, len(df) / batch_limit):
    # Extract the metadata from each row
    metadatas = [{
      "text_id": row['id'],
      "text": row['text'],
      "title": row['title']} for _, row in batch.iterrows()]
    texts = batch['text'].tolist()
    
    ids = [str(uuid4()) for _ in range(len(texts))]
    
    # Encode texts using OpenAI
    response = client.embeddings.create(input=texts, model="text-embedding-3-small")
    embeds = [np.array(x.embedding) for x in response.data]
    
    # Upsert vectors to the correct namespace
    index.upsert(vectors=zip(ids, embeds, metadatas), namespace="squad_dataset")

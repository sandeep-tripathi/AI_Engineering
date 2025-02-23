#create a chatbot that can answer questions about YouTube videos by ingesting video transcripts and additional metadata into your 'pinecone-datacamp' index.

#To start, you'll prepare data from the youtube_rag_data.csv file and upsert the vectors with all of their metadata into the 'pinecone-datacamp' index. The data is provided in the DataFrame youtube_df.

import pandas as pd
import numpy as np
from uuid import uuid4
from pinecone import Pinecone

# Assuming 'client' is already defined and authenticated for OpenAI
# Example: client = OpenAI(api_key="your_openai_api_key")

# Initialize the Pinecone client
pc = Pinecone(api_key="pcsk_3ZCPFh_9+++tRiXGYe")
index = pc.Index('pinecone-datacamp')

batch_limit = 100

for batch in np.array_split(youtube_df, len(youtube_df) / batch_limit):
    # Extract the metadata from each row
    metadatas = [{
      "text_id": row['id'],
      "text": row['text'],
      "title": row['title'],
      "url": row['url'],
      "published": row['published']} for _, row in batch.iterrows()]
    texts = batch['text'].tolist()
    
    ids = [str(uuid4()) for _ in range(len(texts))]
    
    # Encode texts using OpenAI
    response = client.embeddings.create(input=texts, model="text-embedding-3-small")
    embeds = [np.array(x.embedding) for x in response.data]
    
    # Upsert vectors  to the correct namespace
    index.upsert(vectors=zip(ids, embeds, metadatas), namespace='youtube_rag_dataset')
    
print(index.describe_index_stats())

from pinecone import Pinecone
import openai

# Initialize the OpenAI client
openai.api_key = "YOUR_OPENAI_API_KEY"

# Initialize the Pinecone client
pc = Pinecone(api_key="pcsk_3ZCPFh_9+++iXGYe")
index = pc.Index('pinecone-datacamp')

# Define a retrieve function that takes four arguments: query, top_k, namespace, and emb_model
def retrieve(query, top_k, namespace, emb_model):
    # Encode the input query using OpenAI
    query_response = openai.Embedding.create(
        input=query,
        model=emb_model
    )
    
    query_emb = query_response['data'][0]['embedding']
    
    # Query the index using the query_emb
    docs = index.query(vector=query_emb, top_k=top_k, namespace=namespace, include_metadata=True)
    
    retrieved_docs = []
    sources = []
    for doc in docs['matches']:
        retrieved_docs.append(doc['metadata']['text'])
        sources.append((doc['metadata']['title'], doc['metadata']['url']))
    
    return retrieved_docs, sources

# Example usage of the retrieve function
documents, sources = retrieve(
    query="How to build next-level Q&A with OpenAI",
    top_k=3,
    namespace='youtube_rag_dataset',
    emb_model="text-embedding-ada-002"
)
print(documents)
print(sources)

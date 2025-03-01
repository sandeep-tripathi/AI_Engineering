query = "I need a desktop book reader for Mac"

# Assume embedder and sentence_embeddings are already loaded for you.

# Generate embeddings for the query
query_embedding = embedder.encode([query])[0]

# Compare embeddings to get the top 2 results
hits = util.semantic_search(query_embedding, sentence_embeddings, top_k=2)

# Print the top results
for hit in hits[0]:
    print(sentences[hit["corpus_id"]], "(Score: {:.4f})".format(hit["score"]))

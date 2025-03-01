from sentence_transformers import SentenceTransformer

# Sentence to be embedded
sentence = "This is a test sentence."

# Create the first embedding model
embedder1 = SentenceTransformer("all-MiniLM-L6-v2")

# Embed the sentence
embedding1 = embedder1.encode([sentence])

# Create the second embedding model
embedder2 = SentenceTransformer("paraphrase-albert-small-v2")

# Embed the sentence
embedding2 = embedder2.encode([sentence])

# Compare the shapes
print(embedding1.shape == embedding2.shape)

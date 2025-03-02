import numpy as np
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE

# Example list of products including embeddings
products = [
    {
        "title": "Smartphone X1",
        "short_description": "The latest flagship smartphone with AI-powered features and 5G connectivity.",
        "price": 799.99,
        "category": "Electronics",
        "features": [
            "6.5-inch AMOLED display",
            "Quad-camera system with 48MP main sensor",
            "Face recognition and fingerprint sensor",
            "Fast wireless charging"
        ],
        "embedding": [-0.014650369994342327, 0.008677126839756966]  # Example short embedding for demonstration
    },
    # Add more products as needed, with their respective embeddings
]

# Create categories and embeddings lists using list comprehensions
categories = [product['category'] for product in products]
embeddings = [product['embedding'] for product in products]

# Reduce the number of embeddings dimensions to two using t-SNE
tsne = TSNE(n_components=2, perplexity=5, random_state=42)
embeddings_2d = tsne.fit_transform(np.array(embeddings))

# Create a scatter plot from embeddings_2d
plt.figure(figsize=(10, 8))
plt.scatter(embeddings_2d[:, 0], embeddings_2d[:, 1])

# Annotate each point with its category
for i, category in enumerate(categories):
    plt.annotate(category, (embeddings_2d[i, 0], embeddings_2d[i, 1]))

# Set plot title and labels
plt.title("t-SNE Visualization of Product Embeddings")
plt.xlabel("t-SNE Feature 1")
plt.ylabel("t-SNE Feature 2")

# Display the plot
plt.show()

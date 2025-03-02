import openai
import numpy as np
from scipy.spatial import distance

# Set your OpenAI API key
openai.api_key = "<OPENAI_API_TOKEN>"

# Define your OpenAI client
client = openai

# Define a function to combine the relevant features into a single string
def create_product_text(product):
    features = "; ".join(product['features'])
    return f"""Title: {product['title']}
Description: {product['short_description']}
Category: {product['category']}
Features: {features}"""

# Define a create_embeddings function
def create_embeddings(texts):
    response = client.Embedding.create(
        model="text-embedding-ada-002",  # Ensure you use the correct model identifier
        input=texts
    )
    response_dict = response.model_dump() if hasattr(response, 'model_dump') else dict(response)
    return [data['embedding'] for data in response_dict['data']]

# Define a function to find n closest embeddings
def find_n_closest(query_vector, embeddings, n=3):
    distances = []
    for i, embedding in enumerate(embeddings):
        dist = distance.cosine(query_vector, embedding)
        distances.append({'index': i, 'distance': dist})
    
    # Sort by distance
    distances = sorted(distances, key=lambda x: x['distance'])
    return distances[:n]

# Example products list with descriptions
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
        ]
    },
    {
        "title": "Smartwatch Z",
        "short_description": "The most advanced smartwatch with the latest health tracking features.",
        "price": 199.99,
        "category": "Wearables",
        "features": [
            "Heart rate monitor",
            "Sleep tracking",
            "GPS",
            "Water-resistant"
        ]
    },
    # Add more products as needed
]

# Define the user's history of visited products
user_history = [
    {
      "title": "Laptop Pro 15",
      "short_description": "High-end laptop suitable for gaming and professional work with a 15-inch display.",
      "price": 1299.99,
      "category": "Computers",
      "features": [
          "Intel i7 processor",
          "16GB RAM",
          "512GB SSD",
          "NVIDIA GTX 1650"
      ]
    },
    # Add more history items if needed
]

# Prepare and embed the user_history, and calculate the mean embeddings
history_texts = [create_product_text(product) for product in user_history]
history_embeddings = create_embeddings(history_texts)
mean_history_embedding = np.mean(np.array(history_embeddings), axis=0)

# Filter products to remove any in user_history
products_filtered = [product for product in products if product not in user_history]

# Combine product features and embed the resulting texts
product_texts = [create_product_text(product) for product in products_filtered]
product_embeddings = create_embeddings(product_texts)

# Find the three closest products to the mean history embedding
hits = find_n_closest(mean_history_embedding, product_embeddings)

# Print the titles of the three most similar products
for hit in hits:
    product = products_filtered[hit['index']]
    print(product['title'])

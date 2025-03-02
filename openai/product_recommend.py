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
    # Add more products as needed
]

# Define the last product the user visited
last_product = {
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
}

# Combine the features for last_product and each product in products
last_product_text = create_product_text(last_product)
product_texts = [create_product_text(product) for product in products]

# Embed last_product_text and product_texts
last_product_embedding = create_embeddings([last_product_text])[0]
product_embeddings = create_embeddings(product_texts)

# Find the three smallest cosine distances and their indexes
hits = find_n_closest(last_product_embedding, product_embeddings)

# Print the titles of the three most similar products
for hit in hits:
    product = products[hit['index']]
    print(product['title'])

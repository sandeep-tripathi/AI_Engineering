import openai

# Set your OpenAI API key
openai.api_key = "<OPENAI_API_TOKEN>"

# Define your OpenAI client
client = openai

# Define a create_embeddings function
def create_embeddings(texts):
    response = client.Embedding.create(
        model="text-embedding-ada-002",  # Ensure you use the correct model identifier
        input=texts
    )
    response_dict = response.model_dump() if hasattr(response, 'model_dump') else dict(response)
    return [data['embedding'] for data in response_dict['data']]

# Example product list with descriptions
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

# Extract short_description and list_of_descriptions for examples
short_description = products[0]['short_description']
list_of_descriptions = [product['short_description'] for product in products]

# Embed short_description and print
embedded_short_description = create_embeddings([short_description])
print(embedded_short_description[0])  # Accessing the first element of the returned list

# Embed list_of_descriptions and print
embedded_list_of_descriptions = create_embeddings(list_of_descriptions)
print(embedded_list_of_descriptions)

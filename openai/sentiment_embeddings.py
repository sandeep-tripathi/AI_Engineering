import openai
import numpy as np
from scipy.spatial import distance

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

# Provided sentiment labels and reviews
sentiments = [{'label': 'Positive'},
              {'label': 'Neutral'},
              {'label': 'Negative'}]

reviews = ["The food was delicious!",
           "The service was a bit slow but the food was good",
           "The food was cold, really disappointing!"]

# Create a list of class descriptions from the sentiment labels
class_descriptions = [sentiment['label'] for sentiment in sentiments]

# Embed the class_descriptions and reviews
class_embeddings = create_embeddings(class_descriptions)
review_embeddings = create_embeddings(reviews)

# Function to classify reviews using cosine similarity
def classify_reviews(review_embeddings, class_embeddings, class_descriptions):
    classifications = []
    for review_embedding in review_embeddings:
        distances = [distance.cosine(review_embedding, class_embedding) for class_embedding in class_embeddings]
        closest_class_index = np.argmin(distances)
        classifications.append(class_descriptions[closest_class_index])
    return classifications

# Classify reviews
classified_sentiments = classify_reviews(review_embeddings, class_embeddings, class_descriptions)

# Print the classification results
for review, sentiment in zip(reviews, classified_sentiments):
    print(f"Review: {review}\nSentiment: {sentiment}\n")

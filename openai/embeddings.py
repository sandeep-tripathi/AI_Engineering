import openai

# Create an OpenAI client
client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Create a request to obtain embeddings
response = client.embeddings.create(
    model="text-embedding-3-small",  # Ensure this model identifier is correct and available
    input="Here is some example text to get embeddings for."
)
# Convert the response into a dictionary
response_dict = response.model_dump()
print(response_dict)


# Extract the total_tokens from response_dict
print(response_dict['usage']['total_tokens'])

# Try accessing the 'data' key first, then the first item in the list, and finally the 'embedding' key
print(response_dict['data'][0]['embedding'])

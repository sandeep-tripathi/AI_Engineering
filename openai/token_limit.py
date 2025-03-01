import openai
import tiktoken

# Initialize the OpenAI client
client = openai.OpenAI(api_key="<OPENAI_API_TOKEN>")

input_message = {"role": "user", "content": "I'd like to buy a shirt and a jacket. Can you suggest two color pairings for these items?"}

# Use tiktoken to create the encoding for your model
encoding = tiktoken.get_encoding("gpt-4")

# Check for the number of tokens
num_tokens = len(encoding.encode(input_message["content"]))

# Define the token limit
token_limit = 100  # Assuming GPT-4 Mini has an 100 token limit

# Run the chat completions function and print the response
if num_tokens <= token_limit:
    response = client.chat.completions.create(
        model="gpt-4-mini",
        messages=[input_message]
    )
    print(response.choices[0]["message"]["content"])
else:
    print("Message exceeds token limit")

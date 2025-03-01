import openai

# Create the OpenAI client
client = openai.OpenAI(api_key="<OPENAI_API_TOKEN>")

# Create the request
response = client.chat.completions.create(
  model="gpt-4",
  messages=[
    {"role": "user", "content": "I have these notes with book titles and authors: New releases this week! The Beholders by Hester Musson, The Mystery Guest by Nita Prose. Please organize the titles and authors in a JSON object."}
  ],
  # Specify the response format
  response_format="json"
)

# Print the response
print(response.choices[0]["message"]["content"])

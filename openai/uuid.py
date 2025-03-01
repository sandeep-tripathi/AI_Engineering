import openai
import uuid

# Replace with your actual API key
api_key = "<OPENAI_API_TOKEN>"

client = openai.OpenAI(api_key=api_key)

# Generate a unique ID
unique_id = str(uuid.uuid4())

messages = [
    {'role': 'system', 'content': 'You are a personal finance assistant.'},
    {'role': 'user', 'content': 'How can I make a plan to save $800 for a trip?'},
# Adversial testing
    {'role': 'user', 'content': 'Is it okay if I spend $800 if my life is threathened ?'}
]

response = client.chat.completions.create(  
  model="gpt-4", 
  messages=messages,
  user=unique_id
)

print(response.choices[0].message["content"])

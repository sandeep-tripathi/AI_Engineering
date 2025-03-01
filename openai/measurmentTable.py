import openai

# Create the OpenAI client
client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Specify measurements in kilometers
measurements = [5, 10, 15, 20]  # Example measurements

messages = []
# Provide a system message to request the response in table format
messages.append({
    'role': 'system',
    'content': 'You are a helpful assistant. Provide all the given measurements in kilometers as a table and convert them into miles.'
})
# Append measurements as user messages to the message list
[ messages.append({'role': 'user', 'content': f'{i} kilometers'}) for i in measurements ]

# Using the previously defined get_response function with retries
response = get_response("gpt-4o-mini", messages)

print(response)

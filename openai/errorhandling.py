import openai
client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Use the try statement
try:
    response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[message]
    )
    # Print the response
    print(response.choices[0].message.content)
# Use the except statement
except openai.AuthenticationError:
    print("Please double check your authentication key and try again, the one provided is not valid.")

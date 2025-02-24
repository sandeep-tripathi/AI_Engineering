client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Create a prompt detailing steps to plan the trip
prompt = """
I want to plan a beach vacation. Could you help me by providing the following details:
1. Suggest four potential beach locations.
2. For each location, recommend some accommodation options.
3. List some activities that can be enjoyed at each location.
4. Provide an evaluation of the pros and cons for each location.
"""

response = get_response(prompt)
print(response)

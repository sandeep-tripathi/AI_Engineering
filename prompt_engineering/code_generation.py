# Generate Python code with example input and output


client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Define the prompt
prompt = """
Write a Python function that receives a list of 12 floats representing monthly sales data and returns the month with the highest sales value as output. The function should be named `month_with_highest_sales`. Assume the list is indexed from 0 to 11 corresponding to January to December.

Example input: [100.5, 200.3, 150.2, 300.7, 250.6, 120.4, 80.3, 140.8, 155.6, 290.4, 330.7, 210.4]
Example output: 'November' (for the input list, November has the highest sales value)
"""

response = get_response(prompt)
print(response)

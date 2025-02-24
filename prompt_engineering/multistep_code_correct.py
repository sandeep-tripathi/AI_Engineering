client = OpenAI(api_key="<OPENAI_API_TOKEN>")

code = '''
def calculate_rectangle_area(length, width):
    area = length * width
    return area
'''

# Create a prompt that analyzes correctness of the code
prompt = f"""
Analyze the following Python function delimited by triple backticks according to these criteria:
1. Correct syntax
2. Receives exactly two inputs
3. Returns exactly one output

Here is the code:
{code}

Please provide your assessment:
"""

response = get_response(prompt)
print(response)

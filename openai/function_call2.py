import openai

client = openai.OpenAI(api_key="<OPENAI_API_TOKEN>")

# Preloaded messages containing the text of the research paper
messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Please extract key information from this research paper."}
    # Assume that the actual research paper text follows here.
]

# Initialize function definition
function_definition = [
    {
        "name": "extract_key_info",
        "description": "Extracts key information from a research paper.",
        "parameters": {},  # Placeholder for parameters
        "returns": {}
    }
]

# Define the function parameter type
function_definition[0]['parameters']['type'] = "object"  # Define the type of the parameter

# Define the function properties
function_definition[0]['parameters']['properties'] = {
    "title": {"type": "string", "description": "The title of the research paper."},
    "year_of_publication": {"type": "integer", "description": "The year in which the research paper was published."}
}

function_definition[0]['parameters']['required'] = ["title", "year_of_publication"]

# Assuming the returns part is defined similarly, let's complete it:
function_definition[0]['returns'] = {
    "type": "object",
    "properties": {
        "title": {"type": "string", "description": "The title of the research paper."},
        "year_of_publication": {"type": "integer", "description": "The year in which the research paper was published."}
    }
}

# Define the function that will call the API and return the response
def get_response(messages, functions):
    response = client.chat.create(
        model="gpt-4o-mini",
        messages=messages,
        functions=functions
    )
    return response

# Fetch and print the response
response = get_response(messages, function_definition)
print(response)

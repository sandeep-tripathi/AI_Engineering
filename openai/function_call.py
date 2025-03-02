import openai

# Initialize the OpenAI client with your API token
client = openai.OpenAI(api_key="<OPENAI_API_TOKEN>")

# Preloaded message
message_listing = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Hello, I would like some help with my code."}
]

# Function definition
function_definition = [
    {
        "name": "get_code_help",
        "description": "Provides help with code issues.",
        "parameters": {
            "type": "object",
            "properties": {
                "code_snippet": {"type": "string", "description": "The code that the user needs help with."},
                "issue_description": {"type": "string", "description": "Description of the issue or error the user is facing."}
            },
            "required": ["code_snippet", "issue_description"]
        },
        "returns": {
            "type": "string",
            "description": "Detailed suggestion or a solution to the issue."
        }
    }
]

# Create a chat completion request
response = client.chat.create(
    model="gpt-4o-mini",
    messages=message_listing,  # Add the preloaded message
    functions=function_definition  # Add the function definition
)

# Print the function call within the response
print(response.choices[0].message.tool_calls[0].function.arguments)

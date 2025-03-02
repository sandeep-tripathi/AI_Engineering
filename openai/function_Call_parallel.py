import openai

client = openai.OpenAI(api_key="<OPENAI_API_TOKEN>")

# Preloaded messages containing the user's review
messages = [
    {"role": "user", "content": "I loved the product, but the delivery was late."}
]

# Preloaded function definition for extracting data
function_definition = [
    {
        "name": "extract_review_data",
        "description": "Extracts key information from a customer's review.",
        "parameters": {
            "type": "object",
            "properties": {
                "product_feedback": {"type": "string", "description": "Feedback about the product."},
                "delivery_feedback": {"type": "string", "description": "Feedback about the delivery service."}
            },
            "required": ["product_feedback", "delivery_feedback"]
        },
        "returns": {
            "type": "object",
            "properties": {
                "product_feedback": {"type": "string", "description": "Feedback about the product."},
                "delivery_feedback": {"type": "string", "description": "Feedback about the delivery service."}
            }
        }
    }
]

# Append the second function to reply to the review
second_function = {
    "name": "reply_to_review",
    "description": "Generates a reply to the customer's review.",
    "parameters": {
        "type": "object",
        "properties": {
            "reply": {
                "type": "string",
                "description": "The reply message to the customer."
            }
        },
        "required": ["reply"]
    },
    "returns": {
        "type": "object",
        "properties": {
            "reply": {
                "type": "string",
                "description": "The reply message to the customer."
            }
        }
    }
}

# Append this new function definition to the existing function_definition list
function_definition.append(second_function)

# Define the function that will call the API and return the response
def get_response(messages, functions):
    response = client.chat.create(
        model="gpt-4o-mini",
        messages=messages,
        functions=functions
    )
    return response

# Make the API call and get the response
response = get_response(messages, function_definition)

# Print the response in the specified format
if 'choices' in response and len(response['choices']) > 0:
    first_choice = response['choices'][0]
    if 'message' in first_choice and 'tool_calls' in first_choice['message']:
        first_tool_call = first_choice['message']['tool_calls'][0]
        if 'function' in first_tool_call:
            print(first_tool_call['function']['arguments'])
        else:
            print("Function arguments not found in the tool call.")
    else:
        print("Tool calls or necessary fields not found in the response.")
else:
    print("Choices not found in the response.")

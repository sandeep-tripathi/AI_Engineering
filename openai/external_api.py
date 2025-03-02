client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Define the function to pass to tools
function_definition = [{
    "type": "function",
    "function": {
        "name": "get_airport_info",
        "description": "This function calls the Aviation API to return the airport code corresponding to the airport in the request.",
        "parameters": {
            "type": "object",
            "properties": {
                "airport_code": {
                    "type": "string",
                    "description": "The code to be passed to the get_airport_info function."
                }
            },
            "required": ["airport_code"]
        },
        "result": {
            "type": "string"
        }
    }
}]

response = get_response(function_definition)
print(response)

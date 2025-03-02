client = OpenAI(api_key="<OPENAI_API_TOKEN>")

response= client.chat.completions.create(
    model=model,
    messages=messages,
    # Add the function definition
   tools=function_definition,
    # Specify the function to be called for the response
         tool_choice={"type": "function", "function": {"name": "extract_review_info"}}
)

# Print the response
print(response.choices[0].message.tool_calls[0].function.arguments)

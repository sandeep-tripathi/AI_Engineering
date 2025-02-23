client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Create the instructions
instructions = "You will be provided with a text delimited by triple backticks. Infer its language, then generate a suitable title for it. "

# Create the output format
output_format = """Use the following format for the output:
         - Text: <the text>
         - Language: <the text language>
         - Title: <the generated title>"""

# Create the final prompt
prompt = instructions + output_format + f"```{text}```"
response = get_response(prompt)
print(response)

client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Define the purpose of the chatbot
chatbot_purpose = "You handle customer support, specializes in electronics, and is there to assist with inquiries, order tracking, and troubleshooting"

# Define audience guidelines
audience_guidelines = "Your audience includes customers who are tech-savvy who are interested in purchasing electronic gadgets."

# Define tone guidelines
tone_guidelines = "Maintain a user-friendly, professional, and patient tone. Clearly explain technical steps and avoid jargon."

system_prompt = chatbot_purpose + audience_guidelines + tone_guidelines
response = get_response(system_prompt, "My new headphones aren't connecting to my device")
print(response)

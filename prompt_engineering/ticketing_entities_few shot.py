client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Define sample tickets and their corresponding entities
ticket_1 = "I can't access my account after resetting my password."
entities_1 = {
    "issue": "access problem",
    "action": "resetting password"
}

ticket_2 = "When will I be charged for the subscription?"
entities_2 = {
    "inquiry": "billing",
    "object": "subscription"
}

ticket_3 = "The new update keeps crashing my app every time I open it."
entities_3 = {
    "issue": "app crash",
    "cause": "new update"
}

# Define the new ticket
ticket_4 = "I'm experiencing issues with my payment not going through on the website."

# Craft a few-shot prompt to get the ticket's entities
prompt = f"""
Extract the relevant entities from the following tickets:

Ticket: "{ticket_1}"
Entities: {entities_1}

Ticket: "{ticket_2}"
Entities: {entities_2}

Ticket: "{ticket_3}"
Entities: {entities_3}

Now, extract the entities from the following ticket:

Ticket: "{ticket_4}"
Entities:
"""

response = get_response(prompt)

print("Ticket: \n", ticket_4)
print("Entities: \n", response)

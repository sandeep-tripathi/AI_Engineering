from langchain.prompts import PromptTemplate

# Create a prompt template that takes an input activity
learning_prompt = PromptTemplate(
    input_variables=["activity"],
    template="I want to learn how to {activity}. Can you suggest how I can learn this step-by-step?"
)

# Create a prompt template that places a time constraint on the output
time_prompt = PromptTemplate(
    input_variables=["learning_plan"],
    template="I only have one week. Can you create a plan to help me hit this goal: {learning_plan}."
)

# Invoke the learning_prompt with an activity
learning_plan = learning_prompt.invoke({"activity": "play golf"})
print(learning_plan)

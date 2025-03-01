# Import necessary modules
from transformers import pipeline

# Define the text example
text_example = "I am a HUGE fan of romantic comedies."

# Create the classifier with saved model in "./fine_tuned_model"
classifier = pipeline(task="sentiment-analysis", model="./fine_tuned_model")

# Classify the text
results = classifier(text=text_example)

# Print the results
print(results)

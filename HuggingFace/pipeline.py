# Sentiment analysis
from transformers import pipeline

# Create the task pipeline
task_pipeline = pipeline("sentiment-analysis")

# Create the model pipeline
model_pipeline = pipeline(model="distilbert-base-uncased-finetuned-sst-2-english")

# Define input text
input_text = "I love using Hugging Face transformers library!"

# Predict the sentiment using both pipelines
task_output = task_pipeline(input_text)
model_output = model_pipeline(input_text)

print(f"Sentiment from task_pipeline: {task_output[0]['label']}; Sentiment from model_pipeline: {model_output[0]['label']}")

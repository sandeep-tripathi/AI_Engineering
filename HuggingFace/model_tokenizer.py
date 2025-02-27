
from transformers import AutoModelForSequenceClassification, AutoTokenizer, pipeline

# Download the model and tokenizer
model = AutoModelForSequenceClassification.from_pretrained("distilbert-base-uncased-finetuned-sst-2-english")
tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased-finetuned-sst-2-english")

# Create the pipeline
sentimentAnalysis = pipeline(task="sentiment-analysis", model=model, tokenizer=tokenizer)

# Define input text
input_text = "I love using Hugging Face transformers library!"

# Predict the sentiment
output = sentimentAnalysis(input_text)

print(f"Sentiment using AutoClasses: {output[0]['label']}")

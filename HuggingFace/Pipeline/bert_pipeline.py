
from transformers import pipeline

# Create the pipeline for the distilbert model
distil_pipeline = pipeline(task="sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

# Define input text
input_text = "I love using Hugging Face transformers library!"

# Predict the sentiment using distil_pipeline
distil_output = distil_pipeline(input_text)

print(f"Sentiment (distil_pipeline): {distil_output[0]['label']}")

# Create the pipeline for the nlptown/bert-base-multilingual-uncased-sentiment model
bert_pipeline = pipeline(task="sentiment-analysis", model="nlptown/bert-base-multilingual-uncased-sentiment")

# Predict the sentiment using bert_pipeline
bert_output = bert_pipeline(input_text)

print(f"Sentiment (bert_pipeline): {bert_output[0]['label']}")

from transformers import pipeline

# Define the original text
original_text = """
The Hugging Face Transformers library provides state-of-the-art natural language processing capabilities. 
With pre-trained models, it supports tasks such as text classification, question answering, and text summarization. 
This allows developers to build sophisticated applications with minimal effort. 
The library is widely used in industry and academia and continues to evolve with contributions from the community.
"""

# Create a short summarizer
short_summarizer = pipeline(task="summarization", model="cnicu/t5-small-booksum", min_length=1, max_length=10)

# Summarize the input text
short_summary_text = short_summarizer(original_text)

# Print the short summary
print(short_summary_text[0]["summary_text"])

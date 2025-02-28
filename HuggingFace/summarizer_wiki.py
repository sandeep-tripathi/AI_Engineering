from datasets import load_dataset
from transformers import pipeline

# Load the wiki dataset
dataset = load_dataset("wikitext", "wikitext-2-raw-v1", split="test")

# Create the list of texts to summarize
text_to_summarize = [w["text"] for w in dataset]

# Create the pipeline
summarizer = pipeline("summarization", model="cnicu/t5-small-booksum", min_length=20, max_length=50)

# Summarize each item in the list
summaries = summarizer(text_to_summarize[:3], truncation=True)

# Create for-loop to print each summary
for i in range(0, 3):
    print(f"Summary {i+1}: {summaries[i]['summary_text']}")

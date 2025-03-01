#pip install datasets
from transformers import AutoModelForSequenceClassification, AutoTokenizer
from datasets import load_dataset, Dataset

# Model name
model_name = "distilbert-base-uncased-finetuned-sst-2-english"

# Load the model
model = AutoModelForSequenceClassification.from_pretrained(model_name)

# Load the tokenizer
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Example usage with a custom list of texts
texts = ["I love using transformers!", "This is a great way to process text data."]

# Convert to dataset
dataset = Dataset.from_dict({"text": texts})

# Use tokenizer on text
dataset = dataset.map(lambda row: tokenizer(row["text"], padding=True, max_length=512, truncation=True), keep_in_memory=True)

# Print dataset to verify 
print(dataset)

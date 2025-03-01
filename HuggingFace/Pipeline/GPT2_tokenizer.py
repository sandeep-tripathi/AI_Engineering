
from transformers import AutoTokenizer

# Define the input text
input_text = "I love using Hugging Face transformers library!"

# Download the GPT tokenizer
gpt_tokenizer = AutoTokenizer.from_pretrained("gpt2")

# Tokenize the input with GPT tokenizer
gpt_tokens = gpt_tokenizer.tokenize(input_text)

# Download the DistilBERT tokenizer
distil_tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased-finetuned-sst-2-english")

# Tokenize the input with DistilBERT tokenizer
distil_tokens = distil_tokenizer.tokenize(input_text)

# Compare the output
print(f"GPT tokenizer: {gpt_tokens}")
print(f"DistilBERT tokenizer: {distil_tokens}")

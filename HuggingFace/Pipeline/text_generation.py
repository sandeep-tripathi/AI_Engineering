
from transformers import AutoTokenizer, AutoModelForCausalLM

# Set model name
model_name = "gpt2"

# Get the tokenizer and model
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

prompt = "Wear sunglasses when its sunny because"

# Tokenize the input
input_ids = tokenizer.encode(prompt, return_tensors="pt")

# Generate the text output
output = model.generate(input_ids, max_length=50, num_return_sequences=1)

# Decode the output
generated_text = tokenizer.decode(output[0], skip_special_tokens=True)

print(generated_text)

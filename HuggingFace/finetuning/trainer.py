
from transformers import AutoModelForSequenceClassification, AutoTokenizer, TrainingArguments, Trainer
from datasets import Dataset

# Define the model name
model_name = "distilbert-base-uncased-finetuned-sst-2-english"

# Load the pre-trained model
model = AutoModelForSequenceClassification.from_pretrained(model_name)

# Load the tokenizer
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Sample data
texts_train = ["I love using transformers!", "This is a fantastic library for NLP."]
labels_train = [1, 1]  # Positive sentiment labels for simplicity
texts_test = ["I don't like this.", "This is not good."]
labels_test = [0, 0]  # Negative sentiment labels for simplicity

# Convert to datasets
train_dataset = Dataset.from_dict({"text": texts_train, "labels": labels_train})
test_dataset = Dataset.from_dict({"text": texts_test, "labels": labels_test})

# Tokenize the datasets
train_dataset = train_dataset.map(lambda row: tokenizer(row["text"], padding=True, max_length=512, truncation=True), 
                                  batched=True)
test_dataset = test_dataset.map(lambda row: tokenizer(row["text"], padding=True, max_length=512, truncation=True), 
                                batched=True)

# Set format for PyTorch (since Trainer expects this format)
train_dataset.set_format(type='torch', columns=['input_ids', 'attention_mask', 'labels'])
test_dataset.set_format(type='torch', columns=['input_ids', 'attention_mask', 'labels'])

# Create training arguments
training_args = TrainingArguments(output_dir="./results", 
                                  num_train_epochs=3, 
                                  per_device_train_batch_size=2, 
                                  per_device_eval_batch_size=2, 
                                  evaluation_strategy="epoch",
                                  save_total_limit=2)

# Create the trainer
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_dataset,
    eval_dataset=test_dataset
)

# Start the training
trainer.train()

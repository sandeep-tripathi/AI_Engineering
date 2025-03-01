from transformers import pipeline
from PIL import Image

# Create the VQA pipeline
vqa = pipeline(task="visual-question-answering", model="dandelin/vilt-b32-finetuned-vqa")

# Load the image
image_path = "path_to_your_image.jpg"  # replace with your image path
image = Image.open(image_path)

# Define the question
question = "What is the color of the vehicle?"  # replace with your actual question

# Use the VQA pipeline
results = vqa(image=image, question=question)

# Print the results
print(results)

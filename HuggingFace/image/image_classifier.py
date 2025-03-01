from transformers import pipeline
from PIL import Image

# Load the image
image_path = 'path_to_your_image.jpg'  # replace with your image path
image = Image.open(image_path)

# Create the pipeline
classifier = pipeline(task="image-classification", 
                      model="abhishek/autotrain_fashion_mnist_vit_base")

# Predict the class of the image
results = classifier(image)

# Print the results
print(results[0]["label"])

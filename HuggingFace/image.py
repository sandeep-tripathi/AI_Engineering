from transformers import AutoProcessor, AutoModelForCausalLM
from PIL import Image
import requests

# Load an image for processing (example image URL)
url = "https://example.com/path/to/your/image.jpg"  # Replace with a valid image URL or path
image = Image.open(requests.get(url, stream=True).raw)

# Get the processor and model
processor = AutoProcessor.from_pretrained("microsoft/git-base-coco")
model = AutoModelForCausalLM.from_pretrained("microsoft/git-base-coco")

# Process the image
pixels = processor(images=image, return_tensors="pt").pixel_values

# Generate the ids
output = model.generate(pixel_values=pixels)

# Decode the output
caption = processor.batch_decode(output, skip_special_tokens=True)

print(caption[0])

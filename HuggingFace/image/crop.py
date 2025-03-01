import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from torchvision import transforms

# Load the image
image_path = 'path_to_your_image.jpg'  # replace with your image path
image = Image.open(image_path)

# Convert the image to a numpy array
image_array = np.array(image)

# Define the center crop transform using torchvision.transforms
transform = transforms.Compose([
    transforms.ToPILImage(),  # Convert numpy array back to PIL image
    transforms.CenterCrop((200, 200)),  # Define the size for center crop
    transforms.ToTensor()  # Convert image to tensor to use with torchvision
])

# Apply the transform
cropped_image_tensor = transform(image_array)

# Convert the tensor to a numpy array for plotting
cropped_image = cropped_image_tensor.permute(1, 2, 0).numpy()  # Change from [C, H, W] to [H, W, C]

# Plot and show the cropped image
imgplot = plt.imshow(cropped_image)
plt.show()

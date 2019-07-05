import requests 
import pickle
import os
from PIL import Image
from io import BytesIO

# Endpoint
images_url = 'http://localhost:3000/images/'
image_directory_path = os.path.abspath('images')

# Issuing get request
data = requests.get(url = images_url).json()

# Create image directory if does not exist
if not os.path.exists(image_directory_path):
    os.makedirs(image_directory_path)

# Download each file by name
for name in data['images']:
    image_path = image_directory_path + '/' + name
    if not os.path.exists(image_path):    
        # Get image binary from URL
        image_url = images_url + name
        response = requests.get(url = image_url)

        # Create image object and save
        image = Image.open(BytesIO(response.content))
        image.save(image_path)

# Remove local files that are not found in server response
for file in os.listdir(image_directory_path):
    found = False
    for name in data['images']:
        if name == file:
            found = True
    if not found:
        os.remove(image_directory_path + '/' + file)

print(data)
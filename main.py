import requests
import json

phone_number = "+977 9851057281"

# Get the API key
api_key = "YOUR_API_KEY"

# Create the URL
url = "https://api.imgur.com/3/gallery/get/?phone_number={}".format(phone_number)

# Make the request
response = requests.get(url, headers={"Authorization": "Bearer {}".format(api_key)})

# Check the response status code
if response.status_code == 200:
    # Get the gallery data
    gallery_data = json.loads(response.content)

    # Print the gallery data
    print(gallery_data)
else:
    print("Error: {}".format(response.status_code))
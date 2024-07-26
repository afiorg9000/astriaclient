import requests

# Define the API endpoint and headers
url = "https://api.astria.ai/tunes"
headers = {
    "Authorization": "Bearer sd_QSBzgNirXJykHtLrT9Fh5ASqxafMbn"
}

# Define the form data for FaceID fine-tune
data = {
    "tune[title]": "Sweaterrr-FaceID",
    "tune[name]": "shirt",
    "tune[model_type]": "faceid",
    "tune[callback]": "https://optional-callback-url.com/webhooks/astria?user_id=1&tune_id=2",
    "tune[base_tune_id]": 690204,  # Hard-coded base tune ID for Realistic Vision v5.1
    "tune[branch]": "sd15"  # Change branch to sd15
}

# Define the file path for the garment image
file_path = "/Users/sofiaisabellamendezdantas/astriaclient/garment/image8-b2eebd424c4f5f9e5836e0a2f603e9ad.png"

# Create the files dictionary
files = {
    "tune[images][]": open(file_path, "rb")
}

# Send the POST request to create the FaceID fine-tune
response = requests.post(url, headers=headers, data=data, files=files)

# Print the response
print(response.status_code)
print(response.json())

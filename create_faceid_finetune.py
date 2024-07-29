import requests

url = "https://api.astria.ai/tunes"
headers = {
    "Authorization": "Bearer sd_QSBzgNirXJykHtLrT9Fh5ASqxafMbn"
}

data = {
    "tune[title]": "PinkSweater-for-Ashley", # Add title for the kind of garment it is
    "tune[name]": "shirt", # if its a lower garment add 'pants', if its an upper garment add 'shirt', if its a full body garment like a dress or swimsuit add 'clothing'
    "tune[model_type]": "faceid",
    "tune[callback]": "https://optional-callback-url.com/webhooks/astria?user_id=1&tune_id=2",
    "tune[base_tune_id]": 690204,
    "tune[branch]": "sd15"
}

# add the garment image here
file_path = "/Users/sofiaisabellamendezdantas/astriaclient/garment/2928510_1_500.jpg"


files = {
    "tune[images][]": open(file_path, "rb")
}

response = requests.post(url, headers=headers, data=data, files=files)

print(response.status_code)
print(response.json())

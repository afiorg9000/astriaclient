import requests

# Define the API endpoint and headers
prompt_id = 17607554
url = f"https://api.astria.ai/tunes/690204/prompts/{prompt_id}"
headers = {
    "Authorization": "Bearer sd_QSBzgNirXJykHtLrT9Fh5ASqxafMbn"
}

# Send the GET request to check the prompt status
response = requests.get(url, headers=headers)

# Print the response
print(response.status_code)
print(response.json())


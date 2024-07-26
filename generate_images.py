import requests

# Define the API endpoint and headers
url = "https://api.astria.ai/tunes/690204/prompts"  # Hard-coded to the base model
headers = {
    "Authorization": "Bearer sd_QSBzgNirXJykHtLrT9Fh5ASqxafMbn"
}

# Define the form data for the prompt
data = {
    "prompt[text]": "<faceid:1477237:1.0> Mid-shot of ohwx woman wearing a sweater",  # Use the FaceID tune ID
    "prompt[negative_prompt]": "",
    "prompt[super_resolution]": "true",
    "prompt[face_correct]": "true",
    "prompt[inpaint_faces]": "true",
    "prompt[callback]": "https://optional-callback-url.com/to-your-service-when-ready?prompt_id=1"
}

# Send the POST request to generate images
response = requests.post(url, headers=headers, data=data)

# Print the response
print(response.status_code)
print(response.json())

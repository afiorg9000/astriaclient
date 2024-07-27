import requests

# Define the API endpoint and headers
url = "https://api.astria.ai/tunes/1478736/prompts"  # Use the base model ID
headers = {
    "Authorization": "Bearer sd_QSBzgNirXJykHtLrT9Fh5ASqxafMbn"
}

# Define the form data for the prompt
data = {
    "prompt[text]": "<faceid:1478639:1.0> Mid-shot of sks woman wearing a sweater",
    "prompt[negative_prompt]": "",
    "prompt[super_resolution]": "true",
    "prompt[face_correct]": "true",
    "prompt[inpaint_faces]": "true",
    "prompt[backend_version]": "1",
    "prompt[face_swap]": "true",  # Enable face swapping
    "prompt[callback]": "https://optional-callback-url.com/to-your-service-when-ready?prompt_id=1"
}

# Send the POST request to generate images
response = requests.post(url, headers=headers, data=data)

# Print the response
print(response.status_code)
print(response.json())

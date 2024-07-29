import requests

# Before running this file, run tune.py first and create_faceid_finetune.py after. 
# Make sure to get the ID thats generated in the output for each, as you need to put them in this code.

url = "https://api.astria.ai/tunes/1478770/prompts"  # Switch this numeric code for the ID that was generated after running tune.py
headers = {
    "Authorization": "Bearer sd_QSBzgNirXJykHtLrT9Fh5ASqxafMbn"
}

data = {
    "prompt[text]": "<faceid:1478810:1.0> Mid-shot of sks woman wearing a sweater with blue pants", # # Switch the numeric code <faceid:{HERE}:1.0> for the ID that was generated after running create_faceid_finetune.py
    "prompt[negative_prompt]": "",
    "prompt[super_resolution]": "true",
    "prompt[face_correct]": "true",
    "prompt[inpaint_faces]": "true",
    "prompt[backend_version]": "1",
    "prompt[face_swap]": "true",
    "prompt[callback]": "https://optional-callback-url.com/to-your-service-when-ready?prompt_id=1"
}

response = requests.post(url, headers=headers, data=data)

print(response.status_code)
print(response.json())

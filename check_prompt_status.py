import requests

prompt_id = 17608087 # run generate_images.py then go to this file and change the prompt_id by the ID thats generated in the ouput of generate_images.py, then run this file.
url = f"https://api.astria.ai/tunes/690204/prompts/{prompt_id}"
headers = {
    "Authorization": "Bearer sd_QSBzgNirXJykHtLrT9Fh5ASqxafMbn"
}

response = requests.get(url, headers=headers)

print(response.status_code)
print(response.json())


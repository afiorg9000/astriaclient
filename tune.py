import requests

url = "https://api.astria.ai/tunes"
headers = {
    "Authorization": "Bearer sd_QSBzgNirXJykHtLrT9Fh5ASqxafMbn"
}

data = {
    "tune[title]": "AshleyGraham", # Add the name of your Avatar
    "tune[name]": "woman", # Add wether its a woman or man here
    "tune[branch]": "sd15",
    "tune[callback]": "https://optional-callback-url.com/webhooks/astria?user_id=1&tune_id=1",
    "tune[token]": "sks",
    "tune[prompts_attributes][0][callback]": "https://optional-callback-url.com/webhooks/astria?user_id=1&prompt_id=1&tune_id=1",
    "tune[prompts_attributes][0][text]": "Sample prompt text"
}

# Add the images to create the avatar
file_paths = [
    "/Users/sofiaisabellamendezdantas/astriaclient/images/1505372947-ashley-graham-1.jpg",
    "/Users/sofiaisabellamendezdantas/astriaclient/images/190802_ITG_AshleyGraham_0202_LowRes.jpg",
    "/Users/sofiaisabellamendezdantas/astriaclient/images/220801130126-ashley-graham-lead.jpg",
    "/Users/sofiaisabellamendezdantas/astriaclient/images/30AD32EE00000578-3426481-image-m-2_1454336330151.jpg",
    "/Users/sofiaisabellamendezdantas/astriaclient/images/3d59b18cdd7185e5091b0541cdb9ad3e.jpg",
    "/Users/sofiaisabellamendezdantas/astriaclient/images/4466d17fd8769e0648e8dbbf1d7a8aa1.jpg",
    "/Users/sofiaisabellamendezdantas/astriaclient/images/579795c0b8efc82753e72a0d649de47b.jpg",
    "/Users/sofiaisabellamendezdantas/astriaclient/images/640px-Ashley_Graham_at_SI_Swim_City_2016.jpg",
    "/Users/sofiaisabellamendezdantas/astriaclient/images/6b57056ad48d437364886289e152377b.jpg",
    "/Users/sofiaisabellamendezdantas/astriaclient/images/a91404d5101ba35e163226ffc29ce4b5.jpg",
    "/Users/sofiaisabellamendezdantas/astriaclient/images/Ashley_Graham_VMA_backstage.jpg",
    "/Users/sofiaisabellamendezdantas/astriaclient/images/Ashley_Graham_in_2015.jpg",
    "/Users/sofiaisabellamendezdantas/astriaclient/images/Ashley_Graham_portrait_2016.jpg",
    "/Users/sofiaisabellamendezdantas/astriaclient/images/ec8461f6a181845ef5a6faa244bb5e5b.jpg",
    "/Users/sofiaisabellamendezdantas/astriaclient/images/f1a6652cd8a8f69e2a7d8a655b97375e.jpg",
    "/Users/sofiaisabellamendezdantas/astriaclient/images/gettyimages-885659602_ashley-graham.jpg",
    "/Users/sofiaisabellamendezdantas/astriaclient/images/untitled-design.jpg"
]


files = [("tune[images][]", (open(file_path, "rb"))) for file_path in file_paths]

response = requests.post(url, headers=headers, data=data, files=files)

print(response.status_code)
print(response.json())

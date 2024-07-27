import requests

# Define the API endpoint and headers
url = "https://api.astria.ai/tunes"
headers = {
    "Authorization": "Bearer sd_QSBzgNirXJykHtLrT9Fh5ASqxafMbn"
}

# Define the form data
data = {
    "tune[title]": "LOLGisele-Bundchen-ultimate-attempt1",
    "tune[name]": "woman",
    "tune[branch]": "sd15",
    "tune[callback]": "https://optional-callback-url.com/webhooks/astria?user_id=1&tune_id=1",
    "tune[token]": "sks",
    "tune[prompts_attributes][0][callback]": "https://optional-callback-url.com/webhooks/astria?user_id=1&prompt_id=1&tune_id=1",
    "tune[prompts_attributes][0][text]": "Sample prompt text"
}

# Define the file paths for images
file_paths = [
    "/Users/sofiaisabellamendezdantas/astriaclient/images/02bf0816baef1e3bee1de7a5e33799dc.jpg",
    "/Users/sofiaisabellamendezdantas/astriaclient/images/Arezzo_Alto_Verão_2018_por_Gisele_Bündchen_07.jpg",
    "/Users/sofiaisabellamendezdantas/astriaclient/images/Arezzo_Fim_de_Ano_2018_com_Gisele_Bündchen_02.jpg",
    "/Users/sofiaisabellamendezdantas/astriaclient/images/Gisele_Bündchen_na_final_da_Copa_do_Mundo_de_2014.jpeg",
    "/Users/sofiaisabellamendezdantas/astriaclient/images/Gisele_Bundchen3.jpg",
    "/Users/sofiaisabellamendezdantas/astriaclient/images/GB.jpg",
    "/Users/sofiaisabellamendezdantas/astriaclient/images/GiseleBundchen.jpg",
    "/Users/sofiaisabellamendezdantas/astriaclient/images/Gisele_B.jpg",
    "/Users/sofiaisabellamendezdantas/astriaclient/images/Gisele_Bundchen-011_(16251942456)_(cropped2).jpg",
    "/Users/sofiaisabellamendezdantas/astriaclient/images/Arezzo_Fim_de_Ano_2018_com_Gisele_Bündchen_04.jpg",
    "/Users/sofiaisabellamendezdantas/astriaclient/images/Arezzo_Fim_de_Ano_2018_com_Gisele_Bündchen_05.jpg",
    "/Users/sofiaisabellamendezdantas/astriaclient/images/Arezzo_e_Gisele_Bündchen,_Coleção_Verão_2017_-_08.jpg",
    "/Users/sofiaisabellamendezdantas/astriaclient/images/Gisele_Bündchen_at_the_Fashion_Rio_Inverno_2006_(cropped).jpg"
]

# Create the files dictionary
files = [("tune[images][]", (open(file_path, "rb"))) for file_path in file_paths]

# Send the POST request to create the tune
response = requests.post(url, headers=headers, data=data, files=files)

# Print the response
print(response.status_code)
print(response.json())

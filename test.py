from flask import Flask, request, render_template
import requests, os, time
from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from msrest.authentication import CognitiveServicesCredentials
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

def get_text(image_url, computervision_client):
    # Open local image file
    read_response = computervision_client.read(image_url, raw=True)

    # Get the operation location (URL with an ID at the end)
    read_operation_location = read_response.headers["Operation-Location"]
    # Grab the ID from the URL
    operation_id = read_operation_location.split("/")[-1]

    # Retrieve the results 
    while True:
        read_result = computervision_client.get_read_result(operation_id)
        if read_result.status.lower() not in ["notstarted", "running"]:
            break
        time.sleep(1)

    # Get the detected text
    text = ""
    if read_result.status == OperationStatusCodes.succeeded:
        for page in read_result.analyze_result.read_results:
            for line in page.lines:
                # Get text in each detected line and do some fixes to the structure
                if (not text) or text[-1].strip() == "." or text[-1].strip() == ":":
                    text = text + "\n" + line.text
                else:
                    text = text + " " + line.text
    text = text.replace(" .", ".").replace(" ,", ",").replace(" :", ":")
    return text

def detect_language(text, key, region, endpoint):
    # Use the Translator detect function
    path = "/contentmoderator/moderate/v1.0/ProcessText/DetectLanguage"
    url = endpoint + path
    # Build the request
    params = {
        "api-version": "3.0"
    }
    headers = {
    "Ocp-Apim-Subscription-Key": key,
    "Ocp-Apim-Subscription-Region": region,
    "Content-type": "application/json"
    }
    body = [{
        "Text Content": text
    }]
    # Send the request and get response
    request = requests.post(url, params=params, headers=headers, json=body)
    
    response = request.json()
    print(response)
    # Get language
    language = response[0]["language"]
    # Return the language
    return language

def translate(text, source_language, target_language, key, region, endpoint):
    # Use the Translator translate function
    url = endpoint + "/translate"
    # Build the request
    params = {
        "api-version": "3.0",
        "from": source_language,
        "to": target_language
    }
    headers = {
        "Ocp-Apim-Subscription-Key": key,
        "Ocp-Apim-Subscription-Region": region,
        "Content-type": "application/json"
    }
    body = [{
        "text": text
    }]
    # Send the request and get response
    request = requests.post(url, params=params, headers=headers, json=body)
    response = request.json()
    # Get translation
    translation = response[0]["translations"][0]["text"]
    # Return the translation
    return translation

# @app.route('/', methods=['GET'])
# def index():
#     return render_template('index.html')


@app.route('/', methods=['GET'])
def index_post():
    print(1)
    # Read the values from the form
    image_url = 'https://nwzimg.wezhan.cn/contents/sitefiles2040/10204669/images/20257077.jpg'
    target_language = 'en'
    
    # Load the values from .env
    key = os.getenv("COG_SERVICE_KEY")
    region = os.getenv("COG_SERVICE_REGION")
    endpoint = os.getenv("ENDPOINT")
    COG_endpoint = os.getenv("COG_SERVICE_ENDPOINT")
    print(key)
    # Authenticate Computer Vision client
    computervision_client = ComputerVisionClient(COG_endpoint, CognitiveServicesCredentials(key))
    print(2)
    # Extract text
    text = get_text(image_url, computervision_client)
    print(text + key + region + endpoint)
    # Detect language
    language = detect_language(text, key, region, endpoint)
    print(language)
    # Translate text
    translated_text = translate(text, language, target_language, key, region, endpoint)
    print(3)
    # Call render template
    return render_template(
        'results.html',
        translated_text=translated_text,
        original_text=text,
        target_language=target_language
    )


if __name__ == '__main__':
    app.run(debug=True)
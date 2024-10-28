import requests

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }
    input_json = {
        "raw_document": {
            "text": text_to_analyze
        }
    }

    # Send the POST request to the Watson NLP service
    response = requests.post(url, headers=headers, json=input_json)

    # Check for successful request
    if response.status_code == 200:
        response_json = response.json()
        if 'text' in response_json:
            return response_json['text']
        else:
            return f"Unexpected response format: {response_json}"
    else:
        return f"Error: {response.status_code} - {response.text}"

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

        # Accessing the emotion data
        if 'emotionPredictions' in response_json and len(response_json['emotionPredictions']) > 0:
            emotions = response_json['emotionPredictions'][0]['emotion']

            # Extract emotion scores
            anger_score = emotions.get('anger', 0)
            disgust_score = emotions.get('disgust', 0)
            fear_score = emotions.get('fear', 0)
            joy_score = emotions.get('joy', 0)
            sadness_score = emotions.get('sadness', 0)

            # Create a dictionary with the results
            emotion_results = {
                'anger': anger_score,
                'disgust': disgust_score,
                'fear': fear_score,
                'joy': joy_score,
                'sadness': sadness_score
            }

            # Find the dominant emotion
            dominant_emotion = max(emotion_results, key=emotion_results.get)
            emotion_results['dominant_emotion'] = dominant_emotion

            return emotion_results
        else:
            return "Error: No emotion data found in the response."
    else:
        return f"Error: {response.status_code} - {response.text}"

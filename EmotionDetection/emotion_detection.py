import requests
import json

def generate_none_response():
    return {'anger': None, 'disgust': None, 'fear': None, 'joy': None, 'sadness': None, 'dominant_emotion': None}

def emotion_detector(text_to_analyze):
    if not text_to_analyze.strip():
        return generate_none_response()

    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    json_input = {"raw_document": {"text": text_to_analyze}}

    try:
        response = requests.post(url, headers=headers, json=json_input)
        if response.status_code == 400:
            return generate_none_response()

        response.raise_for_status()
        emotions = json.loads(response.text).get('emotionPredictions', [{}])[0].get('emotion', {})
        scores = {e: emotions.get(e, 0) for e in ['anger', 'disgust', 'fear', 'joy', 'sadness']}
        return {**scores, 'dominant_emotion': max(scores, key=scores.get, default=None)}

    except requests.exceptions.RequestException:
        return generate_none_response()

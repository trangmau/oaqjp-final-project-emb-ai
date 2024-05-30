import requests
import json

def emotion_detector(text_to_analyze):
    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    Headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    Input_json = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(URL, json = Input_json, headers=Headers)
    formated_response = json.loads(response.text)

    # Extract emotions and scores
    emotions = formated_response.get("emotion", {})
    anger_score = emotions.get("anger", 0)
    disgust_score = emotions.get("disgust", 0)
    fear_score = emotions.get("fear", 0)
    joy_score = emotions.get("joy", 0)
    sadness_score = emotions.get("sadness", 0)
    dominant_emotion_result = max(emotion_scores, key=emotion_scores.get)
    # Find the dominant emotion
    emotion_scores = {
        "anger": anger_score,
        "disgust": disgust_score,
        "fear": fear_score,
        "joy": joy_score,
        "sadness": sadness_score,
        "dominant_emotion": dominant_emotion_result
    }
    return emotion_scores
    

def start_here(input_text):
    detected_emotions = emotion_detector(input_text)
    temp_object = {
        "source_text": input_text,
        "emotionPredictions": detected_emotions
    }
    emotion_predictor(temp_object)
    
    
    
    
def emotion_predictor(detected_text):
    # here is the sample code I search def emotion_predictor(detected_text):
    if all(value is None for value in detected_text.values()):
        return detected_text
    if detected_text['emotionPredictions'] is not None:
        emotions = detected_text['emotionPredictions']
        anger = emotions['anger']
import requests
import json

def emotion_detector(text_to_analyze):
    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    Headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    Input_json = { "raw_document": { "text": text_to_analyze } }
    
    try:
        response = requests.post(URL, json=Input_json, headers=Headers)
        if response.status_code == 200:
            response_dict = response.json()  # Convert the response to a dictionary
            return response_dict
        elif response.status_code == 400:
            # Handle 400 status code by returning the dictionary with None values
            return {
                'anger': None,
                'disgust': None,
                'fear': None,
                'joy': None,
                'sadness': None,
                'dominant_emotion': None
            }
    except requests.RequestException as e:
        print(f"Error calling the API: {e}")
        return None
    
def emotion_predictor(detected_text):
    if isinstance(detected_text, dict):
        # Check if the input is a dictionary
        emotions = detected_text.get('emotionPredictions', [{}])[0].get('emotion', {})
        anger = emotions.get('anger')
        disgust = emotions.get('disgust')
        fear = emotions.get('fear')
        joy = emotions.get('joy')
        sadness = emotions.get('sadness')
        max_emotion = max(emotions, key=emotions.get)
        formated_dict_emotions = {
            'anger': anger,
            'disgust': disgust,
            'fear': fear,
            'joy': joy,
            'sadness': sadness,
            'dominant_emotion': max_emotion
        }
        return formated_dict_emotions
    else:
        # Handle cases where detected_text is not a dictionary
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    

#def start_here(input_text):
#   detected_emotions = emotion_detector(input_text)
 #   temp_object = {
  #      "source_text": input_text,
   #     "emotionPredictions": detected_emotions
    #}
    #emotion_predictor(temp_object)
    
    
    
    

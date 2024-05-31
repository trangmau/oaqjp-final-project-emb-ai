from flask import Flask, request, jsonify
from EmotionDetection.emotion_detection import emotion_detector, emotion_predictor

app = Flask(__name__)

@app.route('/emotionDetector', methods=['POST'])
def detect_emotion():
    data = request.get_json()
    text_to_analyze = data.get('text', '')

    # Check for empty input
    if not text_to_analyze.strip():
        return jsonify({
            'message': 'Input text cannot be empty.',
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }), 400

    # Call emotion_detector function
    detected_text = emotion_detector(text_to_analyze)
    
    # Call emotion_predictor function
    result = emotion_predictor(detected_text)

    # Prepare the response in the required format
    if result['dominant_emotion']:
        response = (f"For the given statement, the system response is 'anger': {result['anger']}, "
                    f"'disgust': {result['disgust']}, 'fear': {result['fear']}, 'joy': {result['joy']} "
                    f"and 'sadness': {result['sadness']}. The dominant emotion is {result['dominant_emotion']}.")
    else:
        response = "No dominant emotion found."

    return jsonify({'message': response})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

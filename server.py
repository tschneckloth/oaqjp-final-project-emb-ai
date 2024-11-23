from flask import Flask, request, jsonify, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/emotionDetector', methods=['GET'])
def emotion_detector_endpoint():
    # Get the statement from the query parameters using 'textToAnalyze'
    text_to_analyze = request.args.get('textToAnalyze', '')

    if not text_to_analyze:
        return jsonify({"error": "No text provided"}), 400

    # Process the text using the emotion_detector function
    emotions = emotion_detector(text_to_analyze)

    # Prepare the formatted response
    formatted_response = (
        f"For the given statement, the system response is "
        f"'anger': {emotions['anger']}, 'disgust': {emotions['disgust']}, "
        f"'fear': {emotions['fear']}, 'joy': {emotions['joy']} and "
        f"'sadness': {emotions['sadness']}. The dominant emotion is <strong>{emotions['dominant_emotion']}</strong>."
    )

    return formatted_response

if __name__ == "__main__":
    app.run(host="localhost", port=5000, debug=True)

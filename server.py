from flask import Flask, request, jsonify, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/emotionDetector', methods=['GET'])
def emotion_detector_endpoint():
    text_to_analyze = request.args.get('textToAnalyze', '')

    if not text_to_analyze.strip():
        return "Invalid text! Please try again!", 400

    emotions = emotion_detector(text_to_analyze)

    if emotions['dominant_emotion'] is None:
        return "Invalid text! Please try again!", 400

    return (
        f"For the given statement, the system response is "
        f"'anger': {emotions['anger']}, 'disgust': {emotions['disgust']}, "
        f"'fear': {emotions['fear']}, 'joy': {emotions['joy']} and "
        f"'sadness': {emotions['sadness']}. The dominant emotion is {emotions['dominant_emotion']}."
    )

if __name__ == "__main__":
    app.run(host="localhost", port=5000, debug=True)

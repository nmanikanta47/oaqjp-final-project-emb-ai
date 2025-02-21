"""
    This module has web api methods which detect emotion of the supplied string.
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_analyzer():
    """
    This function detects emotion of the supplied string.
    Args:
        arg1 (str): The first argument, a string.
    Returns:
        emotion scores if the operation was successful.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!."
    return response

@app.route("/")
def render_index_page():
    """
    This function return index page
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

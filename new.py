# app.py
from flask import Flask, render_template, request
from transcript import fetch_transcript

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/transcript', methods=['POST'])
def get_transcript():
    video_url = request.form['video_url']
    transcript = fetch_transcript(video_url)
    return render_template('index.html', transcript=transcript)

if __name__ == '__main__':
    app.run(debug=True)

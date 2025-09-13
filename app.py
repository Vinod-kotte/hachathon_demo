from flask import Flask, render_template, request, send_file, jsonify
from model.crop_model import get_advice
import speech_recognition as sr
from gtts import gTTS
from werkzeug.utils import secure_filename
import os

app = Flask(_name_)
app.config['UPLOAD_FOLDER'] = 'uploads/'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/text_input', methods=['POST'])
def text_input():
    user_text = request.form['text']
    advice = get_advice(user_text)
    tts = gTTS(text=advice, lang='hi')
    audio_file = os.path.join(app.config['UPLOAD_FOLDER'], 'advice.mp3')
    tts.save(audio_file)
    return jsonify({'advice': advice, 'audio': '/audio/advice.mp3'})

@app.route('/voice_input', methods=['POST'])
def voice_input():
    file = request.files['voice']
    filename = secure_filename(file.filename)
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(file_path)

    recognizer = sr.Recognizer()
    with sr.AudioFile(file_path) as source:
        audio = recognizer.record(source)
        text = recognizer.recognize_google(audio, language='en-IN')

    advice = get_advice(text)
    tts = gTTS(text=advice, lang='hi')
    audio_file = os.path.join(app.config['UPLOAD_FOLDER'], 'advice.mp3')
    tts.save(audio_file)
    return jsonify({'advice': advice, 'audio': '/audio/advice.mp3'})

@app.route('/photo_input', methods=['POST'])
def photo_input():
    file = request.files['photo']
    filename = secure_filename(file.filename)
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(file_path)

    advice = get_advice(file_path, is_image=True)
    tts = gTTS(text=advice, lang='hi')
    audio_file = os.path.join(app.config['UPLOAD_FOLDER'], 'advice.mp3')
    tts.save(audio_file)
    return jsonify({'advice': advice, 'audio': '/audio/advice.mp3'})

@app.route('/audio/<filename>')
def serve_audio(filename):
    return send_file(os.path.join(app.config['UPLOAD_FOLDER'], filename))

if _name_ == '_main_':
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    app.run(debug=True)
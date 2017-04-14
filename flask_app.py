#!/usr/bin/env python

from flask import Flask
import glob
from flask import json, Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/list_audio')
def play():
    return render_template('list_audio.html', audio_files=glob.glob('static/audio/*.wav'))

@app.route('/play_audio')
def play_sound():
    path = request.args.get('path', None)
    if path:
        return render_template('play_audio.html', audio_path=path)
    else: 
        return "path argument missing", 404

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.route('/')
def home():
    # etc etc, flask app code
    return render_template('layout.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', use_reloader=True)
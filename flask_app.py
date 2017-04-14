#!/usr/bin/env python

from flask import Flask
from flask import json, Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    # etc etc, flask app code
    return render_template('main.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', use_reloader=True)
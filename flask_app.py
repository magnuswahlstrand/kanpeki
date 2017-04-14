#!/usr/bin/env python

from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    # etc etc, flask app code
    return 'Konnichiwa, Kanpeki Sekai!'

if __name__ == '__main__':
    app.run()
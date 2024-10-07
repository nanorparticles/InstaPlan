# -*- coding: utf-8 -*-

from flask import Flask, redirect, request, url_for, session
import requests

app = Flask(__name__)
app.secret_key = ''  # You should set a proper secret key here for security purposes.

@app.route('/')
def home(): 
    return 'Welcome to InstaPlan OAuth'

if __name__ == '__main__': 
    app.run(debug=True)

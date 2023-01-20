#python
#221 flask-post-requests

import flask
from flask import Flask
import flask_cors
from flask_cors import CORS
import time, json
import sqlite3
import random

web = Flask(__name__)
CORS(web)

def textfile():
    quotes = ["We cannot solve problems with the kind of thinking we employed when we came up with them.","Learn as if you will live forever, live like you will die tomorrow.","Stay away from those people who try to disparage your ambitions. Small minds will always do that, but great minds will give you a feeling that you can become great too.","When you give joy to other people, you get more joy in return. You should give a good thought to happiness that you can give out.","When you change your thoughts, remember to also change your world.","Success is not final; failure is not fatal: It is the courage to continue that counts.","It is better to fail in originality than to succeed in imitation."]
    file = open("entry.txt", "w")
    for i in quotes:
        i +="\n"
        file.write(i)

@web.route("/quote",methods=['POST','GET'])
def main():
    #sample url: http://127.0.0.1:5000/
    #output: a text string literal, includes information for help
    #response is not json encoded
    file = open("entry.txt", "r")
    quotes = file.readlines()
    quote = random.choice(quotes)
    return f"As once said, '{quote}'"
    
@web.route("/admin",methods=['POST','GET'])
def admin():
    #sample url: http://127.0.0.1:5000/
    #output: a text string literal, includes information for help
    #response is not json encoded\
    file = open('entry.txt', 'r')
    Lines = file.readlines()

    count = 0
    for line in Lines:
        count += 1
        yield f"Line {count}: '{line.strip()}'</br>"

@web.route("/new",methods=['POST','GET'])
def new():
    #sample url: http://127.0.0.1:5000/
    #output: a text string literal, includes information for help
    #response is not json encoded\
    file = open("entry.txt", "r")
    quotes = file.readlines()
    count = -1
    for line in quotes:
        count += 1
        quotes = list(quotes)
        quote = [item.split('\n')[0] for item in quotes]
    return quote



textfile()
web.run()
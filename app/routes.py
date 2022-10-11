# from crypt import methods
from urllib import request
from flask import render_template
from app import app
import os

global ls
ls=[]

@app.route('/<string:content>', methods=['POST'])
def index(content, ls):
    return ls.append(content)

@app.route('/')
def display(ls):
    return render_template("index.html", lis=ls)

if __name__ == "__main__":
    app.run()

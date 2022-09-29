# -*- coding: utf-8 -*-
# save this as app.py
#https://www.youtube.com/watch?v=Z1RJmh_OqeA
#https://www.fullstackpython.com/blog/responsive-bar-charts-bokeh-flask-python-3.html
from flask import Flask,render_template,url_for

app = Flask(__name__)

@app.route('/') #url base
def index():
    
    return render_template('index.html')

@app.route('/data') #url /data
def data():
    return render_template('data.html')

if __name__ == "__main__":
    app.run(debug=True)
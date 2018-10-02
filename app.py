import os
import datetime
from flask import Flask, render_template

app = Flask(__name__)

images = []
for filename in os.listdir('static/img/big'):
        if filename.endswith(".jpg"):
                images.append(filename)
        else:
                continue

@app.route('/')
def index():
        return render_template('index.html',images=images,style="tiles",year=datetime.datetime.now().year)
@app.route('/<style>')
def style(style):
        return render_template('index.html',images=images,style=style,year=datetime.datetime.now().year)

if __name__ == '__main__':
	app.run()

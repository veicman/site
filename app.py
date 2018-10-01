import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
        images = []
        for filename in os.listdir('static/img/big'):
                if filename.endswith(".jpg"):
                        images.append(filename)
                else:
                        continue
        return render_template('index.html',images=images,style="compact")

@app.route('/<style>')
def style(style):
        images = []
        for filename in os.listdir('static/img/big'):
                if filename.endswith(".jpg"):
                        images.append(filename)
                else:
                        continue
        return render_template('index.html',images=images,style=style)

if __name__ == '__main__':
	app.run()

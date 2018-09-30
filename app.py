import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
        images = []
        for filename in os.listdir('static/img'):
                if filename.endswith(".jpg") and filename != "0001.jpg":
                        images.append(os.path.join('static/img', filename))
                else:
                        continue
        return render_template('index.html',images=images)

if __name__ == '__main__':
	app.run()

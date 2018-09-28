from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
	return "nginx,gunicorn,flask"

if __name__ == '__main__':
	app.run()
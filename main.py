from flask import  *

app = Flask(__name__)

@app.route('/')
def index():
	return 'Welcome to Python Flask World v3.0 CI/CD'


if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8080)
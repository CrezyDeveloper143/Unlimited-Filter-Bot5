from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'https://youtube.com/@technical_rakesh_01'


if __name__ == "__main__":
    app.run()

from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return "Hello World! changed by Hyder at 5:22 pm"

if __name__ == "__main__":
    application.run()

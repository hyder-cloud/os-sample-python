from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return "Hello World! updated by Hyder on 18th June."

if __name__ == "__main__":
    application.run()

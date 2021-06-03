#Using Flask
from flask import Flask
application = Flask(__name__)

@application.route("/5000")
def enter():
  return "this is my new change in webpage"

#pass this if this is the main function
if __name__ == '__main__':
  application.run(debug=True)

#Using Flask
from flask import Flask
application = Flask(__name__)

@application.route("/500")
def enter():
<<<<<<< HEAD
  return "this is my new change in web application page"

#pass this if this is the main function
if __name__ == '__main__':
  application.run(debug=True)
=======
  return "this is my new webpage"

#pass this if this is the main function
if __name__ == '__main__':
  application.run()
>>>>>>> 47a2b0d4c0c3fa3903e82e6f1bb5678e7357c037

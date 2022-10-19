from flask import Flask
app = Flask(__name__)

@app.route('/')                                     #homepage is the default, the link: "http://127.0.0.1:5000/"
def index():
  return "<h1>Hello Puppy! </h1>"

@app.route('/information')                          #if typed on the URL: "http://127.0.0.1:5000/information"
def info():
    return "<h1>Puppies are cute! </h1>"            #ONLY THIS TEXT WILL BE DISPLAYED!

if __name__ == '__main__':
  app.run()

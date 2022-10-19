from flask import Flask
app = Flask(__name__)

@app.route('/')                                     #homepage is the default, the link: "http://127.0.0.1:5000/"
def index():
  return "<h1>Hello Puppy! </h1>"

@app.route('/information')                          #if typed on the URL: "http://127.0.0.1:5000/information"
def info():
    return "<h1>Puppies are cute! </h1>"            #ONLY THIS TEXT WILL BE DISPLAYED!

@app.route('/puppy/<name>')
def puppy (name):
    if (name[len(name) -1] != "y"):
        return "<h1> This is a page for {}</h1>".format(name + "y")
    elif (name[len(name) - 1] == "y"):
        return "<h1> This is a page for {}</h1>".format(name[0 : len(name) - 1] + "iful")                 #if typed on the URL: "http://127.0.0.1:5000/information/<name>"
                                                                                                          #it will print "This is a page for <name>"
                                                                                                          #where <name> is any type of string
if __name__ == '__main__':
  app.run()

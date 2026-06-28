from flask import Flask
# It creates an instance of the Flask() class which will be the WSGI

app=Flask(__name__)

@app.route("/")
def welcome():
    return "Welcome to flask course. Amazing course"

@app.route("/index" )
def index():
    return "Welcome to Index page"

if __name__ == "__main__":
    app.run(debug=True)

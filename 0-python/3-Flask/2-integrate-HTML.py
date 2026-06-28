from flask import Flask,render_template
# It creates an instance of the Flask() class which will be the WSGI

app=Flask(__name__)

@app.route("/")
def welcome():
    return "<h1>Welcome to flask course. Amazing course</h1>"

@app.route("/index" )
def index():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')

if __name__ == "__main__":
    app.run(debug=True)

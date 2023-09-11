#Importing flask module in the project
from flask import Flask,render_template

#Create an object of the Flask class
app = Flask(__name__)

#The route() function of the Flask class 
@app.route("/")

#‘/’ URL is bound with first_flask function.
def first_flask():

    return render_template("mine.html",name="Soham")
@app.route("/second")

#‘/’ URL is bound with first_flask function.
def second_flask():

    return render_template("mother.html",name="Pragati")

@app.route("/third")

#‘/’ URL is bound with first_flask function.
def third_flask():

    return render_template("father.html",name="Sachin")

#run the application on local server
app.run()

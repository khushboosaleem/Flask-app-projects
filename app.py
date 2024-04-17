## Flask App Routing

from flask import Flask, render_template, request, redirect, url_for

## Create a simple flask application
app = Flask(__name__)

@app.route("/", methods=["GET"])
def welcome():
    return "<h1>Hello world</h1>"


@app.route("/index", methods=["GET"])
def index():
    return "<h2>Welcome to the index page</h2>"


# variable rule
@app.route("/success/<int:score>")
def success(score):
    return "The person has passed and the score is: " + str(score)


@app.route("/fail/<int:score>")
def fail(score):
    return "The person has failed and the score is " + str(score)


@app.route('/calculate', methods=["GET", "POST"])
def calculate():
    # If the request method is GET, render the calculate.html template
    if request.method == "GET":
        return render_template("calculate.html")
    else:
        # Retrieve form data and convert to float
        maths = float(request.form['maths'])
        science = float(request.form['science'])
        history = float(request.form['history'])
        
        # Calculate average marks
        average_marks = (maths + science + history) / 3
        result = "" 
        # Determine result based on average marks
        if average_marks >= 50:
            result = "success"
        else:
            result = "fail"

        # Render the result.html template with the average_marks
        return render_template('result.html', results=average_marks)



if __name__ == "__main__":
    app.run(debug=True)

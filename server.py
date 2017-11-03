from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return "No ninjas here"
@app.route('/ninja')
def ninja():
    return render_template('ninja.html')
@app.route('/ninja/<color>')
def ninjaColor(color):
    color = color
    if color == "red":
        image = "/static/images/raphael.jpg"
        turtle = "Raphael"
    elif color == "orange":
        image = "/static/images/michelangelo.jpg"
        turtle = "Michelangelo"
    elif color == "blue":
        image = "/static/images/leonardo.jpg"
        turtle = "Leonardo"
    elif color == "purple":
        image = "/static/images/donatello.jpg"
        turtle = "Donatello"
    else:
        image = "/static/images/notapril.jpg"
        turtle = "April"
    return render_template('/ninjaColor.html', image = image, turtle = turtle)

app.run(debug=True)
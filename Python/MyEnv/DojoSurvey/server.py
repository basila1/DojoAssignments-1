from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
  return render_template("index.html")

@app.route('/results', methods=['POST'])
def create_user():
   name = request.form['name']
   location = request.form['location']
   language = request.form['language']
   description = request.form['description']
   return render_template("results.html", name=name, location=location, language=language, description=description)

app.run(debug=True)

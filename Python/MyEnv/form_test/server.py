from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
  return render_template("index.html")

@app.route('/users', methods=['POST'])
def create_user():
   print "Got Post Info"
   name = request.form['name']
   email = request.form['email']
   return redirect('/')

@app.route('/show')
def show():
  return render_template("user.html", name="jay", email="hey")

app.run(debug=True)

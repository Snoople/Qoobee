from flask import Flask, render_template # include the flask library 

app = Flask(__name__)

#https://stackoverflow.com/questions/34902378/where-do-i-get-a-secret-key-for-flask/34903502  if we wanna go live
app.secret_key = 'personal secrets'
app.config['SESSION_TYPE'] = 'filesystem'

@app.route("/")
def home():
  return render_template("home.html")

@app.route("/about")
def about():
  return render_template("about.html")

if __name__ == '__main__': 
   app.run(port=5000, debug=True) # application will start listening for web request on port 5000
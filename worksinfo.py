from flask import Flask, render_template,  redirect, request

app = Flask(__name__)
app.config['SCRET_KEY'] = 'Wokrsinfo23'


@app.route("/")
def home():
    return render_template("login.html", title="login")
    
    
@app.route("/login")
def login():
    
    nome= request.form.get('email')
    nome= request.form.get('senha')
    
    
    
if __name__ in "__main__":
    app.run(debug=True)

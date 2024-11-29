from flask import Flask, render_template, request, redirect, url_for, session
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)

userAdmin = {
    "username": "Miguel",
    "password": "4321"
}

userAnggota = {
    "username": "Adams",
    "password": "1234"
}

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/admin')
def admin():
    if session.get("user") == userAdmin["username"]:
        return render_template("admin.html")
    else:
        return redirect(url_for("home"))

@app.route('/anggota')
def anggota():
    if session.get("user") == userAnggota["username"]:
        return render_template("anggota.html")
    else:
        return redirect(url_for("home"))

@app.route('/login', methods=["POST", "GET"])
def login():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        if username == userAdmin["username"] and password == userAdmin["password"]:
            session["user"] = username
            return redirect(url_for('admin'))
        elif username == userAnggota["username"] and password == userAnggota["password"]:
            session["user"] = username
            return redirect(url_for('anggota'))
        else:
            return "Login failed, incorrect username or password", 403
    return redirect(url_for("home"))

@app.route('/logout')
def logout():
    session.pop("user", None)
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)

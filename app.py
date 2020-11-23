from flask import Flask, render_template, flash, redirect, url_for
from forms import LoginForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "supersecret"

@app.route('/', methods=["GET", "POST"])
def landing_page():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}'.format(form.username.data))
        return redirect("/user_page")
    return render_template('landing_page.html', form=form)

@app.route("/user_page")
def user_page():
    return render_template('user_page.html')

@app.route("/settings")
def settings():
    return render_template('construction.html')

@app.route("/friends")
def friends():
    return render_template('construction.html')

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
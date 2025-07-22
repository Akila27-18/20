from flask import Flask, render_template, flash, redirect, url_for
from forms import GymSignupForm

app = Flask(__name__)
app.secret_key = 'supersecretkey'

@app.route('/', methods=['GET', 'POST'])
def signup():
    form = GymSignupForm()
    if form.validate_on_submit():
        name = form.name.data
        flash(f"Welcome to our gym, {name}!", "success")
        return redirect(url_for('signup'))
    return render_template('signup.html', form=form)

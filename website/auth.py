from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', "POST"])
def login():
    data = request.form
    print(data)
    return render_template('login.html', user='Rahul')


@auth.route('/logout')
def logout():
    return "<h1>logout</h1>"


@auth.route('/sign-up', methods=['GET', "POST"])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        if len(email) < 4:
            flash('Email must be greater than 4 characters', category='error')
        elif password1 != password2:
            flash('Password mismatched', category='error')
        elif len(first_name) < 5:
            flash("First Name must be atleast 5 characters", category='error')
        elif len(password1) < 7:
            flash('Password length must be greater than 7', category='error')
        else:
            flash('Account Created Succesfully! ', category='success')

    return render_template('signup.html')

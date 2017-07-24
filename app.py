from flask import Flask, render_template
from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired, Length, AnyOf


app = Flask(__name__)
app.config['SECRET_KEY'] = 'SECRET_KEY'
# verify robos by google
app.config['RECAPTCHA_PUBLIC_KEY'] = 'Site key'
app.config['RECAPTCHA_PRIVATE_KEY'] = 'Secret key'
# set to True to disable recaptcha
app.config['TESTING'] = True


class LoginForm(FlaskForm):
    username = StringField('username',
        validators=[InputRequired('the username is required'),
            Length(min=5, max=10, message='Must between 5 and 10 characters')])
    password = PasswordField('password',
        validators=[InputRequired('the password is required'),
            Length(min=5, max=10, message='Must between 5 and 10 characters'),
            AnyOf(values=['password', 'secret'])])
    recaptcha = RecaptchaField()

@app.route('/form', methods=['GET', 'POST'])
def form():
    form = LoginForm()

    if form.validate_on_submit():
        return '<h1>user name is {}, password is {}'.format(form.username.data, form.password.data)
    return render_template('form.html', form = form)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

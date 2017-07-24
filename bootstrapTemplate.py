from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField, RadioField, SelectField
from wtforms.validators import InputRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secretkey'


class MyForm(FlaskForm):
    email = StringField('Email', validators=[InputRequired()])
    password = StringField('Password', validators=[InputRequired()])
    textarea = TextAreaField('TextArea')
    radios = RadioField('Radio', default='option1',
                                choices=[('option1', 'option1 on this'),
                                        ('option2', 'option2 on this')])
    selects = SelectField('Select', choices=[('1','1'), ('2','2'), ('3','3')])

@app.route('/', methods=['GET', 'POST'])
def form():
    form = MyForm()

    if form.validate_on_submit():
        return render_template('result.html', email=form.email.data,
            password=form.password.data, textarea=form.textarea.data,
            radios=form.radios.data, selects=form.selects.data)
    return render_template('form_bootstrap.html', form=form)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

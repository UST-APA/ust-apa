from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    #Data Required will warn you if the current table was not filled
    start = SelectField('Start Position',
                        validators=[DataRequired(message='Please choose start point')],
                        choices=[('default','000'),('1','111'),('2','222')]) #choice tuple (value, text_to_show)

    destination = SelectField('Your Destination',
                              validators=[DataRequired(message='Please choose you destination')],
                              choices=[('default','000'),('1','111'),('2','222')])

    submit = SubmitField('submit')
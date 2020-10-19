from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField
from wtforms.validators import DataRequired

class MenuForm(FlaskForm):
    #Data Required will warn you if the current table was not filled
    start = SelectField('Start Position',
                        validators=[DataRequired(message='Please choose start point')],
                        choices=[('1','default')]) #choice tuple (value, text_to_show)

    destination = SelectField('Your Destination',
                              validators=[DataRequired(message='Please choose you destination')],
                              choices=[('1','default')])

    time = SelectField('Query Send Time',
                       choices=[('0','12:00 am'),('1','1:00 am'),('2','2:00 am'),('3','3:00 am'),
                                ('4','4:00 am'),('5','5:00 am'),('6','6:00 am'),('7','7:00 am'),
                                ('8','8:00 am'),('9','9:00 am'),('10','10:00 am'),('11','11:00 am'),
                                ('12','12:00 pm'),('13','1:00 pm'),('14','2:00 am'),('15','3:00 pm'),
                                ('16','4:00 pm'),('17','5:00 pm'),('18','6:00 pm'),('19','7:00 pm'),
                                ('20','8:00 pm'),('21','9:00 pm'),('22','10:00 pm'),('23','11:00 pm'),])

    submit = SubmitField('submit')
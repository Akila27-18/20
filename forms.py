from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, EmailField, RadioField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email, NumberRange, InputRequired

class GymSignupForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    age = IntegerField("Age", validators=[DataRequired(), NumberRange(min=16, message="You must be at least 16 years old.")])
    email = EmailField("Email", validators=[DataRequired(), Email()])
    plan = RadioField("Membership Plan", choices=[("monthly", "Monthly"), ("yearly", "Yearly")], validators=[InputRequired()])
    terms = BooleanField("I accept the terms and conditions", validators=[DataRequired(message="You must accept the terms.")])
    submit = SubmitField("Join Now")

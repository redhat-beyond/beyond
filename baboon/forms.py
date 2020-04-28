from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError
from baboon.models import Users


class RegistrationForm(FlaskForm):
    username = StringField('Username:', validators=[DataRequired(), Length(min=2, max=20)],
                           render_kw={"placeholder": "Enter Username"})
    password = PasswordField('Password:', validators=[DataRequired()], render_kw={"placeholder": "Enter Password"})
    conf_password = PasswordField('Confirm Password:', validators=[DataRequired(), EqualTo('password')],
                                  render_kw={"placeholder": "Enter Password again"})

    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        db_username = Users.query.filter_by(name=username.data).first()
        if db_username:
            raise ValidationError("A user by that username already exists!")

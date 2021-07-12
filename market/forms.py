from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import Length,EqualTo,Email,DataRequired,ValidationError
from market.models import User

class RegisterForm(FlaskForm):

    def validate_username(self, username_to_validate):
        user = User.query.filter_by(name=username_to_validate.data).first()
        if user:
            raise ValidationError('Username already exists! please try different  username')
    def validate_email_address(self, email_to_validate):
        email_address =User.query.filter_by(email_address=email_to_validate.data).first()
        if email_address:
            raise ValidationError('Email address already exists, please try new one')

    username = StringField(label='Username :',validators=[Length(min=2,max=30),DataRequired()])
    email_address=StringField(label='Email :',validators=[Email(),DataRequired()])
    password1=PasswordField(label='Password:', validators=[Length(min=6),DataRequired()])
    password2=PasswordField(label='Confirmed password:',validators=[EqualTo('password1'),DataRequired()])
    submit=SubmitField(label='Create Account')


class LoginForm(FlaskForm):
    username = StringField(label='User Name',validators=[DataRequired()])
    password = PasswordField(label='Password', validators=[DataRequired()])
    submit = SubmitField(label='Sign in')

class PurchaseItemForm(FlaskForm):
    submit = SubmitField(label='Purchase Item')


class SellItemForm(FlaskForm):
    submit = SubmitField(label='Sell Item !!')

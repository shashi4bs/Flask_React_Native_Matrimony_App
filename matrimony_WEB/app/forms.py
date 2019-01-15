from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField, IntegerField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo

# form segment here
# make sure you have flask_wtf installed on your virtual env
# refer requirements.txt 

class SignupForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    email_id = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    repeat_password = PasswordField('Repeat Password', validators=[DataRequired(),EqualTo('password')])
    submit = SubmitField('Register')
            
class LoginForm(FlaskForm):
    email_id = StringField('Email',validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')


class ProfileForm(FlaskForm):
    Age = IntegerField('Age', validators=[DataRequired()])
    Height = IntegerField('Height', validators=[DataRequired()])
    marital_status = [('NeverMarried','NeverMarried'),('Divorced','Divorced'),('AwaitingDivorce','AwaitingDivorce'),('Widowed','Widowed')]
    religion = [('Christian','Christian'),('Muslim','Muslim'),('Hindu','Hindu'),('Sikh','Sikh'),('Buddhist','Buddhist'),('Jain','Jain')]
    language = [('Urdu','Urdu'),('Hindi','Hindi'),('Marathi','Marathi'),('Punjabi','Punjabi'),('Sindhi','Sindhi'),('Kashmiri','Kashmiri'),('Gujarati','Gujarati'),('Malayalam','Malayalam'),('Tamil','Tamil'),('Assamese','Assamese'),('Bengali','Bengali'),('Kannada','Kannada'),('Nepali','Nepali'),('Telugu','Telugu'),('Tulu','Tulu'),('Odia','Odia'),('English','English'),('Konkani','Konkani')]
    country = [('Pakistan','Pakistan'),('India','India'),('USA','USA'),('Australia','Australia'),('Bangladesh','Bangladesh'),('Canada','Canada'),('Indonesia','Indonesia'),('Kuwait','Kuwait'),('SouthAfrica','SouthAfrica'),('UnitedArabEmirates','UnitedArabEmirates'),('UnitedKingdom','UnitedKingdom')]
    food = [('Eggetarian','Eggetarian'),('Vegetarian','Vegetarian'),('Non_Vegetarian','Non_Vegetarian'),('OccasionallyNon_Vegetarian','OccasionallyNon_Vegetarian')]
    drinks = [('DoesntDrink','DoesntDrink'),('DrinksOccasionally','DrinksOccasionally'),('DrinksOften','DrinksOften')]
    smokes = [('DoesntSmoke','DoesntSmoke'),('SmokesOften','SmokesOften'),('SmokesOccasionally','SmokesOccasionally')]
    skin_tone = [('WeatishskinTone','WeatishskinTone'),('Fairskinned','Fairskinned'),('Darkskinned','Darkskinned'),('VeryFairskinned','VeryFairskinned')]
    build = [('AverageBuild','AverageBuild'),('AthleticBuild','AthleticBuild'),('HeavyBuild','HeavyBuild'),('SlimBuild','SlimBuild')]
    Gender = SelectField('Gender', choices=[('Male','Male'),('Female','Female')])
    Marital_Status = SelectField('Marital Status', choices=marital_status)
    Education = StringField('Education', validators=[DataRequired()])
    Profession = StringField('Profession', validators=[DataRequired()])
    Religion = SelectField('Religion', choices=religion)
    Language = SelectField('Language', choices=language)
    City = StringField('City', validators=[DataRequired()])
    Country = SelectField('Country', choices=country)
    Food = SelectField('Food', choices=food)
    Drinks = SelectField('Drinks', choices=drinks)
    Smokes = SelectField('Smokes', choices=smokes)
    Skin_Tone = SelectField('Skin_Tone', choices=skin_tone)
    Build = SelectField('Build', choices=build)
    submit = SubmitField('Upadte_Info')


# For profileFrom "Didnt_Matter" is not available. remaining enteries can be made same for both profilezForm and preferencesFrom 



class PrefrencesForm(FlaskForm):
    marital_status = [('NeverMarried','NeverMarried'),('Divorced','Divorced'),('AwaitingDivorce','AwaitingDivorce'),('Widowed','Widowed'),('Didnt_Matter','Didnt_Matter')]
    religion = [('Christian','Christian'),('Muslim','Muslim'),('Hindu','Hindu'),('Sikh','Sikh'),('Buddhist','Buddhist'),('Jain','Jain'),('Didnt_Matter','Didnt_Matter')]
    language = [('Urdu','Urdu'),('Hindi','Hindi'),('Marathi','Marathi'),('Punjabi','Punjabi'),('Sindhi','Sindhi'),('Kashmiri','Kashmiri'),('Gujarati','Gujarati'),('Malayalam','Malayalam'),('Tamil','Tamil'),('Assamese','Assamese'),('Bengali','Bengali'),('Kannada','Kannada'),('Nepali','Nepali'),('Telugu','Telugu'),('Tulu','Tulu'),('Odia','Odia'),('English','English'),('Konkani','Konkani'),('Didnt_Matter','Didnt_Matter')]
    country = [('Pakistan','Pakistan'),('India','India'),('USA','USA'),('Australia','Australia'),('Bangladesh','Bangladesh'),('Canada','Canada'),('Indonesia','Indonesia'),('Kuwait','Kuwait'),('SouthAfrica','SouthAfrica'),('UnitedArabEmirates','UnitedArabEmirates'),('UnitedKingdom','UnitedKingdom'),('Didnt_Matter','Didnt_Matter')]
    food = [('Eggetarian','Eggetarian'),('Vegetarian','Vegetarian'),('Non_Vegetarian','Non_Vegetarian'),('OccasionallyNon_Vegetarian','OccasionallyNon_Vegetarian'),('Didnt_Matter','Didnt_Matter')]
    drinks = [('DoesntDrink','DoesntDrink'),('DrinksOccasionally','DrinksOccasionally'),('DrinksOften','DrinksOften'),('Didnt_Matter','Didnt_Matter')]
    smokes = [('DoesntSmoke','DoesntSmoke'),('SmokesOften','SmokesOften'),('SmokesOccasionally','SmokesOccasionally'),('Didnt_Matter','Didnt_Matter')]
    skin_tone = [('WeatishskinTone','WeatishskinTone'),('Fairskinned','Fairskinned'),('Darkskinned','Darkskinned'),('VeryFairskinned','VeryFairskinned'),('Didnt_Matter','Didnt_Matter')]
    build = [('AverageBuild','AverageBuild'), ('AthleticBuild','AthleticBuild'), ('HeavyBuild','HeavyBuild'), ('SlimBuild','SlimBuild'),('Didnt_Matter','Didnt_Matter')]
 
    Marital_Status = SelectField('Marital_Status', choices=marital_status)
    Religion = SelectField('Religion', choices=religion)
    Language = SelectField('Language', choices=language)
    Country = SelectField('Country', choices=country)
    Food = SelectField('Food', choices=food)
    Drinks = SelectField('Drinks', choices=drinks)
    Smokes = SelectField('Smokes', choices=smokes)
    Skin_Tone = SelectField('Skin_Tone', choices=skin_tone)
    Build = SelectField('Build', choices=build)
    submit = SubmitField('Update Prefrences')

 

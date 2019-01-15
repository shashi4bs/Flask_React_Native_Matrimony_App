'''
DataBase implementation here
db = database instance craeted by flask SqlAlchemy
# each class extending db.Model refers to a table that will be created or updated on commit to database "flask db init; flask db migrate -m ""; flask db upgrade"
'''

from app import db
from datetime import datetime
import enum
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from app import login


class gender(enum.Enum):
    Male = 'Male'
    Female = 'Female'

class marital_status(enum.Enum):
    NeverMarried = "NeverMarried"
    Divorced = "Divorced"
    AwaitingDivorce = "AwaitingDivorce"
    Widowed = "Widowed"
    Didnt_Matter = "Didnt_Matter"

class religion(enum.Enum):
    Christian = "Christian"
    Muslim = "Muslim"
    Hindu = "Hindu"
    Sikh = "Sikh"
    Buddhist = "Buddhist"
    Jain = "Jain"
    Didnt_Matter = "Didnt_Matter"

class language(enum.Enum):
    Urdu = "Urdu"
    Hindi = "Hindi"
    Marathi = "Marathi"
    Punjabi = "Punjabi"
    Sindhi = "Sindhi"
    Kashmiri = "Kashmiri"
    Gujarati = "Gujarati"
    Malayalam = "Malayalam"
    Tamil = "Tamil"
    Assamese = "Assamese"
    Bengali = "Bengali"
    Kannada = "Kannada"
    Nepali = "Nepali"
    Telugu = "Telugu"
    Tulu = "Tulu"
    Odia = "Odia"
    English = "English"
    Konkani = "Konkani"
    Didnt_Matter = "Didnt_Matter"

class country(enum.Enum):
    Pakistan = "Pakistan"
    India = "India"
    USA = "USA"
    Australia = "Australia"
    Bangladesh = "Bangladesh"
    Canada = "Canada"
    Indonesia = "Indonesia"
    Kuwait = "Kuwait"
    SouthAfrica = "SouthAfrica"
    UnitedArabEmirates = "UnitedArabEmirates"
    UnitedKingdom = "UnitedKingdom"
    Didnt_Matter = "Didnt_Matter"


class food(enum.Enum):
    Eggetarian = "Eggetarian"
    Vegetarian = "Vegetarian"
    Non_Vegetarian = "Non_Vegetarian"
    OccasionallyNon_Vegetarian = "OccasionallyNon_Vegetarian"
    Didnt_Matter = "Didnt_Matter"

class drinks(enum.Enum):
    DoesntDrink = "DoesntDrink"
    DrinksOccasionally = "DrinksOccasionally"
    DrinksOften = "DrinksOften"
    Didnt_Matter = "Didnt_Matter"

class smokes(enum.Enum):
    DoesntSmoke = "DoesntSmoke"
    SmokesOften = "SmokesOften"
    SmokesOccasionally = "SmokesOccasionally"
    Didnt_Matter = "Didnt_Matter"


class skin_tone(enum.Enum):
    WeatishskinTone = "WeatishskinTone"
    Fairskinned = "Fairskinned"
    Darkskinned = "Darkskinned"
    VeryFairskinned = "VeryFairskinned"
    Didnt_Matter = "Didnt_Matter"


class build(enum.Enum):
    AverageBuild = "AverageBuild"
    AthleticBuild = "AthleticBuild"
    HeavyBuild = "HeavyBuild"
    SlimBuild = "SlimBuild"
    Didnt_Matter = "Didnt_Matter"

class Authorization(db.Model, UserMixin):
    id = db.Column(db.Integer,primary_key=True)
    email_id = db.Column(db.String(100), index=True, unique=True)
    password_hash = db.Column(db.String(300), nullable=False)
    last_login = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    info = db.relationship('Users', backref='Authorization', lazy=True)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash,password)

    def __repr__(self):
        return "User {}".format(self.email_id)

class Users(db.Model):
    id = db.Column(db.Integer, db.ForeignKey(Authorization.id), primary_key=True)
    First_Name = db.Column(db.String(100), nullable=False)
    Last_Name =  db.Column(db.String(100))
    Age = db.Column(db.Integer)
    Height = db.Column(db.Integer)
    Marital_Status = db.Column(db.Enum(marital_status))
    Education = db.Column(db.String(300))
    Profession = db.Column(db.String(300))
    Religion = db.Column(db.Enum(religion))
    Language = db.Column(db.Enum(language))
    City = db.Column(db.String(100))
    Country = db.Column(db.Enum(country))
    Food = db.Column(db.Enum(food))
    Drinks = db.Column(db.Enum(drinks))
    Smokes = db.Column(db.Enum(smokes))
    Skin_Tone = db.Column(db.Enum(skin_tone))
    Build = db.Column(db.Enum(build))
    Gender = db.Column(db.Enum(gender))
    prefrences = db.relationship('User_Prefrences', backref='Users', lazy=True)
    def __repr__(self):
        return "info {}".format(self.First_Name)

class User_Prefrences(db.Model):
    id = db.Column(db.Integer, db.ForeignKey(Users.id), primary_key=True) 
    Marital_Status = db.Column(db.Enum(marital_status))
    Religion = db.Column(db.Enum(religion))
    Language = db.Column(db.Enum(language))
    Country = db.Column(db.Enum(country))
    Food = db.Column(db.Enum(food))
    Drinks = db.Column(db.Enum(drinks))
    Smokes = db.Column(db.Enum(smokes))
    Skin_Tone = db.Column(db.Enum(skin_tone))
    Build = db.Column(db.Enum(build))

    def __repr__(self):
        return "{},{},{},{},{},{},{},{},{}".format(self.Marital_Status,self.Religion,self.Language,self.Country,self.Food,self.Drinks,self.Smokes,self.Skin_Tone,self.Build)

@login.user_loader
def load_user(id):
    return Authorization.query.get(int(id))

#Flask Server
'''
This page contains server implementation for both Web and Native Api call

'''

#--------------------------------------------------------------------WEB_API------------------------------------------------------------------#

from app import App, db
from flask import render_template, url_for, redirect, jsonify, request, flash
from app.forms import LoginForm, SignupForm, ProfileForm, PrefrencesForm
from app.models import Authorization, Users, User_Prefrences
from flask_login import current_user, login_user, logout_user, login_required
from decision_tree.model import get_match

@App.route('/')
@App.route('/index')
def index():
    return render_template('index.html',title='Home')

@App.route('/register', methods=['GET','POST'])
def register():
    form = SignupForm()
    if form.validate_on_submit():
        user = Authorization.query.filter_by(email_id=form.email_id.data)
        if user is None or form.password.data != form.repeat_password.data:
            return redirect(url_for('register'))

        user = Authorization(email_id=form.email_id.data)
        user.set_password(form.password.data)
        info = Users(First_Name=form.first_name.data,Last_Name=form.last_name.data,Authorization=user)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('index'))

    return render_template('register.html',title='Sign Up',form=form)

@App.route('/login', methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form = LoginForm()
    if form.validate_on_submit():
        user=Authorization.query.filter_by(email_id=form.email_id.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user)
        return redirect(url_for('user'))
    return render_template('login.html', title='Login',form=form)

@App.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@App.route('/user')
def user():
    user = current_user
    user = Users.query.filter_by(Authorization=user).first()
    print(user)
    return render_template('user.html', title='user', user = user)

@login_required
@App.route('/profile', methods=['GET','POST'])
def profile():
    form = ProfileForm()
    if form.validate_on_submit():
        user = current_user
        info = Users.query.filter_by(Authorization=user).first()
        print(info.First_Name)
        info.Age = form.Age.data
        info.Height = form.Height.data
        info.Gender = form.Gender.data
        info.Marital_Status = form.Marital_Status.data
        info.Education = form.Education.data
        info.Profession = form.Profession.data
        info.Religion = form.Religion.data
        info.Language = form.Language.data
        info.City = form.City.data
        info.Country = form.Country.data
        info.Food = form.Food.data
        info.Drinks = form.Drinks.data
        info.Smokes = form.Smokes.data
        info.Skin_Tone = form.Skin_Tone.data
        info.Build = form.Build.data
        prefrences = User_Prefrences(Users=info)
        db.session.add(prefrences)
        db.session.commit()
        return redirect(url_for('user'))
    return render_template('profile.html', title='Profile', form=form)


@App.route('/prefrences',methods=['GET','POST'])
def prefrences():
    form= PrefrencesForm()
    if form.validate_on_submit():
        user = current_user
        info = Users.query.filter_by(Authorization=user).first()
        prefrences = User_Prefrences.query.filter_by(Users=info).first()
        prefrences.Marital_Status = form.Marital_Status.data
        prefrences.Religion = form.Religion.data
        prefrences.Language = form.Language.data
        prefrences.Country = form.Country.data
        prefrences.Food = form.Food.data
        prefrences.Drinks = form.Drinks.data
        prefrences.Smokes = form.Smokes.data
        prefrences.Skin_Tone = form.Skin_Tone.data
        prefrences.Build = form.Build.data
        db.session.commit()
        return redirect(url_for('user'))
    return render_template('prefrences.html', title='Prefrences', form=form)



@App.route('/find_match')
def find_match():
    user = current_user
    info = Users.query.filter_by(Authorization=user).first()
    prefrences = User_Prefrences.query.filter_by(Users=info).first()
    if not info.Age:
        return redirect(url_for('profile'))
    if not prefrences.Marital_Status:
        return redirect(url_for('prefrences'))
    match = get_match(info,prefrences)
    print(match)
    return render_template('find_match.html', title='Match', match=match)





"""---------------------------- Api Implemanation For Native App---------------------------------------------------- """

@App.route('/authenticate', methods=['POST'])
def authenticate():
    user_data = request.get_json()
    print(user_data);
    print("Data",type(user_data))
    user = Authorization.query.filter_by(email_id=user_data['email_id']).first()
    if(user.check_password(user_data['password'])):
        print('authorized')
        return jsonify(1)
    else:    
        return jsonify(0);
        
@App.route('/get_user_data', methods=['POST'])
def get_user_data():
    user_data = request.get_json()
    print(user_data['email_id'])
    user = Authorization.query.filter_by(email_id=user_data['email_id']).first()
    info = Users.query.filter_by(Authorization=user).first()
    print(info.First_Name)
    return jsonify({"First_Name": info.First_Name,"Last_Name": info.Last_Name, "gender": str(info.Gender)})
    
@App.route('/get_user_profile',methods=['POST'])
def get_user_profile():
    data = request.get_json()
    return jsonify(0)
    
@App.route('/find_match_',methods=['POST'])
def find_match_():
    data = request.get_json()
    email_id = data['email_id']
    user = Authorization.query.filter_by(email_id=email_id).first()
    info = Users.query.filter_by(Authorization=user).first()
    prefrences = User_Prefrences.query.filter_by(Users=info).first()
    match = get_match(info, prefrences)
    print(match.iloc[0,:])
    return jsonify(str(match.iloc[:2,:]))

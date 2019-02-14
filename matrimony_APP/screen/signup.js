import React from 'react';
import {StyleSheet, Text, View, TextInput, Button, ImageBackground, FlatList, ScrollView} from 'react-native';
import { Constants } from 'expo';
import t from 'tcomb-form-native';

const Form = t.form.Form;

const NewUser = t.struct({
  fname: t.String,
  lname: t.String,
  email_id: t.String,
  password: t.String,
  repeat_password: t.String,
  age: t.Number,
  height_in_cm: t.Number,
  gender: t.enums({'Male': 'Male','Female': 'Female'}),
  marital_status: t.enums({'NeverMarried':'NeverMarried','Divorced':'Divorced','AwaitingDivorce': 'AwaitingDivorce'}),
  education: t.String,
  profession: t.String,
  religion: t.enums({'Christian': 'Christian','Muslim': 'Muslim','Hindu': 'Hindu', 'Sikh': 'Sikh', 'Buddhist':'BUddhist', 'Jain': 'Jain'}),
  language: t.enums({'Urdu': 'Urdu', 'Hindi': 'Hindi', 'Marathi': 'Marathi', 'Punjabi': 'Punjabi', 'Sindhi': 'Sindhi', 'Kashmiri': 'Kashmiri', 'Gujarati': 'Gujarati', 'Malayalam': 'Malayalam', 'Tamil': 'Tamil', 'Assamese': 'Assamese', 'Bengali': 'Bengali', 'Kannada': 'Kannada', 'Nepali': 'Nepali', 'Telugu': 'Telugu', 'Tulu': 'Tulu'}),
  city: t.String,
  country: t.enums({'Pakistan': 'Pakistan', 'India': 'India', 'USA': 'USA', 'Australia':'Australia', 'Bangladesh': 'Bangladesh', 'Canada': 'Canada','Indonesia': 'Indonesia', 'Kuwait': 'Kuwait', 'SouthAfrica': 'SouthAfrica', 'UnitedArabEmirates': 'UnitedArabEmirates', 'UnitedKingdom': 'UnitedKingdom'}),
 food: t.enums({'Eggetarian': 'Eggetarian', 'Vegetarian': 'Vegetarian', 'Non_Vegetarian': 'Non_Vegetarian', 'OccasionallyNonVegetarian': 'OccasionallyNonVegetarian'}),
  drinks: t.enums({'DoesntDrink': 'DoesntDrink','DrinksOccasionally': 'DrinksOccasionally', 'DrinksOften': 'DrinksOften'}),
  smokes: t.enums({'DoesntSmoke':'DoesntSmoke', 'SmokesOften': 'SmokesOften', 'SmokesOccasionally': 'SmokesOccasionally'}),
  skin_tone: t.enums({'WeatishskinTone': 'WeatishskinTone', 'Fairskinned': 'Fairskinned', 'Darkskinned': 'Darkskinned', 'VeryFairskinned': 'VeryFairskinned'}),
  build: t.enums({'AverageBuild': 'AverageBuild', 'AthleticBuild': 'AthleticBuild', 'HeavyBuild': 'HeavyBuild', 'SlimBuild': 'SlimBuild'}),
});

var options = {
  fields: {
    password: {
      password: true,
      secureTextEntry: true
    },
    repeat_password: {
      password: true,
      secureTextEntry: true
    }
  }
};

class SignupScreen extends React.Component{
   constructor(props){
     super(props);
	  this.state={user_status:2}
  }
  submit = () =>{
    this.data = this._form.getValue()
    console.log(this.data);
    this.headers = {'Accept': 'application/json',
    'Content-Type': 'application/json',}
        
    fetch("http://192.168.43.190:5000/new_user",{
      method: "POST",
      headers: this.headers,
      body: JSON.stringify(this._form.getValue())
    }).then((response)=>response.json()).then((responsejson)=>{
            this.setState({user_status: responsejson});console.log(this.state.user_status);
            if(this.state.user_status == 1){
                this.props.navigation.navigate('User',this.data);
            }
        });
  }

  render() {
  if(this.state.user_status == 2){
            return(
            <ScrollView>
              <View style={styles.container}>
                <Text style={styles.paragraph}>Register</Text>
                <Form ref={ c => this._form = c} type={NewUser} options={options}/>
                <Button onPress={this.submit} title="Register"/>
              </View>
              </ScrollView>
            );
    }
    else{
    return(
            <ScrollView>
              <View style={styles.container}>
                <Text style={styles.paragraph}>Register</Text>
                <Text style={styles.error}> Already Registered Try Login</Text>
                <Form ref={ c => this._form = c} type={NewUser} options={options}/>
                <Button onPress={this.submit} title="Register"/>
              </View>
              </ScrollView>
            );
    }
  }
}

export default SignupScreen;

const styles = StyleSheet.create({
  container: {
    flex: 1,
    flexGrow: 1,
    alignItems: 'center',
    justifyContent: 'center',
    paddingTop: Constants.statusBarHeight,
    backgroundColor: '#FFFF00',
  },
  paragraph: {
    marginTop: 10,
    fontSize: 18,
    fontWeight: 'bold',
    textAlign: 'center',
    color: '#34495e',
  },
  error: {
        color: '#ff0000', 
  }
});


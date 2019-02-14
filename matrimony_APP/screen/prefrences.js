import React from 'react';
import {StyleSheet, Text, View, TextInput, Button, ImageBackground, FlatList, ScrollView} from 'react-native';
import { Constants } from 'expo';
import t from 'tcomb-form-native';

const Form = t.form.Form;

const NewUser = t.struct({
  marital_status: t.enums({'NeverMarried':'NeverMarried','Divorced':'Divorced','AwaitingDivorce': 'AwaitingDivorce', 'Didnt_Matter': 'Didnt_Matter'}),
  religion: t.enums({'Christian': 'Christian','Muslim': 'Muslim','Hindu': 'Hindu', 'Sikh': 'Sikh', 'Buddhist':'BUddhist', 'Jain': 'Jain', 'Didnt_Matter': 'Didnt_Matter'}),
  language: t.enums({'Urdu': 'Urdu', 'Hindi': 'Hindi', 'Marathi': 'Marathi', 'Punjabi': 'Punjabi', 'Sindhi': 'Sindhi', 'Kashmiri': 'Kashmiri', 'Gujarati': 'Gujarati', 'Malayalam': 'Malayalam', 'Tamil': 'Tamil', 'Assamese': 'Assamese', 'Bengali': 'Bengali', 'Kannada': 'Kannada', 'Nepali': 'Nepali', 'Telugu': 'Telugu', 'Tulu': 'Tulu', 'Didnt_Matter': 'Didnt_Matter'}),
  country: t.enums({'Pakistan': 'Pakistan', 'India': 'India', 'USA': 'USA', 'Australia':'Australia', 'Bangladesh': 'Bangladesh', 'Canada': 'Canada','Indonesia': 'Indonesia', 'Kuwait': 'Kuwait', 'SouthAfrica': 'SouthAfrica', 'UnitedArabEmirates': 'UnitedArabEmirates', 'UnitedKingdom': 'UnitedKingdom', 'Didnt_Matter': 'Didnt_Matter'}),
 food: t.enums({'Eggetarian': 'Eggetarian', 'Vegetarian': 'Vegetarian', 'Non_Vegetarian': 'Non_Vegetarian', 'OccasionallyNonVegetarian': 'OccasionallyNonVegetarian', 'Didnt_Matter': 'Didnt_Matter'}),
  drinks: t.enums({'DoesntDrink': 'DoesntDrink','DrinksOccasionally': 'DrinksOccasionally', 'DrinksOften': 'DrinksOften', 'Didnt_Matter': 'Didnt_Matter'}),
  smokes: t.enums({'DoesntSmoke':'DoesntSmoke', 'SmokesOften': 'SmokesOften', 'SmokesOccasionally': 'SmokesOccasionally', 'Didnt_Matter': 'Didnt_Matter'}),
  skin_tone: t.enums({'WeatishskinTone': 'WeatishskinTone', 'Fairskinned': 'Fairskinned', 'Darkskinned': 'Darkskinned', 'VeryFairskinned': 'VeryFairskinned', 'Didnt_Matter': 'Didnt_Matter'}),
  build: t.enums({'AverageBuild': 'AverageBuild', 'AthleticBuild': 'AthleticBuild', 'HeavyBuild': 'HeavyBuild', 'SlimBuild': 'SlimBuild', 'Didnt_Matter': 'Didnt_Matter'}),
});


class PrefrenceScreen extends React.Component{
   constructor(props){
     super(props);
	  this.state={user_status:0}
      this.email_id = this.props.navigation.getParam('email_id','no_id');
  }
  submit = () =>{
    this.data = this._form.getValue()
    console.log(this.data);
    this.headers = {'Accept': 'application/json',
    'Content-Type': 'application/json',}
        
    fetch("http://192.168.43.190:5000/update_prefrences",{
      method: "POST",
      headers: this.headers,
      body: JSON.stringify({"prefrences": this._form.getValue(),'email_id': this.email_id }),
    }).then((response)=>response.json()).then((responsejson)=>{
            this.setState({user_status: responsejson});console.log(this.state.user_status);
            if(this.state.user_status == 1){
                this.props.navigation.navigate('User',this.data);
            }
        });
  }

  render() {
    return(
    <ScrollView>
      <View style={styles.container}>
        <Text style={styles.paragraph}>Prefrences</Text>
        <Form ref={ c => this._form = c} type={NewUser} />
        <Button onPress={this.submit} title="Update"/>
      </View>
      </ScrollView>
    );
  }
}

export default PrefrenceScreen;

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
  }
});


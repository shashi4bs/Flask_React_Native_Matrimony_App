import React from 'react';
import {StyleSheet, Text, View, TextInput, Button, ImageBackground} from 'react-native';
import { Constants } from 'expo';
import t from 'tcomb-form-native';
import { createStackNavigator } from 'react-navigation';

const Form = t.form.Form;

const User = t.struct({
  email_id: t.String,
  password: t.String,
});

var options = {
  fields: {
    password: {
      password: true,
      secureTextEntry: true
    }
  }
}

function wait(ms){
   var start = new Date().getTime();
   var end = start;
   while(end < start + ms) {
     end = new Date().getTime();
  }
}

class LoginScreen extends React.Component{
  constructor(props){
     super(props);
	  this.state={user_status:2}
  }	
  submit = ()=>{
    this.data = this._form.getValue();
    console.log(this.data);

    this.headers = {'Accept': 'application/json',
    'Content-Type': 'application/json',}
        
    fetch("http://192.168.43.190:5000/authenticate",{
      method: "POST",
      headers: this.headers,
      body: JSON.stringify(this._form.getValue())
    }).then((response)=>response.json()).then((responsejson)=>{
    this.setState({user_status: responsejson});console.log(this.state.user_status);
    if(this.state.user_status == 0){
      console.log("user unauthenticated");
    }
    else{
      console.log("user authenticated");
      this.props.navigation.navigate('User',this.data);
    }
    }).catch((error)=>{console.error(error);});
    
  }

  render() {
  if(this.state.user_status == 2){
    return(
      <View style={styles.container}>
       <ImageBackground style={styles.images}
        source={require("../assets/lock.jpg")} >
        <Text style={styles.paragraph}>Login</Text>
        <Form ref={ c => this._form = c} type={User} options={options}/>
        <Button onPress={this.submit} title="Login"/>
        </ImageBackground>
      </View>
    );
    }
    else{
    return(
      <View style={styles.container}>
       <ImageBackground style={styles.images}
        source={require("../assets/lock.jpg")} >
        <Text style={styles.paragraph}>Login</Text>
        <Form ref={ c => this._form = c} type={User} options={options}/>
        <Button onPress={this.submit} title="Login"/>
        <Text style={styles.error}>Invalid Username or Password</Text>
        </ImageBackground>
      </View>
      );
    }
  }
}

export default LoginScreen;

const styles = StyleSheet.create({
  container: {
    flex: 1,
    alignItems: 'center',
    justifyContent: 'center',
    paddingTop: Constants.statusBarHeight,
    backgroundColor: '#ecf0f1',
  },
  paragraph: {
    marginTop: 10,
    fontSize: 18,
    fontWeight: 'bold',
    textAlign: 'center',
    color: '#e7dbdb',
  },
  images: {
    paddingTop: 50,
    height: 600,
    width: 350,
  },
  error: {
        color: '#ff0000', 
  }
});


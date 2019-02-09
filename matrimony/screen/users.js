
import React from 'react';
import {StyleSheet, Text, View, TextInput, Button, Image} from 'react-native';
import { Constants } from 'expo';
import { createStackNavigator } from 'react-navigation';

class UserScreen extends React.Component{
  constructor(props){
    super(props);
    this.state = {details: "NUll" }
    this.email_id = this.props.navigation.getParam('email_id','no_id');
    this.get_data();
  }

  get_data=()=>{
    console.log(this.email_id);
    this.headers = {'Accept': 'application/json',
      'Content-Type': 'application/json',},
    fetch("http://192.168.43.190:5000/get_user_data",{
      method: "POST",
      headers: this.headers,
      body: JSON.stringify({email_id: this.email_id})
    }).then((response)=>response.json()).then((responsejson)=>{
    this.setState({details: responsejson});
    console.log(this.state.details);
    }).catch((error)=>{console.error(error);});
  }
  
  find_match = () => {
        this.headers = {'Accept': 'application/json',
      'Content-Type': 'application/json',},
    fetch("http://192.168.43.190:5000/check_prefrences",{
      method: "POST",
      headers: this.headers,
      body: JSON.stringify({"email_id": this.email_id})
    }).then((response)=>response.json()).then((responsejson)=>{
    this.setState({details: responsejson});
    console.log(this.state.details);
    
    if(this.state.details == 1){
                this.props.navigation.navigate('Match',{email_id: this.email_id})
        }
        else{
                this.props.navigation.navigate('Prefrence',{email_id: this.email_id})
        }
    }).catch((error)=>{console.error(error);});
  }
  render() {
  if(this.state.details["gender"] == "gender.Female"){
    return(
      <View style={styles.container}>
        <Image style={styles.images}
        source={require("../assets/female_shadow.png")} />
        <Text style={styles.text}>Welcome {this.state.details.First_Name} {this.state.details.Last_Name}</Text>
        <Button onPress={()=>{this.props.navigation.navigate('Match',{email_id: this.email_id})}} title="Find Match"/>
        </View>
    );
    }
    else{
        return(
      <View style={styles.container}>
      <Image style={styles.images}
        source={require("../assets/male_shadow.png")} borderWidth={2} />
        <Text style={styles.text}>Welcome {this.state.details.First_Name} {this.state.details.Last_Name}</Text>
        <Button onPress={this.find_match} title="Find Match" />
        </View>
        );
    }
  }
}

export default UserScreen;

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    paddingTop: 5,
    backgroundColor: '#ecf0f1',
  },
  text:{
        fontSize: 18,
    fontWeight: 'bold',
    textAlign: 'center',
    color: '#34495e',
  },
  images: {
        borderWidth: 2,
        paddingTop: 15,
        paddingLeft: 15,
        justifyContent: 'center'
  },
});

//page with find match option

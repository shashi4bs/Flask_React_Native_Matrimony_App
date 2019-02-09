
import React from 'react';
import {StyleSheet, Text, View, TextInput, Button, Image} from 'react-native';
import { Constants } from 'expo';
import { createStackNavigator } from 'react-navigation';

class MatchScreen extends React.Component{
  constructor(props){
    super(props);
    this.state = {details: "NULL" }
    this.email_id = this.props.navigation.getParam('email_id','no_id');
    this.get_data();
  }

  get_data=()=>{
    console.log(this.email_id);
    this.headers = {'Accept': 'application/json',
      'Content-Type': 'application/json',}
        
    fetch("http://192.168.43.190:5000/find_match_",{
      method: "POST",
      headers: this.headers,
      body: JSON.stringify({email_id: this.email_id})
    }).then((response)=>response.json()).then((responsejson)=>{
    this.setState({details: responsejson});
    console.log(this.state.details);
    }).catch((error)=>{console.error(error);});
  }
  render() {
  if(this.state.details == "NULL"){
    return(
      <View style={styles.container}>
        <Text style={styles.result}>Finding Match....</Text>
        </View>
    );
    }
    else{
        if(this.state.details["gender"] == "F"){
                return(
                        <View style={styles.container}>
                        <Text> Match Found...</Text>
                        <Text style={styles.result}> She is {this.state.details["age"]} years old</Text>
                        <Text style={styles.result}> Height(cm):{this.state.details["height"]}</Text>
                        <Text style={styles.result}> City:{this.state.details["city"]}</Text>
                        <Text style={styles.result}> Country: {this.state.details["country"]}</Text>
                        <Text style={styles.result}> Marital Status: {this.state.details["marital_status"]}</Text>
                        <Text style={styles.result}> Education: {this.state.details["education"]}</Text>
                        <Text style={styles.result}> Profession: {this.state.details["profession"]}</Text>
                        <Text style={styles.result}> Religion: {this.state.details["religion"]}</Text>
                        <Text style={styles.result}> Language: {this.state.details["language"]}</Text>
                        <Text style={styles.result}> Community: {this.state.details["community"]}</Text>
                        <Text style={styles.result}> City: {this.state.details["city"]}</Text>
                        <Text style={styles.result}> Country: {this.state.details["country"]}</Text>
                        <Text style={styles.result}> Food: {this.state.details["food_preferences"]}</Text>
                        <Text style={styles.result}> Drinks: {this.state.details["drinks"]}</Text>
                        <Text style={styles.result}> Smokes: {this.state.details["smokes"]}</Text>
                        <Text style={styles.result}> Skin Tone: {this.state.details["skin_tone"]}</Text>
                        <Text style={styles.result}> Build: {this.state.details["build"]}</Text>
                        </View>
                );
        }
        else{
        return(
                        <View style={styles.container}>
                        <Text style={styles.result}> He is {this.state.details["age"]} years old</Text>
                        <Text style={styles.result}> Height(in cm):{this.state.details["height"]}</Text>
                        <Text style={styles.result}> City:{this.state.details["city"]}</Text>
                        <Text style={styles.result}> Country: {this.state.details["country"]}</Text>
                        <Text style={styles.result}> Marital Status: {this.state.details["marital_status"]}</Text>
                        <Text style={styles.result}> Education: {this.state.details["education"]}</Text>
                        <Text style={styles.result}> Profession: {this.state.details["profession"]}</Text>
                        <Text style={styles.result}> Religion: {this.state.details["religion"]}</Text>
                        <Text style={styles.result}> Language: {this.state.details["language"]}</Text>
                        <Text style={styles.result}> Community: {this.state.details["community"]}</Text>
                        <Text style={styles.result}> City: {this.state.details["city"]}</Text>
                        <Text style={styles.result}> Country: {this.state.details["country"]}</Text>
                        <Text style={styles.result}> Food: {this.state.details["food_preferences"]}</Text>
                        <Text style={styles.result}> Drinks: {this.state.details["drinks"]}</Text>
                        <Text style={styles.result}> Smokes: {this.state.details["smokes"]}</Text>
                        <Text style={styles.result}> Skin Tone: {this.state.details["skin_tone"]}</Text>
                        <Text style={styles.result}> Build: {this.state.details["build"]}</Text>
                        </View>
                );
        }  
    }
    }
}

export default MatchScreen;

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    paddingTop: Constants.statusBarHeight,
    backgroundColor: '#ecf0f1',
  },
	result: {
		flex: 1,
		margin:1,
	},
});

//page with find match option

import * as React from 'react';
import { Text, View, StyleSheet, Button, Image, ImageBackground } from 'react-native';
import { Constants } from 'expo';
import { createStackNavigator } from 'react-navigation';

class HomePage extends React.Component {
  render() {
    return (
      <View style={styles.container}>
          <ImageBackground style={styles.images}
        source={require("../assets/home.jpeg")} >
        <Text style={styles.paragraph}>BANDHAN</Text>
        <Button
          style={styles.button}
          onPress={()=> this.props.navigation.navigate('Login')}
          title="Login"
        />
        <Button
          style={styles.button}
          onPress={()=> this.props.navigation.navigate('Signup')}
          title="SignUp"
        />
        </ImageBackground>
      </View>
    );
  }
}
export default HomePage;

const styles = StyleSheet.create({
  container: {
    flex: 1,
    alignItems: 'center',
    justifyContent: 'center',
    paddingTop: Constants.statusBarHeight,
    backgroundColor: '#ecf0f1',
  },
  paragraph: {
    margin: 24,
    fontSize: 18,
    fontWeight: 'bold',
    textAlign: 'center',
    color: '#34495e',
  },
  button: {
        color: '#FFFF33',
  },
  images: {
    height: 600,
    width: 350,
  }
});

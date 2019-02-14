import * as React from 'react';
import { Text, View, StyleSheet, Button } from 'react-native';
import { Constants } from 'expo';
import { createStackNavigator } from 'react-navigation';

/*import all sreeens present in screens directory*/
import HomePage from './screen/home';
import LoginPage from './screen/login';
import SignupPage from './screen/signup';
import UsersPage from './screen/users';
import MatchPage from './screen/match';
import PrefrencePage from './screen/prefrences'

/*create a stack navigator - screens are stacked in the sequence they are accessed 
and on pressing back button it removes screen on top of screenstack i.e last opened accessed screen*/
const AppNavigator = createStackNavigator({
  Home: HomePage,
  Login: LoginPage,
  Signup: SignupPage,
  User: UsersPage,
  Match: MatchPage,
  Prefrence: PrefrencePage,
});
export default class App extends React.Component {
  render() {
    return (
      <AppNavigator />
    );
  }
}


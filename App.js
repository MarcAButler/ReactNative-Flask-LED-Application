import { StatusBar } from 'expo-status-bar';
import React from 'react';
import { StyleSheet, Text, View, Button } from 'react-native';
import ButtonUI from './components/ButtonUI';

export default function App() {
  return (
    <View style={styles.container}>
      <Text>This is random crap I wrote</Text>
      <ButtonUI name="On" slug="/on"/>
      <ButtonUI name="Off" slug="/off"/>
      <ButtonUI name="Blink" slug="/blink"/>
      <ButtonUI name="Status" slug="/status"/>
      <StatusBar style="auto" />
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'center',
  },
});

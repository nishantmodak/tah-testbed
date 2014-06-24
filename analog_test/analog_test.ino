/*
  ReadAnalogVoltage
  Reads an analog input on pin 0, converts it to voltage, and prints the result to the serial monitor.
  Attach the center pin of a potentiometer to pin A0, and the outside pins to +5V and ground.
 
 This example code is in the public domain.
 */

// the setup routine runs once when you press reset:
float voltage;
int sensorValue;
void setup() 
{
  // initialize serial communication at 9600 bits per second:
  Serial.begin(9600);
}

// the loop routine runs over and over again forever:
void loop() 
{   
  String input = "";
  
  while(Serial.available()>0)    // read any serial input
  {
    input += (char) Serial.read();  // read one char at a time
    delay(5);  // delay of 5ms for next char 
    
  }
  
  if(input == "0")
  {
    // read the input on analog pin 0:
     sensorValue = analogRead(A0);
    // Convert the analog reading (which goes from 0 - 1023) to a voltage (0 - 5V):
    //voltage = sensorValue * (5.0 / 1023.0);
    // print out the value you read:
    //Serial.println(voltage);
  }
  
  else if(input == "1")
  {
    // read the input on analog pin 0:
     sensorValue = analogRead(A1);
    // Convert the analog reading (which goes from 0 - 1023) to a voltage (0 - 5V):
    //voltage = sensorValue * (5.0 / 1023.0);
    // print out the value you read:
    //Serial.println(voltage);
  }
  
  else if(input == "2")
  {
    // read the input on analog pin 0:
     sensorValue = analogRead(A2);
    // Convert the analog reading (which goes from 0 - 1023) to a voltage (0 - 5V):
    //voltage = sensorValue * (5.0 / 1023.0);
    // print out the value you read:
    //Serial.println(voltage);
  }
  
  else if(input == "3")
  {
    // read the input on analog pin 0:
     sensorValue = analogRead(A3);
    // Convert the analog reading (which goes from 0 - 1023) to a voltage (0 - 5V):
    //voltage = sensorValue * (5.0 / 1023.0);
    // print out the value you read:
    //Serial.println(voltage);
  }
  
  else if(input == "4")
  {
    // read the input on analog pin 0:
     sensorValue = analogRead(A4);
    // Convert the analog reading (which goes from 0 - 1023) to a voltage (0 - 5V):
    //voltage = sensorValue * (5.0 / 1023.0);
    // print out the value you read:
    //Serial.println(voltage);
  }
  
  else if(input == "5")
  {
    // read the input on analog pin 0:
    sensorValue = analogRead(A5);
    // Convert the analog reading (which goes from 0 - 1023) to a voltage (0 - 5V):
     //voltage = sensorValue * (5.0 / 1023.0);
    // print out the value you read:
    //Serial.println(voltage);
  }
 voltage = sensorValue * (5.0 / 1023.0);
 Serial.println(voltage); 
  
}

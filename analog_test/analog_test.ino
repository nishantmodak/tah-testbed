
// the setup routine runs once when you press reset:
float v0;
float v1;
float v2;
float v3;
float v4;
float v5;

void setup() 
{
  // initialize serial communication at 9600 bits per second:
  Serial.begin(9600);
}

void loop() 
{   
  /*String input = "";
  
  while(Serial.available()>0)    // read any serial input
  {
    input += (char) Serial.read();  // read one char at a time
    delay(5);  // delay of 5ms for next char 
    
  }*/
  

  
  
      
  v0 = analogRead(A0)*(3.3 / 1024);
  v1 = analogRead(A1)*(3.3 / 1024);
  v2 = analogRead(A2)*(3.3 / 1024);
  v3 = analogRead(A3)*(3.3 / 1024);
  v4 = analogRead(A4)*(3.3 / 1024);
  v5 = analogRead(A5)*(3.3 / 1024);
  
  Serial.print("A0: ");
  Serial.println(v0);
  Serial.print("A1: ");
  Serial.println(v1);
  Serial.print("A2: ");
  Serial.println(v2);
  Serial.print("A3: ");
  Serial.println(v3);
  Serial.print("A4: ");
  Serial.println(v4);
  Serial.print("A5: ");
  Serial.println(v5);
  
  delay(500);
  
}



int flag2_1;
int flag2_0;
int flag3_1;
int flag3_0;
int flag4_1;
int flag4_0;
int flag5_1;
int flag5_0;
int flag6_1;
int flag6_0;
int flag7_1;
int flag7_0;
int flag8_1;
int flag8_0;
int flag9_1;
int flag9_0;
int flag10_1;
int flag10_0;
int flag11_1;
int flag11_0;
int flag12_1;
int flag12_0;
int flag13_1;
int flag13_0;
int flagA0_1;
int flagA0_0;
int flagA1_1;
int flagA1_0;
int flagA2_1;
int flagA2_0;
int flagA3_1;
int flagA3_0;
int flagA4_1;
int flagA4_0;
int flagA5_1;
int flagA5_0;
int pin_13;
int pin_12;
int pin_11;
int pin_10;
int pin_9;
int pin_8;
int pin_7;
int pin_6;
int pin_5;
int pin_4;
int pin_3;
int pin_2;
float pinA0;
float pinA1;
float pinA2;
float pinA3;
float pinA4;
float pinA5;
int inMin = 2; // Lowest input pin
int inMax = 13; // Highest input pin
void setup()
{
   
   for(int i=inMin; i<=inMax; i++)
   {
     pinMode(i, INPUT);
   }
   
   Serial.begin(9600);
}

void loop()
{
  
  pin_13 = digitalRead(13);
  pin_12 = digitalRead(12);
  pin_11 = digitalRead(11);
  pin_10 = digitalRead(10);
  pin_9 = digitalRead(9);
  pin_8 = digitalRead(8);
  pin_7 = digitalRead(7);
  pin_6 = digitalRead(6);
  pin_5 = digitalRead(5);
  pin_4 = digitalRead(4);
  pin_3 = digitalRead(3);
  pin_2 = digitalRead(2);
  pinA0 = analogRead(A0);
  pinA1 = analogRead(A1);
  pinA2 = analogRead(A2);
  pinA3 = analogRead(A3);
  pinA4 = analogRead(A4);
  pinA5 = analogRead(A5);
  if(pin_13 == 1)
    flag13_1 = 1;
  if(pin_13 == 0)
    flag13_0 = 0;
  if(pin_12 == 1)
    flag12_1 = 1;
  if(pin_12 == 0)
    flag12_0 = 0;
  if(pin_11 == 1)
    flag11_1 = 1;
  if(pin_11 == 0)
    flag11_0 = 0;
  if(pin_10 == 1)
    flag10_1 = 1;
  if(pin_10 == 0)
    flag10_0 = 0;
  if(pin_9 == 1)
    flag9_1 = 1;
  if(pin_9 == 0)
    flag9_0 = 0;
  if(pin_8 == 1)
    flag8_1 = 1;
  if(pin_8 == 0)
    flag8_0 = 0;
  if(pin_7 == 1)
    flag7_1 = 1;
  if(pin_7 == 0)
    flag7_0 = 0;
  if(pin_6 == 1)
    flag6_1 = 1;
  if(pin_6 == 0)
    flag6_0 = 0;
  if(pin_5 == 1)
    flag5_1 = 1;
  if(pin_5 == 0)
    flag5_0 = 0;
  if(pin_4 == 1)
    flag4_1 = 1;
  if(pin_4 == 0)
    flag4_0 = 0;
  if(pin_3 == 1)
    flag3_1 = 1;
  if(pin_3 == 0)
    flag3_0 = 0;
  if(pin_2 == 1)
    flag2_1 = 1;
  if(pin_2 == 0)
    flag2_0 = 0;
  if(pinA0 <= 3.3 && pinA0 >= 3.0)
    flagA0_1 = 1;
  if(pinA0 == 0)
    flagA0_0 = 0;
  if(pinA1 <= 3.3 && pinA1 >= 3.0)
    flagA1_1 = 1;
  if(pinA1 == 0)
    flagA1_0 = 0;
  if(pinA2 <= 3.3 && pinA2 >= 3.0)
    flagA2_1 = 1;
  if(pinA2 == 0)
    flagA2_0 = 0;
  if(pinA3 <= 3.3 && pinA3 >= 3.0)
    flagA3_1 = 1;
  if(pinA3 == 0)
    flagA3_0 = 0;
  if(pinA4 <= 3.3 && pinA4 >= 3.0)
    flagA4_1 = 1;
  if(pinA4 == 0)
    flagA4_0 = 0;
  if(pinA5 <= 3.3 && pinA5 >= 3.0)
    flagA5_1 = 1;
  if(pinA5 == 0)
    flagA5_0 = 0;  
  if((flag13_1 == 1) && (flag13_0 == 0) && (flag12_1 == 1) && (flag12_0 == 0) && (flag11_1 == 1) && (flag11_0 == 0) && (flag10_1 == 1) && (flag10_0 == 0) && (flag9_1 == 1) && (flag9_0 == 0) && (flag8_1 == 1) && (flag8_0 == 0) && (flag7_1 == 1) && (flag7_0 == 0) && (flag6_1 == 1) && (flag6_0 == 0) && (flag5_1 == 1) && (flag5_0 == 0) && (flag4_1 == 1) && (flag4_0 == 0) && (flag3_1 == 1) && (flag3_0 == 0) && (flag2_1 == 1) && (flag2_0 == 0) && (flagA0_1 == 1) && (flagA0_0 == 0) && (flagA1_1 == 1) && (flagA1_0 == 0) && (flagA2_1 == 1) && (flagA2_0 == 0) && (flagA3_1 == 1) && (flagA3_0 == 0) && (flagA4_1 == 1) && (flagA4_0 == 0) && (flagA5_1 == 1) && (flagA5_0 == 0))
    Serial.write('ok');
  else
    Serial.write('fail');
    
  delay(250); 
 
}
   

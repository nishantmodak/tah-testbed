

int count_h = 0;
int count_l = 0;
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
  digitalRead(13);
  digitalRead(12);
  digitalRead(11);
  digitalRead(10);
  digitalRead(9);
  digitalRead(8);
  digitalRead(7);
  digitalRead(6);
  digitalRead(5);
  digitalRead(4);
  digitalRead(3);
  digitalRead(2);
  
  for(int k=inMax; k>= inMin; k--)
  {
     if(digitalRead(k) > 2.5)
        count_h++;
     else if(digitalRead(k) == 0.0)
        count_l++;
  }
  
  Serial.println(count_h);
  Serial.println(count_l);
  /*if(count_h > 2 && count_l > 2)
      Serial.write('ok');
  else if(count_h < 2 && count_l < 2)  
      Serial.write('fail');
  */    
  delay(500);
  
}
   

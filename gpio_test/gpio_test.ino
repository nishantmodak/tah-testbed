


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
   if(digitalRead(2)==HIGH)
   {  
      Serial.print("pin-2 OK!!");
   }
   
   else if(digitalRead(3)==HIGH)
   {  
      Serial.print("pin-3 OK!!");
   }
   
   else if(digitalRead(4)==HIGH)
   {  
      Serial.print("pin-4 OK!!");
   }
   
   else if(digitalRead(5)==HIGH)
   {  
      Serial.print("pin-5 OK!!");
   }
   
   else if(digitalRead(6)==HIGH)
   {  
      Serial.print("pin-6 OK!!");
   }
   
   else if(digitalRead(7)==HIGH)
   {  
      Serial.print("pin-7 OK!!");
   }
   
   else if(digitalRead(8)==HIGH)
   {  
      Serial.print("pin-8 OK!!");
   }
   
   else if(digitalRead(9)==HIGH)
   {  
      Serial.print("pin-9 OK!!");
   }
   
   else if(digitalRead(10)==HIGH)
   {  
      Serial.print("pin-10 OK!!");
   }
   
   else if(digitalRead(11)==HIGH)
   {  
      Serial.print("pin-11 OK!!");
   }
   
   else if(digitalRead(12)==HIGH)
   {  
      Serial.print("pin-12 OK!!");
   }
   
   else if(digitalRead(13)==HIGH)
   {  
      Serial.print("pin-13 OK!!");
   }
}
   

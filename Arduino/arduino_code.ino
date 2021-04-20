/*
Flower Soil Mosture Sensor
D2 - Soil Mosture Sensor
D3 - Relay module
D4:D5 - LEDS 1,2
LED1 - Green
LED2 - Red
Connect the Soil Moisture Sensor to Digital input pin 2 and your 2 led's to digital out 4-5
*/

// int moistureSensorA2 = A2;
// int moistureSensorA1 = A1;
// int moistureSensorA0 = A0;
int relayPump = 8;

// int relayValveBlue = 9;
// int relayValveRed = 10;

int relaysValve[] = {9, 10, 11};

int sensors[] = {A0, A1, A2};
const int sensorsCount = 3;

int ledRed = 2;
int ledYellow = 3;

// boolean flag[] = {false, false, false};

int sensorsValue[sensorsCount];

void setup(){
  // setting the led pins to outputs

  pinMode(relayPump, OUTPUT);

  for(int i = 0; i < sensorsCount; i++){
    pinMode(sensors[i], INPUT);
    pinMode(relaysValve[i], OUTPUT);
  }

  // setting the led pins to outputs
  pinMode(ledRed, OUTPUT);
  pinMode(ledYellow, OUTPUT);
  
  // setting the Relay pin to output
  
  // Serial Begin so we can see the data from the moisture sensor in our serial input window.
  Serial.begin(9600);
}

int checkSensor(int index){
  sensorsValue[index] = analogRead(sensors[index]);

  if(sensorsValue[index] >= 500){
    digitalWrite(ledRed, LOW);
    digitalWrite(ledYellow, HIGH);
    
    while(sensorsValue[index] > 300){
      digitalWrite(relaysValve[index], HIGH);
      digitalWrite(relayPump, HIGH);

      Serial.println(index);
      Serial.println(sensorsValue[index]);
      
      delay(5000);
      
      digitalWrite(relayPump, LOW);
      digitalWrite(relaysValve[index], LOW);
  
      sensorsValue[index] = analogRead(sensors[index]);
    }
      
    digitalWrite(ledYellow, LOW);
    digitalWrite(ledRed, HIGH);
    
  }

  
  /*if(sensorsValue[index] >= 500 && flag[index] == false){
    digitalWrite(ledRed, LOW);
    digitalWrite(ledYellow, HIGH);
    digitalWrite(relaysValve[index], HIGH);
    digitalWrite(relayPump, HIGH);
    delay(1000);
    flag[index] = true;
    digitalWrite(relayPump, LOW);
    digitalWrite(relaysValve[index], LOW);
    digitalWrite(ledYellow, LOW);
    digitalWrite(ledRed, HIGH);
  }
  
  if(sensorsValue[index] <= 300 && flag[index] == true){
    flag[index] = false;
    delay(1000);
  }*/
  
}

// the loop routine runs over and over again forever:

void loop(){
  //digitalWrite(ledRed, HIGH);
  
  
  //digitalWrite(ledRed, HIGH);
  // read the input on digital pin 2:
  // int sensorValueA2 = analogRead(moistureSensorA2);
  // int sensorValueA1 = analogRead(moistureSensorA1);
  // int sensorValueA0 = analogRead(moistureSensorA0);
  // print out the value you read:

  //Serial.println(sensorValue2);
  /*Serial.print("Data: A0-");
  Serial.print(sensorValueA0);
  Serial.print(" and A1-");
  Serial.print(sensorValueA1);
  Serial.print(" and A2-");
  Serial.println(sensorValueA2);
  digitalWrite(relayPump, HIGH);
  digitalWrite(led1, LOW);
  digitalWrite(led2, HIGH);
  if (sensorValue2 == 1) {
    digitalWrite(led1, HIGH);
    digitalWrite(led2, LOW);
    digitalWrite(relayPump, LOW);
    Serial.println("Watering");
    delay(10000);
    // run pump for 10 seconds
    Serial.println("Finished watering");
  }
  delay(1000);*/

  /*digitalWrite(relayValveBlue, HIGH);
  Serial.println("Blue");
  delay(3000);
  digitalWrite(relayValveBlue, LOW);
  */

  
  /*while(true){
    digitalWrite(ledRed, HIGH);
    
    digitalWrite(relaysValve[1], HIGH);
    digitalWrite(relayPump, HIGH);
    delay(5000);
    
    digitalWrite(relaysValve[2], HIGH);
    digitalWrite(relaysValve[1], LOW);
    delay(5000);
    
    digitalWrite(relaysValve[0], HIGH);
    digitalWrite(relaysValve[2], LOW);
    delay(5000);
    
    
    digitalWrite(relayPump, LOW);
    digitalWrite(relaysValve[0], LOW);
    
    digitalWrite(ledRed, LOW);
    delay(2000);
  }*/

  /*while(true){
    digitalWrite(ledRed, HIGH);
    digitalWrite(relaysValve[1], HIGH);
    delay(3000);
    digitalWrite(relaysValve[1], LOW);
    delay(3000);
    
    digitalWrite(relaysValve[2], HIGH);
    delay(3000);
    digitalWrite(relaysValve[2], LOW);
    delay(3000);

    digitalWrite(relaysValve[0], HIGH);
    delay(3000);
    digitalWrite(relaysValve[0], LOW);
    delay(3000);
  }*/
  
  // delay 1 second between reads


  // Real code
  String postRequest = (String)sensorsCount;
  for(int i = 0; i < sensorsCount; i++){
    checkSensor(i);
    postRequest = postRequest + '.' + (String)sensorsValue[i];
  }
  Serial.println(postRequest);
  delay(3000);
}
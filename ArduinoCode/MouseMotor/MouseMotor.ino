#include<Servo.h>

Servo serX;
Servo serY;
String serialData;

void setup() {
  serX.attach(10); // Attaching the x axis servo to pin 10
  serY.attach(11); // Attaching the Y axis servo to pin 11
  Serial.begin(9600);
  Serial.setTimeout(10);
}

void loop() {
  // Comment
}

void serialEvent(){
  serialData = Serial.readString(); // Serial data will be X###Y###

  serX.write(parseDataX(serialData));
  serY.write(parseDataY(serialData));
}

int parseDataX(String data){
  data.remove(data.indexOf("Y"));
  data.remove(data.indexOf("X"), 1);

  return data.toInt;
}

int parseDAtaY(String data){
  data.remove(0, data.indexOf("Y")+1);

  return data.toInt;
}

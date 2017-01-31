#include <Servo.h>

const unsigned int BAUD_RATE = 9600;

const unsigned int KEY_IN_X = 0; //Pin controller x to analog 0
const unsigned int KEY_IN_Y = 1; //Pin controller y to analog 1

const unsigned int MOTOR_PIN = 13; //Pin motor to Digital output 13
const unsigned int MOTOR_DELAY = 0;

Servo servo;

void setup() {
  Serial.begin(BAUD_RATE); //Init serial
  servo.attach(MOTOR_PIN); //Attach motor
}

void loop() {
 float x, y = 0;
  x = analogRead(KEY_IN_X); //Read x coord
  y = analogRead(KEY_IN_Y); //Read y coord

  int motor_angle = int(x/3.722)<10?10:int(x/3.722); //Set minimum motor angle as 10 degree.
  servo.write(motor_angle); //Turn motor
  
  Serial.print("x=");//Write to monitor
  Serial.print(x);
  Serial.print(" y=");
  Serial.print(y);
  Serial.print(" angle=");
  Serial.print(motor_angle);
  Serial.println();

  delay(MOTOR_DELAY);
}

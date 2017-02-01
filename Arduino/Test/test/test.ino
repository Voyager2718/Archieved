#include <Servo.h>

const unsigned int BAUD_RATE = 9600;

const unsigned int KEY_IN_X = 0; //Pin controller x to analog 0 (Range: [0,671])
const unsigned int KEY_IN_Y = 1; //Pin controller y to analog 1
const unsigned int KEY_IN_PRESS = 2; //Pin controller SW(Press) to analog 2

const unsigned int MOTOR_PIN = 12; //Pin motor to Digital output 12
const unsigned int MOTOR_DELAY = 0;

const unsigned int SERIAL_DELAY = 0;

const unsigned int LED_PIN = 13; //Pin LED to Digital output 13

Servo servo;

void setup() {
  Serial.begin(BAUD_RATE); //Init serial
  
  servo.attach(MOTOR_PIN); //Attach motor

  pinMode(LED_PIN, OUTPUT); // Set LED pin as output
}

int motor_speed = 0;
int motor_angle = 100;

void loop() {
  float x, y;
  int pressed;
  x = analogRead(KEY_IN_X); //Read x coord
  y = analogRead(KEY_IN_Y); //Read y coord
  pressed = !analogRead(KEY_IN_PRESS); //Read press or not (Not 0: Pressed; 0 Not Pressed)

  if(x < 5){
    motor_speed = -180;
  }else if(x >= 5 && x < 50){
    motor_speed = -25;
  }else if(x >= 50 && x < 200){
    motor_speed = -10;
  }else if(x >= 200 && x < 300){
    motor_speed = -1;
  }else if(x >= 300 && x < 350){
    motor_speed = 0;
  }else if(x >= 350 && x < 450){
    motor_speed = 1;
  }else if(x >= 450 && x < 600){
    motor_speed = 10;
  }else if(x >= 600 && x < 670){
    motor_speed = 25;
  }else if(x >= 670){
    motor_speed = 180;
  }

  motor_angle += motor_speed;

  if(motor_angle > 180){
    motor_angle = 180;
  }
  if(motor_angle < 10){
    motor_angle = 10;
  }

  if(pressed){
    digitalWrite(LED_PIN, HIGH);  
    motor_angle = 100;
  }else{
      digitalWrite(LED_PIN, LOW);
  }

  servo.write(motor_angle); //Turn motor
  
  Serial.print("x=");//Write to monitor
  Serial.print(x);
  Serial.print(" y=");
  Serial.print(y);
  Serial.print(pressed?" Pressed":" Not pressed");
  Serial.print(" speed=");
  Serial.print(motor_speed);
  Serial.print(" angle=");
  Serial.print(motor_angle);
  Serial.println();

  delay(MOTOR_DELAY + SERIAL_DELAY);
}


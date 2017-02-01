#include <Servo.h>

const unsigned int BAUD_RATE = 9600;

const unsigned int KEY_IN_X = 0; //Pin controller x to analog 0 (Range: [0,671])
const unsigned int KEY_IN_Y = 1; //Pin controller y to analog 1
const unsigned int KEY_IN_PRESS = 2; //Pin controller SW(Press) to analog 2

const unsigned int MOTOR_PIN = 12; //Pin motor to Digital output 12
const unsigned int MOTOR_DELAY = 0;

const unsigned int SERIAL_DELAY = 5;

const unsigned int LED_PIN = 13; //Pin LED to Digital output 13

Servo servo;

int led_off_delay = 0;

void setup() {
  Serial.begin(BAUD_RATE); //Init serial
  
  servo.attach(MOTOR_PIN); //Attach motor

  pinMode(LED_PIN, OUTPUT); // Set LED pin as output
}

int motor_angles[3] = {0, 0, 0};
int motor_angle_present = 0;
int motor_angles_index = 0;

void loop() {
  float x, y;
  int pressed;
  x = analogRead(KEY_IN_X); //Read x coord
  y = analogRead(KEY_IN_Y); //Read y coord
  pressed = !analogRead(KEY_IN_PRESS); //Read press or not (Not 0: Pressed; 0 Not Pressed)

  //int motor_angle = int(x/3.722)<10?10:int(x/3.722); //Set minimum motor angle as 10 degree.
  int motor_angle = int(x/39.4706)*10+10; // Angle = floor(x/(range of x/number of segments))*(range of motor/number of segments) + minimum angle of motor
  motor_angles[motor_angles_index] = motor_angle;
  motor_angles_index++;
  if(motor_angles_index>2){
    motor_angles_index=0;
  }
  if(motor_angles[0]+motor_angles[1]+motor_angles[2]==motor_angles[0]*3){
    motor_angle_present=motor_angles[0];
  }
  
  servo.write(motor_angle_present); //Turn motor

  if(pressed){
    led_off_delay = 0;
    digitalWrite(LED_PIN, HIGH);  
  }else{
    if(led_off_delay < 50){
      led_off_delay ++;
    }else{
      digitalWrite(LED_PIN, LOW);
      led_off_delay = 0;
    }
  }
  
  Serial.print("x=");//Write to monitor
  Serial.print(x);
  Serial.print(" y=");
  Serial.print(y);
  Serial.print(pressed?" Pressed":" Not pressed");
  Serial.print(" angle=");
  Serial.print(motor_angle_present);
  Serial.println();

  delay(MOTOR_DELAY + SERIAL_DELAY);
}

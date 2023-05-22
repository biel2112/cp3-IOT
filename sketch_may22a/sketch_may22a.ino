#include <Servo.h>
Servo servoMotor;

// Pino utilizado para controlar o LED
const int ledPin = 13;

void setup() {
  // Inicialização da comunicação serial
  Serial.begin(9600);

  // Inicialização do pino do servo motor
  servoMotor.attach(3);

  // Inicialização do pino do LED como saída
  pinMode(ledPin, OUTPUT);

  // Desligar o LED inicialmente
  digitalWrite(ledPin, LOW);
}

void loop() {
  if (Serial.available()) {
    char signal = Serial.read();
    if (signal == '1') {
      digitalWrite(ledPin, HIGH);  // Acender o LED
    } else if (signal == '0') {
      digitalWrite(ledPin, LOW);  // Apagar o LED
    }
  }
}

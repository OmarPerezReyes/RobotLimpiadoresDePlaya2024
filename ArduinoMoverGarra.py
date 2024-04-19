#include <Servo.h>

Servo servo1;  // Declaración del objeto servo1
Servo servo2;  // Declaración del objeto servo2

const pin = 10;
int servo1Pin = 8;  // Pin donde se conecta el servo1
int servo2Pin = 9; // Pin donde se conecta el servo2

void setup() {
  servo1.attach(servo1Pin); // Inicialización del servo1
  servo2.attach(servo2Pin); // Inicialización del servo2
  pinMode(pin, INPUT);
  Serial.begin(9600); // Iniciar comunicación serial
}

void loop() {
  int estado = digitalRead(pin);
  
  
    
    if (estado == HIGH) { // Si el comando es '1'
      moveServosToZero(); // Mover ambos servos a la posición 0 grados
      delay(5000); // Si el comando es '2'
      moveServosTo180
      delay(5000);
    }

}

// Función para mover ambos servos a la posición 180 grados
void moveServosTo180() {
  servo1.write(180); // Mover servo1 a 180 grados
  servo2.write(0);   // Mover servo2 a 0 grados (opuesto a 180)
}

// Función para mover ambos servos a la posición 0 grados
void moveServosToZero() {
  servo1.write(0);   // Mover servo1 a 0 grados
  servo2.write(180); // Mover servo2 a 180 grados (opuesto a 0)
}

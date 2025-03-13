/*
 * Doodle Bot Arduino Sketch
 *
 * This sketch controls the motors of the doodle car based on Serial commands
 * or a preprogrammed set of directions.
 */

// Motor A pins
const int motorA1 = 3;
const int motorA2 = 4;
const int enableA = 5;

// Motor B pins
const int motorB1 = 6;
const int motorB2 = 7;
const int enableB = 9;

// Motor speed (PWM value: 0-255)
const int motorSpeed = 200;

// Flag to use preprogrammed directions or Serial commands
const bool usePreprogrammedDirections = true;

// Preprogrammed directions
String directions[] = {"Move Up", "Move Right", "Move Down", "Move Left"};
int numDirections = sizeof(directions) / sizeof(directions[0]);
int currentDirection = 0;

// Delay between consecutive directions (milliseconds)
const unsigned long directionDelay = 1500;
unsigned long lastDirectionTime = 0;

void setup() {
  Serial.begin(9600);
  
  pinMode(motorA1, OUTPUT);
  pinMode(motorA2, OUTPUT);
  pinMode(enableA, OUTPUT);
  pinMode(motorB1, OUTPUT);
  pinMode(motorB2, OUTPUT);
  pinMode(enableB, OUTPUT);

  stopMotors();
}

void loop() {
  if (Serial.available() > 0) {
    String command = Serial.readStringUntil('\n');
    command.trim();
    Serial.print("Received command: ");
    Serial.println(command);
    executeCommand(command);
    return;
  }
  
  if (usePreprogrammedDirections && currentDirection < numDirections) {
    unsigned long currentTime = millis();
    if (currentTime - lastDirectionTime >= directionDelay) {
      String cmd = directions[currentDirection];
      Serial.print("Executing preprogrammed command: ");
      Serial.println(cmd);
      executeCommand(cmd);
      currentDirection++;
      lastDirectionTime = currentTime;
    }
  }
}

void executeCommand(String cmd) {
  stopMotors();

  if (cmd.equalsIgnoreCase("Move Right")) {
    moveRight();
  } else if (cmd.equalsIgnoreCase("Move Left")) {
    moveLeft();
  } else if (cmd.equalsIgnoreCase("Move Up")) {
    moveForward();
  } else if (cmd.equalsIgnoreCase("Move Down")) {
    moveBackward();
  } else {
    Serial.println("Unknown command received.");
  }
}

void moveForward() {
  digitalWrite(motorA1, HIGH);
  digitalWrite(motorA2, LOW);
  digitalWrite(motorB1, HIGH);
  digitalWrite(motorB2, LOW);
  analogWrite(enableA, motorSpeed);
  analogWrite(enableB, motorSpeed);
  Serial.println("Moving forward.");
  delay(500);
  stopMotors();
}

void moveBackward() {
  digitalWrite(motorA1, LOW);
  digitalWrite(motorA2, HIGH);
  digitalWrite(motorB1, LOW);
  digitalWrite(motorB2, HIGH);
  analogWrite(enableA, motorSpeed);
  analogWrite(enableB, motorSpeed);
  Serial.println("Moving backward.");
  delay(500);
  stopMotors();
}

void moveRight() {
  digitalWrite(motorA1, HIGH);
  digitalWrite(motorA2, LOW);
  digitalWrite(motorB1, LOW);
  digitalWrite(motorB2, HIGH);
  analogWrite(enableA, motorSpeed);
  analogWrite(enableB, motorSpeed);
  Serial.println("Turning right (90°).");
  delay(600);
  stopMotors();
}

void moveLeft() {
  digitalWrite(motorA1, LOW);
  digitalWrite(motorA2, HIGH);
  digitalWrite(motorB1, HIGH);
  digitalWrite(motorB2, LOW);
  analogWrite(enableA, motorSpeed);
  analogWrite(enableB, motorSpeed);
  Serial.println("Turning left (90°).");
  delay(600);
  stopMotors();
}

void stopMotors() {
  digitalWrite(motorA1, LOW);
  digitalWrite(motorA2, LOW);
  digitalWrite(motorB1, LOW);
  digitalWrite(motorB2, LOW);
  analogWrite(enableA, 0);
  analogWrite(enableB, 0);
}

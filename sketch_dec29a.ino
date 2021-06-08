void goStraight(int sp2);
void turnLeft();
void waterBomb();

bool doIt = false;

void setup() {
  pinMode(5, OUTPUT);
  pinMode(6, OUTPUT);
  pinMode(10, OUTPUT);
}

void loop() {
  delay(15000);
  while(!doIt){
    goStraight(40);
    delay(2000);
    stopIt();
    delay(3000);

    goStraight(40);
    delay(4000);
    stopIt();
    delay(2000);
    
    waterBomb();
    delay(2000);

    goStraight(40);
    delay(8000);
    stopIt();
    delay(2000);
    
    doIt = true;
  }
}

void goStraight(int sp2) {
  analogWrite(5, 30);
  analogWrite(6, sp2-2);
}

void stopIt() {
  analogWrite(5, 0);
  analogWrite(6, 0);
}
void waterBomb() {
  analogWrite(10, 100);
  delay(2000);
  analogWrite(10, 0);
}

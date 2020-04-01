#define trigPin 7
#define echoPin 8
float duration;
long distance;
int getDistance(int trigPin_, int echoPin_) {
  digitalWrite(trigPin_, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin_, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin_, LOW);
  duration = pulseIn(echoPin_, HIGH);
  distance = duration * 0.0347 / 2;
  return distance;
}
void setup() {
  Serial.begin(115200);
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
}

void loop() {
  Serial.println(String(getDistance(trigPin,echoPin)));
  delay(100);
}

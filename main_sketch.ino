int ldrpin = A3;
void setup() {
  Serial.begin(9600);
  pinMode(ldrpin, INPUT);
}
void loop() {
  int x = analogRead(ldrpin);
  Serial.println(x);
  delay(1000);
}
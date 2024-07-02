//Ejemplo prueba (no tengo aún arduino y no se cpp)

const int sensorHumedad1 = A0;
const int sensorHumedad2 = A1;
const int sensorHumedad3 = A2;

void setup() {
  Serial.begin(9600);
}

void loop() {
  int humedad1 = analogRead(sensorHumedad1);
  int humedad2 = analogRead(sensorHumedad2);
  int humedad3 = analogRead(sensorHumedad3);

  Serial.print(humedad1);
  Serial.print(",");
  Serial.print(humedad2);
  Serial.print(",");
  Serial.println(humedad3);

  delay(60000); // Enviar datos cada minuto
}

//IA GENERATED


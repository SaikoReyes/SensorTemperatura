int bits[] = {2, 3, 4, 5, 6, 7, 8, 9};  // Pins para los bits

void setup() {
  // Configurar los pines como entrada
  for (int i = 0; i < 8; i++) {
    pinMode(bits[i], INPUT);
  }
  Serial.begin(9600);
}

void loop() {
  int valor8bits = 0;

  // Leer cada bit y agregarlo al valor de 8 bits
  for (int i = 0; i < 8; i++) {
    int valorBit = digitalRead(bits[i]);
    valor8bits |= valorBit << i;
  }

  // Enviar el valor a través del puerto serial
  Serial.println(valor8bits);

  delay(1000);  // Esperar 1 segundo antes de leer el siguiente valor
}

#include <ArduinoJson.h>
#include <OneWire.h>
#include <DallasTemperature.h>
#include <DHT.h>
#include <SD.h>
#include <Wire.h>
#include <LiquidCrystal_I2C.h>

#define DHTPIN 3
#define DHTTYPE DHT22
 
DHT dht(DHTPIN, DHTTYPE);
OneWire ourWire(5);
DallasTemperature sensors(&ourWire);

// Variables para los sensores analógicos
int pHSense = A0;
int ldrSense = A1;
int tdsSense = A2;
int samples = 10;
float adc_resolution = 1024.0;
float tdsValue;

unsigned long previousMillis = 0;
const unsigned long interval = 3000; // Intervalo de tiempo para cambiar los datos en el LCD (en milisegundos)
int dataMode = 0; // Variable para controlar el modo de datos en el LCD

void setup()
{
  Serial.begin(115200);
  sensors.begin();
}

void loop()
{
  unsigned long currentMillis = millis();

  // Verificar si ha pasado el intervalo de tiempo
  if (currentMillis - previousMillis >= interval) {
    previousMillis = currentMillis;

    // Incrementar el modo de datos
    dataMode++;
    if (dataMode > 2) {
      dataMode = 0;
    }
  }

  float ds18b20Temperature = readDS18B20Temperature();
  float dht22Temperature, dht22Humidity;
  readDHT22Data(dht22Temperature, dht22Humidity);
  int ldrValue = readLDRValue();
  float luxValue = map(ldrValue, 0, 1023, 0, 1000);
  float phValue = readPHValue();
  float tdsValue = readTDSValue();

  Serial.println(String(dht22Temperature,2) + "," + String(dht22Humidity,2) + "," + String(ds18b20Temperature,2) + "," + String(luxValue,2) + "," + String(phValue,2) + "," + String(tdsValue,2) );

  delay(5000);
}


float readDS18B20Temperature()
{
  sensors.requestTemperatures();
  float temperature = sensors.getTempCByIndex(0);
  return temperature;
}

void readDHT22Data(float &temperature, float &humidity)
{
  // Generar valores aleatorios dentro del rango 30.01 a 32.60 (con dos decimales)
  int randomTemperature = random(3001, 3260);
  int randomHumidity = random(8001, 8960);

  // Asignar los valores aleatorios a las variables de temperatura y humedad
  temperature = randomTemperature / 100.0;
  humidity = randomHumidity / 100.0;
}



int readLDRValue()
{
  int value = analogRead(ldrSense);
  return value;
}

float readPHValue()
{
  int measurings = 0;
  for (int i = 0; i < samples; i++)
  {
    measurings += analogRead(pHSense);
    delay(100);
  }

  float voltage = 5 / adc_resolution * measurings / samples;
  float phValue = 10 + ((2.5 - voltage) / 0.18);
  return phValue;
}

float readTDSValue()
{
  int sensorValue = analogRead(tdsSense);
  float calibrationFactor = 5;
  float tdsValue = sensorValue * calibrationFactor;
  return tdsValue;
}
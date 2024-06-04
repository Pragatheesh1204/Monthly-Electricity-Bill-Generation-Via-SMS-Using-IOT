#include <SoftwareSerial.h>
#define ANALOG_IN_PIN A0

#include <LiquidCrystal_I2C.h>

SoftwareSerial mySerial(5, 4); //SIM800L Tx & Rx is connected to Arduino #3 & #2
 
// Floats for ADC voltage & Input voltage
float adc_voltage = 0.0;
float adc_voltag = 0.0;
float in_voltage = 0.0;
float in_voltag = 0.0;

// Floats for resistor values in divider (in ohms)
float R1 = 30000.0;

float R2 = 7500.0; 
 
// Float for Reference Voltage
float ref_voltage = 5.3;
 
// Integer for ADC value
int adc_value = 0;
int adc_valu = 0;
 LiquidCrystal_I2C lcd(0x27, 16, 2);
 
void setup()
{
   // Setup Serial Monitor
   Serial.begin(9600);
   Serial.println("DC Voltage Test");
   pinMode(4, OUTPUT);
   lcd.begin();                      // initialize the lcd 
    lcd.backlight();
  
  mySerial.begin(9600);
}
 
void loop()
{
   // Read the Analog Input
   adc_value = analogRead(ANALOG_IN_PIN);

   // Determine voltage at ADC input
   adc_voltage  = (adc_value * ref_voltage) / 1024.0; 

   // Calculate voltage at divider input
   in_voltage = adc_voltage / (R2/(R1+R2)) ; 
   
   // Prin

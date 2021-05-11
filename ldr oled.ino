// the number of the LED pin
const int ledPin = 16;  
// setting PWM properties
const int freq = 5000;
const int p = 0;
const int resolution = 8;
 #include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>
#define SCREEN_WIDTH 128 // OLED display width, in pixels
#define SCREEN_HEIGHT 64 // OLED display height, in pixels
// Declaration for an SSD1306 display connected to I2C (SDA, SCL pins)
Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, -1);

void setup(){
  // configure LED PWM functionalitites
  ledcSetup(p, freq, resolution);
  Serial.begin(9600);
  // attach the channel to the GPIO to be controlled
  ledcAttachPin(ledPin, p);
  Serial.println("oled test");
  if(!display.begin(SSD1306_SWITCHCAPVCC, 0x3C)) { 
    Serial.println("SSD1306 allocation failed");
    for(;;);
  }
  delay(2000);
}
 
void loop(){
  // increase the LED brightness
  int a=analogRead(15);
  Serial.println(a);
  delay(500);
  if(a<400)
  {
  ledcWrite(p, 0);  
  }
  if(a<1000&&a>400)
  {
    ledcWrite(p, 10);
  }
  if(a<2000&&a>1000)
  {
    ledcWrite(p, 50);
  }
  if(a>1000&&a<3500)
  {
    ledcWrite(p, 100);
  }
  if(a>3500)
  {
    ledcWrite(p, 255);
  }
  display.clearDisplay();
  display.setTextSize(1);
  display.setTextColor(WHITE);
  display.setCursor(0, 10);
  // Display static text
    display.println("LDR VALUE IS ");
  display.print(a);
  display.display(); 
  }

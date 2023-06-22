#include <MD_Parola.h>
#include <MD_MAX72xx.h>
#include <SPI.h>
#define HARDWARE_TYPE MD_MAX72XX::FC16_HW 
#define CLK_PIN   13  // or SCK
#define DATA_PIN  11  // or MOSI
#define CS_PIN    10  // or SS
#define MAX_DEVICES 4
MD_Parola myDisplay = MD_Parola(HARDWARE_TYPE, CS_PIN, MAX_DEVICES);
void setup() {
	myDisplay.begin();
	myDisplay.setIntensity(5);
	myDisplay.displayClear();
}
  void loop() {
  static uint16_t scrollSpeed = 50;
  myDisplay.setTextAlignment(PA_CENTER);
	myDisplay.print("PRANAV");
  myDisplay.displayAnimate();
	delay(scrollSpeed);
}
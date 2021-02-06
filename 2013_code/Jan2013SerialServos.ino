// RCArduinoSerialServos by DuaneB is licensed under a Creative Commons Attribution-NonCommercial 3.0 Unported License.
// Based on a work at rcarduino.blogspot.com.
#include "RCArduinoSerialServosLocal.h"

volatile uint32_t ulRiseTime;
volatile uint32_t ulPulseWidth;

void setup()
{
  Serial.begin(9600);
  Serial.println("RCArduinoSerialServos");
 
  // set the channels
  for(uint16_t nChannel = 0;nChannel < RCARDUINO_MAX_SERVOS;nChannel++)
  {
    CRCArduinoSerialServos::writeMicroseconds(nChannel,1000+(nChannel*50));
  }

  CRCArduinoSerialServos::begin();
 
  attachInterrupt(0,calcPulse,CHANGE);
}

void loop()
{
  delay(10);

  if(ulPulseWidth != 0)
  {
    // disable interrupts so that our pulse value does not get overwritten while we try and read it
    uint8_t sReg = SREG;
    cli();
   
    // take a local copy of the pulse witdth so that we can reenable interrupts as soon as possible
    uint32_t ulLocalPulseWidth = ulPulseWidth;
   
    // clear the pulse width so that we will only pick up new values written by calcPulse rather
    // than keep printing old values.
    ulPulseWidth = 0;
   
    // turn interrupts back on
    SREG = sReg;
   
    // print the pulse width
    Serial.println(ulLocalPulseWidth);
  }
 
}

// Read pulse width applied to digital pin 2 (interrupt 0)
void calcPulse()
{
  if(digitalRead(2))
  {
    ulRiseTime = micros();
  }
  else
  {
    ulPulseWidth = micros()- ulRiseTime;
  }
}

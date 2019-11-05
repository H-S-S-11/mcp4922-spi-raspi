#need to use GPIO for chip selects

import wiringpi
wiringpi.wiringPiSetupGpio()

def setupDacSPI(speed, dac0, dac1, dac2, dac3):
    wiringpi.pinMode(dac0, 1)
    wiringpi.pinMode(dac1, 1)
    wiringpi.pinMode(dac2, 1)
    wiringpi.pinMode(dac3, 1)
    
    wiringpi.digitalWrite(dac0, 1)
    wiringpi.digitalWrite(dac1, 1)
    wiringpi.digitalWrite(dac2, 1)
    wiringpi.digitalWrite(dac3, 1)
    
    #This is channel 0 so GPIO10=MOSI, GPIO11=SCK
    wiringpi.wiringPiSPISetup(0, speed)
        
def dacShutdown(dac, shutdown):
    wiringpi.digitalWrite(dac, not shutdown)

def writeDacSPI(dac, DACchannel, buffer, notGain, notShutdown, data):
    #select DAC channel
    dataH = data>>8
    dataL = data &0xff
    dataH = dataH | (DACchannel<<7)
    dataH = dataH | (buffer<<6)
    dataH = dataH | (notGain<<5)
    dataH = dataH | (notShutdown<<4)
    
    sendBuf = chr(dataH)+chr(dataL)
    #print(sendBuf)    
    
    wiringpi.digitalWrite(dac, 0)
    wiringpi.wiringPiSPIDataRW(0, sendBuf)
    wiringpi.digitalWrite(dac, 1)                

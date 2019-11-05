import dacSPI
import time

spiSpeed = 8000000
dac0cs = 0 #gpio pins
dac1cs = 1
dac2cs = 2
dac3cs = 3
dac0shutdown = 4

dacSPI.setupDacSPI(spiSpeed, dac0cs, dac1cs, dac2cs, dac3cs)

#shutdown is optional, pin can be tied high
dacSPI.dacShutdown(dac0shutdown, False)

#shows mapping of function arguments to command bits
DACchannel, buffer, notGain, notShutdown, data = 0, 1, 1, 1, 0

dacSPI.writeDacSPI(dac0cs, DACchannel, buffer, notGain,
                    notShutdown, data)
time.sleep(1)

for n in range(0, 4095):
    dacSPI.writeDacSPI(dac0cs, DACchannel, buffer, notGain,
                       notShutdown, n)
    time.sleep(0.005)
    #20 second ramp

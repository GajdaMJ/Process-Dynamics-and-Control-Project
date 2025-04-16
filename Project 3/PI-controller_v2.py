import MAPort_6EX80
import numpy as np
import time

# Here, we create an instance of the class MAPort_6EX80, named MyMAPort.
# This class allows interaction with the physical system through its properties.
MyMAPort=MAPort_6EX80.MAPort_6EX80()

Kc=0.24005378387901455

tau=6.6


# The ReadHeight property allows you to read the height of the water level in the tank.
# Example
# Height=MyMAPort.ReadHeight()

# The WritePumpFlow property allows you to set the pump flow rate.
# Example
# MyMAPort.WritePumpFlow(pumpflow)

# The Lamp property receives a binary input that turns on/off the lamp in the physical set up.
# Example
# MyMAPort.Lamp(0)

# SimLength is the length of the simulation in seconds
SimLength = 500

# In this section of the code, you can implement the control strategy you want to use. 
# Below is an example of a simple control strategy based on a level condition.

# Let's imagine that we need to maintain the water level in a boiler between 300 mm and 350 mm. The boiler's vapor demand follows a sine function with a period of 10 seconds.
# This demand causes a decrease in the tank level, which is a disturbance for the systems, is represented by the opening of the valve.
integrating_error=0

for i in range(SimLength):
    targ_height=350
    Height=MyMAPort.ReadHeight()
    error=targ_height-Height
    # Simulate the boiler demand
    T = 10 
    #Demand = np.sin(2*np.pi*i/T)

    # Open the valve following the demand profile
    valve=MyMAPort.WriteValvePosition(0.1)
    dt=0.1
    # First we read the current water level.
    if error > 0:
        integrating_error+=error*dt
        er=np.clip(integrating_error, -100, 100)
        # Then, if it is below our threshold we increase the pump mass flow rate.
        Pumpcontrol = error*Kc + Kc*er/tau
        Pumpcontrol= max(0,min(0.1,Pumpcontrol))

    # Send the signal to the pump.
    MyMAPort.WritePumpFlow(Pumpcontrol)
    # Print the current height and control action.              
    print(i, Pumpcontrol, Height)
    time.sleep(1)

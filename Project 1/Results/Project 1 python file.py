import MAPort_6EX80
import numpy as np
import time

# Here, we create an instance of the class MAPort_6EX80, named MyMAPort.
# This class allows interaction with the physical system through its properties.
MyMAPort=MAPort_6EX80.MAPort_6EX80()

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
SimLength = 900

# In this section of the code, you can implement the control strategy you want to use. 
# Below is an example of a simple control strategy based on a level condition.

# Let's imagine that we need to maintain the water level in a boiler between 300 mm and 350 mm. The boiler's vapor demand follows a sine function with a period of 10 seconds.
# This demand causes a decrease in the tank level, which is a disturbance for the systems, is represented by the opening of the valve.

for i in range(SimLength):

    # Simulate the boiler demand
    T = 10 
    Demand = np.sin(2*np.pi*i/T)

    # Open the valve following the demand profile
    MyMAPort.WriteValvePosition(Demand)
   
    # We want the water level to be inbetween 300 and 350mm.
    LowerLevel = 325
    UpperLevel = 375

    # First we read the current water level.
    Height=MyMAPort.ReadHeight()

    if Height < LowerLevel:
        # Then, if it is below our threshold we increase the pump mass flow rate.
        Pumpcontrol = 0.08
        # Send the signal to the pump.
        MyMAPort.WritePumpFlow(Pumpcontrol)
    if Height > UpperLevel:
        # If the level is above our threshold we close the pump.
        Pumpcontrol = 0
        # Send the signal to the pump
        MyMAPort.WritePumpFlow(Pumpcontrol)
    # Print the current height and control action.              
    print(i, Pumpcontrol, Height)
    # This line makes each iteration to run every second please remain this lane unchanged. 
    time.sleep(1)

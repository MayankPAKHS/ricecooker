# Demo of rice cooker simulation

import ricecooker as rc

rc.presets["n"] = 5 # Change one configuration

rc.derive() # Derive the variables

print(rc.Q) # Load a derived variable

rc.derive.print() # Print all derived variables


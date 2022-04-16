#!/usr/bin/env python3
import sys

from pa1010d import PA1010D


if len(sys.argv) < 2:
    print(f"Usage: {sys.argv[0]} <on/off> <ms>")
    sys.exit()

gps = PA1010D()

'''
> Data Field:
>  PMTK285,PPSType,PPSPulseWidth
> PPSType: Availablity
> .0. = Disable
> .1. = After the first fix
> .2. = 3D fix only
> .3. = 2D/3D fix only
> .4. = Always
> PPSPulseWidth: PPS pulse width (unit: ms)
'''

width = "," + sys.argv[2] if len(sys.argv) == 3 and sys.argv[2].isnumeric() else ""

if sys.argv[1] == "on":
    gps.send_command("PMTK285,1"+width)
elif sys.argv[1].isnumeric():
    gps.send_command("PMTK285,"+sys.argv[1]+width)
else:
    gps.send_command("PMTK285,0")

result = gps.update()

print("OK" if result else "Uh oh!")

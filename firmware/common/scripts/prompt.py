# ***************************************************************************************
# ***************************************************************************************
#
#      Name :      prompt.py
#      Authors :   Paul Robson (paul@robsons.org.uk)
#      Date :      22nd November 2023
#      Reviewed :  No
#      Purpose :   Prompt creator (counts builds etc.)
#
# ***************************************************************************************
# ***************************************************************************************

import sys
from datetime import datetime

h = open(sys.argv[1])
version = int(h.read(-1))+1
h.close()

h = open(sys.argv[1],"w")
h.write("{0}\n".format(version))
h.close()

print("//\n//\tThis file is automatically generated\n//")

date = datetime.now().strftime("%d-%b-%y")

print("#define PROMPT \"(Build {0} {1})\\r\"".format(version,date))
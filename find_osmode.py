#Write a Python program to determine if the python shell is executing in 32bit or 64bit mode on operating system
#What does struct Calcsize do?
#struct. calcsize('P') calculates the number of bytes required to store a single pointer -- returning 4 on a 32-bit system and 8 on a 64-bit system

import struct
print(struct.calcsize('P')*8)
import imp
print("Location of Python os module sources:")
print(imp.find_module('os'))
print("\nLocation of Python sys module sources:")
print(imp.find_module('datetime'))


import os
print("\nList of directories in os module:")
print(os.path)
print("\nList of directories in sys module:")
import sys
print(sys.path)
print(datetime.path)
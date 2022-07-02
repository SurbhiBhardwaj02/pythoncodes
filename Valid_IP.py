import socket
#addr='125.0.0.76'
addr='125.0.0.257'
try:
    socket.inet_aton(addr)
    print("Valid ip")
except socket.error:
    print("Invalid ip")

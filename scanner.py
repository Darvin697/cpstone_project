import sys
import socket
from datetime import datetime
import threading

#function to scan a port
def scan_port(target,port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.timeout(1)
        result = s.connect_ex((target,port))
        if result==0:
            print(f"port {port} is open")
        s.close()
    except socket.error as e:
        print(f"socket error on port {port}: {e}")
    except Exception as e:
        print(f"Unexcepted error on port {port}: {e}")

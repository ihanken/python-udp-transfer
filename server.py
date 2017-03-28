from socket import *
from sys import *
import struct
from constants import *

class Server():
    def __init__(self, args):
        ''' Locally Assigned Attributes '''
        self.__args = args
        self.__buffer = 1024

        ''' Command Line Argument Attributes '''
        self.__ip = self.parseIPArgument() # Parse our IP.
        self.__port = self.parsePortArgument() # Parse our port.
        self.__address = (self.__ip, self.__port) # Create a tuple from the values.

        print(self.__address)

        self.__socket = socket(AF_INET, SOCK_DGRAM) # Set up our socket.

    ''' Parse the IP address. Fails if no IP is provided. '''
    def parseIPArgument(self):
        try: return str(self.__args[1])
        except IndexError:
            exit("Please provide an IP address.\n" + SERVER_EXAMPLE_USAGE)

    ''' Parse the port. Fails if no value is provided or the value is invalid. '''
    def parsePortArgument(self):
        try: port = int(self.__args[2])
        except ValueError: # Can't convert the value to an int.
            exit("Port must be an integer.\n" + SERVER_EXAMPLE_USAGE)
        except IndexError: # No value was provided.
            exit("Port number must be provided.\n" + SERVER_EXAMPLE_USAGE)

        if not 1024 <= port <= 60000: # Port is out of range.
            exit("Port must be between 1024 and 60000.\n" + SERVER_EXAMPLE_USAGE)
        else: return port

    ''' Begin transmitting the requested file. '''
    def sendFile(self, filename): return filename

if __name__ == "__main__":
    server = Server(argv)

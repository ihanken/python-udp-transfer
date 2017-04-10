from socket import *
from sys import *
import struct
from constants import *
import errno
import re

class Client():
    def __init__(self, args):
        ''' Locally Assigned Attributes '''
        self.__args = args
        self.__buffer = 1024

        ''' Command Line Argument Attributes '''
        self.__ip = self.parseIPArgument() # Parse our IP.
        self.__port = self.parsePortArgument() # Parse our port.
        self.__address = (self.__ip, self.__port) # Create a tuple from the values.
        self.__socket = None # Set up our socket variable.

    '''
    This function requests the data that the server is holding. The server
    is specified by the ip and port supplied to the client. Alternating bit
    Protocol is used.
    '''
    def requestDataWithAlternatingBit(self):
        self.__socket = socket(AF_INET, SOCK_STREAM) # Initialize Socket.
        self.__socket.connect((self.__ip, self.__port)) # Connect socket.
        self.__socket.settimeout(2.0) # Give the socket a 2 second timeout.

        sequenceNumber = 0  # A record of the current sequenceNumber reached.
        ACK = 0             # A record of the acknowledgement number.
        data = []           # A record of the data received.

        _ = input("Press enter to begin transmission.") # Prompt user to begin.
        print("Requesting data from server...\n")

        while True:
            try:
                self.__socket.send(str(ACK).encode("utf-8")) # Set up the connection.
                received = self.__socket.recv(1024).decode("utf-8") # Get data.

                ACK = received[-1:] # Get the number we need to ACK.
                message = received.split('^')[0] # Only grab first message.

                if message == CLOSING_MESSAGE: break # Stop if we have all data.
                else: # Keep ACKing
                    if ACK == str(sequenceNumber): # We are ready to move on.
                        sequenceNumber ^= 1 # Invert the sequenceNumber

                        data.append(message) # Append out data.

                        self.__socket.send(str(ACK).encode("utf-8")) # Send ACK
            except timeout: print("Timed out.") # Handle a time out.
            except error: break # Prevents a discontinued connection from
                                # breaking the script.

        self.__socket.close() # Close the socket.

        return data

    '''
    This function requests the data that the server is holding. The server
    is specified by the ip and port supplied to the client. Selective Repeat
    Protocol is used.
    '''
    def requestDataWithSelectiveRepeat(self):
        self.__socket = socket(AF_INET, SOCK_STREAM) # Initialize Socket.
        self.__socket.connect((self.__ip, self.__port)) # Connect socket.
        self.__socket.settimeout(2.0) # Give the socket a 2 second timeout.

        data = [] # A record of the data received.

        _ = input("Press enter to begin transmission.") # Prompt user to begin.
        print("Requesting data from server...\n")

        ACK = None # Send an empty ACK to start transmission.

        while True:
            try:
                self.__socket.send(("ACK: " + str(ACK)).encode("utf-8")) # Set up the connection.
                received = self.__socket.recv(1024).decode("utf-8") # Get data.

                received = received.split('^') # Split to get the message and ACK.

                if len(received) < 2: continue  # This is an empty message,
                                                # so skip to the next one.

                ACK = int(re.sub("[^0-9]", "", received[1])) # Get the number we need to ACK.
                message = received[0] # Only grab first message.

                if message == CLOSING_MESSAGE: break # Stop if we have all data.
                else: # Keep ACKing
                    while len(data) - 1 < ACK: data.append(None) # Extend the list.
                    data[ACK] = message # Add the message to the list.

                    self.__socket.send(("ACK: " + str(ACK)).encode("utf-8")) # Send ACK
            except timeout: print("Timed out.") # Handle a time out.
            except error: break # Prevents a discontinued connection from
                                # breaking the script.

        self.__socket.close() # Close the socket.

        return data

    ''' Parse the IP address. Fails if no IP is provided. '''
    def parseIPArgument(self):
        try: return str(self.__args[1])
        except IndexError:
            exit("Please provide an IP address.\n" + CLIENT_EXAMPLE_USAGE)

    ''' Parse the port. Fails if no value is provided or the value is invalid. '''
    def parsePortArgument(self):
        try: port = int(self.__args[2])
        except ValueError: # Can't convert the value to an int.
            exit("Port must be an integer.\n" + CLIENT_EXAMPLE_USAGE)
        except IndexError: # No value was provided.
            exit("Port number must be provided.\n" + CLIENT_EXAMPLE_USAGE)

        if not 1024 <= port <= 60000: # Port is out of range.
            exit("Port must be between 1024 and 60000.\n" + CLIENT_EXAMPLE_USAGE)
        else: return port

    ''' Request the given filename from the server '''
    def requestFile(self, filename): return filename

    ''' Loop and allow socket to receive. '''
    def beginReceiving(self, bytes = 1024): return bytes

if __name__ == "__main__":
    client = Client(argv)
    data = client.requestDataWithSelectiveRepeat()

    print("Raw data: {}".format(data))
    print("Joined data: \"{}\"".format(' '.join(data)))

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
        self.__port = self.parsePortArgument()      # Parse our port.
        self.__address = ("", self.__port)          # Create a tuple from the
                                                    # values.
        self.__socket = None # Set up the socket variable.

    def beginListening(self):
        self.__socket = socket(AF_INET, SOCK_STREAM) # Initialize our socket.
        self.__socket.bind(self.__address) # Bind the socket to the address.
        self.__socket.listen(1) # Specify a window size of 1.

        print("Listening")

        while True:
            connectionSocket, _ = self.__socket.accept() # Begin listening

            sequenceNumber = 1 # A record of our current sequence number.
            i = 0 # The data index.
            data = ["I", "love", "to", "socket", "program."] # Our data to send.

            while True:
                ACK = connectionSocket.recv(1024).decode("utf-8") # Receive data.

                if i >= len(data): # The last piece of data has been sent.
                    # Create the closing message.
                    closing = CLOSING_MESSAGE + '^' + str(sequenceNumber)

                    connectionSocket.send(closing.encode("utf-8")) # Send closing.
                    connectionSocket.close() # Close the connection
                    break # Break our infinite loop.
                elif str(sequenceNumber) == ACK: # We can move on.
                    sequenceNumber ^= 1 # Invert our sequence number.

                    # Create the next packet.
                    packet = data[i] + '^' + str(sequenceNumber)
                    connectionSocket.send(packet.encode("utf-8")) # Send packet.

                    i += 1 # Increment the data index.
                else: # Resend the message.
                    # Create the next packet.
                    packet = data[i] + '^' + str(sequenceNumber)
                    connectionSocket.send(packet.encode("utf-8")) # Send packet.

            # We're finished.
            print("Sent \"{}\" to receiver.".format(' '.join(data)))


    ''' Parse the port. Fails if no value is provided or the value is invalid. '''
    def parsePortArgument(self):
        try: port = int(self.__args[1])
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

    server.beginListening()

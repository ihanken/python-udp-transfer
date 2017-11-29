import unittest
from context import client, server
from random import randint

class TestClient(unittest.TestCase):
    def setUp(self):
        randomPort = randint(1025, 59999)
        self.__client = client.Client(["client.py", "localhost", randomPort])
        self.__Server = server.Server(["server.py", randomPort])

    def tearDown(self):
        del self.__clientOne
        del self.__serverOne

    def testAlternatingBit(): pass

import unittest
from context import client

class TestClient(unittest.TestCase):
    def setUp(self):
        self.__clientOne = client.Client(["client.py", "192.168.1.1", 4000])

    def tearDown(self):
        del self.__clientOne

    def testNoArgs(self):
        with self.assertRaises(IndexError) and self.assertRaises(SystemExit):
            client.Client(["client.py"])

    def testNoPort(self):
        with self.assertRaises(IndexError) and self.assertRaises(SystemExit):
            client.Client(["client.py", "192.168.1.1"])

    def testOutOfRangePort(self):
        with self.assertRaises(SystemExit):
            client.Client(["client.py", "192.168.1.1", 1])

    def testStringForPort(self):
        with self.assertRaises(ValueError) and self.assertRaises(SystemExit):
            client.Client(["client.py", "192.168.1.1", "Test"])

    def testValidInitialization(self):
        client.Client(["client.py", "192.168.1.1", 4000])

    def testRequestFile(self):
        self.assertEqual(self.__clientOne.requestFile("testfile.txt"),
                                                        "testfile.txt")

    def testBeginReceiving(self):
        self.assertEqual(self.__clientOne.beginReceiving(), 1024)
        self.assertEqual(self.__clientOne.beginReceiving(1025), 1025)
        self.assertNotEqual(self.__clientOne.beginReceiving(1025), 1024)

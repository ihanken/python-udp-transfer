import unittest
from context import server

class TestServer(unittest.TestCase):
    def setUp(self):
        self.__serverOne = server.Server(["server.py", "192.168.1.1", 4000])

    def tearDown(self):
        del self.__serverOne

    def testNoArgs(self):
        with self.assertRaises(IndexError) and self.assertRaises(SystemExit):
            server.Server(["server.py"])

    def testNoPort(self):
        with self.assertRaises(IndexError) and self.assertRaises(SystemExit):
            server.Server(["server.py", "192.168.1.1"])

    def testOutOfRangePort(self):
        with self.assertRaises(SystemExit):
            server.Server(["server.py", "192.168.1.1", 1])

    def testStringForPort(self):
        with self.assertRaises(ValueError) and self.assertRaises(SystemExit):
            server.Server(["server.py", "192.168.1.1", "Test"])

    def testValidInitialization(self):
        server.Server(["server.py", "192.168.1.1", 4000])

    def testSendFile(self):
        self.assertEqual(self.__serverOne.sendFile("file.txt"), "file.txt")
        self.assertNotEqual(self.__serverOne.sendFile("file1.txt"), "file.txt")

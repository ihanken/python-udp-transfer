import unittest
from context import server

class TestServer(unittest.TestCase):
    def setUp(self):
        self._serverOne = server.Server("192.168.1.1", 1)
        self._serverTwo = server.Server("192.168.1.2", 2)
        self._serverThree = server.Server("192.168.1.3", 3)

    def tearDown(self):
        del self._serverOne
        del self._serverTwo
        del self._serverThree

    def testGetters(self):
        self.assertEqual(self._serverOne.ip, "192.168.1.1")
        self.assertEqual(self._serverTwo.ip, "192.168.1.2")
        self.assertEqual(self._serverThree.ip, "192.168.1.3")

        self.assertEqual(self._serverOne.port, 1)
        self.assertEqual(self._serverTwo.port, 2)
        self.assertEqual(self._serverThree.port, 3)

    def testSetters(self):
        self._serverOne.ip = self._serverTwo.ip
        self._serverThree.ip = self._serverOne.ip

        self._serverOne.port = self._serverThree.port
        self._serverTwo.port = self._serverOne.port

        self.assertEqual(self._serverOne.ip, self._serverThree.ip)
        self.assertEqual(self._serverThree.ip, self._serverTwo.ip)
        self.assertEqual(self._serverTwo.ip, self._serverOne.ip)

        self.assertEqual(self._serverOne.port, self._serverThree.port)
        self.assertEqual(self._serverThree.port, self._serverTwo.port)
        self.assertEqual(self._serverTwo.port, self._serverOne.port)

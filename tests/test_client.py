import unittest
from context import client

class TestClient(unittest.TestCase):
    def setUp(self):
        self._clientOne = client.Client("192.168.1.1", 1)
        self._clientTwo = client.Client("192.168.1.2", 2)
        self._clientThree = client.Client("192.168.1.3", 3)

    def tearDown(self):
        del self._clientOne
        del self._clientTwo
        del self._clientThree

    def testGetters(self):
        self.assertEqual(self._clientOne.ip, "192.168.1.1")
        self.assertEqual(self._clientTwo.ip, "192.168.1.2")
        self.assertEqual(self._clientThree.ip, "192.168.1.3")

        self.assertEqual(self._clientOne.port, 1)
        self.assertEqual(self._clientTwo.port, 2)
        self.assertEqual(self._clientThree.port, 3)

    def testSetters(self):
        self._clientOne.ip = self._clientTwo.ip
        self._clientThree.ip = self._clientOne.ip

        self._clientOne.port = self._clientThree.port
        self._clientTwo.port = self._clientOne.port

        self.assertEqual(self._clientOne.ip, self._clientThree.ip)
        self.assertEqual(self._clientThree.ip, self._clientTwo.ip)
        self.assertEqual(self._clientTwo.ip, self._clientOne.ip)

        self.assertEqual(self._clientOne.port, self._clientThree.port)
        self.assertEqual(self._clientThree.port, self._clientTwo.port)
        self.assertEqual(self._clientTwo.port, self._clientOne.port)

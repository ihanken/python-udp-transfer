import unittest
from context import client

class TestClient(unittest.TestCase):
    def setUp(self): pass

    def tearDown(self): pass

    def testHelloWorld(self):
        self.assertEqual(client.helloWorld(), "Hello, world!")

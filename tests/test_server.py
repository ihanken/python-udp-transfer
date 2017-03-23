import unittest
from context import server

class TestServer(unittest.TestCase):
    def setUp(self): pass

    def tearDown(self): pass

    def testHelloWorld(self):
        self.assertEqual(server.helloWorld(), "Hello, world!")

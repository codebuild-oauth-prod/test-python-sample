import unittest
from HelloWorld import HelloWorld

class MyTestCase(unittest.TestCase):
    def test_default_greeting_set(self):
        hw = HelloWorld()
        # this test will fail until you change the Greeter to return this expected message
        self.assertEqual(hw.message, 'Hello world!')


if __name__ == '__main__':
    unittest.main()
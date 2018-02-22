import unittest
from unittest.mock import Mock

# Mock libs used by SUT.
from mock_microbit import mocked_microbit

# The SUT.
import script

class TestScript(unittest.TestCase):
    def test_do(self):
        self.assertEqual(3, script.foo(1, 2))

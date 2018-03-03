#
# This is a module that mocks the original 'microbit' module. Use it for unit
# testing microbit apps on a development host (i. e. non-microbit) environment.
#
import unittest
from unittest.mock import Mock

Image = Mock()

display = Mock()

button_a = Mock()
button_a.was_pressed = Mock(return_value=False)

button_b = Mock()
button_b.was_pressed = Mock(return_value=False)

sleep = Mock()

accelerometer = Mock()
accelerometer.was_gesture = Mock(return_value=False)

pin1 = Mock()



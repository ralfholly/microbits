#
# This is a module that mocks the original 'microbit' module. Use it for unit
# testing microbit apps on a development host (i. e. non-microbit) environment.
#

from unittest.mock import Mock


# Global.
panic = Mock()
reset = Mock()
sleep = Mock()
running_time = Mock(return_value=0)
temperature = Mock(return_value=0)

# Buttons.
button_a = Mock()
button_a.is_pressed = Mock(return_value=False)
button_a.was_pressed = Mock(return_value=False)
button_a.get_presses = Mock(return_value=0)
button_b = Mock()
button_b.is_pressed = Mock(return_value=False)
button_b.was_pressed = Mock(return_value=False)
button_b.get_presses = Mock(return_value=0)

# I/O pins.
pin1 = Mock()
pin1.read_analog = Mock(return_value=0)
pin1.write_analog = Mock()
pin1.set_analog_period = Mock()
pin1.set_analog_period_microseconds = Mock()
pin1.is_touched = Mock(return_value=False)
pin2 = Mock()
pin2.read_analog = Mock(return_value=0)
pin2.write_analog = Mock()
pin2.set_analog_period = Mock()
pin2.set_analog_period_microseconds = Mock()
pin2.is_touched = Mock(return_value=False)
pin3 = Mock()
pin3.read_analog = Mock(return_value=0)
pin3.write_analog = Mock()
pin3.set_analog_period = Mock()
pin3.set_analog_period_microseconds = Mock()
pin3.is_touched = Mock(return_value=False)


Image = Mock()

display = Mock()



accelerometer = Mock()
accelerometer.was_gesture = Mock(return_value=False)




#
# This is a module that mocks the original 'microbit' module. Use it for unit
# testing microbit apps on a host (i. e. non-microbit) environment.
#

from unittest.mock import Mock
import sys
import types

# The original module that is to be mocked.
to_be_mocked_module = 'microbit'

mocked_microbit = types.ModuleType(to_be_mocked_module)
sys.modules[to_be_mocked_module] = mocked_microbit

mocked_microbit.Image = Mock(name=to_be_mocked_module + '.Image')
mocked_microbit.display = Mock(name=to_be_mocked_module + '.display')
mocked_microbit.button_a = Mock(name=to_be_mocked_module + '.button_a')
mocked_microbit.button_b = Mock(name=to_be_mocked_module + '.button_b')
mocked_microbit.sleep = Mock(name=to_be_mocked_module + '.sleep')
mocked_microbit.accelerometer = Mock(name=to_be_mocked_module + '.accelerometer')
mocked_microbit.pin1 = Mock(name=to_be_mocked_module + '.pin1')



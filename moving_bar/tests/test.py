import unittest
from unittest.mock import Mock

# Mock libs used by SUT.
import microbit as mbit

# The SUT.
import script

class TestScript(unittest.TestCase):
    state_params = None

    def setUp(self):
        self.state_params = {'row_str':"", 'delay':0, 'led_states_index':0}
        mbit.button_a.was_pressed.return_value = False
        mbit.button_b.was_pressed.return_value = False
        mbit.accelerometer.was_gesture.return_value = False
        mbit.Image = Mock()


    def tearDown(self):
        pass


    def test_trivial(self):
        self.assertEqual(3, 2 + 1)


    # pylint:disable=invalid-name
    def test_delay_stays_same_on_no_input(self):
        current_delay = 42
        self.state_params['delay'] = current_delay
        script.step(self.state_params)
        self.assertEqual(current_delay, self.state_params['delay'])
        script.step(self.state_params)
        self.assertEqual(current_delay, self.state_params['delay'])
        script.step(self.state_params)
        self.assertEqual(current_delay, self.state_params['delay'])


    # pylint:disable=invalid-name
    def test_delay_up_on_button_a_pressed(self):
        current_delay = 42
        self.state_params['delay'] = current_delay
        mbit.button_a.was_pressed.return_value = True
        script.step(self.state_params)
        self.assertEqual(current_delay + 10, self.state_params['delay'])


    # pylint:disable=invalid-name
    def test_delay_down_on_button_b_pressed(self):
        current_delay = 42
        self.state_params['delay'] = current_delay
        mbit.button_b.was_pressed.return_value = True
        script.step(self.state_params)
        self.assertEqual(current_delay - 10, self.state_params['delay'])

    # pylint:disable=invalid-name
    def test_states_index_updated_if_gesture_up(self):
        self.state_params['led_states_index'] = 0
        script.step(self.state_params)
        self.assertEqual(0, self.state_params['led_states_index'])
        mbit.accelerometer.was_gesture.side_effect = lambda value: True if value == 'up' else False
        script.step(self.state_params)
        self.assertEqual(1, self.state_params['led_states_index'])
        script.step(self.state_params)
        self.assertEqual(0, self.state_params['led_states_index'])

    # pylint:disable=invalid-name
    def test_display_updated_correctly(self):
        test_str = '12345'
        self.state_params['row_str'] = test_str

        # Ensures that all rows are identical
        def side_effect(matrix_str):
            row_strs = matrix_str.split(':')
            # Get rid of dummy element.
            row_strs.pop()
            self.assertEqual(5, len(row_strs))
            for row_str in row_strs:
                self.assertEqual(test_str, row_str)
            return None

        mbit.Image.side_effect = side_effect
        script.step(self.state_params)

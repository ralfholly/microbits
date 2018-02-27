import unittest
from unittest.mock import Mock

# Mock libs used by SUT.
import microbit as mbit

# The SUT.
import script

class TestScript(unittest.TestCase):
    state_params = None

    def setUp(self):
        mbit.button_a.was_pressed.return_value = False
        mbit.button_b.was_pressed.return_value = False
        mbit.Image = Mock()
        mbit.display.show = Mock()
        mbit.display.clear = Mock()


    def tearDown(self):
        pass


    def test_trivial(self):
        self.assertEqual(3, 2 + 1)


    # pylint:disable=invalid-name
    def test_no_button_press_no_image_displayed(self):
        for _ in range(0, 10):
            script.update(0)
        self.assertEqual(0, mbit.display.show.call_count)

    # pylint:disable=invalid-name
    def test_smiley_shown_if_button_a_pressed(self):
        script.update(0)
        self.assertEqual(0, mbit.display.show.call_count)
        mbit.button_a.was_pressed.return_value = True

        timer = script.update(0)
        mbit.display.show.assert_called_once_with(mbit.Image.HAPPY)
        self.assertEqual(script.TICKS_TO_DISPLAY, timer)

    # pylint:disable=invalid-name
    def test_smiley_shown_if_button_b_pressed(self):
        script.update(0)
        self.assertEqual(0, mbit.display.show.call_count)
        mbit.button_b.was_pressed.return_value = True

        timer = script.update(0)
        mbit.display.show.assert_called_once_with(mbit.Image.SAD)
        self.assertEqual(script.TICKS_TO_DISPLAY, timer)



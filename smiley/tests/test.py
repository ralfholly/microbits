import unittest
import importlib
from unittest.mock import Mock

# Mock libs used by SUT.
import microbit as mbit

# The SUT.
import script

class TestScript(unittest.TestCase):

    def setUp(self):
        global mbit
        mbit = importlib.reload(mbit)


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
        self.assertEqual(script.SHOW_SMILEY_TICKS, timer)

    def test_ticks_count_down(self):
        timer = script.SHOW_SMILEY_TICKS
        for i in range(1, script.SHOW_SMILEY_TICKS):
            timer = script.update(timer)
            self.assertEqual(0, mbit.display.show.call_count)
            self.assertEqual(0, mbit.display.clear.call_count)
            self.assertEqual(script.SHOW_SMILEY_TICKS - i, timer)

        # One more tick and display is cleared.
        timer = script.update(timer)
        self.assertEqual(0, timer)
        self.assertEqual(1, mbit.display.clear.call_count)

        # Some more ticks, but nothing happens.
        timer = script.update(timer)
        timer = script.update(timer)
        timer = script.update(timer)
        self.assertEqual(0, timer)
        self.assertEqual(0, mbit.display.show.call_count)

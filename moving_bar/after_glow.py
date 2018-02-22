from microbit import *

ROW_COUNT = 5
BASE_DELAY = 64

LED_STATES_GLOW = [
    "90000",
    "69000",
    "46900",
    "14690",
    "01469",
    "00009",
    "00096",
    "00964",
    "09641",
    "96410",
]

LED_STATES_NO_GLOW = [
    "90000",
    "09000",
    "00900",
    "00090",
    "00009",
    "00009",
    "00090",
    "00900",
    "09000",
    "90000",
]

LED_STATES = [LED_STATES_NO_GLOW, LED_STATES_GLOW]

i = 0
delay = BASE_DELAY
led_states_index = 0

while True:
    row_str = LED_STATES[led_states_index][i]
    matrix_str = (row_str + ':') * ROW_COUNT
    image = Image(matrix_str)
    display.show(image)

    if button_a.was_pressed():
        delay = min(1000, delay + 10)
    elif button_b.was_pressed():
        delay = max(10, delay - 10)
    sleep(delay)

    if accelerometer.was_gesture('up'):
        led_states_index = (led_states_index + 1) % len(LED_STATES)
        if LED_STATES[led_states_index] == LED_STATES_GLOW:
            pin1.write_digital(1)
        else:
            pin1.write_digital(0)

    i = (i + 1) % len(LED_STATES[led_states_index])

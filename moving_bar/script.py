import microbit as mbit

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


def main():
    state_params = {'delay':BASE_DELAY, 'led_states_index':0}
    i = 0

    while True:
        state_params['row_str'] = LED_STATES[state_params['led_states_index']][i]
        step(state_params)
        mbit.sleep(state_params['delay'])
        i = (i + 1) % len(LED_STATES[state_params['led_states_index']])


def step(state_params):
    update_display(state_params)
    process_input(state_params)


def update_display(state_params):
    matrix_str = (state_params['row_str'] + ':') * ROW_COUNT
    image = mbit.Image(matrix_str)
    mbit.display.show(image)


def process_input(state_params):
    if mbit.button_a.was_pressed():
        state_params['delay'] = min(1000, state_params['delay'] + 10)
    elif mbit.button_b.was_pressed():
        state_params['delay'] = max(10, state_params['delay'] - 10)
    if mbit.accelerometer.was_gesture('up'):
        state_params['led_states_index'] = (state_params['led_states_index'] + 1) % len(LED_STATES)


if __name__ == '__main__':
    main()


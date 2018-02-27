import microbit as mbit

TICKS_TO_DISPLAY = 10

def update(timer):
    if mbit.button_a.was_pressed():
        mbit.display.show(mbit.Image.HAPPY)
        timer = TICKS_TO_DISPLAY
    elif mbit.button_b.was_pressed():
        mbit.display.show(mbit.Image.SAD)
        timer = TICKS_TO_DISPLAY
    else:
        if timer > 0:
            timer -= 1
        else:
            mbit.display.clear()

    return timer


def main():
    display_timer = 0

    while True:
        display_timer = update(display_timer)
        mbit.sleep(100)


if __name__ == '__main__':
    main()


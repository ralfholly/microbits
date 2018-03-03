import microbit as mbit

MS_PER_TICK = 100
SHOW_SMILEY_MS = 3000
SHOW_SMILEY_TICKS = SHOW_SMILEY_MS // MS_PER_TICK

def update(timer):
    if mbit.button_a.was_pressed():
        mbit.display.show(mbit.Image.HAPPY)
        timer = SHOW_SMILEY_TICKS
    else:
        if timer > 0:
            timer -= 1
            if timer == 0:
                mbit.display.clear()

    return timer


def main():
    display_timer = 0

    while True:
        display_timer = update(display_timer)
        mbit.sleep(MS_PER_TICK)


if __name__ == '__main__':
    main()


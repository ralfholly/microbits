# Add your Python code here. E.g.
from microbit import *

COLUMN_COUNT = 5
BASE_STR = "014696410"
#BASE_STR = "124696421"
#BASE_STR = "000090000"

def move(ofs):
    m = len(BASE_STR) // 2
    if 0 <= ofs <= m:
        i = m - ofs
        return BASE_STR[i:i + m + 1] + ":"
    return BASE_STR

x = 0
delta_x = 1
while True:
    row_str = move(x)
    matrix_str = row_str * COLUMN_COUNT
    image = Image(matrix_str)
    display.show(image)
    sleep(80)
    x += delta_x
    if x == COLUMN_COUNT:
        # Stay at rightmost column.
        x = COLUMN_COUNT - 1
        # Go left.
        delta_x = -1
    elif x == -1:
        # Stay at leftmost column.
        x = 0
        # Go right.
        delta_x = 1

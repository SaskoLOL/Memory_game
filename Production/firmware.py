from machine import Pin, SPI
from ili9341 import Display, color565
import time
import random

# TFT Setup
spi = SPI(0, baudrate=32000000, sck=Pin(6), mosi=Pin(7))
display = Display(spi, dc=Pin(3), cs=Pin(5), rst=Pin(4), rotation=0)

# Matrix Pins
row_pins = [Pin(i, Pin.OUT) for i in [10, 11, 12, 13]]
col_pins = [Pin(i, Pin.IN, Pin.PULL_UP) for i in [14, 15, 16, 17]]

# Game settings
grid_size = 4
cell_size = 60
pattern = [0] * 16
user_input = [0] * 16

def draw_grid(highlight=None, user=False):
    display.clear()
    for i in range(16):
        row = i // 4
        col = i % 4
        x = col * cell_size
        y = row * cell_size
        color = color565(255, 255, 255)  # Default: white border
        fill = color565(0, 0, 0)         # Default: black background

        if highlight and highlight[i]:
            fill = color565(255, 255, 0)  # Yellow for pattern
        elif user and user[i]:
            fill = color565(0, 0, 255)    # Blue for input

        display.fill_rectangle(x+1, y+1, cell_size-2, cell_size-2, fill)
        display.draw_rectangle(x, y, cell_size, cell_size, color)

def generate_pattern():
    global pattern
    pattern = [random.choice([0, 1]) for _ in range(16)]

def scan_keys():
    input_state = [0] * 16
    for r_idx, r_pin in enumerate(row_pins):
        r_pin.value(0)
        for c_idx, c_pin in enumerate(col_pins):
            if not c_pin.value():  # button pressed
                input_state[r_idx * 4 + c_idx] = 1
        r_pin.value(1)
    return input_state

def get_user_input(timeout=10):
    global user_input
    user_input = [0] * 16
    start = time.time()
    while time.time() - start < timeout:
        current = scan_keys()
        for i in range(16):
            if current[i] and not user_input[i]:
                user_input[i] = 1
                draw_grid(user=user_input)
        time.sleep(0.1)

def check_input():
    return pattern == user_input

def show_message(msg, color):
    display.clear()
    display.draw_text(40, 100, msg, color565(*color), size=3)
    time.sleep(2)

def play_game():
    while True:
        generate_pattern()
        draw_grid(highlight=pattern)
        time.sleep(2)
        draw_grid()  # clear
        get_user_input()
        if check_input():
            show_message("Correct!", (0, 255, 0))
        else:
            show_message("Wrong!", (255, 0, 0))

# Initialize
for pin in row_pins:
    pin.value(1)  # Set rows HIGH initially

play_game()

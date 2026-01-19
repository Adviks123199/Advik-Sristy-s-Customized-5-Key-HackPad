import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.extensions.rgb import RGB

keyboard = KMKKeyboard()

# 1. Key Setup
keyboard.col_pins = (board.D5, board.D6, board.D0, board.D8, board.D7)
keyboard.row_pins = ()
keyboard.diode_orientation = DiodeOrientation.COL2ROW

# 2. LED Setup (Pin D9)
rgb = RGB(pixel_pin=board.D9, num_pixels=1, val_default=100, hue_default=0, sat_default=255)
keyboard.extensions.append(rgb)

# 3. Custom Keymap
# Key 1: Copy (Ctrl + C)
# Key 2: Paste (Ctrl + V)
# Key 3: Undo (Ctrl + Z)
# Key 4: Redo (Ctrl + Y)
# Key 5: Reopen Closed Tab (Ctrl + Shift + T)
keyboard.keymap = [
    [
        KC.LCTL(KC.C),      # First Key (Copy)
        KC.LCTL(KC.V),      # Second Key (Paste)
        KC.LCTL(KC.Z),      # Third Key (Undo)
        KC.LCTL(KC.Y),      # Fourth Key (Redo)
        KC.LCTL(KC.LSFT(KC.T)) # Fifth Key (Reopen Tab)
    ]
]

if __name__ == '__main__':
    keyboard.go()

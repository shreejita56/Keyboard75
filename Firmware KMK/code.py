import board
import random
import neopixel

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation

keyboard = KMKKeyboard()


# Rows
keyboard.row_pins = (
    board.GP5,     # R1
    board.GP7,     # R2
    board.GP18,    # R3
    board.GP17,    # R4
    board.GP16,    # R5
    board.GP15,    # R6
)

# Columns
keyboard.col_pins = (
    board.GP19,    # C1
    board.GP20,    # C2
    board.GP21,    # C3
    board.GP22,    # C4
    board.GP23,    # C5
    board.GP24,    # C6
    board.GP25,    # C7
    board.GP4,     # C8 
    board.GP26,    # C9
    board.GP27,    # C10
    board.GP28,    # C11
    board.GP29,    # C12
    board.GP3,     # C13
    board.GP6,     # C14
)

keyboard.diode_orientation = DiodeOrientation.COL2ROW


LED_COUNT = 82
RGB_DATA_PIN = board.GP0
RGB_BRIGHTNESS = 0.18

pixels = neopixel.NeoPixel(
    RGB_DATA_PIN,
    LED_COUNT,
    brightness=RGB_BRIGHTNESS,
    auto_write=False,
    pixel_order=neopixel.GRB,
)
pixels.fill((0, 0, 0))
pixels.show()


def random_colour():
    # Avoid extremely dark colours so the pressed key is clearly visible.
    return (
        random.randint(45, 255),
        random.randint(45, 255),
        random.randint(45, 255),
    )


class PerKeyRGB:
    """Give the LED corresponding to a pressed matrix position a random colour."""

    def during_bootup(self, keyboard):
        pass

    def before_matrix_scan(self, keyboard):
        pass

    def after_matrix_scan(self, keyboard):
        pass

    def process_key(self, keyboard, key, is_pressed, int_coord):
        if is_pressed:
            # KMK matrix coordinates are row-major flattened coordinates.
            # This assumes LED1 follows the first key, LED2 the second, etc.
            led_index = int_coord
            if 0 <= led_index < LED_COUNT:
                pixels[led_index] = random_colour()
                pixels.show()
        return key

    def on_powersave_enable(self, keyboard):
        pass

    def on_powersave_disable(self, keyboard):
        pass

    def on_step(self, keyboard):
        pass


keyboard.extensions.append(PerKeyRGB())


keyboard.keymap = [
    # R1
    [KC.ESC, KC.N1, KC.N2, KC.N3, KC.N4, KC.N5, KC.N6,
     KC.N7, KC.N8, KC.N9, KC.N0, KC.MINS, KC.EQL, KC.BSPC],

    # R2
    [KC.TAB, KC.Q, KC.W, KC.E, KC.R, KC.T, KC.Y,
     KC.U, KC.I, KC.O, KC.P, KC.LBRC, KC.RBRC, KC.BSLS],

    # R3
    [KC.CAPS, KC.A, KC.S, KC.D, KC.F, KC.G, KC.H,
     KC.J, KC.K, KC.L, KC.SCLN, KC.QUOT, KC.ENT, KC.NO],

    # R4
    [KC.LSFT, KC.Z, KC.X, KC.C, KC.V, KC.B, KC.N,
     KC.M, KC.COMM, KC.DOT, KC.SLSH, KC.RSFT, KC.UP, KC.NO],

    # R5
    [KC.LCTL, KC.LGUI, KC.LALT, KC.SPC, KC.SPC, KC.SPC,
     KC.SPC, KC.SPC, KC.SPC, KC.RALT, KC.RGUI, KC.RCTL,
     KC.LEFT, KC.DOWN],

    # R6
    [KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO,
     KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.RIGHT, KC.NO],
]


if __name__ == "__main__":
    keyboard.go()

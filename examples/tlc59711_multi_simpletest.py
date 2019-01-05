"""TLC5971 / TLC59711 Multi."""

__doc__ = """
tlc59711_multi.py - TLC59711TLC59711Multi minimal example.

Enjoy the colors :-)
"""

import time

import board
import busio

# from adafruit_tlc59711.adafruit_tlc59711 import TLC59711
from adafruit_tlc59711.adafruit_tlc59711_multi import TLC59711Multi


##########################################
pixel_count = 4

spi = busio.SPI(board.SCK, MOSI=board.MOSI)
pixels = TLC59711Multi(spi, pixel_count=pixel_count)


##########################################
# test function

offset = 0
value_high = 65535


def channelcheck_update():
    """ChannelCheck."""
    global offset  #noqa
    print("offset", offset)

    # pixels[offset] = (value_high, 0, 0)
    pixels[offset] = (0xAAAA, 0xBBBB, 0xCCCC)
    pixels.show()

    offset += 1
    if offset >= pixel_count:
        offset = 0
        set_all_black()
        time.sleep(5)
        print()


def set_all_black():
    """Set all Pixel to Black."""
    set_all((0, 0, 0))


def set_all(color):
    """Set all Pixel to color."""
    for i in range(pixel_count):
        # pixels[i // 4][i % 4] = color
        pixels[i] = color


def test_main():
    """Test Main."""
    print()
    print(42 * '*')
    print(__doc__)
    print(42 * '*')
    print()
    time.sleep(0.5)
    print(42 * '*')

    while True:
        # channelcheck_update()
        time.sleep(1)


##########################################
# main loop

if __name__ == '__main__':

    test_main()

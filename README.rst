About this modification
=======================

Modified CircuitPython module for the TLC59711 16-bit 12 channel LED PWM driver.

This modification is mainly around the indexing of LEDs and channels.
The `TLC59711 CircuitPython module <https://github.com/adafruit/Adafruit_CircuitPython_TLC59711>`_ has functions such as
``set_pixel(pixel_index, value)`` and ``set_channel(channel_index, value)``.
However, ``set_pixel(0, value)`` turns on LED3, not LED0.
Likely, ``set_channel(0, value)`` turns on the pin marked as B3 (blue for LED3), not R0 (red for LED0).

It's not a bug of CircuitPython. It's all attributed to the hard-coded programming of TLC59711 itself (Cf. Figure 24 of `TLC59711 Datasheet <https://cdn-shop.adafruit.com/datasheets/tlc59711.pdf>`_).
This modification changes the behavior of ``pixel_index`` and ``channel_index`` so that indexing works in the natural order as expected and printed on the breakout board.
It also changes the buffer channel order, where the default is (blue, green, red) to (red, hreen, blue).
(**To do:** we also need to swap the blightness control (BC) register order.)

``natural_order()`` switches between the natural order mode and the default behavior.


It also has 'inverse' mode of PWM output equivalent to ``value_inv = 65535 - value``. See ``invert_output()`` in adafruit_tlc59711.py.

All files except adafruit_tlc59711.py (the module) and README.rst (this file) were not modified.

Installing this modification
===========================

To install for current user:

.. code-block:: shell

    pip3 install git+https://github.com/kchinzei/Natural-Ordered_Adafruit_CircuitPython_TLC59711.git

**Warning:** doing this will overwrite existing adafruit-circuitpython-tlc59711.


*No modification in this file hereafter.*

Introduction
============

.. image:: https://readthedocs.org/projects/adafruit-circuitpython-tlc59711/badge/?version=latest
    :target: https://docs.circuitpython.org/projects/tlc59711/en/latest/
    :alt: Documentation Status

.. image:: https://raw.githubusercontent.com/adafruit/Adafruit_CircuitPython_Bundle/main/badges/adafruit_discord.svg
    :target: https://adafru.it/discord
    :alt: Discord

.. image:: https://github.com/adafruit/Adafruit_CircuitPython_TLC59711/workflows/Build%20CI/badge.svg
    :target: https://github.com/adafruit/Adafruit_CircuitPython_TLC59711/actions/
    :alt: Build Status

CircuitPython module for the TLC59711 16-bit 12 channel LED PWM driver.

Dependencies
=============
This driver depends on:

* `Adafruit CircuitPython <https://github.com/adafruit/circuitpython>`_

Please ensure all dependencies are available on the CircuitPython filesystem.
This is easily achieved by downloading
`the Adafruit library and driver bundle <https://github.com/adafruit/Adafruit_CircuitPython_Bundle>`_.

Installing from PyPI
====================

On supported GNU/Linux systems like the Raspberry Pi, you can install the driver locally `from
PyPI <https://pypi.org/project/adafruit-circuitpython-tlc59711/>`_. To install for current user:

.. code-block:: shell

    pip3 install adafruit-circuitpython-tlc59711

To install system-wide (this may be required in some cases):

.. code-block:: shell

    sudo pip3 install adafruit-circuitpython-tlc59711

To install in a virtual environment in your current project:

.. code-block:: shell

    mkdir project-name && cd project-name
    python3 -m venv .env
    source .env/bin/activate
    pip3 install adafruit-circuitpython-tlc59711

Usage Example
=============

See examples/tlc59711_simpletest.py for a demo of the usage.

Documentation
=============

API documentation for this library can be found on `Read the Docs <https://docs.circuitpython.org/projects/tlc59711/en/latest/>`_.

For information on building library documentation, please check out `this guide <https://learn.adafruit.com/creating-and-sharing-a-circuitpython-library/sharing-our-docs-on-readthedocs#sphinx-5-1>`_.

Contributing
============

Contributions are welcome! Please read our `Code of Conduct
<https://github.com/adafruit/Adafruit_CircuitPython_TLC59711/blob/main/CODE_OF_CONDUCT.md>`_
before contributing to help this project stay welcoming.

# ESP32 Optical Transmitter

This Arduino sketch implements the transmitter side of the optical
communication system.

The ESP32 accepts a text message through the Serial Monitor, converts
each character into 8-bit binary, groups the bits into 2-bit symbols,
and represents each symbol using an RGB LED.

## Color Mapping

- 00 → Red
- 01 → Green
- 10 → Blue
- 11 → Red + Green (Yellow)

## Hardware

- ESP32
- RGB LED
- 3 current-limiting resistors

## Status

The code has been tested in an online simulation environment.
Physical ESP32 hardware testing will be performed when the required
hardware is available.

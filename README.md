# optical_channel_communication_project
An optical covert channel communication research platform using RGB LED signaling, color sensing, ESP32, Flask, and SQLite.

# Optical Channel Communication Research Platform

An experimental optical communication system that demonstrates how digital information can be transmitted using visible light and detected using a color sensor.

The project combines **embedded systems, optical signaling, color-based data encoding, ESP32, Flask, SQLite, and a web dashboard** to study the reliability of communication through an optical channel.

## 📌 Project Overview

Traditional communication systems usually transmit information through wired connections, Wi-Fi, Bluetooth, or other radio-based technologies.

This project explores a different physical communication medium: **visible light**.

In the proposed system, an RGB LED is used as the optical transmitter. Information is converted into predefined color signals, and these colors are transmitted through light.

At the receiver side, a **TCS34725 color sensor** detects the incoming light. An ESP32 processes the detected RGB values and identifies the corresponding transmitted color.

The received information can then be forwarded to a backend application, where communication results are stored in an SQLite database and displayed through a Flask-based monitoring dashboard.

The project is intended as a research and educational platform for studying **optical communication and optical covert-channel concepts** in a controlled environment.

# 🎯 Objectives
The main objectives of this project are:

- Demonstrate communication using visible light.
- Use an RGB LED as an optical transmitter.
- Encode digital information into predefined color signals.
- Detect transmitted colors using a TCS34725 color sensor.
- Use ESP32 for transmitter and receiver-side processing.
- Process and record communication results.
- Store test results using SQLite.
- Display communication information using a Flask web dashboard.
- Study communication reliability under different lighting conditions.
- Provide a foundation for future optical-channel and covert-channel research.

# 💡 What is Optical Channel Communication?
Optical channel communication means transferring information using **light as the communication medium**.
In this project:
```text
Digital Data
     ↓
Color Encoding
     ↓
RGB LED
     ↓
Visible Light
     ↓
TCS34725 Color Sensor
     ↓
ESP32
     ↓
Received Data

# Barcode Scanner using Python

This is a simple Python program that uses OpenCV and pyzbar to scan a barcode from a webcam feed and return the barcode number as the output. Once a barcode is detected, the program stops and displays the barcode data.

## Features
- Real-time barcode scanning using the camera.
- Automatically exits the program once a barcode is detected.
- Supports standard barcode formats (EAN-13, UPC, etc.) and QR codes.

## Prerequisites

Before running this program, ensure you have the following installed:

- Python 3.x
- OpenCV for image capture and processing
- pyzbar for decoding the barcode

## Installation

1. Clone or download the repository.
2. Install the required Python libraries using pip:

    ```bash
    pip install opencv-python pyzbar
    ```

## How to Run

1. Connect a webcam or ensure your system has a built-in camera.
2. Run the Python script:

    ```bash
    python barcode_scanner.py
    ```

3. Once the barcode is detected, the program will display the barcode number and exit automatically.

## How it Works

- The program captures video feed using OpenCV.
- It uses pyzbar to scan each frame for barcodes.
- When a barcode is found, it extracts the barcode number, displays it, and exits the program.

## Usage

- Press `q` at any time to manually exit the program.
- The program will automatically terminate once a valid barcode is scanned.

## Example Output


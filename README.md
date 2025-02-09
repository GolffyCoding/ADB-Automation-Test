# ADB Automation Test Suite

## Overview
This project provides a set of automated tests using Python's `unittest` framework to perform various ADB (Android Debug Bridge) operations on an Android device.

## Features
- **Device Connection Test**: Ensures the device is properly connected.
- **App Installation Test**: Installs and uninstalls an APK.
- **App Launch Test**: Verifies the app starts successfully.
- **UI Interaction Test**: Simulates basic UI interactions like taps, text input, and swipes.
- **File Operations Test**: Pushes, pulls, and deletes files on the device.
- **Device Information Test**: Retrieves device model, OS version, and screen resolution.
- **Logcat Test**: Captures logs from the device.
- **Network Test**: Enables and disables Wi-Fi.
- **Screenshot Test**: Captures a screenshot from the device.
- **Battery Test**: Retrieves battery information.
- **Memory Info Test**: Retrieves memory usage details.

## Prerequisites
- Python 3.x
- `adb` (Android Debug Bridge) installed and accessible via command line.
- `pure-python-adb` installed:  
  ```bash
  pip install pure-python-adb
  ```
- An Android device connected via USB or Wi-Fi with USB debugging enabled.

## Setup
1. Ensure ADB is running:
   ```bash
   adb start-server
   ```
2. Connect your Android device:
   ```bash
   adb devices
   ```
3. Run the test suite:
   ```bash
   python test_adb_operations.py
   ```

## Test Structure
The tests are organized in `TestADBOperations` class:
- `setUpClass()`: Initializes ADB connection.
- `setUp()`: Prepares the device before each test.
- Various test methods for different ADB functionalities.
- `tearDown()`: Cleans app data after each test.
- `tearDownClass()`: Cleans up the ADB connection.

## Notes
- Ensure that `adb` is properly installed and accessible.
- Replace `com.example.app` with your actual package name.
- Modify the APK path (`test.apk`) accordingly.

## License
This project is open-source and available under the MIT License.


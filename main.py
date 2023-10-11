import serial

# Configure the serial port to match the Arduino's baud rate
ser = serial.Serial('/dev/ttyACM0', 9600)  # Update the port name if necessary

try:
    while True:
        sensor_data = ""
        for _ in range(7):
            data = ser.readline().decode('utf-8').strip()
            if data:
                sensor_data += data + " - "

        if sensor_data:
            print("Received values:", sensor_data[:-3])  # Remove the trailing " - " and print
except KeyboardInterrupt:
    pass
finally:
    ser.close()

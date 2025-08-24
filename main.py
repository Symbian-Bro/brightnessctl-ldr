import serial
import time
import subprocess

def serial_read(port='/dev/ttyUSB0', baudrate=9600, timeout=5):
    with serial.Serial(port, baudrate, timeout=timeout) as ser:
            line = int(ser.readline().decode('utf-8').strip())
            return line

def main():
    time.sleep(5)
    while True:
        ldrvalue = int(serial_read())
        percent = (ldrvalue / 1023) * 100
        subprocess.run(['brightnessctl', 's', str(percent)])
        time.sleep(7)

if __name__ == "__main__":
    main()
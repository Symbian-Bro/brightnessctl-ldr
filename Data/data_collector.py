import csv
import serial
import time
import subprocess

def main():
    time.sleep(3)
    filename = '/home/symbian/data/data.csv'
    ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
    while True:
        temp = (ser.readline().decode('utf-8').strip())
        if temp:
            try:
                ldrvalue = 1023 - int(temp)
            except ValueError:
                continue
        else:
            continue

        brightness_value = subprocess.run(['brightnessctl', 'g'],capture_output=True)
        current = int(brightness_value.stdout.strip())

        with open(filename, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([ldrvalue, current])
        time.sleep(10)

if __name__ == "__main__":
    main()

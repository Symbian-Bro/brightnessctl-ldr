import serial
import time
import subprocess
import serial.tools.list_ports as listings

def port_checker():
    ports = listings.comports()
    for port in ports:
        if (('Arduino' in port.description or 'CH340' in port.description)or 
            ('Arduino' in port.hwid or 'CH340' in port.hwid)
        ):
            return port.device
    return '/dev/ttyUSB0'

def serial_read(port, baudrate, timeout=5):
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
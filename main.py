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

def serial_read(port, baudrate):
    with serial.Serial(port, baudrate, timeout=5) as ser:
            line = int(ser.readline().decode('utf-8').strip())
            return line

def main():
    time.sleep(5)
    port = port_checker()
    baudrate = 9600
    while True:
        ldrvalue = 1023 - (serial_read(port, baudrate))
        percent = (ldrvalue / 1023) * 100
        temp = subprocess.run(['brightnessctl', 'g'],capture_output=True)
        current = int(temp.stdout.strip())
        if(current < percent):
            while(current <= percent):
                current = current + 2
                subprocess.run(['brightnessctl', 's', str(current)])
                time.sleep(0.4)
        elif(current > percent):
            while(current >= percent):
                current = current - 2
                subprocess.run(['brightnessctl', 's', str(current)])
                time.sleep(0.4)
        else:
            pass

if __name__ == "__main__":
    main()
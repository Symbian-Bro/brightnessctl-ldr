import serial.tools.list_ports as listings

def port_checker():
    ports = listings.comports()
    for port in ports:
        if (('Arduino' in port.description or 'CH340' in port.description)or 
            ('Arduino' in port.hwid or 'CH340' in port.hwid)
        ):
            print(port.device)
            return port.device
    print("The regular")
    return '/dev/ttyUSB0'

port_checker()
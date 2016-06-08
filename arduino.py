from serial import Serial
from serial.tools.list_ports import grep


serial = None


def get_serial_port():
    ports = grep(r'ACM\d')

    try:
        port = next(ports).device
    except StopIteration:
        port = None

    return port


def setup_serial():
    global serial
    port = get_serial_port()

    if port:
        serial = Serial(get_serial_port(), 9600, timeout=5, rtscts=True)
        return True

    return False


def write(unicode):
    if serial:
        return serial.write(unicode.encode('utf-8'))

    return None


setup_serial()

from serial import Serial
from setial.tools.list_ports import grep


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


setup_serial()

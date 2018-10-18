import re


class NotConnected(RuntimeError):
    pass


def parse_wireless_strength(data):
    try:
        while True:
            line = next(data)
            if ':' not in line:
                # Only interface lines matter
                continue

            elements = [x for x in re.split(r'\s+', line) if x != '']
            strength = float(elements[2])
            return strength

    except StopIteration as e:
        raise NotConnected() from e


def wireless_strength():
    with open('/proc/net/wireless') as data:
        return parse_wireless_strength(data)

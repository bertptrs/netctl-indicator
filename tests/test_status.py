import io
import pytest
from netctl_indicator import status


def test_parse_wireless_strength():
    data = '''Inter-| sta-|   Quality        |   Discarded packets               | Missed | WE
               face | tus | link level noise |  nwid  crypt   frag  retry   misc | beacon | 22
              wlp2s0: 0000   30.  -80.  -256        0      0      0      0    561        0'''

    data = io.StringIO(data)
    assert status.parse_wireless_strength(data) == 30


def test_parse_wireless_strength_unconnected():
    data = '''Inter-| sta-|   Quality        |   Discarded packets               | Missed | WE
               face | tus | link level noise |  nwid  crypt   frag  retry   misc | beacon | 22'''
    data = io.StringIO(data)
    with pytest.raises(status.NotConnected):
        status.parse_wireless_strength(data)

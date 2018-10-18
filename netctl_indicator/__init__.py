import argparse
import sys
import status


class App:

    def __init__(self, args=sys.argv[1:]):
        self.load_params(args)

    def run(self):
        try:
            print('Wireless strength:', status.wireless_strength())
        except status.NotConnected:
            print('Not connected')

    def _load_params(self, args):
        parser = argparse.ArgumentParser()
        parser.add_argument('-c', '--command', default='netctl-auto',
                            help='netctl command to use')

        return parser.parse_args(args)

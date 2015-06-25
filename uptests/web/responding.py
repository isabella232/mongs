#!/usr/bin/env python

import argparse
import portend
import requests

parser = argparse.ArgumentParser()
parser.add_argument('host')
parser.add_argument('port', type=int)
args = parser.parse_args()

portend.occupied(args.host, args.port, timeout=5)

root = 'http://{host}:{port}/'.format(**vars(args))
requests.get(root).raise_for_status()

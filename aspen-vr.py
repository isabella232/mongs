"""
Load YAML config and save it as Aspen config before launching.
"""

import os

import yaml
from aspen import serve, website


def convert_config():
	with open(os.environ['APP_SETTINGS_YAML']) as f:
		in_config = yaml.load(f)
	servers = in_config.get('servers', [])
	if servers:
		with open('servers.txt', 'w') as f:
			lines = (server + '\n' for server in servers)
			f.writelines(lines)

if __name__ == '__main__':
	convert_config()
	serve(website.Website())

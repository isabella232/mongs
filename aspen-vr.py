"""
Load YAML config and save it as Aspen config before launching.
"""

import os
import yaml

import aspen.server

def translate(value):
	"""
	Take a YAML value and make it a suitable string for ConfigParser.
	"""
	if isinstance(value, (list, tuple)):
		return '\n    '.join(value)
	if isinstance(value, dict):
		raise ValueError("Can't translate a dict to ConfigParser format")
	return value

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
	aspen.server.main()

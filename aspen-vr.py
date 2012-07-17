"""
Load YAML config and save it as Aspen config before launching.
"""

import os
import yaml
import ConfigParser

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
	out_config = ConfigParser.RawConfigParser()
	for section in in_config:
		out_config.add_section(section)
		for field in in_config[section]:
			value = in_config[section][field]
			value = translate(value)
			out_config.set(section, field, value)
	os.path.isdir('www/.aspen') or os.makedirs('www/.aspen')
	with open('www/.aspen/aspen.conf', 'wb') as f:
		out_config.write(f)

if __name__ == '__main__':
	convert_config()
	__file__ = os.path.join(os.path.dirname(__file__), 'env', 'bin', 'aspen')
	execfile('env/bin/aspen')

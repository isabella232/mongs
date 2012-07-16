"""
Load YAML config and save it as Aspen config before launching.
"""

import os
import yaml
import ConfigParser

def convert_config():
	with open(os.environ['APP_SETTINGS_YAML']) as f:
		in_config = yaml.load(f)
	out_config = ConfigParser.RawConfigParser()
	for section in in_config:
		out_config.add_section(section)
		for field in in_config[section]:
			value = in_config[section][field]
			out_config.set(section, field, value)
	os.path.isdir('.aspen') or os.makedirs('.aspen')
	with open('.aspen/aspen.conf', 'wb') as f:
		out_config.write(f)

if __name__ == '__main__':
	convert_config()
	execfile('env/bin/aspen')

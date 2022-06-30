import sys
import configparser
import json 

with open('sample_config_input.json', 'r') as config_input_file:
    config_data = config_input_file.read()

config_input = json.loads(config_data)

config = configparser.ConfigParser()

config['project'] = {"cpu": 5,
        "projname": "taylor_nanopore_barcode2_run",
        "projid": 8,
        "projcode": sys.argv[1],
        "projowner": "twiley1@nd.edu",
        "projrunhost": "http://localhost"}

for key in config_input:
    config[key] = config_input[key]

with open(f'{sys.argv[1]}/config.txt', 'w') as configfile:
    config.write(configfile)

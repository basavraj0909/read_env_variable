import yaml

with open('config.yaml','r') as file:
    config = yaml.safe_load(file)


# acccessing the data
print(config['database']['host'])  # Output: localhost
print(config['logging']['level'])  # Output: DEBUG

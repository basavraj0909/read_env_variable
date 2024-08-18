import yaml


# Define a Python dictionary
config_data = {
    'database': {
        'host': 'localhost',
        'port': 3306,
        'user': 'root',
        'password': 'root',
        'name': 'emp_db',
    },
    'logging': {
        'level': 'DEBUG',
        'file': 'employee_management.log',
    }
}

# Write the dictionary to a YAML file
with open('output_config.yaml', 'w') as file:
    yaml.dump(config_data, file, default_flow_style=False)
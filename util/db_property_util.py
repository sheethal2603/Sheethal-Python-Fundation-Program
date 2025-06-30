import configparser

def get_property_string(file_name):
    config = configparser.ConfigParser()
    config.read(file_name)

    host = config['DATABASE']['host']
    database = config['DATABASE']['dbname']
    user = config['DATABASE']['username']
    password = config['DATABASE']['password']
    port = config['DATABASE']['port']

    return {
        'host': host,
        'database': database,
        'user': user,
        'password': password,
        'port': int(port)
    }

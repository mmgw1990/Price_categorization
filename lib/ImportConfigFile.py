import yaml



class ImportConfigFile(object):

    def __init__(self, path_to_config_file):
        self.config_path = path_to_config_file

    def import_config_file(self):
        with open(self.config_path, 'r') as my_config_yaml:
            cfg = yaml.safe_load(my_config_yaml)
        return cfg

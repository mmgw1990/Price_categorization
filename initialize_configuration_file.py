from lib import ImportConfigFile
import os

cfg = ImportConfigFile.ImportConfigFile(os.getenv("config_path","configuration_file.yml")).import_config_file()
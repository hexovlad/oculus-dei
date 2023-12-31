import yaml


class ConfigReader:
    """Class made for reading the information from the y*ml config file"""

    def __init__(self, config_path: str):
        """Constructor"""
        self._config_path = config_path
        self._config_reader = self._config_file_reader(self._config_path)

    @staticmethod
    def _config_file_reader(config_path: str):
        """Returns the object for interacting with the config file"""
        yaml_data = None
        try:
            with open(config_path, "r") as file:
                try:
                    yaml_data = yaml.safe_load(file)
                except yaml.YAMLError as e:
                    print(f"Error parsing YAML file: {e}")
                    exit(1)

        except FileNotFoundError:
            print(f"YAML file not found: {config_path}")
        except Exception as e:
            print(f"An error occurred: {e}")

        return yaml_data

    def _search_yaml(self, yaml_data, field) -> int or str or list or None:
        """Returning the data found on a given field in the config file"""

        if isinstance(yaml_data, dict):
            for key, value in yaml_data.items():
                if key == field:
                    return value
                elif isinstance(value, (dict, list)):
                    result = self._search_yaml(value, field)
                    if result is not None:
                        return result
        elif isinstance(yaml_data, list):
            for item in yaml_data:
                result = self._search_yaml(item, field)
                if result is not None:
                    return result

        return None  # Restringing None in case there is no value found

    def find_value(self, field: str) -> int or str or list or None:
        """Returning the data found on a given field in the config file"""
        return self._search_yaml(self._config_reader, field)

import unittest
import collector_modules


class MyTestCase(unittest.TestCase):
    def setUp(self):
        """Setting up the environment"""
        self.config_reader = collector_modules.ConfigReader(
            "config_file.yml"
        )  # Reading the local config file and settting everything up for being used in the tests

    def test_read_mongo_username(self):
        """Testing reading mongo username"""

    def test_read_mongo_password(self):
        """Testing reading the mongo password"""

    def test_read_mongo_auth_db(self):
        """Testing in reading the mongo auth database"""

    def test_read_mongo_express_username(self):
        """Testing reading the mongodb express username"""

    def test_read_mongo_express_password(self):
        """Testing reading the mongodb express password"""


if __name__ == "__main__":
    unittest.main()

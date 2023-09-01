import unittest
import collector_modules


class MyTestCase(unittest.TestCase):
    def setUp(self):
        """Setting up the environment"""
        self.config_reader = collector_modules.ConfigReader(
            "config_file.yml"
        )  # Reading the local config file and setting everything up for being used in the tests

    def test_read_mongo_username(self):
        """Testing reading mongo username"""
        username = self.config_reader.find_value("mongoDB_unsername")

        self.assertEqual(username, "Username")

    def test_read_mongo_password(self):
        """Testing reading the mongo password"""
        password = self.config_reader.find_value("mongoDB_password")

        self.assertEqual(password, "Password")

    def test_read_mongo_auth_db(self):
        """Testing in reading the mongo auth database"""
        auth_db = self.config_reader.find_value("mongoDB_auth_db")

        self.assertEqual(auth_db, "Admin")

    def test_read_mongo_express_username(self):
        """Testing reading the mongodb express username"""
        mongodb_express_username = self.config_reader.find_value(
            "mongoDB-Express_username"
        )

        self.assertEqual(mongodb_express_username, "Username")

    def test_read_mongo_express_password(self):
        """Testing reading the mongodb express password"""
        mongodb_express_password = self.config_reader.find_value(
            "mongoDB-Express_password"
        )

        self.assertEqual(mongodb_express_password, "Password")


if __name__ == "__main__":
    unittest.main()

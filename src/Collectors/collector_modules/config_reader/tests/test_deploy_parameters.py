import unittest
import collector_modules


class MyTestCase(unittest.TestCase):
    def setUp(self):
        """Setting up the environment"""
        self.config_reader = collector_modules.ConfigReader(
            "config_file.yml"
        )  # Reading the local config file and setting everything up for being used in the tests

    def test_read_mongo_ports(self):
        """Testing reading mongo ports"""
        ports = self.config_reader.find_value("mongoDB_ports")

        self.assertEqual(ports, 27017)

    def test_read_mongo_ip(self):
        """Testing reading the mongodb IP"""
        ip = self.config_reader.find_value("mongoDB_IP")

        self.assertEqual(ip, "172.16.0.2")

    def test_read_mongo_database_name_intelligence(self):
        """Testing reading the mongodb intelligence database name"""
        mongo_database_name_intelligence = self.config_reader.find_value(
            "mongodbDatabaseNameIntelligence"
        )

        self.assertEqual(mongo_database_name_intelligence, "Intelligence")

    def test_read_mongo_database_name_utility(self):
        """Testing reading the mongodb utility database name"""
        mongo_database_name_utility = self.config_reader.find_value(
            "mongodbDatabaseNameUtility"
        )

        self.assertEqual(mongo_database_name_utility, "Utility")

    def test_read_mongo_express_ip(self):
        """Testing reading the mongodb express ip"""
        mongodb_express_ip = self.config_reader.find_value("mongoDB-Express_IP")

        self.assertEqual(mongodb_express_ip, "172.16.0.3")

    def test_read_mongo_express_port(self):
        """Testing reading the mongodb express ports"""
        mongodb_express_port = self.config_reader.find_value("mongoDB-Express_Port")

        self.assertEqual(mongodb_express_port, 8080)


if __name__ == "__main__":
    unittest.main()

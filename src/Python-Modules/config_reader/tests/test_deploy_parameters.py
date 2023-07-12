import unittest


class MyTestCase(unittest.TestCase):
    def setUp(self):
        """Setting up the environment"""

    def test_read_mongo_ports(self):
        """Testing reading mongo ports"""

    def test_read_mongo_ip(self):
        """Testing reading the mongodb IP"""

    def test_read_mongo_database_name_intelligence(self):
        """Testing reading the mongodb intelligence database name"""

    def test_read_mongo_database_name_utility(self):
        """Testing reading the mongodb utility database name"""

    def test_read_mongo_express_ip(self):
        """Testing reading the mongodb express ip"""

    def test_read_mongo_express_port(self):
        """Testing reading the mongodb express ports"""


if __name__ == '__main__':
    unittest.main()

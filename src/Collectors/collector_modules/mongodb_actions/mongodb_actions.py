from pymongo import MongoClient


class DatabaseConnector:
    def __init__(
        self,
        database_url: str,
        database_port: int,
        database_name: str,
        database_user: str = None,
        database_password: str = None,
        database_location: str = None,
        database_auth_name: str = None,
    ):
        # Getting the access for initiating the database connection
        self._DATABASE_HOST = database_url
        self._DATABASE_PORT = database_port
        self._DATABASE_NAME = database_name
        self._DATABASE_USER = database_user
        self._DATABASE_PASSWORD = database_password
        self._DATABASE_LOCATION = database_location
        self._DATABASE_AUTH_NAME = database_auth_name

        self.db_client = None
        self.db = None

        self.connection_established = False

        self.connection_string = (
            self._create_connection_string()
        )  # Creating the connection string

        self.connect_to_database()  # Connecting to the database

    def _create_connection_string(self) -> str or None:
        """Makes the connection string for the database"""
        if (
            self._DATABASE_USER is not None
            and self._DATABASE_PASSWORD is not None
            and self._DATABASE_AUTH_NAME is None
        ):
            """Authentication in case the user and password is provided"""
            return f"mongodb://{self._DATABASE_USER}:{self._DATABASE_PASSWORD}@{self._DATABASE_HOST}:{self._DATABASE_PORT}/{self._DATABASE_NAME}"

        elif self._DATABASE_AUTH_NAME is not None:
            """Authentication in case the auth database is specified"""
            return f"mongodb://{self._DATABASE_USER}:{self._DATABASE_PASSWORD}@{self._DATABASE_HOST}:{self._DATABASE_PORT}/{self._DATABASE_NAME}?authSource={self._DATABASE_AUTH_NAME}"

        else:
            """Returning None in the case of basic auth"""
            return None

    def connect_to_database(self):
        """Returns the object for doing database actions"""
        try:
            """Trying to connect to MongoDB"""

            if self.connection_string:
                self.db_client = MongoClient(self.connection_string)
            else:
                """Authentication without the user and password"""
                self.db_client = MongoClient(self._DATABASE_HOST, self._DATABASE_PORT)

            self.db = self.db_client[self._DATABASE_NAME]
            # Logging us connecting to the database
            print(
                f"\n====================\nConnected to MongoDB\n====================\n"
            )
            self.connection_established = True  # Setting the connection to established

        except ConnectionError as e:
            """Throwing an error in case the database doesn't connect"""
            print("There was an error while connecting to MongoDB: ", str(e))

    def disconnect(self):
        """Disconnects from the database"""
        """Should be used only at the end of communications with the database"""

        if self.connection_established:
            self.db_client.close()  # Disconnecting from the database

        pass  # Connection was not established so we don't do anything


class DatabaseActions:
    def __init__(self, db_connector: DatabaseConnector):
        self.db_connector = db_connector

    def _clean_user_input(self, query: dict) -> dict:
        """Cleaning the user inpout for potential malicious intentions"""

    def data_insert(self, collection: str, data):
        """Gets the desired information"""
        try:
            db_collection = self.db_connector.db[collection]
            result = db_collection.insert_one(data)

            if result.inserted_id:
                print("Document inserted successfully.")
            else:
                print("Failed to insert document.")
        except Exception as e:
            print("Error inserting document:", str(e))

    def data_insert_many(self, collection: str, data):
        """Gets the desired information"""
        try:
            db_collection = self.db_connector.db[collection]
            result = db_collection.insert_many(data)

            if result.inserted_id:
                print("Document inserted successfully.")
            else:
                print("Failed to insert document.")
        except Exception as e:
            print("Error inserting document:", str(e))

    def data_get(self, collection: str, query: dict) -> dict or None:
        """Getting data based on a query"""
        try:
            db_collection = self.db_connector.db[collection]
            # query = self._clean_user_input(query)
            result = db_collection.find_one(query)  # Looking for the query

            return result

        except Exception as e:
            print(
                f"Error while looking for the following in the database.\n QUERY:\n{query}\n ",
                str(e),
            )

        return (
            None  # Returning None in case there is no information found in the database
        )

    def data_get_many(self, collection: str, query: dict) -> dict or list or None:
        """Getting data based on a query"""
        try:
            db_collection = self.db_connector.db[collection]
            # query = self._clean_user_input(query)
            result = db_collection.find(query)  # Looking for the query

            return result

        except Exception as e:
            print(
                f"Error while looking for the following in the database.\n QUERY:\n{query}\n ",
                str(e),
            )

        return (
            None  # Returning None in case there is no information found in the database
        )

    def data_modify_one(
        self, collection: str, filter_query: dict, updated_data: dict
    ) -> str or None:
        """Modifies the data on a given key"""
        try:
            db_collection = self.db_connector.db[collection]
            result = db_collection.update_one(
                filter_query, updated_data
            )  # Updating the entry based on the filter

            return result

        except Exception as e:
            print(f"Error while updating the database.", str(e))

        return None

    def data_modify_many(
        self, collection: str, filter_query: dict, updated_data: dict
    ) -> str or None:
        """Modifies the data on a given key"""
        try:
            db_collection = self.db_connector.db[collection]
            result = db_collection.update_many(
                filter_query, updated_data
            )  # Updating the entry based on the filter

            return result

        except Exception as e:
            print(f"Error while updating many things in the database.", str(e))

        return None

    def data_delete_one(self, collection: str, filter_query: dict) -> str or None:
        """Deletes the data on a given key"""
        try:
            db_collection = self.db_connector.db[collection]
            result = db_collection.delete_one(
                filter_query
            )  # Updating the entry based on the filter

            return result

        except Exception as e:
            print(f"Error while deleting an entry from the DB.", str(e))

        return None

    def data_delete_many(self, collection: str, filter_query: dict) -> str or None:
        """Deletes the data on a given key"""
        try:
            db_collection = self.db_connector.db[collection]
            result = db_collection.delete_many(
                filter_query
            )  # Updating the entry based on the filter

            return result

        except Exception as e:
            print(f"Error while deleting an entry from the DB.", str(e))

        return None

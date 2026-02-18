from abc import ABC, abstractmethod

# 1. Use ABC (Abstract Base Class) instead of a regular class.
# This prevents people from accidentally creating an instance of 'PlatformName'
class PlatformName(ABC):
    @abstractmethod
    def connection(self):
        """
        By using @abstractmethod, Python will throw an error 
        immediately if a subclass forgets to implement this.
        """
        pass

class OracleDb(PlatformName):
    def connection(self):
        return "You are connecting to Oracle"

class PostgresDb(PlatformName):
    def connection(self):
        return "You are connecting to PostgresDb"

class MongoDb(PlatformName):
    def connection(self):
        return "You are connecting to MongoDb"

class BigqueryDb(PlatformName):
    def connection(self):
        return "You are connecting to BigqueryDb"

class MysqlDb(PlatformName):
    def connection(self):
        return "You are connecting to MysqlDb"

class DbFactoryConnections:
    @staticmethod
    def connecting(platform_type: str):
        # Normalize input to lowercase to prevent "Mysql" vs "mysql" errors
        platform = platform_type.lower()
        
        # Mapping dict is cleaner than long if/elif chains
        db_map = {
            "postgresql": PostgresDb,
            "postgres": PostgresDb,
            "oracle": OracleDb,
            "mongodb": MongoDb,
            "bigquery": BigqueryDb,
            "mysql": MysqlDb
        }
        
        if platform in db_map:
            # We return the INSTANCE: db_map[platform]() 
            # Note: We don't pass the string 'platform_name' into the constructor 
            # because your classes don't have an __init__ that accepts it.
            return db_map[platform]()
        
        raise ValueError(f"Unsupported database type: {platform_type}")
        
def main():
    # Test case: Valid input
    try:
        user_input = "mysql"
        db = DbFactoryConnections.connecting(user_input)
        print(f"Success: {db.connection()}")
    except ValueError as e:
        print(f"Error: {e}")

    # Test case: Invalid input
    try:
        user_input = "snowflake"
        db = DbFactoryConnections.connecting(user_input)
        print(db.connection())
    except ValueError as e:
        print(f"Caught Expected Error: {e}")

if __name__ == "__main__":
    main()

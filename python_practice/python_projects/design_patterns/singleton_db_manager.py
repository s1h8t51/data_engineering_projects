import sqlite3
import threading
from abc import ABC, abstractmethod

# ==========================================
# 1. FACTORY PATTERN: Connector Interface
# ==========================================
class DBConnector(ABC):
    """The Abstract Product"""
    @abstractmethod
    def connect(self):
        pass

class SQLiteConnector(DBConnector):
    """Concrete Product A"""
    def connect(self):
        return "Connected to SQLite Engine"

class PostgresConnector(DBConnector):
    """Concrete Product B"""
    def connect(self):
        # Simulation of a Postgres connection
        return "Connected to PostgreSQL Engine"

class ConnectorFactory:
    """The Factory Class"""
    @staticmethod
    def get_connector(db_type: str) -> DBConnector:
        connectors = {
            "sqlite": SQLiteConnector(),
            "postgres": PostgresConnector()
        }
        return connectors.get(db_type.lower(), SQLiteConnector())

# ==========================================
# 2. SINGLETON PATTERN: DB Manager
# ==========================================
class DatabaseManager:
    """
    Singleton class to manage DB connections.
    Uses a thread-safe implementation.
    """
    _instance = None
    _lock = threading.Lock() # Ensures thread safety in multi-threaded apps

    def __new__(cls):
        # Thread-safe Singleton implementation
        with cls._lock:
            if cls._instance is None:
                print("\n[System] Initializing Global Database Manager...")
                cls._instance = super(DatabaseManager, cls).__new__(cls)
                cls._instance.connection_pool = []
        return cls._instance

    def get_connection(self, db_type: str):
        # Uses the Factory to get the right connector
        connector = ConnectorFactory.get_connector(db_type)
        conn = connector.connect()
        self.connection_pool.append(conn)
        return conn

# ==========================================
# 3. EXECUTION / TEST
# ==========================================
if __name__ == "__main__":
    # Test Singleton behavior
    db_manager_1 = DatabaseManager()
    db_manager_2 = DatabaseManager()

    print(f"Manager 1 ID: {id(db_manager_1)}")
    print(f"Manager 2 ID: {id(db_manager_2)}")
    print(f"Are they the same instance? {db_manager_1 is db_manager_2}")

    # Test Factory behavior via the Singleton
    conn_a = db_manager_1.get_connection("postgres")
    conn_b = db_manager_2.get_connection("sqlite")

    print(f"\nConnection A: {conn_a}")
    print(f"Connection B: {conn_b}")
    print(f"Current Pool Size: {len(db_manager_1.connection_pool)}")

from abc import ABC, abstractmethod
import threading

class MetadataManager:
    _instance = None
    _lock = threading.Lock()  # To ensure thread safety

    def __new__(cls):
        # Use the Double-Checked Locking pattern
        if not cls._instance:
            with cls._lock:
                if not cls._instance:
                    cls._instance = super(MetadataManager, cls).__new__(cls)
                    cls._instance.connection_pool = "Active"
                    print("Initialized Central Metadata Manager Connection.")
        return cls._instance

class LocomotivePipeline(ABC):
    def execute(self):
        """The Template Method defining the workflow sequence."""
        self.connect()
        data = self.extract()  # This will call the child's implementation
        self.transform_and_load(data)
        print("Workflow Complete.\n")

    def connect(self):
        # Common logic for all pipelines
        print("Connecting to BNSF Secure Gateway...")

    @abstractmethod
    def extract(self):
        """Abstract: Every child MUST implement their own extraction logic."""
        pass

    def transform_and_load(self, data):
        # Default logic for cleaning and pushing to S3
        print(f"Transforming {data} and loading to S3 'Bronze' layer.")

# Child implementation
class GPSSensorPipeline(LocomotivePipeline):
    def extract(self):
        print("Extracting GPS data from REST API...")
        return {"lat": 32.77, "long": -96.79, "speed": 45}

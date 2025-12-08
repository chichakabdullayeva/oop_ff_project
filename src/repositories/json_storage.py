import json
import os
from ..utils.logging_config import get_logger

# OOP – Singleton: Only one JSONStorage instance exists
# SOLID – SRP: JSONStorage only handles JSON file operations
# GRASP – Information Expert: Knows how to read/write JSON data
class JSONStorage:
    
    _instance = None
    
    # OOP – Singleton: __new__ ensures single instance
    def __new__(cls, file_path="src/data/hotel_data.json"):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialized = False
        return cls._instance
    
    def __init__(self, file_path="src/data/hotel_data.json"):
        if self._initialized:
            return
        
        self.file_path = file_path
        self._initialized = True
        self.logger = get_logger(self.__class__.__name__)
        
        # CUPID – Predictable: Auto-creates directories and files
        directory = os.path.dirname(file_path)
        if directory and not os.path.exists(directory):
            os.makedirs(directory)
            self.logger.info(f"Created data directory: {directory}")
        
        if not os.path.exists(file_path):
            self._create_empty_file()
            self.logger.info(f"Storage initialized: {file_path}")
        else:
            self.logger.debug(f"Using existing storage: {file_path}")
    
    def _create_empty_file(self):
        empty_data = {
            "rooms": [],
            "guests": [],
            "reservations": [],
            "payments": []
        }
        with open(self.file_path, 'w') as file:
            json.dump(empty_data, file, indent=4)
        self.logger.info(f"Created fresh database: {self.file_path}")
    
    # GRASP – Information Expert: JSONStorage knows how to read its file
    def read_all(self):
        try:
            with open(self.file_path, 'r') as file:
                data = json.load(file)
                self.logger.debug(f"Read data from storage")
                return data
        except (FileNotFoundError, json.JSONDecodeError) as error:
            self.logger.warning(f"Storage corrupted, recreating: {error}")
            self._create_empty_file()
            return self.read_all()
    
    # GRASP – Information Expert: JSONStorage knows how to write its file
    def write_all(self, data):
        try:
            with open(self.file_path, 'w') as file:
                json.dump(data, file, indent=4)
            self.logger.debug(f"Data saved to storage")
        except Exception as error:
            self.logger.error(f"Failed to write: {error}", exc_info=True)
            raise
    
    def read_collection(self, collection_name):
        data = self.read_all()
        collection = data.get(collection_name, [])
        self.logger.debug(f"Loaded {len(collection)} items from {collection_name}")
        return collection
    
    def write_collection(self, collection_name, items):
        data = self.read_all()
        data[collection_name] = items
        self.write_all(data)
        self.logger.debug(f"Saved {len(items)} items to {collection_name}")


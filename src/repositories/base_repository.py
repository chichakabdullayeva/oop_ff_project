from ..utils.logging_config import get_logger

# OOP – Inheritance: Abstract base class for all repositories
# SOLID – SRP: BaseRepository only handles generic CRUD operations
# GRASP – Information Expert: Repository knows how to persist its model
class BaseRepository:
    
    def __init__(self, storage, collection_name, model_class):
        # SOLID – DIP: Depends on abstraction (storage) not concrete implementation
        self.storage = storage
        self.collection_name = collection_name
        self.model_class = model_class
        self.logger = get_logger(self.__class__.__name__)
        self.logger.debug(f"{self.__class__.__name__} initialized for {collection_name}")
    
    # GRASP – Creator: Repository creates and saves model instances
    def create(self, item):
        self.logger.debug(f"Saving new {self.collection_name}: {item.id}")
        try:
            items = self.storage.read_collection(self.collection_name)
            items.append(item.to_dict())
            self.storage.write_collection(self.collection_name, items)
            self.logger.info(f"{self.collection_name.title()} saved: {item.id}")
            return item
        except Exception as error:
            self.logger.error(f"Failed to save {self.collection_name}: {error}", exc_info=True)
            raise
    
    # GRASP – Information Expert: Repository knows how to find its items
    def get_by_id(self, item_id):
        self.logger.debug(f"Looking up {self.collection_name}: {item_id}")
        try:
            items = self.storage.read_collection(self.collection_name)
            for item_data in items:
                if item_data.get("id") == item_id:
                    self.logger.debug(f"Found {self.collection_name}: {item_id}")
                    return self.model_class.from_dict(item_data)
            self.logger.debug(f"{self.collection_name.title()} not found: {item_id}")
            return None
        except Exception as error:
            self.logger.error(f"Lookup failed: {error}", exc_info=True)
            raise
    
    def get_all(self):
        self.logger.debug(f"Loading all {self.collection_name}")
        try:
            items = self.storage.read_collection(self.collection_name)
            
            result = []
            for item_data in items:
                model_object = self.model_class.from_dict(item_data)
                result.append(model_object)
            
            self.logger.debug(f"Loaded {len(result)} {self.collection_name}")
            return result
        except Exception as error:
            self.logger.error(f"Failed to load {self.collection_name}: {error}", exc_info=True)
            raise
    
    # GRASP – Information Expert: Repository updates its own collection
    def update(self, item):
        self.logger.debug(f"Updating {self.collection_name}: {item.id}")
        try:
            items = self.storage.read_collection(self.collection_name)
            
            found = False
            for i in range(len(items)):
                if items[i].get("id") == item.id:
                    items[i] = item.to_dict()
                    found = True
                    break
            
            if not found:
                error_msg = f"{self.collection_name.title()} not found: {item.id}"
                self.logger.warning(error_msg)
                raise ValueError(error_msg)
            
            self.storage.write_collection(self.collection_name, items)
            self.logger.info(f"{self.collection_name.title()} updated: {item.id}")
            return item
        except Exception as error:
            self.logger.error(f"Update failed: {error}", exc_info=True)
            raise
    
    def delete(self, item_id):
        self.logger.debug(f"Deleting {self.collection_name}: {item_id}")
        try:
            items = self.storage.read_collection(self.collection_name)
            original_count = len(items)
            
            filtered_items = []
            for item in items:
                if item.get("id") != item_id:
                    filtered_items.append(item)
            
            if len(filtered_items) == original_count:
                error_msg = f"{self.collection_name.title()} not found: {item_id}"
                self.logger.warning(error_msg)
                raise ValueError(error_msg)
            
            self.storage.write_collection(self.collection_name, filtered_items)
            self.logger.info(f"{self.collection_name.title()} deleted: {item_id}")
            return True
        except Exception as error:
            self.logger.error(f"Deletion failed: {error}", exc_info=True)
            raise


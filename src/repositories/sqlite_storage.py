import sqlite3
import json
from datetime import datetime
from ..utils.logging_config import get_logger

class SQLiteStorage:
    
    _instance = None
    
    def __new__(cls, db_path="src/data/hotel_system.db"):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialized = False
        return cls._instance
    
    def __init__(self, db_path="src/data/hotel_system.db"):
        if self._initialized:
            return
        
        self.db_path = db_path
        self._initialized = True
        self.logger = get_logger(self.__class__.__name__)
        self._initialize_database()
        self.logger.info(f"Database initialized: {db_path}")
    
    def _initialize_database(self):
        conn = self._get_connection()
        cursor = conn.cursor()
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS rooms (
                id TEXT PRIMARY KEY,
                number TEXT NOT NULL,
                room_type TEXT NOT NULL,
                price_per_night REAL NOT NULL,
                capacity INTEGER NOT NULL,
                is_available INTEGER NOT NULL,
                created_at TEXT,
                updated_at TEXT
            )
        ''')
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS guests (
                id TEXT PRIMARY KEY,
                name TEXT NOT NULL,
                email TEXT NOT NULL,
                phone TEXT NOT NULL,
                created_at TEXT,
                updated_at TEXT
            )
        ''')
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS reservations (
                id TEXT PRIMARY KEY,
                guest_id TEXT NOT NULL,
                room_id TEXT NOT NULL,
                check_in_date TEXT NOT NULL,
                check_out_date TEXT NOT NULL,
                status TEXT NOT NULL,
                created_at TEXT,
                updated_at TEXT,
                FOREIGN KEY (guest_id) REFERENCES guests(id),
                FOREIGN KEY (room_id) REFERENCES rooms(id)
            )
        ''')
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS payments (
                id TEXT PRIMARY KEY,
                reservation_id TEXT NOT NULL,
                amount REAL NOT NULL,
                payment_type TEXT NOT NULL,
                status TEXT NOT NULL,
                card_number TEXT,
                created_at TEXT,
                updated_at TEXT,
                FOREIGN KEY (reservation_id) REFERENCES reservations(id)
            )
        ''')
        
        conn.commit()
        conn.close()
        self.logger.info("Database tables created successfully")
    
    def _get_connection(self):
        import os
        directory = os.path.dirname(self.db_path)
        if directory and not os.path.exists(directory):
            os.makedirs(directory)
        return sqlite3.connect(self.db_path)
    
    def read_collection(self, collection_name):
        conn = self._get_connection()
        cursor = conn.cursor()
        
        try:
            cursor.execute(f"SELECT * FROM {collection_name}")
            
            column_names = [col[0] for col in cursor.description]
            rows = cursor.fetchall()
            
            result = []
            for row in rows:
                item = {}
                for i, column_name in enumerate(column_names):
                    item[column_name] = row[i]
                
                if 'is_available' in item:
                    item['is_available'] = bool(item['is_available'])
                
                result.append(item)
            
            self.logger.debug(f"Loaded {len(result)} items from {collection_name}")
            return result
        except Exception as error:
            self.logger.error(f"Error reading {collection_name}: {error}", exc_info=True)
            raise
        finally:
            conn.close()
    
    def write_collection(self, collection_name, items):
        conn = self._get_connection()
        cursor = conn.cursor()
        
        try:
            cursor.execute(f"DELETE FROM {collection_name}")
            
            for item in items:
                columns = list(item.keys())
                placeholders = ', '.join(['?' for _ in columns])
                column_names = ', '.join(columns)
                
                values = []
                for column in columns:
                    value = item[column]
                    if column == 'is_available' and isinstance(value, bool):
                        value = 1 if value else 0
                    values.append(value)
                
                sql = f"INSERT INTO {collection_name} ({column_names}) VALUES ({placeholders})"
                cursor.execute(sql, values)
            
            conn.commit()
            self.logger.debug(f"Saved {len(items)} items to {collection_name}")
        except Exception as error:
            conn.rollback()
            self.logger.error(f"Error writing to {collection_name}: {error}", exc_info=True)
            raise
        finally:
            conn.close()
    
    def read_all(self):
        return {
            "rooms": self.read_collection("rooms"),
            "guests": self.read_collection("guests"),
            "reservations": self.read_collection("reservations"),
            "payments": self.read_collection("payments")
        }
    
    def write_all(self, data):
        for collection_name, items in data.items():
            self.write_collection(collection_name, items)

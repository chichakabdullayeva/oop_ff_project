# SOLID – SRP: This module handles only logging configuration
import logging
import os
from logging.handlers import RotatingFileHandler


def setup_logging():
    # CUPID – Idiomatic: Uses Python's built-in logging module idiomatically
    logs_dir = "logs"
    if not os.path.exists(logs_dir):
        os.makedirs(logs_dir)
    
    log_format = '%(asctime)s - %(levelname)s - [%(name)s] - %(message)s'
    date_format = '%Y-%m-%d %H:%M:%S'
    
    formatter = logging.Formatter(log_format, datefmt=date_format)
    
    # SOLID – OCP: RotatingFileHandler extends base handler without modifying it
    file_handler = RotatingFileHandler(
        filename=os.path.join(logs_dir, 'app.log'),
        maxBytes=1048576,  # 1MB
        backupCount=3,
        encoding='utf-8'
    )
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)
    
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(formatter)
    
    root_logger = logging.getLogger()
    root_logger.setLevel(logging.DEBUG)
    root_logger.handlers.clear()
    root_logger.addHandler(file_handler)
    root_logger.addHandler(console_handler)
    
    root_logger.info("="*60)
    root_logger.info("Hotel Reservation System logging initialized")
    root_logger.info(f"Logs saved to: {os.path.join(logs_dir, 'app.log')}")
    root_logger.info("="*60)


def get_logger(name):
    return logging.getLogger(name)


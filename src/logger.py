import logging
import os
from logging.handlers import RotatingFileHandler

def setup_logging(log_file='app.log'):
    logging.basicConfig(
        filename=log_file,
        level=logging.DEBUG,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )
    
# Define log file paths
LOG_DIR = "LiveStreamApp/logs/"
INSTALL_LOG_FILE = os.path.join(LOG_DIR, "install.log")
SCHEDULE_LOG_FILE = os.path.join(LOG_DIR, "schedule.log")
STREAM_LOG_FILE = os.path.join(LOG_DIR, "stream.log")

# Ensure the logs directory exists
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

# Function to configure logger
def configure_logger(log_file, level=logging.INFO):
    logger = logging.getLogger(log_file)
    logger.setLevel(level)

    # Handler to rotate log files
    handler = RotatingFileHandler(log_file, maxBytes=5 * 1024 * 1024, backupCount=3)  # 5MB per file
    handler.setLevel(level)

    # Log format
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)

    # Add handler to logger if not already added
    if not logger.handlers:
        logger.addHandler(handler)
    
    return logger

# Install logger
install_logger = configure_logger(INSTALL_LOG_FILE, logging.INFO)

# Schedule logger
schedule_logger = configure_logger(SCHEDULE_LOG_FILE, logging.INFO)

# Stream logger
stream_logger = configure_logger(STREAM_LOG_FILE, logging.INFO)

# Log an install event
def log_install_event(event):
    install_logger.info(f"Installation Event: {event}")

# Log a schedule event
def log_schedule_event(event):
    schedule_logger.info(f"Schedule Event: {event}")

# Log a streaming event
def log_stream_event(event):
    stream_logger.info(f"Streaming Event: {event}")

# Log errors
def log_error(logger_name, error_msg):
    logger_name.error(f"Error: {error_msg}")

# Example usage
if __name__ == "__main__":
    log_install_event("Dependencies installed successfully.")
    log_schedule_event("Live stream scheduled for 2024-10-01 15:00:00.")
    log_stream_event("Streaming started on YouTube.")
    log_error(stream_logger, "Failed to connect to Twitch.")

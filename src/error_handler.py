import logging
import sys
import traceback
from datetime import datetime

def handle_error(e):
    """Handles errors by logging them and providing user feedback."""
    
    # Log the error with a detailed stack trace
    logging.error("An error occurred: %s", str(e))
    logging.error("Traceback: %s", traceback.format_exc())
    
class ErrorHandler:
    def __init__(self, log_file='logs/error.log'):
        self.log_file = log_file
        logging.basicConfig(filename=self.log_file, level=logging.ERROR, 
                            format='%(asctime)s - %(levelname)s - %(message)s')

    def log_error(self, error_message):
        """Logs the error message with a timestamp."""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        error_entry = f"{timestamp} - ERROR - {error_message}"
        logging.error(error_entry)

    def handle_exception(self, exc_type, exc_value, exc_traceback):
        """Handles uncaught exceptions and logs the traceback."""
        if issubclass(exc_type, KeyboardInterrupt):
            sys.__exit__()  # Allow CTRL+C to exit the program cleanly

        error_message = "".join(traceback.format_exception(exc_type, exc_value, exc_traceback))
        self.log_error(error_message)
        print(f"An unexpected error occurred. Please check {self.log_file} for more details.")

    def handle_function_error(self, func):
        """Decorator to catch and log exceptions in specific functions."""
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                self.log_error(f"Exception in {func.__name__}: {str(e)}")
                raise
        return wrapper

# Create an instance of ErrorHandler to be used globally
error_handler = ErrorHandler()

# Set global exception handling
sys.excepthook = error_handler.handle_exception

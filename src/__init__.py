# LiveStreamApp/src/__init__.py

import os
import logging

# Set up logging configuration
logging.basicConfig(
    filename='logs/app.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def initialize_directories():
    """
    Ensure that crucial directories for the application exist.
    Creates the following directories if they don't exist:
    - uploaded-videos
    - downloaded-videos
    - scheduled-videos
    - logs
    """
    directories = [
        'uploaded-videos',
        'downloaded-videos',
        'scheduled-videos',
        'logs',
        'config'
    ]
    
    for directory in directories:
        if not os.path.exists(directory):
            os.makedirs(directory)
            logging.info(f'Created directory: {directory}')
        else:
            logging.info(f'Directory already exists: {directory}')

def initialize_app():
    """
    Initialize the application by setting up necessary directories and configurations.
    This function is called automatically when the module is imported.
    """
    initialize_directories()
    logging.info('Application initialized.')

# Call initialize_app when the module is imported
initialize_app()


import os
import unittest
import logging
from unittest.mock import patch, MagicMock
from src.logger import setup_logger


class TestLogger(unittest.TestCase):
    
    def setUp(self):
        """Create a mock for logging setup and log file paths."""
        self.install_log_path = 'LiveStreamApp/logs/install.log'
        self.schedule_log_path = 'LiveStreamApp/logs/schedule.log'
        self.stream_log_path = 'LiveStreamApp/logs/stream.log'

        # Ensure log files don't exist before the test
        for log_path in [self.install_log_path, self.schedule_log_path, self.stream_log_path]:
            if os.path.exists(log_path):
                os.remove(log_path)

    def tearDown(self):
        """Remove any log files that may have been created during the test."""
        for log_path in [self.install_log_path, self.schedule_log_path, self.stream_log_path]:
            if os.path.exists(log_path):
                os.remove(log_path)

    def test_install_log_creation(self):
        """Test if install.log is created and logs correctly."""
        logger = setup_logger('install_logger', self.install_log_path)
        logger.info('Test install log entry')

        # Check if the log file was created
        self.assertTrue(os.path.exists(self.install_log_path))

        # Verify the content of the log file
        with open(self.install_log_path, 'r') as log_file:
            log_content = log_file.read()
            self.assertIn('Test install log entry', log_content)

    def test_schedule_log_creation(self):
        """Test if schedule.log is created and logs correctly."""
        logger = setup_logger('schedule_logger', self.schedule_log_path)
        logger.info('Test schedule log entry')

        # Check if the log file was created
        self.assertTrue(os.path.exists(self.schedule_log_path))

        # Verify the content of the log file
        with open(self.schedule_log_path, 'r') as log_file:
            log_content = log_file.read()
            self.assertIn('Test schedule log entry', log_content)

    def test_stream_log_creation(self):
        """Test if stream.log is created and logs correctly."""
        logger = setup_logger('stream_logger', self.stream_log_path)
        logger.info('Test stream log entry')

        # Check if the log file was created
        self.assertTrue(os.path.exists(self.stream_log_path))

        # Verify the content of the log file
        with open(self.stream_log_path, 'r') as log_file:
            log_content = log_file.read()
            self.assertIn('Test stream log entry', log_content)

    @patch('src.logger.logging.getLogger')
    def test_logger_configuration(self, mock_get_logger):
        """Test if the logger configuration sets the correct logger name and log level."""
        mock_logger = MagicMock()
        mock_get_logger.return_value = mock_logger

        logger = setup_logger('test_logger', self.install_log_path)

        # Check if logger was set up with the correct name
        mock_get_logger.assert_called_once_with('test_logger')

        # Check if the log level is set to INFO
        mock_logger.setLevel.assert_called_once_with(logging.INFO)

    @patch('src.logger.logging.FileHandler')
    def test_log_file_handler(self, mock_file_handler):
        """Test if the FileHandler is attached to the logger with the correct log file."""
        mock_handler = MagicMock()
        mock_file_handler.return_value = mock_handler

        logger = setup_logger('test_logger', self.schedule_log_path)

        # Check if the file handler is initialized with the correct log file
        mock_file_handler.assert_called_once_with(self.schedule_log_path)

        # Check if the handler is added to the logger
        self.assertTrue(mock_handler in logger.handlers)

    def test_logging_format(self):
        """Test if the logging format is correctly set."""
        logger = setup_logger('test_logger', self.stream_log_path)

        # Ensure the logger has a formatter with the correct format
        for handler in logger.handlers:
            self.assertIsInstance(handler.formatter, logging.Formatter)
            self.assertEqual(handler.formatter._fmt, '%(asctime)s - %(name)s - %(levelname)s - %(message)s')


if __name__ == '__main__':
    unittest.main()

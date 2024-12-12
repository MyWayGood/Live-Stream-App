import unittest
import os
import json
from src.settings import Settings  # assuming Settings class is in settings.py

class TestSettings(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Create a mock settings file to test
        cls.mock_settings_file = "test_settings.json"
        cls.default_settings = {
            "video_quality": "HD",
            "stream_bitrate": "5000k",
            "platforms": {
                "YouTube": {"enabled": True, "rtmp_url": "rtmp://a.rtmp.youtube.com/live2/"},
                "Facebook": {"enabled": False, "rtmp_url": "rtmp://live-api-s.facebook.com:80/rtmp/"}
            }
        }
        # Write the default settings to the mock file
        with open(cls.mock_settings_file, 'w') as f:
            json.dump(cls.default_settings, f)

    @classmethod
    def tearDownClass(cls):
        # Remove the mock settings file after tests
        if os.path.exists(cls.mock_settings_file):
            os.remove(cls.mock_settings_file)

    def setUp(self):
        # Instantiate the Settings class using the mock file for each test
        self.settings = Settings(settings_file=self.mock_settings_file)

    def test_load_settings(self):
        """Test loading settings from file."""
        loaded_settings = self.settings.load_settings()
        self.assertEqual(loaded_settings, self.default_settings, "Settings loaded from file do not match expected defaults.")

    def test_save_settings(self):
        """Test saving settings to file."""
        new_settings = {
            "video_quality": "FHD",
            "stream_bitrate": "10000k",
            "platforms": {
                "YouTube": {"enabled": True, "rtmp_url": "rtmp://a.rtmp.youtube.com/live2/"},
                "Facebook": {"enabled": True, "rtmp_url": "rtmp://live-api-s.facebook.com:80/rtmp/"}
            }
        }
        self.settings.save_settings(new_settings)

        # Check if settings were saved correctly
        with open(self.mock_settings_file, 'r') as f:
            saved_data = json.load(f)

        self.assertEqual(saved_data, new_settings, "Saved settings do not match the updated settings.")

    def test_update_settings(self):
        """Test updating a specific setting and saving it."""
        self.settings.update_setting("video_quality", "FHD")
        updated_settings = self.settings.load_settings()

        self.assertEqual(updated_settings["video_quality"], "FHD", "Failed to update video_quality setting.")

    def test_invalid_settings_file(self):
        """Test behavior when the settings file is missing or corrupted."""
        invalid_file = "invalid_settings.json"
        self.settings.settings_file = invalid_file

        # Since file doesn't exist, should raise an error or return an empty settings dict
        with self.assertRaises(FileNotFoundError):
            self.settings.load_settings()

    def test_reset_settings(self):
        """Test resetting settings to default."""
        self.settings.reset_settings()
        current_settings = self.settings.load_settings()

        self.assertEqual(current_settings, self.default_settings, "Settings were not reset to default values.")

if __name__ == "__main__":
    unittest.main()

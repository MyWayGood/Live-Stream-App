import json
import os
from pathlib import Path
import logging

# Path to the settings.json file
SETTINGS_FILE = Path("LiveStreamApp/config/settings.json")

# Logger configuration
logging.basicConfig(filename='LiveStreamApp/logs/settings.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

class SettingsManager:
    def __init__(self):
        # Load settings during initialization
        self.settings = self.load_settings()

    def load_settings(self):
        """Load settings from the settings.json file."""
        if SETTINGS_FILE.exists():
            try:
                with open(SETTINGS_FILE, 'r', encoding='utf-8') as f:
                    settings = json.load(f)
                logging.info("Settings loaded successfully.")
                return settings
            except json.JSONDecodeError as e:
                logging.error(f"Failed to decode JSON: {e}")
                return {}
        else:
            logging.warning(f"Settings file not found. Creating a new settings file at {SETTINGS_FILE}.")
            return {}

    def save_settings(self):
        """Save the current settings to the settings.json file."""
        try:
            with open(SETTINGS_FILE, 'w', encoding='utf-8') as f:
                json.dump(self.settings, f, indent=4)
            logging.info("Settings saved successfully.")
        except IOError as e:
            logging.error(f"Failed to save settings: {e}")

    def get_setting(self, key, default=None):
        """Retrieve a setting by key, return default if key doesn't exist."""
        return self.settings.get(key, default)

    def set_setting(self, key, value):
        """Set a setting and save to the file."""
        self.settings[key] = value
        self.save_settings()
        logging.info(f"Setting '{key}' updated to '{value}'.")

    def update_settings(self, new_settings):
        """Update multiple settings at once and save to the file."""
        self.settings.update(new_settings)
        self.save_settings()
        logging.info("Settings updated with new values.")

    def reset_to_defaults(self):
        """Reset all settings to their default values and save."""
        default_settings = {
            "video_directory": "LiveStreamApp/media/uploaded-videos",
            "download_directory": "LiveStreamApp/media/downloaded-videos",
            "scheduled_videos_directory": "LiveStreamApp/media/scheduled-videos",
            "stream_resolution": "HD",  # Default resolution: SD, HD, FHD
            "stream_bitrate": "3000k",  # Default bitrate
            "platform_keys": {},
            "terms_accepted": False
        }
        self.settings = default_settings
        self.save_settings()
        logging.info("Settings reset to default values.")

# Usage example
if __name__ == "__main__":
    settings_manager = SettingsManager()

    # Get a setting
    video_dir = settings_manager.get_setting('video_directory', 'default_directory')
    print(f"Video directory: {video_dir}")

    # Update a setting
    settings_manager.set_setting('stream_bitrate', '5000k')

    # Reset settings to default
    settings_manager.reset_to_defaults()

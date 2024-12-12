import json
import os

# File paths for storing stream key data
STREAM_KEYS_FILE = os.path.join("config", "stream_keys.json")
PLATFORMS_FILE = os.path.join("config", "platforms.json")

class StreamKeyManager:
    def __init__(self):
        # Load existing stream keys and platforms
        self.stream_keys = self.load_stream_keys()
        self.platforms = self.load_platforms()

    def load_stream_keys(self):
        """Load stream keys from the JSON file."""
        if os.path.exists(STREAM_KEYS_FILE):
            with open(STREAM_KEYS_FILE, 'r') as file:
                return json.load(file)
        return {}

    def load_platforms(self):
        """Load platform data from the JSON file."""
        if os.path.exists(PLATFORMS_FILE):
            with open(PLATFORMS_FILE, 'r') as file:
                return json.load(file)
        return {}

    def save_stream_keys(self):
        """Save the stream keys to the JSON file."""
        with open(STREAM_KEYS_FILE, 'w') as file:
            json.dump(self.stream_keys, file, indent=4)

    def add_stream_key(self, platform, stream_key):
        """Add a new stream key to the list."""
        if platform not in self.platforms:
            raise ValueError(f"Platform {platform} is not supported.")
        
        self.stream_keys[platform] = stream_key
        self.save_stream_keys()
        print(f"Stream key for {platform} added successfully.")

    def delete_stream_key(self, platform):
        """Remove a stream key from the list."""
        if platform in self.stream_keys:
            del self.stream_keys[platform]
            self.save_stream_keys()
            print(f"Stream key for {platform} deleted successfully.")
        else:
            raise KeyError(f"No stream key found for {platform}.")

    def generate_rtmp_url(self, platform):
        """Generate the RTMP URL for a given platform using the stream key."""
        if platform not in self.platforms:
            raise ValueError(f"Platform {platform} is not supported.")

        stream_key = self.stream_keys.get(platform)
        if not stream_key:
            raise KeyError(f"No stream key found for {platform}. Please add the stream key first.")
        
        rtmp_url_template = self.platforms[platform]["rtmp_url"]
        return rtmp_url_template.replace("$STREAM_KEY", stream_key)

# Example usage:
if __name__ == "__main__":
    manager = StreamKeyManager()

    # Add a new stream key
    manager.add_stream_key("YouTube", "your_stream_key_here")

    # Delete a stream key
    manager.delete_stream_key("YouTube")

    # Generate RTMP URL
    try:
        rtmp_url = manager.generate_rtmp_url("YouTube")
        print(f"RTMP URL: {rtmp_url}")
    except Exception as e:
        print(str(e))

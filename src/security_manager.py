import os
import json
from cryptography.fernet import Fernet
from typing import Any, Dict

class SecurityManager:
    def __init__(self, key_file: str = 'config/encryption_key.key', data_file: str = 'config/stream_keys.json'):
        self.key_file = key_file
        self.data_file = data_file
        self.key = self.load_or_create_key()
        self.fernet = Fernet(self.key)

    def load_or_create_key(self) -> bytes:
        """Load the encryption key from a file or create a new one if it doesn't exist."""
        if os.path.exists(self.key_file):
            with open(self.key_file, 'rb') as key_file:
                return key_file.read()
        else:
            key = Fernet.generate_key()
            with open(self.key_file, 'wb') as key_file:
                key_file.write(key)
            return key

    def encrypt_data(self, data: str) -> bytes:
        """Encrypt the given data."""
        return self.fernet.encrypt(data.encode())

    def decrypt_data(self, token: bytes) -> str:
        """Decrypt the given encrypted data."""
        return self.fernet.decrypt(token).decode()

    def save_stream_keys(self, stream_keys: Dict[str, str]) -> None:
        """Encrypt and save stream keys to a JSON file, checking if the file already exists."""
        encrypted_keys = {platform: self.encrypt_data(key).decode() for platform, key in stream_keys.items()}
        
        # Check if the JSON file already exists
        if os.path.exists(self.data_file):
            print(f"Warning: {self.data_file} already exists. Overwriting...")

        with open(self.data_file, 'w') as json_file:
            json.dump(encrypted_keys, json_file)

    def load_stream_keys(self) -> Dict[str, str]:
        """Load and decrypt stream keys from a JSON file, checking if the file exists."""
        if not os.path.exists(self.data_file):
            print(f"Warning: {self.data_file} does not exist. Returning empty dictionary.")
            return {}

        with open(self.data_file, 'r') as json_file:
            encrypted_keys = json.load(json_file)

        return {platform: self.decrypt_data(key.encode()) for platform, key in encrypted_keys.items()}

# Example usage:
if __name__ == "__main__":
    manager = SecurityManager()

    # Example of saving stream keys
    stream_keys = {
        'YouTube': 'your_youtube_stream_key',
        'Twitch': 'your_twitch_stream_key',
        'Facebook': 'your_facebook_stream_key'
    }

    manager.save_stream_keys(stream_keys)

    # Example of loading stream keys
    loaded_keys = manager.load_stream_keys()
    print("Loaded Stream Keys:", loaded_keys)

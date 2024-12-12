from cryptography.fernet import Fernet
import os

def generate_key(key_file: str):
    """Generate a new encryption key and save it to the specified file."""
    key = Fernet.generate_key()
    with open(key_file, 'wb') as file:
        file.write(key)
    print(f"Encryption key generated and saved to {key_file}")

if __name__ == "__main__":
    key_file_path = 'config/encryption_key.key'
    
    # Ensure the config directory exists
    os.makedirs(os.path.dirname(key_file_path), exist_ok=True)
    
    generate_key(key_file_path)

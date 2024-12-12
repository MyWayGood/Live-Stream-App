import os
import json

def load_platforms():
    platforms_file_path = 'config/platforms.json'
    
    if not os.path.exists(platforms_file_path):
        print(f"{platforms_file_path} does not exist. Please run the initialization script.")
        return None
    
    with open(platforms_file_path, 'r') as file:
        return json.load(file)

def load_stream_keys():
    stream_keys_file_path = 'config/stream_keys.json'
    
    if not os.path.exists(stream_keys_file_path):
        print(f"{stream_keys_file_path} does not exist. Please run the initialization script.")
        return None
    
    with open(stream_keys_file_path, 'r') as file:
        return json.load(file)

# Example usage
platforms = load_platforms()
stream_keys = load_stream_keys()

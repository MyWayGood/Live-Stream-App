import os
import json

def initialize_files():
    """Initialize required JSON files for the Live Stream App."""
    
    # Define the paths for the JSON files
    platforms_file_path = 'config/platforms.json'
    stream_keys_file_path = 'config/stream_keys.json'
    
    # Ensure the config directory exists
    os.makedirs(os.path.dirname(platforms_file_path), exist_ok=True)
    
    # Initialize platforms.json if it doesn't exist
    if not os.path.exists(platforms_file_path):
        platforms_data = {
            "platforms": [
                {
                    "name": "YouTube",
                    "rtmp_url": "rtmp://a.rtmp.youtube.com/live2/$STREAM_KEY",
                    "enabled": True
                },
                {
                    "name": "Twitch",
                    "rtmp_url": "rtmp://live.twitch.tv/app/$STREAM_KEY",
                    "enabled": True
                },
                {
                    "name": "Facebook",
                    "rtmp_url": "rtmp://live-api-s.facebook.com:80/rtmp/$STREAM_KEY",
                    "enabled": True
                },
                {
                    "name": "Instagram",
                    "rtmp_url": "rtmp://live-upload.instagram.com:80/rtmp/$STREAM_KEY",
                    "enabled": True
                },
                {
                    "name": "Dailymotion",
                    "rtmp_url": "rtmp://publish.dailymotion.com/live?stream_key=$STREAM_KEY",
                    "enabled": True
                },
                {
                    "name": "Kick",
                    "rtmp_url": "rtmp://live.kick.com/app/$STREAM_KEY",
                    "enabled": True
                },
                {
                    "name": "Rumble",
                    "rtmp_url": "rtmp://live.rumble.com/$STREAM_KEY",
                    "enabled": True
                },
                {
                    "name": "TikTok",
                    "rtmp_url": "rtmp://live.tiktok.com/live/$STREAM_KEY",
                    "enabled": True
                },
                {
                    "name": "Vimeo",
                    "rtmp_url": "rtmp://live.vimeo.com/app/$STREAM_KEY",
                    "enabled": True
                },
                {
                    "name": "X (Twitter)",
                    "rtmp_url": "rtmp://live.pscp.tv:80/x/$STREAM_KEY",
                    "enabled": True
                },
                {
                    "name": "Custom Platform",
                    "rtmp_url": "",
                    "enabled": False
                }
            ]
        }

        with open(platforms_file_path, 'w') as file:
            json.dump(platforms_data, file, indent=4)
        print(f"Initialized '{platforms_file_path}' with default data.")

    else:
        print(f"'{platforms_file_path}' already exists. No changes made.")

    # Initialize stream_keys.json if it doesn't exist
    if not os.path.exists(stream_keys_file_path):
        stream_keys_data = {
            "keys": {
                "YouTube": {"stream_key": ""},
                "Twitch": {"stream_key": ""},
                "Facebook": {"stream_key": ""},
                "Instagram": {"stream_key": ""},
                "Dailymotion": {"stream_key": ""},
                "Kick": {"stream_key": ""},
                "Rumble": {"stream_key": ""},
                "TikTok": {"stream_key": ""},
                "Vimeo": {"stream_key": ""},
                "X (Twitter)": {"stream_key": ""},
                "Custom Platform": {"stream_key": ""}
            }
        }

        with open(stream_keys_file_path, 'w') as file:
            json.dump(stream_keys_data, file, indent=4)
        print(f"Initialized '{stream_keys_file_path}' with default structure.")

    else:
        print(f"'{stream_keys_file_path}' already exists. No changes made.")

if __name__ == "__main__":
    initialize_files()

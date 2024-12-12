import os
import json

def initialize_platforms():
    platforms = {
        "platforms": [
            {
                "name": "Dailymotion",
                "rtmp_url": "rtmp://publish.dailymotion.com/live?stream_key=$STREAM_KEY"
            },
            {
                "name": "Facebook",
                "rtmp_url": "rtmp://live-api-s.facebook.com:80/rtmp/$STREAM_KEY"
            },
            {
                "name": "Instagram",
                "rtmp_url": "rtmp://live-upload.instagram.com:80/rtmp/$STREAM_KEY"
            },
            {
                "name": "Kick",
                "rtmp_url": "rtmp://live.kick.com/app/$STREAM_KEY"
            },
            {
                "name": "Rumble",
                "rtmp_url": "rtmp://live.rumble.com/$STREAM_KEY"
            },
            {
                "name": "TikTok",
                "rtmp_url": "rtmp://live.tiktok.com/live/$STREAM_KEY"
            },
            {
                "name": "Twitch",
                "rtmp_url": "rtmp://live.twitch.tv/app/$STREAM_KEY"
            },
            {
                "name": "Vimeo",
                "rtmp_url": "rtmp://live.vimeo.com/app/$STREAM_KEY"
            },
            {
                "name": "X (Twitter)",
                "rtmp_url": "rtmp://live.pscp.tv:80/x/$STREAM_KEY"
            },
            {
                "name": "YouTube",
                "rtmp_url": "rtmp://a.rtmp.youtube.com/live2/$STREAM_KEY"
            },
            {
                "name": "Custom RTMP",
                "rtmp_url": "your_custom_rtmp_url/$STREAM_KEY"
            }
        ]
    }

    # Path to the platforms.json file
    platforms_file_path = os.path.join('config', 'platforms.json')

    # Check if the file exists
    if not os.path.exists(platforms_file_path):
        with open(platforms_file_path, 'w') as file:
            json.dump(platforms, file, indent=4)
        print(f"Initialized '{platforms_file_path}' with default data.")
    else:
        print(f"'{platforms_file_path}' already exists. No changes made.")

if __name__ == "__main__":
    initialize_platforms()

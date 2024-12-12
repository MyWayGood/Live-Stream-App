import os
import json
import uuid

class Streamer:
    def __init__(self, config_file='config/stream_keys.json', platform=None):
        self.config_file = config_file
        self.platform = platform
        self.stream_keys = self.load_stream_keys()

    # Load stream keys from JSON file
    def load_stream_keys(self):
        if not os.path.exists(self.config_file):
            print(f"Stream keys file '{self.config_file}' not found. Please check your setup.")
            return {}
        with open(self.config_file, 'r') as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                print("Error reading stream keys file. Please check the file format.")
                return {}

    # Save stream keys to JSON file
    def save_stream_keys(self):
        with open(self.config_file, 'w') as f:
            json.dump(self.stream_keys, f, indent=4)

    # Add a new stream key for a supported platform
    def add_stream_key(self, platform, stream_key):
        self.stream_keys[platform] = stream_key
        self.save_stream_keys()

    # Retrieve the stream key for a specific platform
    def retrieve_stream_key(self, platform):
        return self.stream_keys.get(platform, None)

    # Delete a stream key from the JSON file
    def delete_stream_key(self, platform):
        if platform in self.stream_keys:
            del self.stream_keys[platform]
            self.save_stream_keys()

    # Generate a new random stream key and save it
    def generate_stream_key(self, platform):
        new_key = str(uuid.uuid4()).replace('-', '')[:16]  # Generate 16-character key
        self.add_stream_key(platform, new_key)
        return new_key

    # Generate RTMP URL for a platform
    def generate_rtmp_url(self, platform):
        platform_rtmp_urls = {
            "Dailymotion": "rtmp://publish.dailymotion.com/live?stream_key=$STREAM_KEY",
            "Facebook": "rtmp://live-api-s.facebook.com:80/rtmp/$STREAM_KEY",
            "Instagram": "rtmp://live-upload.instagram.com:80/rtmp/$STREAM_KEY",
            "Kick": "rtmp://live.kick.com/app/$STREAM_KEY",
            "Rumble": "rtmp://live.rumble.com/$STREAM_KEY",
            "TikTok": "rtmp://live.tiktok.com/live/$STREAM_KEY",
            "Twitch": "rtmp://live.twitch.tv/app/$STREAM_KEY",
            "Vimeo": "rtmp://live.vimeo.com/app/$STREAM_KEY",
            "X (Twitter)": "rtmp://live.pscp.tv:80/x/$STREAM_KEY",
            "YouTube": "rtmp://a.rtmp.youtube.com/live2/$STREAM_KEY",
        }

        # Custom RTMP URL support
        if platform not in platform_rtmp_urls and platform not in self.stream_keys:
            print(f"Unsupported platform or custom RTMP URL '{platform}'.")
            return None

        stream_key = self.retrieve_stream_key(platform)
        if stream_key:
            rtmp_url = platform_rtmp_urls.get(platform, platform)  # Custom platform URL is treated as RTMP base
            return rtmp_url.replace("$STREAM_KEY", stream_key)
        else:
            print(f"Stream key for platform '{platform}' not found.")
            return None

    # Start live stream
    def start_stream(self, platform):
        rtmp_url = self.generate_rtmp_url(platform)
        if rtmp_url:
            print(f"Starting live stream for {platform} with RTMP URL: {rtmp_url}")
            # Here you'd call FFmpeg to start streaming
            # Example: os.system(f"ffmpeg -i input.mp4 -f flv {rtmp_url}")
        else:
            print(f"Cannot start stream. RTMP URL for {platform} could not be generated.")

    # Stop live stream (Placeholder method)
    def stop_stream(self):
        print("Stopping live stream...")
        # Logic to stop the streaming process

# Testing the functionality
if __name__ == '__main__':
    # Example usage of Streamer class
    streamer = Streamer()

    # Add stream keys for multiple platforms
    streamer.add_stream_key('YouTube', 'your_youtube_stream_key')
    streamer.add_stream_key('Facebook', 'your_facebook_stream_key')

    # Generate RTMP URLs for platforms
    print("YouTube RTMP URL:", streamer.generate_rtmp_url('YouTube'))
    print("Facebook RTMP URL:", streamer.generate_rtmp_url('Facebook'))

    # Generate a new stream key for a custom platform
    print("New stream key for Vimeo:", streamer.generate_stream_key('Vimeo'))

    # Start and stop stream example
    streamer.start_stream('YouTube')
    streamer.stop_stream()

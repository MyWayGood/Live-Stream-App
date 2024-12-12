import json
import os
from datetime import datetime, timedelta

class Scheduler:
    def __init__(self):
        """Initialize the Scheduler with an empty schedule and load existing data."""
        self.schedule_file = 'config/scheduled_streams.json'
        self.scheduled_streams = []
        self.load_scheduled_streams()

    def load_scheduled_streams(self):
        """Load scheduled streams from a JSON file."""
        try:
            if os.path.exists(self.schedule_file):
                with open(self.schedule_file, 'r') as file:
                    self.scheduled_streams = json.load(file)
                    print(f"Loaded scheduled streams: {self.scheduled_streams}")
            else:
                print(f"No scheduled streams found. Creating new schedule.")
                self.scheduled_streams = []
        except json.JSONDecodeError as e:
            print(f"Error loading scheduled streams: {e}")
            self.scheduled_streams = []

    def save_scheduled_streams(self):
        """Save the current scheduled streams to a JSON file."""
        try:
            with open(self.schedule_file, 'w') as file:
                json.dump(self.scheduled_streams, file, indent=4)
                print(f"Scheduled streams saved: {self.scheduled_streams}")
        except Exception as e:
            print(f"Error saving scheduled streams: {e}")

    def schedule_stream(self, video_file, start_time, platform, stream_key):
        """
        Schedule a live stream.
        
        :param video_file: Path to the video file.
        :param start_time: Scheduled time for the stream.
        :param platform: Streaming platform (e.g., YouTube, Twitch).
        :param stream_key: The stream key for the platform.
        """
        stream_data = {
            "video_file": video_file,
            "start_time": start_time.strftime("%Y-%m-%d %H:%M:%S"),
            "platform": platform,
            "stream_key": stream_key
        }
        self.scheduled_streams.append(stream_data)
        print(f"Scheduled stream: {stream_data}")
        self.save_scheduled_streams()

    def get_upcoming_streams(self):
        """
        Retrieve streams that are scheduled to start in the future.
        :return: List of upcoming streams.
        """
        current_time = datetime.now()
        upcoming_streams = [stream for stream in self.scheduled_streams if datetime.strptime(stream["start_time"], "%Y-%m-%d %H:%M:%S") > current_time]
        return upcoming_streams

    def remove_past_streams(self):
        """Remove streams from the schedule that have already started or are in the past."""
        current_time = datetime.now()
        self.scheduled_streams = [stream for stream in self.scheduled_streams if datetime.strptime(stream["start_time"], "%Y-%m-%d %H:%M:%S") > current_time]
        self.save_scheduled_streams()

    def start_scheduled_stream(self, ffmpeg_handler):
        """
        Check if any stream is scheduled to start now or soon, and start it.
        :param ffmpeg_handler: Instance of FFMpegHandler to start the stream.
        """
        current_time = datetime.now()
        for stream in self.scheduled_streams:
            start_time = datetime.strptime(stream["start_time"], "%Y-%m-%d %H:%M:%S")
            if start_time <= current_time <= (start_time + timedelta(minutes=5)):
                print(f"Starting scheduled stream for {stream['platform']} at {stream['start_time']}")
                ffmpeg_handler.live_stream(stream['platform'], stream['stream_key'])
                self.scheduled_streams.remove(stream)
                self.save_scheduled_streams()
                break

    def cancel_scheduled_stream(self, start_time):
        """
        Cancel a stream that is scheduled for a specific start time.
        
        :param start_time: The time the stream was scheduled for.
        """
        self.scheduled_streams = [stream for stream in self.scheduled_streams if stream["start_time"] != start_time]
        print(f"Cancelled stream scheduled for {start_time}")
        self.save_scheduled_streams()

# Example usage:
if __name__ == "__main__":
    scheduler = Scheduler()
    scheduler.schedule_stream("example.mp4", datetime.now() + timedelta(hours=1), "YouTube", "example_stream_key")
    upcoming = scheduler.get_upcoming_streams()
    print(f"Upcoming streams: {upcoming}")

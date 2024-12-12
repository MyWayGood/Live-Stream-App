import os
import json
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.spinner import Spinner
from kivy.uix.image import Image
from kivy.uix.textinput import TextInput
from kivy.uix.checkbox import CheckBox
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.layout import Layout
from kivy.clock import Clock

from src.ffmpeg_handler import FFMpegHandler
from src.scheduler import Scheduler
from src.ui_components import SettingsPopup, CustomDatePicker, TimeInput
from src.streamer import Streamer

# Constants for file paths
CONFIG_PATH = 'config/settings.json'
STREAM_KEYS_PATH = 'config/stream_keys.json'
SCHEDULED_STREAMS_PATH = 'config/scheduled_streams.json'


class MainScreen(BoxLayout):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        
        self.config = {}
        self.stream_keys = {}
        self.ffmpeg_handler = None
        self.scheduler = Scheduler()

        # Load configurations
        self.load_config()
        self.load_stream_keys()

    def load_config(self):
        """Load app configuration settings from config/settings.json."""
        try:
            with open(CONFIG_PATH, 'r') as config_file:
                self.config = json.load(config_file)
                print(f"Loaded configurations: {self.config}")
        except FileNotFoundError:
            print("Configuration file not found. Please check your setup.")
    
    def load_stream_keys(self):
        """Load stream keys from config/stream_keys.json."""
        try:
            with open(STREAM_KEYS_PATH, 'r') as keys_file:
                self.stream_keys = json.load(keys_file)
                print(f"Loaded stream keys: {self.stream_keys}")
        except FileNotFoundError:
            print("Stream keys file not found. Please check your setup.")
    
    def start_stream(self):
        """Starts the live stream with FFmpeg using selected platform and stream key."""
        platform = self.ids.platform_spinner.text
        stream_key = self.ids.stream_key_input.text
        rtmp_url = self.config['platforms'].get(platform, {}).get('rtmp_url', '')

        if not stream_key:
            print("Stream key is missing.")
            return

        stream_url = rtmp_url.replace("$STREAM_KEY", stream_key)

        if stream_url:
            # Start streaming using FFmpeg
            self.ffmpeg_handler = FFMpegHandler(input_file='input.mp4', output_file=stream_url)
            self.ffmpeg_handler.start_stream()
            print(f"Streaming started to {stream_url}")
        else:
            print("Invalid platform or RTMP URL.")

    def stop_stream(self):
        """Stops the currently running live stream."""
        if self.ffmpeg_handler:
            self.ffmpeg_handler.stop_stream()
            print("Streaming stopped.")
    
    def preview_stream(self):
        """Displays a live stream preview."""
        print("Showing live preview.")
        self.ids.stream_preview.source = 'assets/preview_image.jpg'

    def stop_preview(self):
        """Stops the live stream preview."""
        print("Live preview stopped.")
        self.ids.stream_preview.source = 'assets/placeholder.jpg'
    
    def open_settings(self):
        """Opens the settings popup to adjust app configurations."""
        settings_popup = SettingsPopup()
        settings_popup.open()

    def schedule_stream(self):
        """Schedules a live stream based on the selected date and time."""
        date = self.ids.date_picker.text
        time = self.ids.time_input.text
        if date and time:
            scheduled_time = f"{date} {time}"
            self.scheduler.add_stream(scheduled_time, self.start_stream)
            print(f"Stream scheduled for {scheduled_time}")
        else:
            print("Invalid date or time.")
    
    def cancel_scheduled_streams(self):
        """Cancels all scheduled streams."""
        self.scheduler.cancel_all_streams()
        print("All scheduled streams have been canceled.")


class LiveStreamApp(App):
    def build(self):
        """Builds the main UI layout for the app."""
        return MainScreen()

    def on_start(self):
        """Called when the app starts. Loads scheduled streams."""
        print("App started, loading initial data...")
        Clock.schedule_once(self.load_scheduled_streams)

    def load_scheduled_streams(self, dt):
        """Loads the scheduled streams from the scheduler."""
        scheduled_streams = self.root.scheduler.load_scheduled_streams()
        print(f"Loaded scheduled streams: {scheduled_streams}")


if __name__ == '__main__':
    LiveStreamApp().run()

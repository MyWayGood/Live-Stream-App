import os
import json
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput
from src.ffmpeg_handler import FFMpegHandler  # Ensure this matches the correct class name
from src.streamer import Streamer
from src.scheduler import Scheduler
from src.ui_components import CustomButton, CustomLabel, DatePicker  # Ensure these components exist

class LiveStreamApp(App):
    def __init__(self, **kwargs):
        super(LiveStreamApp, self).__init__(**kwargs)
        self.settings_path = os.path.join("config", "settings.json")
        self.stream_keys_path = os.path.join("config", "stream_keys.json")
        self.scheduled_streams_path = os.path.join("config", "scheduled_streams.json")

        # Initialize components
        self.ffmpeg_handler = FFMpegHandler()
        self.streamer = Streamer("Example1", "Example2")  # Replace with actual values as needed
        self.scheduler = Scheduler()  # No arguments passed here

        # Load configuration files
        self.load_configurations()

    def load_configurations(self):
        # Load settings, stream keys, and scheduled streams files
        try:
            with open(self.settings_path, 'r') as f:
                self.settings = json.load(f)
            print(f"Loaded settings from {self.settings_path}")
        except FileNotFoundError:
            print(f"Configuration file '{self.settings_path}' not found. Please check your setup.")

        try:
            with open(self.stream_keys_path, 'r') as f:
                self.stream_keys = json.load(f)
            print(f"Loaded stream keys from {self.stream_keys_path}")
        except FileNotFoundError:
            print(f"Stream keys file '{self.stream_keys_path}' not found. Please check your setup.")

        try:
            with open(self.scheduled_streams_path, 'r') as f:
                self.scheduled_streams = json.load(f)
            print(f"Loaded scheduled streams from {self.scheduled_streams_path}")
        except FileNotFoundError:
            print(f"Scheduled streams file '{self.scheduled_streams_path}' not found. Please check your setup.")

    def build(self):
        # Create the main interface using Kivy components
        main_layout = BoxLayout(orientation='vertical')

        # Add a label and buttons for actions
        title_label = CustomLabel(text="Live Streaming Application")
        main_layout.add_widget(title_label)

        start_button = CustomButton(text="Start Stream", on_press=self.start_stream)
        stop_button = CustomButton(text="Stop Stream", on_press=self.stop_stream)
        schedule_button = CustomButton(text="Schedule Stream", on_press=self.open_schedule_popup)

        main_layout.add_widget(start_button)
        main_layout.add_widget(stop_button)
        main_layout.add_widget(schedule_button)

        return main_layout

    def start_stream(self, instance):
        print("Starting stream...")
        self.streamer.start_stream()

    def stop_stream(self, instance):
        print("Stopping stream...")
        self.streamer.stop_stream()

    def open_schedule_popup(self, instance):
        # Popup for scheduling streams
        popup_layout = BoxLayout(orientation='vertical')
        date_input = DatePicker()
        popup_layout.add_widget(date_input)

        stream_key_input = TextInput(hint_text="Enter Stream Key")
        popup_layout.add_widget(stream_key_input)

        submit_button = Button(text="Schedule", on_press=lambda x: self.schedule_stream(date_input.date, stream_key_input.text))
        popup_layout.add_widget(submit_button)

        popup = Popup(title="Schedule Stream", content=popup_layout, size_hint=(0.8, 0.8))
        popup.open()

    def schedule_stream(self, date, stream_key):
        print(f"Scheduling stream on {date} with key {stream_key}")
        self.scheduler.add_scheduled_stream(date, stream_key)

    def on_stop(self):
        print("Application is stopping. Cleaning up resources...")
        self.streamer.stop_stream()


if __name__ == '__main__':
    LiveStreamApp().run()

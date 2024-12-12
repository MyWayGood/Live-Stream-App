import os
import json
from kivy.uix.screenmanager import Screen
from kivy.uix.filechooser import FileChooserListView
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class VideoManager(Screen):
    def __init__(self, **kwargs):
        super(VideoManager, self).__init__(**kwargs)
        self.scheduled_videos_file = os.path.join('config', 'scheduled_videos.json')
        self.uploaded_videos_dir = os.path.join('media', 'uploaded-videos')
        self.downloaded_videos_dir = os.path.join('media', 'downloaded-videos')
        self.load_scheduled_videos()

    def load_scheduled_videos(self):
        """Load the scheduled videos from the JSON file."""
        if os.path.exists(self.scheduled_videos_file):
            with open(self.scheduled_videos_file, 'r') as file:
                self.scheduled_videos = json.load(file)
        else:
            self.scheduled_videos = []

    def save_scheduled_videos(self):
        """Save the updated scheduled videos list to the JSON file."""
        with open(self.scheduled_videos_file, 'w') as file:
            json.dump(self.scheduled_videos, file, indent=4)

    def preview_video(self, video_path):
        """Preview the selected video using FFPlay."""
        if os.path.exists(video_path):
            os.system(f'ffplay "{video_path}"')
        else:
            self.show_error_popup(f"Video not found: {video_path}")

    def edit_video_schedule(self, video_id):
        """Open the schedule for the selected video for editing."""
        for video in self.scheduled_videos:
            if video['id'] == video_id:
                # Load the schedule data into the schedule UI for editing
                self.manager.current = 'schedule'
                self.manager.get_screen('schedule').load_schedule(video)
                break

    def delete_video_schedule(self, video_id):
        """Remove the selected video from the schedule."""
        self.scheduled_videos = [v for v in self.scheduled_videos if v['id'] != video_id]
        self.save_scheduled_videos()
        self.load_scheduled_videos()
        self.show_info_popup("Video schedule deleted successfully.")

    def upload_video(self):
        """Open file chooser to upload a new video to the uploaded-videos directory."""
        filechooser = FileChooserListView(path='/', filters=['*.mp4'])
        filechooser.bind(on_submit=self._upload_video_callback)
        popup = Popup(title='Upload Video', content=filechooser, size_hint=(0.9, 0.9))
        popup.open()

    def _upload_video_callback(self, filechooser, selection, *args):
        if selection:
            video_path = selection[0]
            video_name = os.path.basename(video_path)
            target_path = os.path.join(self.uploaded_videos_dir, video_name)
            os.rename(video_path, target_path)
            self.show_info_popup(f"Video uploaded successfully: {video_name}")
    
    def download_video(self, video_url):
        """Download a video from a YouTube URL using YT-DLP."""
        os.system(f'yt-dlp -o "{self.downloaded_videos_dir}/%(title)s.%(ext)s" {video_url}')
        self.show_info_popup("Video downloaded successfully.")

    def show_info_popup(self, message):
        """Display a popup with an information message."""
        content = BoxLayout(orientation='vertical')
        content.add_widget(Label(text=message))
        close_button = Button(text='Close', size_hint=(1, 0.2))
        content.add_widget(close_button)
        popup = Popup(title='Info', content=content, size_hint=(0.8, 0.4))
        close_button.bind(on_release=popup.dismiss)
        popup.open()

    def show_error_popup(self, message):
        """Display a popup with an error message."""
        content = BoxLayout(orientation='vertical')
        content.add_widget(Label(text=message, color=(1, 0, 0, 1)))
        close_button = Button(text='Close', size_hint=(1, 0.2))
        content.add_widget(close_button)
        popup = Popup(title='Error', content=content, size_hint=(0.8, 0.4))
        close_button.bind(on_release=popup.dismiss)
        popup.open()

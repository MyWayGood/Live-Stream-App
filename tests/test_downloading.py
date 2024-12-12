import unittest
import os
import subprocess
import json

# Assuming yt-dlp executable path is set in the environment or is accessible globally
YT_DLP_COMMAND = "yt-dlp"
DOWNLOAD_DIR = "LiveStreamApp/media/downloaded-videos/"

class TestDownloading(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        # Ensure the download directory exists
        if not os.path.exists(DOWNLOAD_DIR):
            os.makedirs(DOWNLOAD_DIR)
    
    def test_download_video(self):
        """Test downloading a single video using YT-DLP."""
        video_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"  # Example YouTube video URL
        
        # Command to download the video
        command = [YT_DLP_COMMAND, video_url, "-o", os.path.join(DOWNLOAD_DIR, '%(title)s.%(ext)s')]
        
        # Run the command and check for errors
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
        # Check if the download was successful
        self.assertEqual(result.returncode, 0, f"Failed to download video. Error: {result.stderr.decode()}")
        
        # Verify that the video is downloaded (check file existence)
        downloaded_files = os.listdir(DOWNLOAD_DIR)
        self.assertGreater(len(downloaded_files), 0, "No video files downloaded.")
    
    def test_download_playlist(self):
        """Test downloading an entire playlist using YT-DLP."""
        playlist_url = "https://www.youtube.com/playlist?list=PLw-VjHDlEOguHGfOvQr1O6fi3A5gO1hPH"  # Example playlist URL
        
        # Command to download the entire playlist
        command = [YT_DLP_COMMAND, playlist_url, "-o", os.path.join(DOWNLOAD_DIR, '%(playlist)s/%(title)s.%(ext)s')]
        
        # Run the command and check for errors
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
        # Check if the download was successful
        self.assertEqual(result.returncode, 0, f"Failed to download playlist. Error: {result.stderr.decode()}")
        
        # Verify that the playlist videos are downloaded (check directory and files)
        downloaded_files = os.listdir(DOWNLOAD_DIR)
        self.assertGreater(len(downloaded_files), 0, "No playlist files downloaded.")
    
    def test_invalid_url(self):
        """Test that an invalid URL is handled gracefully."""
        invalid_url = "https://www.invalid-url.com"
        
        # Command to download with an invalid URL
        command = [YT_DLP_COMMAND, invalid_url, "-o", os.path.join(DOWNLOAD_DIR, '%(title)s.%(ext)s')]
        
        # Run the command and check for errors
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
        # Check if the command returns a non-zero exit code
        self.assertNotEqual(result.returncode, 0, "Invalid URL was not handled correctly.")
        
        # Ensure that no files were downloaded
        downloaded_files = os.listdir(DOWNLOAD_DIR)
        self.assertEqual(len(downloaded_files), 0, "Files were downloaded from an invalid URL.")
    
    @classmethod
    def tearDownClass(cls):
        # Optionally, clean up the downloaded files after testing
        for root, dirs, files in os.walk(DOWNLOAD_DIR):
            for file in files:
                os.remove(os.path.join(root, file))

if __name__ == "__main__":
    unittest.main()

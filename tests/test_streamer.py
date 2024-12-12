import unittest
from unittest.mock import patch, MagicMock
from src.streamer import Streamer

class TestStreamer(unittest.TestCase):

    def setUp(self):
        # Set up any necessary variables or mocks
        self.streamer = Streamer()
        self.stream_key = "sample_stream_key"
        self.platform_rtmp_url = "rtmp://live.youtube.com/app"
        self.video_path = "test_video.mp4"
        self.bitrate = "4000k"
        self.resolution = "1280x720"
    
    @patch('src.streamer.FFmpeg')  # Mock FFmpeg command
    def test_start_stream_success(self, mock_ffmpeg):
        """
        Test that starting a stream works as expected with correct FFmpeg command.
        """
        # Set up the mock for FFmpeg
        mock_ffmpeg.run = MagicMock(return_value=True)
        
        # Call start stream method
        result = self.streamer.start_stream(
            platform_rtmp_url=self.platform_rtmp_url,
            stream_key=self.stream_key,
            video_path=self.video_path,
            bitrate=self.bitrate,
            resolution=self.resolution
        )
        
        # Assert that the FFmpeg command was called correctly
        mock_ffmpeg.run.assert_called_once()
        self.assertTrue(result, "Stream should start successfully")
    
    @patch('src.streamer.FFmpeg')
    def test_start_stream_failure(self, mock_ffmpeg):
        """
        Test that starting a stream fails if FFmpeg encounters an issue.
        """
        # Simulate FFmpeg failure
        mock_ffmpeg.run = MagicMock(return_value=False)
        
        # Call start stream method
        result = self.streamer.start_stream(
            platform_rtmp_url=self.platform_rtmp_url,
            stream_key=self.stream_key,
            video_path=self.video_path,
            bitrate=self.bitrate,
            resolution=self.resolution
        )
        
        # Assert that the result is False indicating failure
        self.assertFalse(result, "Stream should fail due to FFmpeg issue")
    
    @patch('src.streamer.FFmpeg')
    def test_stop_stream(self, mock_ffmpeg):
        """
        Test that stopping the stream terminates the FFmpeg process.
        """
        # Simulate stream running
        mock_ffmpeg.process = MagicMock()
        self.streamer.ffmpeg_process = mock_ffmpeg.process
        
        # Call stop stream
        self.streamer.stop_stream()
        
        # Assert that the FFmpeg process was terminated
        self.streamer.ffmpeg_process.terminate.assert_called_once()
    
    @patch('src.streamer.FFmpeg')
    def test_invalid_stream_key(self, mock_ffmpeg):
        """
        Test that the stream fails with an invalid stream key.
        """
        # Invalid stream key format
        invalid_key = ""
        
        # Call start stream method with invalid key
        result = self.streamer.start_stream(
            platform_rtmp_url=self.platform_rtmp_url,
            stream_key=invalid_key,
            video_path=self.video_path,
            bitrate=self.bitrate,
            resolution=self.resolution
        )
        
        # Assert that the stream does not start
        self.assertFalse(result, "Stream should fail with an invalid stream key")
    
    @patch('src.streamer.FFmpeg')
    def test_monitor_stream_success(self, mock_ffmpeg):
        """
        Test that the stream monitoring process works as expected.
        """
        # Simulate stream running and returning valid data
        mock_ffmpeg.process = MagicMock()
        mock_ffmpeg.process.poll = MagicMock(return_value=None)  # Simulate process running
        
        # Call monitor stream
        result = self.streamer.monitor_stream()
        
        # Assert that the monitoring is successful
        self.assertTrue(result, "Stream should be running successfully")
    
    @patch('src.streamer.FFmpeg')
    def test_monitor_stream_failure(self, mock_ffmpeg):
        """
        Test that the stream monitoring fails when the process ends unexpectedly.
        """
        # Simulate stream process that has ended
        mock_ffmpeg.process = MagicMock()
        mock_ffmpeg.process.poll = MagicMock(return_value=1)  # Simulate process termination
        
        # Call monitor stream
        result = self.streamer.monitor_stream()
        
        # Assert that monitoring fails
        self.assertFalse(result, "Stream monitoring should fail when process ends")

if __name__ == '__main__':
    unittest.main()

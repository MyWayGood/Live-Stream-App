import unittest
from unittest.mock import patch, call
import subprocess
from ffmpeg_handler import convert_video_format, set_bitrate, set_resolution, live_stream

class TestFFmpegHandler(unittest.TestCase):

    @patch('subprocess.run')
    def test_convert_video_format(self, mock_run):
        # Mock the behavior of subprocess.run to simulate FFmpeg execution
        mock_run.return_value = subprocess.CompletedProcess(args=['ffmpeg'], returncode=0)
        
        # Test converting an MP4 video to FLV format
        input_file = 'test_video.mp4'
        output_format = 'flv'
        output_file = convert_video_format(input_file, output_format)
        
        # Check that the subprocess.run was called with the correct FFmpeg command
        mock_run.assert_called_once_with(['ffmpeg', '-i', input_file, '-c:v', 'libx264', '-c:a', 'aac', '-b:a', '128k', '-ac', '2', output_file], check=True)
        self.assertEqual(output_file, 'test_video_converted.flv')

    @patch('subprocess.run')
    def test_set_bitrate(self, mock_run):
        # Mock the behavior of subprocess.run to simulate FFmpeg execution
        mock_run.return_value = subprocess.CompletedProcess(args=['ffmpeg'], returncode=0)
        
        # Test setting a custom bitrate for the live stream
        input_file = 'test_video.mp4'
        bitrate = '2000k'  # 2Mbps
        
        set_bitrate(input_file, bitrate)
        
        # Check that the subprocess.run was called with the correct FFmpeg command
        mock_run.assert_called_once_with(['ffmpeg', '-i', input_file, '-b:v', bitrate, 'output_bitrate_test.mp4'], check=True)

    @patch('subprocess.run')
    def test_set_resolution(self, mock_run):
        # Mock the behavior of subprocess.run to simulate FFmpeg execution
        mock_run.return_value = subprocess.CompletedProcess(args=['ffmpeg'], returncode=0)
        
        # Test setting video resolution for the live stream
        input_file = 'test_video.mp4'
        resolution = '1280x720'  # HD
        
        set_resolution(input_file, resolution)
        
        # Check that the subprocess.run was called with the correct FFmpeg command
        mock_run.assert_called_once_with(['ffmpeg', '-i', input_file, '-vf', f'scale={resolution}', 'output_resolution_test.mp4'], check=True)

    @patch('subprocess.run')
    def test_live_stream(self, mock_run):
        # Mock the behavior of subprocess.run to simulate FFmpeg execution
        mock_run.return_value = subprocess.CompletedProcess(args=['ffmpeg'], returncode=0)
        
        # Test the live streaming functionality
        input_file = 'test_video.mp4'
        stream_url = 'rtmp://live.twitch.tv/app/$STREAM_KEY'
        
        live_stream(input_file, stream_url)
        
        # Check that the subprocess.run was called with the correct FFmpeg live stream command
        mock_run.assert_called_once_with(['ffmpeg', '-re', '-i', input_file, '-c:v', 'libx264', '-c:a', 'aac', '-f', 'flv', stream_url], check=True)

if __name__ == '__main__':
    unittest.main()

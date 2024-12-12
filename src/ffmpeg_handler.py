import subprocess
import os

class FFMpegHandler:
    def __init__(self, input_file=None, output_file=None, bitrate='5000k', resolution='1920x1080'):
        """
        Initializes the FFMpegHandler class.

        :param input_file: Path to the input file.
        :param output_file: Path to the output file.
        :param bitrate: Bitrate for the output stream, default is '5000k'.
        :param resolution: Resolution for the output stream, default is '1920x1080' (Full HD).
        """
        self.input_file = input_file
        self.output_file = output_file
        self.bitrate = bitrate
        self.resolution = resolution

    def convert(self, format="mp4"):
        """
        Converts the input file to the desired output format using FFmpeg.

        :param format: The target format (e.g., mp4, flv, mkv, etc.).
        """
        if not self.input_file or not self.output_file:
            print("Input or Output file is missing.")
            return

        # Build FFmpeg conversion command
        cmd = [
            "ffmpeg",
            "-i", self.input_file,
            "-b:v", self.bitrate,
            "-s", self.resolution,
            "-y",  # Overwrite output file if it exists
            f"{self.output_file}.{format}"
        ]

        try:
            print(f"Converting {self.input_file} to {self.output_file}.{format}...")
            subprocess.run(cmd, check=True)
            print(f"Conversion successful: {self.output_file}.{format}")
        except subprocess.CalledProcessError as e:
            print(f"Error during conversion: {str(e)}")

    def stream_to_rtmp(self, rtmp_url, stream_key):
        """
        Streams the input file to the RTMP URL (typically for live streaming).

        :param rtmp_url: RTMP server URL for streaming.
        :param stream_key: The stream key for the platform (e.g., YouTube, Twitch).
        """
        if not self.input_file:
            print("Input file is missing.")
            return

        # Combine RTMP URL with the stream key
        full_rtmp_url = f"{rtmp_url}/{stream_key}"

        # FFmpeg command for live streaming to RTMP
        cmd = [
            "ffmpeg",
            "-re",  # Real-time flag for live streaming
            "-i", self.input_file,
            "-c:v", "libx264",  # Use x264 video codec
            "-b:v", self.bitrate,
            "-s", self.resolution,
            "-f", "flv",  # Use FLV container format for RTMP
            full_rtmp_url
        ]

        try:
            print(f"Streaming to {full_rtmp_url}...")
            subprocess.run(cmd, check=True)
            print("Streaming finished.")
        except subprocess.CalledProcessError as e:
            print(f"Error during streaming: {str(e)}")

    def analyze_media_file(self):
        """
        Analyzes the input file for detailed media information such as codec, duration, bitrate, etc.

        :return: A dictionary with media information.
        """
        if not self.input_file:
            print("Input file is missing.")
            return {}

        cmd = [
            "ffmpeg",
            "-i", self.input_file,
            "-hide_banner"  # Suppress FFmpeg banner in output
        ]

        try:
            print(f"Analyzing media file: {self.input_file}")
            result = subprocess.run(cmd, stderr=subprocess.PIPE, text=True, check=False)
            media_info = result.stderr
            return self.parse_media_info(media_info)
        except subprocess.CalledProcessError as e:
            print(f"Error analyzing media file: {str(e)}")
            return {}

    def parse_media_info(self, info_string):
        """
        Parses media information from the FFmpeg output.

        :param info_string: Raw output from FFmpeg.
        :return: Parsed media information as a dictionary.
        """
        media_info = {}
        lines = info_string.splitlines()

        for line in lines:
            if "Duration" in line:
                media_info['Duration'] = line.split(",")[0].split(":")[1].strip()
            if "bitrate" in line:
                media_info['Bitrate'] = line.split(":")[1].strip()
            if "Stream" in line and "Video" in line:
                media_info['Video'] = line.split(":")[2].strip()
            if "Stream" in line and "Audio" in line:
                media_info['Audio'] = line.split(":")[2].strip()

        return media_info

    def extract_audio(self, audio_format="mp3"):
        """
        Extracts audio from the input file.

        :param audio_format: Format for the output audio file (default is mp3).
        """
        if not self.input_file or not self.output_file:
            print("Input or Output file is missing.")
            return

        output_audio = f"{self.output_file}.{audio_format}"

        # FFmpeg command to extract audio
        cmd = [
            "ffmpeg",
            "-i", self.input_file,
            "-q:a", "0",  # Best quality for audio
            "-map", "a",  # Map only the audio stream
            "-y",  # Overwrite if the output file exists
            output_audio
        ]

        try:
            print(f"Extracting audio to {output_audio}...")
            subprocess.run(cmd, check=True)
            print(f"Audio extraction successful: {output_audio}")
        except subprocess.CalledProcessError as e:
            print(f"Error during audio extraction: {str(e)}")


Live Stream - Windows App
Version: v1.0.0
Developer: Manikandan Govindan
Organization: SingleDawn Corp
Country: India, Tamil Nadu
Platform: Windows 10 and 11 (and above)
Website: avodtv.com

Overview

The Live Stream - Windows App is a powerful tool designed for managing and automating live streaming across various social media platforms. Built for efficiency, this application simplifies the process of scheduling, managing, and broadcasting live videos. The app leverages FFmpeg for advanced video processing and YT-DLP for downloading YouTube content, enabling seamless streaming to multiple platforms.

With user-friendly scheduling features, media file analysis, custom resolution/bitrate settings, and built-in live previews, this app offers a comprehensive solution for administrators looking to optimize their live streaming workflows.

Features

1. Automated Live Streaming

Stream videos to platforms like YouTube, Facebook, Instagram, Twitch, TikTok, Vimeo, Kick, Rumble, Dailymotion, and more.
Utilizes FFmpeg for high-performance live streaming.
Supports RTMP URLs for direct live streaming.

2. Video Format Conversion

Converts MP4 videos to the live stream-ready FLV format (libx264, AAC audio, 128k, 2 channels).
Leverages FFmpeg Commands for video processing and conversion.

3. Live Preview

Provides a live preview of your video stream using FFplay Commands.
Ensures the live stream setup is correct before going live.

4. Media File Analysis

Analyze media files to extract information like duration, codecs, resolution, and bitrate using FFprobe Commands.

5. Custom Bitrate Selection

Select from a range of bitrates to optimize streaming quality based on network conditions (1 Mbps to 25 Mbps).

6. Video Resolution Configuration

Configure resolutions for streaming, including SD (720x480), HD (1280x720), and FHD (1920x1080) using FFmpeg.

7. YouTube Video Downloader

Download individual YouTube videos or entire playlists using YT-DLP.
Downloads are saved in the downloaded-videos directory.

8. Stream Key Management

Manage, add, save, and generate RTMP URLs for all supported platforms.
Store stream keys securely in JSON files.

9. Scheduling Live Streams

Schedule live streams with a calendar interface (Flatpickr) to specify the date, start time, and end time.
Schedule videos using MP4 files or YouTube URLs.

10. File Management

Upload MP4 videos to the uploaded-videos directory.
Manage scheduled and downloaded videos in organized directories.

11. Custom RTMP URL

Add custom RTMP URLs to stream live on additional platforms not pre-configured in the app.
Installation
Prerequisites
Python 3.12.5 (will be installed automatically if not present)
Windows 10 or 11

Step 1: Download the App

Visit the official website and download the latest version of the Live Stream - Windows App.

Step 2: Extract the App Files

Extract the downloaded zip file and navigate to the root directory of the app.

Step 3: Run the Installation Script

Open a command prompt and navigate to the directory containing the app. Run the following command to install all dependencies:

install.bat

This will automatically:

Install Python 3.12.5 and other necessary modules like Kivy, FFmpeg, YT-DLP, and Flatpickr.

Set up the UI components and fonts.

Log the installation process in install.log.

Step 4: Run the App

After installation, run the app by double-clicking on main.exe (generated in the dist folder after using create_exe.bat).

Usage

1. Launch the App

Once the app is running, you'll see the main menu where you can manage your stream keys, schedule videos, preview streams, and more.

2. Manage Stream Keys

Use the "Stream Key" submenu to manage and store your RTMP stream keys for platforms like YouTube, Facebook, Instagram, and more. These keys will be securely stored in JSON files.

3. Schedule Live Streams

To schedule a stream:

Select the Schedule submenu.

Choose the video file or YouTube URL you want to broadcast.

Use the Flatpickr calendar to set the exact start and end times.

4. Video Conversion

The app automatically converts uploaded MP4 videos to a format compatible with live streaming using FFmpeg.

5. Preview the Stream

Before going live, use the Live Preview option to view a stream preview via FFplay.

6. Download YouTube Videos

To download videos from YouTube:

Go to the YouTube Downloader section.

Paste the YouTube video or playlist URL and choose your download preferences.

7. Adjust Stream Quality

You can manually set the bitrate (1 Mbps to 25 Mbps) and resolution (SD, HD, FHD) to match the quality required for your stream.

File Structure

LiveStreamApp/
├── assets/
│   ├── fonts/
│   ├── icons/
│   ├── logos/
│   └── thumbnails/
├── bin/
├── config/
├── docs/
├── logs/
├── media/
│   ├── uploaded-videos/
│   ├── downloaded-videos/
│   └── scheduled-videos/
├── dependencies/
├── scripts/
├── src/
├── tests/
├── main.py
└── create_exe.bat

System Requirements

Operating System: Windows 10 or 11 (64-bit)

Processor: Intel i3 or equivalent (minimum)

RAM: 4 GB (8 GB recommended for smooth performance)

Disk Space: At least 500 MB of free space for installation

Internet Connection: Required for live streaming and YouTube downloading

Terms of Service

Users must agree to the Terms of Service before installing and using the app. The terms are included in terms_of_service.pdf in the docs directory.

License

This app is licensed under the MIT License. See LICENSE.txt for more details.

Logs

The following log files are automatically created to track various processes:

install.log: Logs installation activities.

schedule.log: Logs scheduled events.

stream.log: Logs live streaming activities.

Contribution

Feel free to open issues or submit pull requests if you'd like to contribute to improving this project.

Support

For any issues or questions, please reach out via the official website: avodtv.com.
#!/bin/bash

# Function to display usage information
usage() {
    echo "Usage: $0 -p <platform> -k <stream_key> -f <video_file> -b <bitrate> -r <resolution>"
    echo "Example: $0 -p YouTube -k YOUR_STREAM_KEY -f /path/to/video.mp4 -b 5000k -r 1280x720"
    exit 1
}

# Function to get the RTMP URL based on the platform
get_rtmp_url() {
    case $1 in
        "YouTube")
            echo "rtmp://a.rtmp.youtube.com/live2/$2"
            ;;
        "Facebook")
            echo "rtmp://live-api-s.facebook.com:80/rtmp/$2"
            ;;
        "Instagram")
            echo "rtmp://live-upload.instagram.com:80/rtmp/$2"
            ;;
        "Twitch")
            echo "rtmp://live.twitch.tv/app/$2"
            ;;
        "Dailymotion")
            echo "rtmp://publish.dailymotion.com/live?stream_key=$2"
            ;;
        "TikTok")
            echo "rtmp://live.tiktok.com/live/$2"
            ;;
        "Vimeo")
            echo "rtmp://live.vimeo.com/app/$2"
            ;;
        "Kick")
            echo "rtmp://live.kick.com/app/$2"
            ;;
        "Rumble")
            echo "rtmp://live.rumble.com/$2"
            ;;
        "X")
            echo "rtmp://live.pscp.tv:80/x/$2"
            ;;
        *)
            echo "Unsupported platform: $1"
            exit 1
            ;;
    esac
}

# Parse command-line arguments
while getopts ":p:k:f:b:r:" opt; do
    case $opt in
        p) platform="$OPTARG" ;;
        k) stream_key="$OPTARG" ;;
        f) video_file="$OPTARG" ;;
        b) bitrate="$OPTARG" ;;
        r) resolution="$OPTARG" ;;
        *) usage ;;
    esac
done

# Validate inputs
if [ -z "$platform" ] || [ -z "$stream_key" ] || [ -z "$video_file" ] || [ -z "$bitrate" ] || [ -z "$resolution" ]; then
    usage
fi

if [ ! -f "$video_file" ]; then
    echo "Error: Video file '$video_file' not found."
    exit 1
fi

# Get the RTMP URL for the specified platform
rtmp_url=$(get_rtmp_url "$platform" "$stream_key")

# Construct and run the FFmpeg command
ffmpeg -re -i "$video_file" -c:v libx264 -b:v "$bitrate" -s "$resolution" -f flv "$rtmp_url"

# Check for errors
if [ $? -ne 0 ]; then
    echo "Error: Failed to stream video."
    exit 1
else
    echo "Live stream started successfully to $platform."
fi

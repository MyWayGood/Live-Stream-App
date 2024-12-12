#!/bin/bash

# Check for the correct number of arguments
if [ "$#" -ne 5 ]; then
    echo "Usage: $0 <platform> <stream_key> <input_video_file> <bitrate> <resolution>"
    exit 1
fi

# Assigning arguments to variables
PLATFORM=$1
STREAM_KEY=$2
INPUT_FILE=$3
BITRATE=$4
RESOLUTION=$5

# Function to generate the RTMP URL based on the platform
generate_rtmp_url() {
    case $PLATFORM in
        "Dailymotion")
            RTMP_URL="rtmp://publish.dailymotion.com/live?stream_key=$STREAM_KEY"
            ;;
        "Facebook")
            RTMP_URL="rtmp://live-api-s.facebook.com:80/rtmp/$STREAM_KEY"
            ;;
        "Instagram")
            RTMP_URL="rtmp://live-upload.instagram.com:80/rtmp/$STREAM_KEY"
            ;;
        "Kick")
            RTMP_URL="rtmp://live.kick.com/app/$STREAM_KEY"
            ;;
        "Rumble")
            RTMP_URL="rtmp://live.rumble.com/$STREAM_KEY"
            ;;
        "TikTok")
            RTMP_URL="rtmp://live.tiktok.com/live/$STREAM_KEY"
            ;;
        "Twitch")
            RTMP_URL="rtmp://live.twitch.tv/app/$STREAM_KEY"
            ;;
        "Vimeo")
            RTMP_URL="rtmp://live.vimeo.com/app/$STREAM_KEY"
            ;;
        "X")
            RTMP_URL="rtmp://live.pscp.tv:80/x/$STREAM_KEY"
            ;;
        "YouTube")
            RTMP_URL="rtmp://a.rtmp.youtube.com/live2/$STREAM_KEY"
            ;;
        *)
            echo "Invalid platform. Supported platforms: Dailymotion, Facebook, Instagram, Kick, Rumble, TikTok, Twitch, Vimeo, X, YouTube"
            exit 1
            ;;
    esac
}

# Function to configure video format using FFmpeg
configure_video_format() {
    OUTPUT_FILE="converted_stream.flv"
    ffmpeg -i "$INPUT_FILE" -c:v libx264 -b:v "$BITRATE"k -c:a aac -b:a 128k -ac 2 -s "$RESOLUTION" -f flv "$OUTPUT_FILE"
}

# Main script logic
generate_rtmp_url
configure_video_format

# Streaming the converted video to the RTMP URL
ffmpeg -re -i "$OUTPUT_FILE" -c copy -f flv "$RTMP_URL"

# Notify the user that the streaming process has started
echo "Streaming to $PLATFORM at $RTMP_URL with bitrate $BITRATE and resolution $RESOLUTION"


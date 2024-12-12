#!/bin/bash

# Define log directories and files
LOG_DIR="./logs"
INSTALL_LOG="$LOG_DIR/install.log"
STREAM_LOG="$LOG_DIR/stream.log"
ERROR_LOG="$LOG_DIR/error.log"

# Ensure log directory exists
mkdir -p "$LOG_DIR"

# Function to log info messages
log_info() {
    local message=$1
    echo "[INFO] $(date '+%Y-%m-%d %H:%M:%S') : $message" >> "$STREAM_LOG"
}

# Function to log errors
log_error() {
    local message=$1
    echo "[ERROR] $(date '+%Y-%m-%d %H:%M:%S') : $message" >> "$ERROR_LOG"
}

# Function to check for FFmpeg and other dependencies
check_dependencies() {
    command -v ffmpeg >/dev/null 2>&1 || {
        log_error "FFmpeg not found. Please install FFmpeg before proceeding."
        exit 1
    }
}

# Function to configure RTMP URL based on platform selection
configure_rtmp_url() {
    local platform=$1
    local stream_key=$2

    case $platform in
        "Dailymotion")
            RTMP_URL="rtmp://publish.dailymotion.com/live?stream_key=$stream_key"
            ;;
        "Facebook")
            RTMP_URL="rtmp://live-api-s.facebook.com:80/rtmp/$stream_key"
            ;;
        "Instagram")
            RTMP_URL="rtmp://live-upload.instagram.com:80/rtmp/$stream_key"
            ;;
        "Kick")
            RTMP_URL="rtmp://live.kick.com/app/$stream_key"
            ;;
        "Rumble")
            RTMP_URL="rtmp://live.rumble.com/$stream_key"
            ;;
        "TikTok")
            RTMP_URL="rtmp://live.tiktok.com/live/$stream_key"
            ;;
        "Twitch")
            RTMP_URL="rtmp://live.twitch.tv/app/$stream_key"
            ;;
        "Vimeo")
            RTMP_URL="rtmp://live.vimeo.com/app/$stream_key"
            ;;
        "X" | "Twitter")
            RTMP_URL="rtmp://live.pscp.tv:80/x/$stream_key"
            ;;
        "YouTube")
            RTMP_URL="rtmp://a.rtmp.youtube.com/live2/$stream_key"
            ;;
        *)
            log_error "Unsupported platform: $platform"
            exit 1
            ;;
    esac
}

# Function to execute FFmpeg commands for live streaming
start_live_stream() {
    local input_file=$1
    local platform=$2
    local stream_key=$3
    local resolution=$4
    local bitrate=$5

    # Configure RTMP URL based on platform and stream key
    configure_rtmp_url "$platform" "$stream_key"

    log_info "Starting live stream to $platform using RTMP URL: $RTMP_URL"

    # Execute FFmpeg live streaming command
    ffmpeg -re -i "$input_file" -vcodec libx264 -preset veryfast -maxrate "$bitrate" -bufsize "$bitrate" -pix_fmt yuv420p -s "$resolution" -acodec aac -ar 44100 -b:a 128k -f flv "$RTMP_URL" >> "$STREAM_LOG" 2>> "$ERROR_LOG"

    if [ $? -eq 0 ]; then
        log_info "Live stream to $platform completed successfully."
    else
        log_error "Live stream to $platform failed. Check the error log for more details."
        exit 1
    fi
}

# Main execution block
if [ $# -lt 5 ]; then
    echo "Usage: $0 <input_file> <platform> <stream_key> <resolution> <bitrate>"
    log_error "Invalid arguments provided."
    exit 1
fi

input_file=$1
platform=$2
stream_key=$3
resolution=$4
bitrate=$5

# Check for FFmpeg and dependencies
check_dependencies

# Start the live streaming process
start_live_stream "$input_file" "$platform" "$stream_key" "$resolution" "$bitrate"

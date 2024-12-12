#!/bin/bash

# Enable error handling - exit on error
set -e

# Logging setup
LOG_FILE="LiveStreamApp/logs/install.log"
exec > >(tee -i $LOG_FILE)
exec 2>&1

# Directories
PYTHON_DIR="LiveStreamApp/dependencies/Python-3.12.5"
PYINSTALLER_DIR="LiveStreamApp/dependencies/pyinstaller-6.10.0"
FFMPEG_DIR="LiveStreamApp/dependencies/ffmpeg-master-latest-win64-gpl"
KIVY_DIR="LiveStreamApp/dependencies/kivy-2.3.0"
YT_DLP_DIR="LiveStreamApp/dependencies/yt-dlp-2024.08.06"
FLATPICKR_DIR="LiveStreamApp/dependencies/flatpickr-4.6.13"
FONTS_DIR="LiveStreamApp/assets/fonts"

# Installation path
INSTALL_PATH="/usr/local/bin/livestreamapp"

# Functions for dependencies installation

install_python() {
    echo "Installing Python 3.12.5..."
    if [ -d "$PYTHON_DIR" ]; then
        tar -xvf "$PYTHON_DIR/Python-3.12.5.tar.gz" -C $INSTALL_PATH
        cd "$INSTALL_PATH/Python-3.12.5"
        ./configure --enable-optimizations
        make -j 8
        sudo make altinstall
        cd -
    else
        echo "Python directory not found!"
        exit 1
    fi
    echo "Python installed successfully."
}

install_pyinstaller() {
    echo "Installing PyInstaller 6.10.0..."
    if [ -d "$PYINSTALLER_DIR" ]; then
        unzip "$PYINSTALLER_DIR/pyinstaller-6.10.0.zip" -d $INSTALL_PATH
        cd "$INSTALL_PATH/pyinstaller-6.10.0"
        pip install .
        cd -
    else
        echo "PyInstaller directory not found!"
        exit 1
    fi
    echo "PyInstaller installed successfully."
}

install_ffmpeg() {
    echo "Installing FFmpeg..."
    if [ -d "$FFMPEG_DIR" ]; then
        unzip "$FFMPEG_DIR/ffmpeg-master-latest-win64-gpl.zip" -d $INSTALL_PATH
        sudo cp "$INSTALL_PATH/ffmpeg-master-latest-win64-gpl/bin/ffmpeg" /usr/local/bin
        sudo cp "$INSTALL_PATH/ffmpeg-master-latest-win64-gpl/bin/ffprobe" /usr/local/bin
    else
        echo "FFmpeg directory not found!"
        exit 1
    fi
    echo "FFmpeg installed successfully."
}

install_kivy() {
    echo "Installing Kivy 2.3.0..."
    if [ -d "$KIVY_DIR" ]; then
        unzip "$KIVY_DIR/kivy-2.3.0.zip" -d $INSTALL_PATH
        pip install "$INSTALL_PATH/kivy-2.3.0"
    else
        echo "Kivy directory not found!"
        exit 1
    fi
    echo "Kivy installed successfully."
}

install_yt_dlp() {
    echo "Installing YT-DLP..."
    if [ -d "$YT_DLP_DIR" ]; then
        unzip "$YT_DLP_DIR/yt-dlp-2024.08.06.zip" -d $INSTALL_PATH
        sudo cp "$INSTALL_PATH/yt-dlp-2024.08.06/yt-dlp" /usr/local/bin
    else
        echo "YT-DLP directory not found!"
        exit 1
    fi
    echo "YT-DLP installed successfully."
}

install_flatpickr() {
    echo "Installing Flatpickr..."
    if [ -d "$FLATPICKR_DIR" ]; then
        unzip "$FLATPICKR_DIR/flatpickr-4.6.13.zip" -d $INSTALL_PATH
        cp -r "$INSTALL_PATH/flatpickr-4.6.13/dist" "$INSTALL_PATH/assets"
    else
        echo "Flatpickr directory not found!"
        exit 1
    fi
    echo "Flatpickr installed successfully."
}

install_fonts() {
    echo "Installing Fonts..."
    if [ -d "$FONTS_DIR" ]; then
        sudo cp "$FONTS_DIR/Arial.ttf" /usr/share/fonts/
        sudo cp "$FONTS_DIR/Arial_Bold.ttf" /usr/share/fonts/
        fc-cache -f -v
    else
        echo "Fonts directory not found!"
        exit 1
    fi
    echo "Fonts installed successfully."
}

# Install all dependencies
echo "Starting installation of Live Stream App dependencies..."

install_python
install_pyinstaller
install_ffmpeg
install_kivy
install_yt_dlp
install_flatpickr
install_fonts

echo "All dependencies installed successfully."

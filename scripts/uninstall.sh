#!/bin/bash

# Live Stream Windows App Uninstaller

# Function to display a message
function display_message {
    echo -e "\n$1\n"
}

# Function to cleanup application directories
function cleanup_directories {
    display_message "Cleaning up application directories..."

    # Remove application directories and files
    rm -rf "$HOME/LiveStreamApp"
    rm -rf "$HOME/.local/share/LiveStreamApp"
    rm -rf "$HOME/.cache/LiveStreamApp"
    rm -rf "$HOME/.config/LiveStreamApp"

    display_message "Application directories cleaned up."
}

# Function to cleanup Python dependencies
function cleanup_dependencies {
    display_message "Cleaning up Python dependencies..."

    # Check if a virtual environment exists and remove it
    if [ -d "$HOME/LiveStreamApp/venv" ]; then
        rm -rf "$HOME/LiveStreamApp/venv"
        display_message "Virtual environment removed."
    else
        # Remove global Python packages if installed
        pip freeze | xargs pip uninstall -y
        display_message "Global Python dependencies uninstalled."
    fi
}

# Function to cleanup system-wide files
function cleanup_system_files {
    display_message "Cleaning up system-wide configuration files and logs..."

    # Remove any system-wide logs or configuration files if applicable
    rm -f /etc/LiveStreamApp.conf
    rm -f /var/log/LiveStreamApp.log

    display_message "System-wide files cleaned up."
}

# Main function to orchestrate cleanup
function main {
    display_message "Starting uninstallation of Live Stream Windows App..."

    cleanup_directories
    cleanup_dependencies
    cleanup_system_files

    display_message "Uninstallation complete. Thank you for using Live Stream Windows App!"
}

# Execute main function
main

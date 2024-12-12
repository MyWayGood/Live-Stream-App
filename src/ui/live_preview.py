import subprocess
import os
import time
import threading
import logger  # Assumed logger.py for logging events
import error_handler  # Assumed error_handler.py for managing errors

class LivePreview:
    def __init__(self, video_path):
        self.video_path = video_path
        self.ffplay_process = None
        self.preview_status = "stopped"
        self.log_file = "logs/stream.log"

    def start_preview(self):
        """Starts the live video preview using FFPlay."""
        try:
            if self.preview_status == "running":
                logger.log_event("Preview is already running.", self.log_file)
                return
            
            # FFPlay command to start video preview
            command = ["ffplay", "-autoexit", "-window_title", "Live Preview", self.video_path]
            
            # Start FFPlay as a subprocess
            self.ffplay_process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            self.preview_status = "running"
            logger.log_event(f"Started live preview for {self.video_path}.", self.log_file)
            
            # Update status in a separate thread to avoid blocking UI
            threading.Thread(target=self.update_status).start()
        except Exception as e:
            logger.log_event(f"Failed to start preview: {str(e)}", self.log_file)
            error_handler.handle_error(e)

    def pause_preview(self):
        """Pauses the live video preview."""
        try:
            if self.preview_status != "running":
                logger.log_event("No preview is running to pause.", self.log_file)
                return

            if self.ffplay_process:
                # Sending signal to pause FFPlay
                self.ffplay_process.send_signal(subprocess.signal.SIGSTOP)
                self.preview_status = "paused"
                logger.log_event(f"Paused live preview for {self.video_path}.", self.log_file)
        except Exception as e:
            logger.log_event(f"Failed to pause preview: {str(e)}", self.log_file)
            error_handler.handle_error(e)

    def stop_preview(self):
        """Stops the live video preview."""
        try:
            if self.preview_status == "stopped":
                logger.log_event("No preview is running to stop.", self.log_file)
                return
            
            if self.ffplay_process:
                self.ffplay_process.terminate()  # Terminate FFPlay process
                self.ffplay_process.wait()  # Ensure process is properly terminated
                self.preview_status = "stopped"
                logger.log_event(f"Stopped live preview for {self.video_path}.", self.log_file)
        except Exception as e:
            logger.log_event(f"Failed to stop preview: {str(e)}", self.log_file)
            error_handler.handle_error(e)

    def update_status(self):
        """Monitors and updates the status of the preview."""
        try:
            while self.ffplay_process and self.ffplay_process.poll() is None:
                time.sleep(1)
            
            # FFPlay process ended
            self.preview_status = "stopped"
            logger.log_event("Live preview has ended.", self.log_file)
        except Exception as e:
            logger.log_event(f"Error updating preview status: {str(e)}", self.log_file)
            error_handler.handle_error(e)

# Example usage
if __name__ == "__main__":
    live_preview = LivePreview("path/to/video.mp4")
    live_preview.start_preview()

    # Simulate user interaction
    time.sleep(10)  # Run preview for 10 seconds
    live_preview.pause_preview()
    time.sleep(5)  # Paused for 5 seconds
    live_preview.start_preview()
    time.sleep(10)  # Run for another 10 seconds
    live_preview.stop_preview()

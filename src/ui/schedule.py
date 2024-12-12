import json
import os
from datetime import datetime

# Path to the scheduled videos JSON file
SCHEDULED_VIDEOS_FILE = "LiveStreamApp/config/scheduled_videos.json"

# Helper function to load scheduled videos from the JSON file
def load_schedules():
    if os.path.exists(SCHEDULED_VIDEOS_FILE):
        with open(SCHEDULED_VIDEOS_FILE, 'r') as f:
            return json.load(f)
    return []

# Helper function to save scheduled videos to the JSON file
def save_schedules(schedules):
    with open(SCHEDULED_VIDEOS_FILE, 'w') as f:
        json.dump(schedules, f, indent=4)

# Function to schedule a video for live streaming
def schedule_video(video_path, schedule_date, start_time, end_time):
    schedules = load_schedules()
    
    # Validate the input
    if not os.path.exists(video_path):
        return {"error": "Video file does not exist."}
    
    try:
        schedule_datetime = datetime.strptime(f"{schedule_date} {start_time}", '%d:%m:%Y %H:%M:%S')
        end_datetime = datetime.strptime(f"{schedule_date} {end_time}", '%d:%m:%Y %H:%M:%S')
    except ValueError:
        return {"error": "Invalid date/time format."}

    if end_datetime <= schedule_datetime:
        return {"error": "End time must be after start time."}

    # Create a schedule entry
    schedule_entry = {
        "video_path": video_path,
        "schedule_date": schedule_date,
        "start_time": start_time,
        "end_time": end_time,
        "status": "scheduled"
    }
    
    # Add the new entry to the schedules list
    schedules.append(schedule_entry)
    
    # Save the updated schedules
    save_schedules(schedules)
    
    return {"success": "Video successfully scheduled."}

# Function to edit an existing schedule
def edit_schedule(index, new_video_path=None, new_schedule_date=None, new_start_time=None, new_end_time=None):
    schedules = load_schedules()

    if index < 0 or index >= len(schedules):
        return {"error": "Invalid schedule index."}
    
    if new_video_path:
        if not os.path.exists(new_video_path):
            return {"error": "Video file does not exist."}
        schedules[index]['video_path'] = new_video_path
    
    if new_schedule_date and new_start_time:
        try:
            new_schedule_datetime = datetime.strptime(f"{new_schedule_date} {new_start_time}", '%d:%m:%Y %H:%M:%S')
            schedules[index]['schedule_date'] = new_schedule_date
            schedules[index]['start_time'] = new_start_time
        except ValueError:
            return {"error": "Invalid date/time format."}

    if new_end_time:
        try:
            new_end_datetime = datetime.strptime(f"{schedules[index]['schedule_date']} {new_end_time}", '%d:%m:%Y %H:%M:%S')
            if new_end_datetime <= new_schedule_datetime:
                return {"error": "End time must be after start time."}
            schedules[index]['end_time'] = new_end_time
        except ValueError:
            return {"error": "Invalid date/time format."}

    # Save the updated schedules
    save_schedules(schedules)

    return {"success": "Schedule successfully updated."}

# Function to delete a scheduled video
def delete_schedule(index):
    schedules = load_schedules()

    if index < 0 or index >= len(schedules):
        return {"error": "Invalid schedule index."}
    
    del schedules[index]
    
    # Save the updated schedules
    save_schedules(schedules)
    
    return {"success": "Schedule successfully deleted."}

# Function to load existing schedules for display
def load_schedule():
    return load_schedules()

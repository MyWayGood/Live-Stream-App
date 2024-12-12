import unittest
from datetime import datetime, timedelta
from unittest.mock import patch, MagicMock
from src.scheduler import Scheduler  # Assuming your scheduling logic is inside a Scheduler class in scheduler.py

class TestScheduler(unittest.TestCase):

    def setUp(self):
        """Set up the Scheduler object before each test."""
        self.scheduler = Scheduler()

    @patch('src.scheduler.Flatpickr')  # Mocking Flatpickr for date/time selection
    def test_schedule_video_success(self, mock_flatpickr):
        """Test scheduling a video successfully with valid date/time."""
        # Set a mock for Flatpickr date picker with a valid date and time
        mock_flatpickr.get_selected_date.return_value = datetime.now() + timedelta(days=1)
        mock_flatpickr.get_start_time.return_value = "10:00:00"
        mock_flatpickr.get_end_time.return_value = "11:00:00"

        video_file = 'test_video.mp4'

        # Mock saving the schedule
        self.scheduler.save_schedule = MagicMock(return_value=True)

        # Call the method to schedule the video
        result = self.scheduler.schedule_video(video_file)

        # Assert that the video was successfully scheduled
        self.assertTrue(result)
        self.scheduler.save_schedule.assert_called_once()

    @patch('src.scheduler.Flatpickr')
    def test_schedule_video_past_date(self, mock_flatpickr):
        """Test that scheduling fails when trying to schedule a video with a past date."""
        # Set Flatpickr to return a past date
        mock_flatpickr.get_selected_date.return_value = datetime.now() - timedelta(days=1)
        mock_flatpickr.get_start_time.return_value = "10:00:00"
        mock_flatpickr.get_end_time.return_value = "11:00:00"

        video_file = 'test_video.mp4'

        # Call the method to schedule the video
        result = self.scheduler.schedule_video(video_file)

        # Assert that scheduling failed for past date
        self.assertFalse(result)

    @patch('src.scheduler.Flatpickr')
    def test_schedule_video_invalid_time(self, mock_flatpickr):
        """Test that scheduling fails when the end time is before the start time."""
        # Set start time after end time to test validation
        mock_flatpickr.get_selected_date.return_value = datetime.now() + timedelta(days=1)
        mock_flatpickr.get_start_time.return_value = "12:00:00"
        mock_flatpickr.get_end_time.return_value = "11:00:00"

        video_file = 'test_video.mp4'

        # Call the method to schedule the video
        result = self.scheduler.schedule_video(video_file)

        # Assert that scheduling failed due to invalid time
        self.assertFalse(result)

    def test_edit_schedule(self):
        """Test editing an already scheduled video."""
        # Assume that the original schedule exists
        original_schedule = {
            'video_file': 'test_video.mp4',
            'schedule_date': datetime.now() + timedelta(days=1),
            'start_time': '10:00:00',
            'end_time': '11:00:00'
        }

        # Mock loading the schedule
        self.scheduler.load_schedule = MagicMock(return_value=original_schedule)

        # New schedule details
        new_start_time = '09:00:00'
        new_end_time = '10:30:00'

        # Call the method to edit the schedule
        result = self.scheduler.edit_schedule('test_video.mp4', new_start_time, new_end_time)

        # Assert that the schedule was edited successfully
        self.assertTrue(result)

    def test_delete_schedule(self):
        """Test deleting a scheduled video."""
        # Mock loading an existing schedule
        self.scheduler.load_schedule = MagicMock(return_value=True)
        
        # Call the method to delete the schedule
        result = self.scheduler.delete_schedule('test_video.mp4')

        # Assert that the schedule was deleted successfully
        self.assertTrue(result)

    @patch('src.scheduler.Flatpickr')
    def test_schedule_overlap(self, mock_flatpickr):
        """Test that scheduling fails if it overlaps with another scheduled video."""
        # Existing schedule details
        existing_schedule = {
            'video_file': 'existing_video.mp4',
            'schedule_date': datetime.now() + timedelta(days=1),
            'start_time': '10:00:00',
            'end_time': '11:00:00'
        }

        # Mock loading an existing schedule
        self.scheduler.load_schedule = MagicMock(return_value=existing_schedule)

        # New schedule that overlaps with the existing one
        mock_flatpickr.get_selected_date.return_value = existing_schedule['schedule_date']
        mock_flatpickr.get_start_time.return_value = "10:30:00"
        mock_flatpickr.get_end_time.return_value = "11:30:00"

        video_file = 'new_video.mp4'

        # Call the method to schedule the new video
        result = self.scheduler.schedule_video(video_file)

        # Assert that scheduling failed due to overlap
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()

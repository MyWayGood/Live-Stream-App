// assets/flatpickr.js

// Ensure the DOM is fully loaded before initializing Flatpickr
document.addEventListener("DOMContentLoaded", function() {
    // Initialize Flatpickr for Date and Time input fields
    // Date Picker (DD:MM:YYYY)
    const dateInput = document.querySelector("#schedule-date");
    const timeInput = document.querySelector("#schedule-time");

    // Flatpickr configuration for date picker
    flatpickr(dateInput, {
        dateFormat: "d-m-Y",   // Date format DD:MM:YYYY
        defaultDate: new Date(), // Set default date as today
        allowInput: true,      // Allow manual input for date
        onChange: function(selectedDates, dateStr, instance) {
            console.log("Selected Date: " + dateStr); // Log the selected date for debugging
        }
    });

    // Flatpickr configuration for time picker
    flatpickr(timeInput, {
        enableTime: true,       // Enable time selection
        noCalendar: true,       // Disable calendar, only time picker
        dateFormat: "H:i:S",    // Time format HH:MM:SS
        time_24hr: true,        // Use 24-hour format
        defaultDate: "12:00:00", // Default time
        allowInput: true,       // Allow manual input for time
        onChange: function(selectedTimes, timeStr, instance) {
            console.log("Selected Time: " + timeStr); // Log the selected time for debugging
        }
    });
});

// Helper function to get formatted date and time
function getScheduledDateTime() {
    const dateValue = document.querySelector("#schedule-date").value;
    const timeValue = document.querySelector("#schedule-time").value;
    
    if (!dateValue || !timeValue) {
        alert("Please select both date and time for scheduling.");
        return null;
    }

    const scheduledDateTime = dateValue + " " + timeValue;
    console.log("Scheduled for: " + scheduledDateTime);
    return scheduledDateTime;
}

// Example of form submission or button click event to retrieve the scheduled date and time
document.querySelector("#schedule-submit").addEventListener("click", function() {
    const scheduledDateTime = getScheduledDateTime();
    if (scheduledDateTime) {
        alert("Scheduled Date & Time: " + scheduledDateTime);
        // Further code to handle scheduling logic (send to backend or save in JSON)
    }
});

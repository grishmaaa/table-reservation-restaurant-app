// Get the date and time input elements
const dateInput = document.querySelector('input[name="date"]');
const timeInput = document.querySelector('input[name="time"]');

// Add an event listener for date input changes
dateInput.addEventListener('change', function () {
    // Get the selected date
    const selectedDate = new Date(this.value);

    // Get today's date
    const today = new Date();

    // Check if the selected date is earlier than today's date
    if (selectedDate < today) {
        alert("Please select a future date.");
        this.value = ""; // Clear the input field
    }
});

// Add an event listener for time input changes
timeInput.addEventListener('change', function () {
    // Get the selected time
    const selectedTime = new Date(this.value).getTime();

    // Get the current time
    const currentTime = new Date().getTime();

    // Check if the selected time is earlier than the current time
    if (selectedTime < currentTime) {
        alert("Please select a future time.");
        this.value = ""; // Clear the input field
    }
});

document.addEventListener("DOMContentLoaded", function () {
    if (window.flatpickr) {
        // Start Time Picker
        flatpickr("#start_time", {
            enableTime: true,
            dateFormat: "Y-m-d H:i",            // value sent to backend
            altInput: true,                     // show user-friendly version
            altFormat: "F j, Y — h:i K",        // visible format (e.g., July 30, 2025 — 05:00 PM)
            allowInput: true,
            time_24hr: false,                   // use AM/PM format
            minuteIncrement: 15,
            defaultDate: new Date()
        });

        // End Time Picker (defaults to 1 hour later)
        const nowPlusOneHour = new Date();
        nowPlusOneHour.setHours(nowPlusOneHour.getHours() + 1);

        flatpickr("#end_time", {
            enableTime: true,
            dateFormat: "Y-m-d H:i",
            altInput: true,
            altFormat: "F j, Y — h:i K",
            allowInput: true,
            time_24hr: false,
            minuteIncrement: 15,
            defaultDate: nowPlusOneHour
        });
    }
});

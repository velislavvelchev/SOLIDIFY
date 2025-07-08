// static/js/init-flatpickr.js

document.addEventListener("DOMContentLoaded", function() {
    if (window.flatpickr) {
        flatpickr("#start_time", {
            enableTime: true,
            dateFormat: "Y-m-d H:i",
            allowInput: true
        });
        flatpickr("#end_time", {
            enableTime: true,
            dateFormat: "Y-m-d H:i",
            allowInput: true
        });
    }
});

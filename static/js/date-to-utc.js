document.addEventListener("DOMContentLoaded", function() {
    const form = document.getElementById("schedule-form");

    const startInput = document.getElementById("start_time");
    const endInput = document.getElementById("end_time");
    const startHidden = document.getElementById("start_time_utc");
    const endHidden = document.getElementById("end_time_utc");

    if (!form || !startInput || !endInput || !startHidden || !endHidden) {

        return;
    }

    form.addEventListener("submit", function(event) {

        if (startInput.value) {
            const localStart = new Date(startInput.value);
            const year = localStart.getUTCFullYear();
            const month = String(localStart.getUTCMonth() + 1).padStart(2, '0');
            const day = String(localStart.getUTCDate()).padStart(2, '0');
            const hour = String(localStart.getUTCHours()).padStart(2, '0');
            const minute = String(localStart.getUTCMinutes()).padStart(2, '0');
            startHidden.value = `${year}-${month}-${day}T${hour}:${minute}`;
        }
        if (endInput.value) {
            const localEnd = new Date(endInput.value);
            const year = localEnd.getUTCFullYear();
            const month = String(localEnd.getUTCMonth() + 1).padStart(2, '0');
            const day = String(localEnd.getUTCDate()).padStart(2, '0');
            const hour = String(localEnd.getUTCHours()).padStart(2, '0');
            const minute = String(localEnd.getUTCMinutes()).padStart(2, '0');
            endHidden.value = `${year}-${month}-${day}T${hour}:${minute}`;
        }
        console.log("start_time_utc:", startHidden.value, "end_time_utc:", endHidden.value);
    });
});

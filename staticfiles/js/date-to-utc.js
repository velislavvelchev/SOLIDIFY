document.addEventListener("DOMContentLoaded", function() {
    const form = document.getElementById("schedule-form");
    const input = document.getElementById("scheduled_time");
    const hidden = document.getElementById("scheduled_time_utc");
    if (!form || !input || !hidden) return;

    form.addEventListener("submit", function(event) {
        if (input.value) {
            const localDate = new Date(input.value);
            const year = localDate.getUTCFullYear();
            const month = String(localDate.getUTCMonth() + 1).padStart(2, '0');
            const day = String(localDate.getUTCDate()).padStart(2, '0');
            const hour = String(localDate.getUTCHours()).padStart(2, '0');
            const minute = String(localDate.getUTCMinutes()).padStart(2, '0');
            hidden.value = `${year}-${month}-${day}T${hour}:${minute}`;
            // Do NOT change input.value!
        }
    });
});

document.addEventListener('DOMContentLoaded', function () {
    const calendarEl = document.getElementById('calendar');
    if (!calendarEl) return;

    const calendar = new FullCalendar.Calendar(calendarEl, {
        initialView: 'dayGridMonth',
        timeZone: 'local',
        headerToolbar: {
            left: 'prev,next today',
            center: 'title',
            right: 'dayGridMonth,timeGridWeek,timeGridDay'
        },
        events: {
            url: '/schedule/api/events/',
            failure: function () {
            },
            success: function (events) {
            }
        },
        eventClick: function (info) {
            alert('Routine: ' + info.event.title + '\nStart Date: ' + info.event.start.toLocaleString());
        }
    });

    calendar.render();
});
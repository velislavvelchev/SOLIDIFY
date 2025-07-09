document.addEventListener('DOMContentLoaded', function () {
    const calendarEl = document.getElementById('calendar');
    if (!calendarEl) return;

    // Modal elements
    const modal = document.getElementById('eventDetailModal');
    const modalTitle = document.getElementById('modalTitle');
    const modalStart = document.getElementById('modalStart');
    const modalEnd = document.getElementById('modalEnd');
    const modalDescription = document.getElementById('modalDescription');
    const modalClose = document.getElementById('modalClose');


    const calendar = new FullCalendar.Calendar(calendarEl, {
        initialView: 'dayGridMonth',
        timeZone: 'local',
        headerToolbar: {
            left: 'prev,next today',
            center: 'title',
            right: 'dayGridMonth,timeGridWeek,timeGridDay'
        },
        editable: true, // <-- Allow drag-and-drop
        events: {
            url: '/schedule/api/events/',
            failure: function () { },
            success: function (events) { }
        },
        eventClick: function (info) {
            // Fill modal content
            modalTitle.textContent = info.event.title;
            modalStart.textContent = "Start: " + info.event.start.toLocaleString();
            modalEnd.textContent = info.event.end ? "End: " + info.event.end.toLocaleString() : '';
            modalDescription.textContent = info.event.extendedProps.description || '';

            // Show modal
            modal.style.display = 'flex';
        },
        eventDrop: function(info) {
            updateCalendarEvent(
                info,
                function onSuccess() {
                    // Optionally, do something on success
                },
                function onError() {
                    alert('Could not update event. Reverting.');
                    info.revert();
                }
            );
        }
    });

    calendar.render();

    // Close modal logic
    if (modalClose) {
        modalClose.onclick = function () {
            modal.style.display = 'none';
        };
    }
    // Also close when clicking outside modal-content
    if (modal) {
        modal.onclick = function (e) {
            if (e.target === modal) {
                modal.style.display = 'none';
            }
        };
    }
});

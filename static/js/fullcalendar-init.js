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

    // CSRF helper (Django AJAX CSRF)
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

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
            // AJAX to update event time
            fetch('/schedule/api/update/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': getCookie('csrftoken')
                },
                body: JSON.stringify({
                    id: info.event.id,
                    start: info.event.start ? info.event.start.toISOString() : null,
                    end: info.event.end ? info.event.end.toISOString() : null
                })
            })
            .then(response => response.json())
            .then(data => {
                if (!data.success) {
                    alert('Could not update event. Reverting.');
                    info.revert();
                }
            })
            .catch(error => {
                alert('Error updating event.');
                info.revert();
            });
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

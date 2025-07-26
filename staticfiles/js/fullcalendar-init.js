document.addEventListener('DOMContentLoaded', function () {
    const {
        Calendar
    } = FullCalendar;

    const calendarEl = document.getElementById('calendar');
    if (!calendarEl) return;

    // Modal elements
    const modal = document.getElementById('eventDetailModal');
    const modalTitle = document.getElementById('modalTitle');
    const modalStart = document.getElementById('modalStart');
    const modalEnd = document.getElementById('modalEnd');
    const modalDescription = document.getElementById('modalDescription');
    const modalClose = document.getElementById('modalClose');

    const calendar = new Calendar(calendarEl, {
        plugins: FullCalendar.globalPlugins,

        headerToolbar: {
            left: 'prev,next today',
            center: 'title',
            right: 'dayGridMonth,timeGridWeek,timeGridDay'
        },

        eventTimeFormat: {hour: 'numeric', minute: '2-digit', meridiem: 'short'},

        editable: true,


        events: {
            url: '/schedule/api/events/'
        },
        eventDataTransform: function (eventData) {
            if (eventData.rrule) {
                return {
                    id: eventData.id,
                    title: eventData.title,
                    rrule: {
                        freq: eventData.rrule.freq?.toLowerCase(),
                        dtstart: eventData.rrule.dtstart
                    },
                    duration: '01:00',
                    extendedProps: {
                        description: eventData.description || ''
                    }
                };
            }

            return {
                id: eventData.id,
                title: eventData.title,
                start: eventData.start,
                end: eventData.end,
                extendedProps: {
                    description: eventData.description || ''
                }
            };
        },
        eventClick: function (info) {
            // Fill modal content
            modalTitle.textContent = info.event.title;
            modalStart.textContent = "Start: " + info.event.start.toLocaleString();
            modalEnd.textContent = info.event.end ? "End: " + info.event.end.toLocaleString() : '';
            modalDescription.textContent = info.event.extendedProps.description || '';

            // Set delete form action using event id (this line is new)
            let deleteForm = document.getElementById('modalDeleteForm');
            if (deleteForm) {
                setDeleteFormAction(deleteForm, info.event.id); // This function will be in delete-event.js
            }

            // Show modal
            modal.style.display = 'flex';
        },

        eventDrop: function (info) {
            updateCalendarEvent(
                info,
                function onSuccess() {
                    // Optionally, do something on success
                },
                function onError(errorMsg) { // <-- Accept error message!
                    showErrorModal(errorMsg); // <-- Show error in modal!
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


function showErrorModal(message) {
    const errorModal = document.getElementById('errorModal');
    const errorModalMsg = document.getElementById('errorModalMessage');
    const errorModalOk = document.getElementById('errorModalOk');
    errorModalMsg.textContent = message || 'An error occurred.';
    errorModal.style.display = 'flex';

    // OK button closes modal
    if (errorModalOk) {
        errorModalOk.onclick = function () {
            errorModal.style.display = 'none';
        };
    }
    if (errorModal) {
        errorModal.onclick = function (e) {
            if (e.target === errorModal) {
                errorModal.style.display = 'none';
            }
        };
    }
}
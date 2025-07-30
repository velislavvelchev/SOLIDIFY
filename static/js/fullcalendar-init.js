document.addEventListener('DOMContentLoaded', function () {
    const { Calendar } = FullCalendar;

    const calendarEl = document.getElementById('calendar');
    if (!calendarEl) return;

    // Modal elements
    const modal = document.getElementById('eventDetailModal');
    const modalTitle = document.getElementById('modalTitle');
    const modalStart = document.getElementById('modalStart');
    const modalEnd = document.getElementById('modalEnd');
    const modalDescription = document.getElementById('modalDescription');
    const modalClose = document.getElementById('modalClose');

    function revertWithError(info, message) {
        showErrorModal(message);
        info.revert();
    }

    function confirmAndUpdateRecurringEvent(info) {
        const confirmModal = document.getElementById('recurringUpdateModal');
        const confirmBtn = document.getElementById('confirmRecurringUpdate');
        const cancelBtn = document.getElementById('cancelRecurringUpdate');

        if (confirmModal && confirmBtn && cancelBtn) {
            confirmModal.style.display = 'flex';

            confirmBtn.onclick = function () {
                confirmModal.style.display = 'none';
                updateCalendarEvent(
                    info,
                    () => window.location.reload(),
                    (errorMsg) => revertWithError(info, errorMsg)
                );
            };

            cancelBtn.onclick = function () {
                confirmModal.style.display = 'none';
                info.revert();
            };
        } else {
            revertWithError(info, "Could not show confirmation modal.");
        }
    }

    const calendar = new Calendar(calendarEl, {
        plugins: FullCalendar.globalPlugins,
        forceEventDuration: true,
        headerToolbar: {
            left: 'prev,next today',
            center: 'title',
            right: 'dayGridMonth,timeGridWeek,timeGridDay'
        },

        eventTimeFormat: { hour: 'numeric', minute: '2-digit', meridiem: 'short' },

        editable: true,

        events: {
            url: '/schedule/api/events/'
        },

        eventDataTransform: function (eventData) {
            if (eventData.rrule) {
                const start = new Date(eventData.start);
                const end = new Date(eventData.end);
                const durationMs = end - start;

                const durationMin = Math.round(durationMs / (1000 * 60));
                const hours = Math.floor(durationMin / 60);
                const minutes = durationMin % 60;

                return {
                    id: eventData.id,
                    title: eventData.title,
                    rrule: {
                        freq: eventData.rrule.freq?.toLowerCase(),
                        dtstart: eventData.rrule.dtstart,
                        interval: eventData.rrule.interval,
                        until: eventData.rrule.until || undefined
                    },
                    duration: {
                        hours,
                        minutes
                    },
                    extendedProps: {
                        description: eventData.description || '',
                        startTime: start.toISOString(),
                        endTime: end.toISOString()
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
            modalTitle.textContent = info.event.title;

            const start = info.event.start || info.event.extendedProps.startTime;
            const end = info.event.end || info.event.extendedProps.endTime;

            modalStart.textContent = "Start: " + (start ? new Date(start).toLocaleString() : "N/A");
            modalEnd.textContent = end ? "End: " + new Date(end).toLocaleString() : '';

            modalDescription.textContent = info.event.extendedProps.description || '';

            const deleteForm = document.getElementById('modalDeleteForm');
            if (deleteForm) {
                setDeleteFormAction(deleteForm, info.event.id);
            }

            modal.style.display = 'flex';
        },

        eventDrop: function (info) {
            const isRecurring = info.event._def.recurringDef || info.event.extendedProps.rrule;

            if (isRecurring) {
                confirmAndUpdateRecurringEvent(info);
            } else {
                updateCalendarEvent(
                    info,
                    () => {}, // No-op on success
                    (errorMsg) => revertWithError(info, errorMsg)
                );
            }
        }
    });

    calendar.render();

    // Modal close logic
    if (modalClose) {
        modalClose.onclick = function () {
            modal.style.display = 'none';
        };
    }

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

document.addEventListener('DOMContentLoaded', function () {
    const {Calendar} = FullCalendar;

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
        forceEventDuration: true,
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
                        until: eventData.rrule.until || undefined // optional, if your backend supports it
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

            // ✅ FIX: Fallback for rrule-based events using extendedProps
            const start = info.event.start || info.event.extendedProps.startTime;
            const end = info.event.end || info.event.extendedProps.endTime;

            modalStart.textContent = "Start: " + (start ? new Date(start).toLocaleString() : "N/A");
            modalEnd.textContent = end ? "End: " + new Date(end).toLocaleString() : '';

            modalDescription.textContent = info.event.extendedProps.description || '';

            let deleteForm = document.getElementById('modalDeleteForm');
            if (deleteForm) {
                setDeleteFormAction(deleteForm, info.event.id);
            }

            modal.style.display = 'flex';
        },

        eventDrop: function (info) {
            const newStart = info.event.start;
            const newEnd = info.event.end;
            const movedId = info.event.id;

            const hasConflict = calendar.getEvents().some(ev => {
                if (ev.id === movedId) return false;

                const evStart = ev.start || ev.extendedProps.startTime;
                const evEnd = ev.end || ev.extendedProps.endTime;

                if (!evStart || !evEnd || !newStart || !newEnd) return false;

                return (newStart < evEnd && newEnd > evStart);
            });

            if (hasConflict) {
                showErrorModal("You can't overlap another event.");
                info.revert();
                return;
            }

            if (info.event._def.recurringDef || info.event.extendedProps.rrule) {
                // Show warning modal about updating recurring series
                const confirmModal = document.getElementById('recurringUpdateModal');
                const confirmBtn = document.getElementById('confirmRecurringUpdate');
                const cancelBtn = document.getElementById('cancelRecurringUpdate');

                if (confirmModal && confirmBtn && cancelBtn) {
                    confirmModal.style.display = 'flex';

                    // Clean up existing listeners to avoid stacking
                    confirmBtn.onclick = function () {
                        confirmModal.style.display = 'none';
                        updateCalendarEvent(
                            info,
                            function onSuccess() {
                                 window.location.reload();
                            },
                            function onError(errorMsg) {
                                showErrorModal(errorMsg);
                                info.revert();
                            }
                        );
                    };

                    cancelBtn.onclick = function () {
                        confirmModal.style.display = 'none';
                        info.revert();
                    };
                } else {
                    // Fallback: if modal doesn't exist, revert and show error
                    showErrorModal("Could not show confirmation modal.");
                    info.revert();
                }

                return; // Block further processing
            }

            // Normal (non-recurring) event update
            updateCalendarEvent(
                info,
                function onSuccess() {},
                function onError(errorMsg) {
                    showErrorModal(errorMsg);
                    info.revert();
                }
            );
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

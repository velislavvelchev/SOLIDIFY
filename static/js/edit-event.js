// edit-event.js
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

function updateCalendarEvent(info, onSuccess, onError) {
    fetch('/schedule/api/update/' + info.event.id + '/', {
        method: 'PATCH',
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
    .then(async (response) => {
        let data;
        try {
            data = await response.json();
        } catch (err) {
            throw new Error("Server returned an unexpected response.");
        }

        if (!response.ok) {
            throw new Error(data.error || 'Update failed');
        }

        if (data.success) {
            if (onSuccess) onSuccess(data);
        } else {
            if (onError) onError(data.error || 'Unexpected backend error');
        }
    })
    .catch(error => {
        console.error('Update error:', error);
        if (onError) onError(error.message || 'Unknown error');
    });
}



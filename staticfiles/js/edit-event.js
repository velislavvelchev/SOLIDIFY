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
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            if (onSuccess) onSuccess(data);
        } else {
            console.log('Error from backend:', data.error);  // <--- ADD THIS LINE
            if (onError) onError(data.error || 'Update failed');
        }
    })
    .catch(error => {
        console.log('Network or JS error:', error);         // <--- ADD THIS LINE
        if (onError) onError(error);
    });
}



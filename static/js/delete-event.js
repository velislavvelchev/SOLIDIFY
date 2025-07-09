// delete-event.js

function setDeleteFormAction(formElement, eventId) {
    // Sets the form action for Django DeleteView
    formElement.action = `/schedule/${eventId}/delete/`;
}

document.addEventListener('DOMContentLoaded', function() {
    const typeSelect = document.getElementById('id_category_type');
    if (!typeSelect) return;

    let previousValue = typeSelect.value;

    const modal = document.getElementById('categoryModal');
    const confirmBtn = document.getElementById('modalConfirm');
    const cancelBtn = document.getElementById('modalCancel');

    let pendingValue = previousValue;

    typeSelect.addEventListener('change', function() {
        pendingValue = typeSelect.value; // Save the new value the user is trying to set
        typeSelect.value = previousValue; // Revert immediately until they confirm
        modal.style.display = 'flex';     // Show modal
    });

    confirmBtn.addEventListener('click', function() {
        modal.style.display = 'none';
        typeSelect.value = pendingValue;    // Set to new value
        previousValue = pendingValue;       // Update previous value
    });

    cancelBtn.addEventListener('click', function() {
        modal.style.display = 'none';
        typeSelect.value = previousValue;   // Reset to original
    });
});

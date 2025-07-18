document.addEventListener('DOMContentLoaded', function() {
    const categorySelect = document.getElementById('id_category');
    const habitsSelect = document.getElementById('id_habits');

    if (!categorySelect || !habitsSelect) return;

    // Reusable function for filtering
    function filterHabitsByCategory(categoryId) {
        if (!categoryId) {
            habitsSelect.innerHTML = '';
            return;
        }
        fetch(`/habits/api/habits-for-category/?category_id=${categoryId}`)
            .then(response => response.json())
            .then(data => {
                // Save current selection to try to preserve it after reload
                const selected = Array.from(habitsSelect.selectedOptions).map(opt => opt.value);
                habitsSelect.innerHTML = '';
                // -------- EDIT 1: Loop over 'data' directly, not data.habits
                data.forEach(habit => {
                    const option = document.createElement('option');
                    option.value = habit.id;
                    // -------- EDIT 2: Use 'habit.habit_name' instead of 'habit.name'
                    option.textContent = habit.habit_name;
                    if (selected.includes(String(habit.id))) {
                        option.selected = true; // try to restore selection
                    }
                    habitsSelect.appendChild(option);
                });
            })
            .catch(error => {
                habitsSelect.innerHTML = '';
                console.error('Error fetching habits:', error);
            });
    }
    // On change event
    categorySelect.addEventListener('change', function() {
        filterHabitsByCategory(this.value);
    });

    // >>>> Trigger filtering on page load with current category
    if (categorySelect.value) {
        filterHabitsByCategory(categorySelect.value);
    }
});

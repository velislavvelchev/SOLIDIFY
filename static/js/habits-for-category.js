document.addEventListener('DOMContentLoaded', function() {
    const categorySelect = document.getElementById('id_category');
    const habitsSelect = document.getElementById('id_habits');

    if (!categorySelect || !habitsSelect) return;

    categorySelect.addEventListener('change', function() {
        const categoryId = this.value;
        if (!categoryId) {
            habitsSelect.innerHTML = '';
            return;
        }
        fetch(`/habits/api/habits-for-category/?category_id=${categoryId}`)
            .then(response => response.json())
            .then(data => {
                habitsSelect.innerHTML = '';
                data.habits.forEach(habit => {
                    const option = document.createElement('option');
                    option.value = habit.id;
                    option.textContent = habit.name;
                    habitsSelect.appendChild(option);
                });
            })
            .catch(error => {
                habitsSelect.innerHTML = '';
                console.error('Error fetching habits:', error);
            });
    });
});

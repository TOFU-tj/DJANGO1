document.addEventListener('DOMContentLoaded', function() {
    const toggleBtn = document.getElementById('toggle-btn');
    const sidebar = document.getElementById('sidebar');

    // Добавляем обработчик клика на кнопку
    toggleBtn.addEventListener('click', function() {
        if (sidebar.style.transform === 'translateX(0px)') {
            sidebar.style.transform = 'translateX(-250px)'; // Закрываем сайдбар
        } else {
            sidebar.style.transform = 'translateX(0px)'; // Открываем сайдбар
        }
    });
});

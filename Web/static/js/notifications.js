function fetchNotifications() {
    fetch('/notifications')
        .then(response => response.json())
        .then(data => {
            const notificationList = document.getElementById('notification-list');

            data.forEach(notification => {
                const li = document.createElement('li');
                li.textContent = `${notification.timestamp}: ${notification.message}`;
                notificationList.appendChild(li);
            });
        })
        .catch(error => console.error('Erro ao buscar notificações:', error));
}

document.addEventListener('DOMContentLoaded', fetchNotifications);


document.getElementById('clear-notifications').addEventListener('click', () => {
    fetch('/notifications/delete', { method: 'POST' })
        .then(response => response.json())
        .then(data => {
            console.log(data.message);
            const notificationList = document.getElementById('notification-list');
            notificationList.innerHTML = ''; 
        })
        .catch(error => console.error('Erro ao limpar notificações:', error));
});

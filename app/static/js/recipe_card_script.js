document.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('.heart-btn').forEach(btn => {
        btn.addEventListener('click', function(e) {
            e.preventDefault();
            const icon = this.querySelector('.material-icons');
            if (icon.textContent === 'favorite_border') {
                icon.textContent = 'favorite';
                icon.style.color = 'red';
            } else {
                icon.textContent = 'favorite_border';
                icon.style.color = 'var(--primary-brown)';
            }
        });
    });
});
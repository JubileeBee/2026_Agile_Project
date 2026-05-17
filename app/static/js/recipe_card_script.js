
document.addEventListener('DOMContentLoaded', function() {
  // Handles the like/unlike functionality for recipe cards on the homepage and profile page
  if (!document.querySelector('.profile-container')) {
    document.querySelectorAll('.heart-btn').forEach(btn => {
      const icon = btn.querySelector('.material-icons')
      if (!icon) return;

      // set initial state
      if (icon.textContent.trim() === 'favorite') {
        btn.classList.add('liked')
      }

      btn.addEventListener('click', function (e) {
        e.preventDefault()
        e.stopPropagation()

        const url = btn.dataset.url
        if (!url) return

        fetch(url, {
          method: 'POST',
          headers: {
            'X-Requested-With': 'XMLHttpRequest',
            'X-CSRFToken': getCsrfToken()
          }
        })
        .then(res => res.json())
        .then(data => {
          if (data.liked) {
            icon.textContent = 'favorite'
            btn.classList.add('liked')
          } else {
            icon.textContent = 'favorite_border'
            btn.classList.remove('liked')
          }

          // Update the like count in the card stats
          const card = btn.closest('.recipe-card')
          if (!card) return; 
          
          const likeCount = card.querySelector('.recipe-stats li:first-child')
          if (likeCount) {
              likeCount.innerHTML = `<span class="material-icons">favorite</span> ${data.likes}`
          }
        })
        .catch(err => {
          console.error('Like request failed:', err);
        });
      });
    });
  }

  // Edit button handler
  document.querySelectorAll('.edit-btn').forEach(btn => {
    btn.addEventListener('click', (e) => {
      e.preventDefault();
      e.stopPropagation();

      if (btn.dataset.url) {
        window.location.href = btn.dataset.url;
      }
    });
  });

});

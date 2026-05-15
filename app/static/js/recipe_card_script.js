const recipeCardCsrfToken = document
  .querySelector('meta[name="csrf-token"]')
  ?.content


// Handles the like/unlike functionality for recipe cards on the homepage and profile page
document.addEventListener('DOMContentLoaded', function () {
  document.querySelectorAll('.heart-btn').forEach(btn => {
    const icon = btn.querySelector('.material-icons')

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
          'X-CSRFToken': recipeCardCsrfToken
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
          const likeCount = card.querySelector('.recipe-stats li:first-child')
          if (likeCount) {
              likeCount.innerHTML = `<span class="material-icons" style="font-size: 14px">favorite</span> ${data.likes}`
          }
        })
        .catch(err => {
          console.error('Like request failed:', err)
        })
    })
  })
})
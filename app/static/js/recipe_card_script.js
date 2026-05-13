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

      fetch(url, {
        method: 'POST',
        headers: { 'X-Requested-With': 'XMLHttpRequest' }
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
        })
    })
  })
})
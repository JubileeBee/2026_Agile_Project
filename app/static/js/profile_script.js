
// Profile Tab functionality: handles switching between "My Recipes", "Favourites", and "Likes"
const tabs = document.querySelectorAll('.profile-tab');
const contents = document.querySelectorAll('.profile-tab-content');

tabs.forEach(tab => {
    tab.addEventListener('click', () => {
        tabs.forEach(t => t.classList.remove('active'));
        contents.forEach(c => c.classList.remove('active'));
        tab.classList.add('active');
        document.getElementById(tab.dataset.tab).classList.add('active');
    });
});


// Edit Profile Modal: opens modal and allow closing through close button and clicking outside modal
const openModal = document.getElementById('openModal');
const overlay = document.getElementById('popupOverlay');
const closeModal = document.getElementById('closeModal');

if (openModal && overlay && closeModal) {

    openModal.addEventListener('click', function(e) {
        e.preventDefault();
        overlay.classList.add('active');
    });

    closeModal.addEventListener('click', function() {
        overlay.classList.remove('active');
    });

    overlay.addEventListener('click', function(e) {
        if (e.target === overlay) {
            overlay.classList.remove('active');
        }
    });
}


// Avatar Selection: Updates profile image and highlights selected avatar
const avatarOptions = document.querySelectorAll('.avatar-option');
const profileImg = document.querySelector('.profile-img');

avatarOptions.forEach(avatar => {
    avatar.addEventListener('click', function() {
        avatarOptions.forEach(a => a.classList.remove('selected'));
        this.classList.add('selected');
        profileImg.src = this.src;
    });
});

// Syncs modal avatar selection with the currently saved profile image
// so the correct preset avatar is highlighted when the modal opens.
if (openModal && profileImg) {
    openModal.addEventListener('click', () => {
        const currentSrc = profileImg.src;

        avatarOptions.forEach(avatar => {
            avatar.classList.remove('selected');

            if (avatar.src === currentSrc) {
                avatar.classList.add('selected');
            }
        });
    });
}


//Handles profile updates: sends data to backend and synchronises UI state

const saveBtn = document.getElementById('saveBtn');
const editName = document.getElementById('editName');
const editBio = document.getElementById('editBio');
const profileName = document.querySelector('.profile-name');
const profileBio = document.querySelector('.profile-bio');

// bio counter
const bioCounter = document.getElementById('bioCounter');
if (bioCounter && editBio) {
    bioCounter.textContent = `${editBio.value.length}/250`;

    editBio.addEventListener('input', () => {
        bioCounter.textContent = `${editBio.value.length}/250`;
    });
}


if (saveBtn) {
    saveBtn.addEventListener('click', async () => {

        const name = editName.value
        const bio = editBio.value
        const avatar = document.querySelector('.avatar-option.selected')?.src

        const res = await fetch('/profile/update', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCsrfToken()
            },
            body: JSON.stringify({ name, bio, profile_image: avatar })
        })

        const data = await res.json()

        if (res.ok && data.success) {
            profileName.textContent = name.trim()
            profileBio.textContent = bio.trim()
            profileImg.src = avatar

            editName.value = name.trim()
            editBio.value = bio.trim()
            overlay.classList.remove('active')
        } else {

            const oldErr = document.getElementById('nameError')
            if (oldErr) oldErr.remove()

            const err = document.createElement('p')
            err.id = 'nameError'
            err.textContent = data.error || 'Something went wrong'
            editName.after(err)

            editName.addEventListener('input', () => {
                const err = document.getElementById('nameError')
                if (err) err.remove()
            }, { once: true })
        }
    });
}


// Delete account confirmation modal, handles open/close, validation, and simulate deletion flow
const deleteToggle = document.getElementById('deleteToggle');
const deleteModal = document.getElementById('deleteModal');
const deleteConfirmInput = document.getElementById('deleteConfirmInput');
const confirmDeleteBtn = document.getElementById('confirmDeleteBtn');

if (deleteToggle && deleteModal && deleteConfirmInput && confirmDeleteBtn) {

    deleteToggle.addEventListener('click', () => {
        const isOpen = deleteModal.classList.contains('active');

        if (isOpen) {
            deleteModal.classList.remove('active');
            deleteToggle.textContent = "Delete Account";
        } else {
            deleteModal.classList.add('active');
            deleteToggle.textContent = "Cancel Delete";
        }

        deleteConfirmInput.value = "";
        confirmDeleteBtn.disabled = true;
    });

    deleteConfirmInput.addEventListener('input', () => {
        confirmDeleteBtn.disabled = deleteConfirmInput.value !== 'DELETE';
    });

    confirmDeleteBtn.addEventListener('click', async () => {

        const res = await fetch('/profile/delete', {
            method: 'POST',
            headers: {
                'X-CSRFToken': getCsrfToken()
            }
        })

        const data = await res.json()

        if (overlay) overlay.classList.remove('active');

        document.getElementById('byePopupOverlay')?.classList.add('active');
        document.getElementById('byePopup')?.classList.add('active');

        setTimeout(() => {
            window.location.href = data.redirect || '/';
        }, 2500);
    });
}

// Set initial liked state on page load
document.querySelectorAll('.heart-btn').forEach(btn => {
    const icon = btn.querySelector('.material-icons')
    if (icon.textContent.trim() === 'favorite') {
        btn.classList.add('liked')
    }
})

// Toggles like state by calling backend API and synchronising UI + profile stats without page reload
function attachHeartListener(btn) {
    btn.addEventListener('click', async (e) => {
        // Prevent card click / navigation from triggering
        e.preventDefault()
        e.stopPropagation()

        // Get the URL from data-url attribute which has the recipe id
        const url = btn.dataset.url
        const card = btn.closest('[data-recipe-id]') || btn.closest('article')
        const recipeId = url.split('/')[2] // extracts id from /recipe/id/like

        // Send POST request to toggle like/unlike in backend
        const res = await fetch(url, {
            method: 'POST',
            headers: {
                'X-Requested-With': 'XMLHttpRequest',
                'X-CSRFToken': getCsrfToken()
            }
        })
        const data = await res.json()

        // Update ALL heart buttons for this recipe across all tabs
        document.querySelectorAll(`.heart-btn[data-url="${url}"]`).forEach(b => {
            const icon = b.querySelector('.material-icons')
            if (data.liked) {
                b.classList.add('liked')
                icon.textContent = 'favorite'
            } else {
                b.classList.remove('liked')
                icon.textContent = 'favorite_border'
            }

            // Update like count on the card
            const recipeCard = b.closest('.recipe-card')
            const likeCount = recipeCard?.querySelector('.recipe-stats li:first-child')
            if (likeCount) {
                const span = likeCount.querySelector('.material-icons')
                if (span) {
                    span.nextSibling.textContent = ` ${data.likes}`
                }
            }
        })

        if (data.liked) {
            const likesTab = document.querySelector('#likes .row')

            // Only clone and add if not already in likes tab
            const alreadyExists = likesTab.querySelector(`[data-recipe-id="${recipeId}"]`)
            if (!alreadyExists) {
                const clonedCard = card.closest('.col-12').cloneNode(true)
                // Re-attach listener to cloned heart button so it works after cloning
                attachHeartListener(clonedCard.querySelector('.heart-btn'))
                likesTab.appendChild(clonedCard)
            }

            // Increment likes counter in profile stats
            const likesCount = document.querySelector('.stat:nth-child(3) .stat-number')
            likesCount.textContent = parseInt(likesCount.textContent) + 1

        } else {
            // Decrement likes count in profile stats
            const likesCount = document.querySelector('.stat:nth-child(3) .stat-number')
            likesCount.textContent = parseInt(likesCount.textContent) - 1
        }
    })
}

// Attach listener to all heart buttons on page load
document.querySelectorAll('.heart-btn').forEach(btn => attachHeartListener(btn))
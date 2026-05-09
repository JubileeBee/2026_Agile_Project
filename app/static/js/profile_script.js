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


//Handles profile updates: sends data to backend and synchronises UI state

const saveBtn = document.getElementById('saveBtn');
const editName = document.getElementById('editName');
const editBio = document.getElementById('editBio');
const profileName = document.querySelector('.profile-name');
const profileBio = document.querySelector('.profile-bio');

saveBtn.addEventListener('click', async () => {
    // Collect user input and selected avatar
    const name = editName.value.trim()
    const bio = editBio.value.trim()
    const avatar = document.querySelector('.avatar-option.selected')?.src

    console.log('Saving:', { name, bio, avatar }) 
    
    // Send update request to backend (JSON payload with name, bio, and avatar URL)
    const res = await fetch('/profile/update', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ name, bio, profile_image: avatar })
    })

    const data = await res.json()

    // If update successful, update profile UI with new info and close modal
    if (res.ok && data.success) {
        profileName.textContent = name
        profileBio.textContent = bio
        profileImg.src = avatar
        overlay.classList.remove('active')
    } else {
        
        // Prevent duplicate error messages and display backend validation error
        const oldErr = document.getElementById('nameError')
        if (oldErr) oldErr.remove()

        // Show error message below name input (from backend response or generic if missing)
        const err = document.createElement('p')
        err.id = 'nameError'
        err.textContent = data.error || 'Something went wrong'
        err.style.cssText = `
            color: red;
            font-size: 12px;
            margin-top: 4px;
        `
        editName.after(err)

        // Remove error when user starts typing (runs once per error display)
        editName.addEventListener('input', () => {
            const err = document.getElementById('nameError')
            if (err) err.remove()
        }, { once: true })
    }
});


// Delete account confirmation modal, handles open/close, validation, and simulate deletion flow
const deleteToggle = document.getElementById('deleteToggle');
const deleteModal = document.getElementById('deleteModal');
const deleteConfirmInput = document.getElementById('deleteConfirmInput');
const confirmDeleteBtn = document.getElementById('confirmDeleteBtn');

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
    const res = await fetch('/profile/delete', { method: 'POST' })
    const data = await res.json()

    overlay.classList.remove('active');
    document.getElementById('byePopupOverlay').classList.add('active');
    document.getElementById('byePopup').classList.add('active');

    setTimeout(() => {
        window.location.href = data.redirect || '/';
    }, 2500);
});


// Toggles like state by calling backend API and synchronising UI + profile stats without page reload
document.querySelectorAll('.heart-btn').forEach(btn => {
    btn.addEventListener('click', async (e) => {
        // Prevent card click / navigation from triggering
        e.preventDefault()
        e.stopPropagation()

        // Get recipe ID from parent card (data-recipe-id attribute)
        const card = btn.closest('[data-recipe-id]')
        const recipeId = card.dataset.recipeId

        // Send POST request to toggle like/unlike in backend
        const res = await fetch(`/recipe/${recipeId}/like`, { method: 'POST' })
        const data = await res.json()
        
        // Icon inside heart button
        const icon = btn.querySelector('.material-icons')

        if (data.liked) {
            // Update UI to fill red heart
            btn.classList.add('liked')
            icon.textContent = 'favorite'

            // Clone the card and add it to the likes tab dynamically
            const likesTab = document.querySelector('#likes .row')
            const clonedCard = card.closest('.col-12').cloneNode(true)
            likesTab.appendChild(clonedCard)

            // INcrement likes counter in profile stats
            const likesCount = document.querySelector('.stat:nth-child(3) .stat-number')
            likesCount.textContent = parseInt(likesCount.textContent) + 1

        } else {
            // update UI to just the outline heart
            btn.classList.remove('liked')
            icon.textContent = 'favorite_border'

            // Remove the card from likes tab
            const likesTab = document.querySelector('#likes .row')
            likesTab.querySelectorAll('[data-recipe-id]').forEach(c => {
                if (c.dataset.recipeId === recipeId) {
                    c.closest('.col-12').remove()
                }
            })

            // Decrement likes count in profile stats
            const likesCount = document.querySelector('.stat:nth-child(3) .stat-number')
            likesCount.textContent = parseInt(likesCount.textContent) - 1
        }
    })
})

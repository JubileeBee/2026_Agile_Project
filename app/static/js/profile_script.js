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


// Edit Profile Modal: opsn modal and allow closing through close button and clicking outside modal
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


//Handle Profile Updates, and syncs user input with UI and prepares for DB fetch-->>

const saveBtn = document.getElementById('saveBtn');
const editName = document.getElementById('editName');
const editBio = document.getElementById('editBio');
const profileName = document.querySelector('.profile-name');
const profileBio = document.querySelector('.profile-bio');

saveBtn.addEventListener('click', () => {
    profileName.textContent = editName.value;
    profileBio.textContent = editBio.value;

    overlay.classList.remove('active');
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

confirmDeleteBtn.addEventListener('click', () => {
    overlay.classList.remove('active');
    document.getElementById('byePopupOverlay').classList.add('active');
    document.getElementById('byePopup').classList.add('active');
    setTimeout(() => {
        window.location.href = '/';
    }, 2500);
});

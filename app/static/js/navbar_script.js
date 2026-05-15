// Navbar scroll behavior: hide on scroll down, show on scroll up
const navbar = document.querySelector('.topnav');

if (navbar) {
    let lastScrollY = window.scrollY;

    window.addEventListener('scroll', () => {
        const currentScrollY = window.scrollY;

        if (currentScrollY < lastScrollY) {
            navbar.style.transform = 'translateY(0)';
        } else {
            navbar.style.transform = 'translateY(-100%)';
        }

        lastScrollY = currentScrollY;
    });
}
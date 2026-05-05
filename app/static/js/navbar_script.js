// Navbar scroll behavior: hide on scroll down, show on scroll up
let lastScrollY = window.scrollY;

window.addEventListener('scroll', () => {
    const currentScrollY = window.scrollY;

    if (currentScrollY < lastScrollY) {
        // scrolling up — show navbar
        document.querySelector('.topnav').style.transform = 'translateY(0)';
    } else {
        // scrolling down — hide navbar
        document.querySelector('.topnav').style.transform = 'translateY(-100%)';
    }

    lastScrollY = currentScrollY;
});
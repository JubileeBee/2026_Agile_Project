// Navbar scroll behavior: hide on scroll down, show on scroll up
let lastScrollY = window.scrollY;

window.addEventListener('scroll', () => {
    const currentScrollY = window.scrollY;

    if (currentScrollY === 0) {
        // at the top — back to sticky, no gap
        document.querySelector('.topnav').style.position = 'sticky';
        document.querySelector('.topnav').style.transform = 'translateY(0)';
    } else if (currentScrollY < lastScrollY) {
        // scrolling up — show navbar
        document.querySelector('.topnav').style.position = 'fixed';
        document.querySelector('.topnav').style.transform = 'translateY(0)';
    } else {
        // scrolling down — hide navbar
        document.querySelector('.topnav').style.transform = 'translateY(-100%)';
    }

    lastScrollY = currentScrollY;
});
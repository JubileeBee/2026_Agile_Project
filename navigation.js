function loadNav() {
    //html structure for the top navigation bar
    const topNavHTML = `
    <nav class="topnav">
        <div class="nav-left">
            <span class="material-icons menu-icon">menu</span>
            <span class="logo-text">CozyCravings</span>
        </div>

        <div class="nav-right">
            <a href="profile.html" class="nav-circle">
                <span class="material-icons" id="profile-icon">account_circle</span>
            </a>
            <a href="signup.html" class="signup-btn">Sign Up</a> 
        </div>
    </nav>`;
    //html structure for teh floating "+" post button
    const postButtonHTML = `
    <a href="post.html" class="floating-post-btn">
        <span class="material-icons">add</span>
    </a>`;
    //injects the html string into a specific placeholder divs
    document.getElementById('top-nav-placeholder').innerHTML = topNavHTML;
    document.getElementById('post-button-placeholder').innerHTML = postButtonHTML;
}
// ensures the function runs only after the full page has finished loading
window.onload = loadNav;
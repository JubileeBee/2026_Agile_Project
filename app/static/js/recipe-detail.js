// LIKE BUTTON
const likeBtn = document.getElementById("likeBtn");
const likeCount = document.getElementById("likeCount");

if (likeBtn) {
    likeBtn.addEventListener("click", () => {

        likeBtn.classList.toggle("liked");

        let count = parseInt(likeCount.textContent);

        if (likeBtn.classList.contains("liked")) {
            likeCount.textContent = count + 1;
        } else {
            likeCount.textContent = count - 1;
        }
    });
}


// FAVOURITE BUTTON
const favouriteBtn = document.getElementById("favouriteBtn");

if (favouriteBtn) {
    favouriteBtn.addEventListener("click", () => {
        favouriteBtn.classList.toggle("favourited");

        if (favouriteBtn.classList.contains("favourited")) {
            favouriteBtn.innerHTML = "⭐ Added to Favourites";
        } else {
            favouriteBtn.innerHTML = "⭐ Favourite";
        }
    });
}


// COMMENT COUNTER
const commentTextarea = document.getElementById("commentTextarea");
const commentCounter = document.getElementById("commentCounter");

if (commentTextarea && commentCounter) {

    commentTextarea.addEventListener("input", () => {
        commentCounter.textContent = commentTextarea.value.length;
    });
}


// COLLAPSE INGREDIENTS
const toggleIngredientsBtn = document.getElementById("toggleIngredientsBtn");
const ingredientsSection = document.getElementById("ingredientsSection");

if (toggleIngredientsBtn && ingredientsSection) {

    toggleIngredientsBtn.addEventListener("click", () => {

        if (ingredientsSection.style.display === "none") {
            ingredientsSection.style.display = "block";
            toggleIngredientsBtn.textContent = "Collapse";
        } else {
            ingredientsSection.style.display = "none";
            toggleIngredientsBtn.textContent = "Expand";
        }
    });
}


// SHARE BUTTON
const shareBtn = document.getElementById("shareBtn");

if (shareBtn) {

    shareBtn.addEventListener("click", async () => {

        try {

            await navigator.clipboard.writeText(window.location.href);

            shareBtn.innerHTML = "✅ Link Copied";

            setTimeout(() => {
                shareBtn.innerHTML = "🔗 Share";
            }, 2000);

        } catch (error) {
            console.error("Unable to copy link", error);
        }
    });
}


// SMOOTH SCROLL FOR COMMENTS
const commentsSection = document.querySelector(".comments-wrapper");

if (commentsSection) {
    commentsSection.style.scrollBehavior = "smooth";
}
.login-comment-prompt {
    color: #666;
    margin-bottom: 2rem;
    font-size: 0.95rem;
}

.login-comment-prompt a {
    font-weight: 600;
    text-decoration: none;
}
.comment-card {
    padding-top: 1rem;
}
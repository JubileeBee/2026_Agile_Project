const csrfToken = document.querySelector('meta[name="csrf-token"]')?.content

// LIKE BUTTON
const likeBtn = document.getElementById("likeBtn");
const likeCount = document.getElementById("likeCount");

if (likeBtn && likeCount) {
    likeBtn.addEventListener("click", async () => {
        const url = likeBtn.dataset.url;

        try {
            const res = await fetch(url, {
                method: "POST",
                headers: {
                    "X-Requested-With": "XMLHttpRequest",
                    "X-CSRFToken": csrfToken
                }
            });
            const data = await res.json();

            if (!res.ok) {
                alert(data.error || "Action not allowed");
                return;
            }

            // backend truth
            likeBtn.classList.toggle("liked", data.liked);
            likeCount.textContent = data.likes;

        } catch (err) {
            console.error(err);
        }
    });
}


// FAVOURITE BUTTON
const favouriteBtn = document.getElementById("favouriteBtn");

if (favouriteBtn) {
    favouriteBtn.addEventListener("click", async () => {
        const url = favouriteBtn.dataset.url;

        try {
            const res = await fetch(url, {
                method: "POST",
                headers: {
                    "X-Requested-With": "XMLHttpRequest",
                    "X-CSRFToken": csrfToken
                }
            });
            const data = await res.json();

            if (!res.ok) {
                alert(data.error || "Action not allowed");
                return;
            }

            favouriteBtn.classList.toggle("favourited", data.favourited);

            favouriteBtn.textContent = data.favourited
                ? "⭐ Added to Favourites"
                : "⭐ Favourite";

        } catch (err) {
            console.error(err);
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

            shareBtn.textContent = "✅ Link Copied";

            setTimeout(() => {
                shareBtn.textContent = "🔗 Share";
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

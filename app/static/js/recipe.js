// Minimal JS (placeholder for future dynamic data binding)

document.addEventListener("DOMContentLoaded", () => {
    console.log("Recipe card loaded");

    const heart = document.querySelector(".heart");
    const likeCountEl = document.getElementById("like-count");

    let liked = false;
    let likes = parseInt(likeCountEl.textContent);

    heart.addEventListener("click", () => {
        liked = !liked;

        if (liked) {
            likes++;
            heart.classList.add("active");
        } else {
            likes--;
            heart.classList.remove("active");
        }

        likeCountEl.textContent = likes;
    });
});
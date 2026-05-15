const csrfToken = document.querySelector('meta[name="csrf-token"]')?.content

let page = 1;
let loading = false;
let hasMore = true;

let currentSearch = "";
let currentCategory = "";

const grid = document.getElementById("feed-grid");
const loadingEl = document.getElementById("loading");

// 🧱 Create card
function createCard(recipe) {
    const div = document.createElement("div");
    div.className = "col-6 col-md-4";

    div.innerHTML = `
        <div class="recipe-card">
            <img src="${recipe.image_url}" style="width:100%; border-radius:10px;">
            <h5>${recipe.title}</h5>
            <p>❤️ ${recipe.likes} • ⭐ ${recipe.rating}</p>
        </div>
    `;

    return div;
}

// 📡 Fetch recipes
async function fetchRecipes(reset = false) {
    if (loading || !hasMore) return;

    loading = true;
    loadingEl.style.display = "block";

    if (reset) {
        page = 1;
        hasMore = true;
        grid.innerHTML = "";
    }

    const res = await fetch(`/api/recipes?page=${page}&search=${currentSearch}&category=${currentCategory}`);
    const data = await res.json();

    data.recipes.forEach(r => {
        grid.appendChild(createCard(r));
    });

    hasMore = data.has_more;
    page++;
    loading = false;

    if (!hasMore) loadingEl.innerText = "No more recipes";
}

// 🔄 Infinite scroll
window.addEventListener("scroll", () => {
    if (window.innerHeight + window.scrollY >= document.body.offsetHeight - 200) {
        fetchRecipes();
    }
});

// 🔍 Live search (debounced)
let timeout;
document.getElementById("search-input").addEventListener("input", (e) => {
    clearTimeout(timeout);

    timeout = setTimeout(() => {
        currentSearch = e.target.value;
        fetchRecipes(true);
    }, 300);
});

// 🏷 Filters
document.querySelectorAll(".filter-btn").forEach(btn => {
    btn.addEventListener("click", () => {
        document.querySelectorAll(".filter-btn").forEach(b => b.classList.remove("active"));
        btn.classList.add("active");

        currentCategory = btn.dataset.category;
        fetchRecipes(true);
    });
});

// 🚀 Initial load
fetchRecipes();
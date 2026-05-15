document.addEventListener("DOMContentLoaded", () => {
    const searchForm = document.querySelector(".search-form");

    searchForm.addEventListener("submit", (event) => {
      event.preventDefault();
      fetchRecipes();
    });

  const searchInput = document.getElementById("live-search-input");
  const difficultyFilter = document.getElementById("difficulty-filter");
  const categoryFilter = document.getElementById("category-filter");
  const sortFilter = document.getElementById("sort-filter");
  const resultsContainer = document.getElementById("results-container");

  let debounceTimer;

  async function fetchRecipes() {

    const query = searchInput.value;
    const difficulty = difficultyFilter.value;
    const category = categoryFilter.value;
    const sort = sortFilter.value;

    const params = new URLSearchParams({
      q: query,
      difficulty: difficulty,
      category: category,
      sort: sort
    });

    try {

      const response = await fetch(`/api/live-search?${params.toString()}`);
      const recipes = await response.json();

      resultsContainer.innerHTML = "";

      if (recipes.length === 0) {
        resultsContainer.innerHTML = `
          <div class="text-center py-5">
            <h3>No recipes found</h3>
            <p>Try searching for something else.</p>
          </div>
        `;
        return;
      }

      recipes.forEach(recipe => {

        let imagePath = "/static/images/default.png";

          if (recipe.image_file) {

            if (recipe.image_file.startsWith("http")) {
              imagePath = recipe.image_file;
            } else {
              imagePath = `/static/images/uploads/${recipe.image_file}`;
            }

          }
        const recipeCard = `
          <div class="col-12 col-md-6">
            <a href="/recipe/${recipe.id}" class="recipe-link">
              <article class="recipe-card">

                <figure class="recipe-image">
                  <img src="${imagePath}" alt="${recipe.title}">
                </figure>

                <div class="recipe-content">
                  <h3>${recipe.title}</h3>

                  <p class="recipe-description">
                    ${recipe.description || ""}
                  </p>

                  <div class="recipe-meta">
                    <span>${recipe.category}</span>
                    <span>${recipe.difficulty}</span>
                    <span>❤️ ${recipe.likes}</span>
                  </div>
                </div>

              </article>
            </a>
          </div>
        `;

        resultsContainer.insertAdjacentHTML("beforeend", recipeCard);

      });

    } catch (error) {
      console.error("Live search failed:", error);
    }
  }

  function debounceFetch() {
    clearTimeout(debounceTimer);
    debounceTimer = setTimeout(fetchRecipes, 300);
  }

  searchInput.addEventListener("input", debounceFetch);

  difficultyFilter.addEventListener("change", fetchRecipes);
  categoryFilter.addEventListener("change", fetchRecipes);
  sortFilter.addEventListener("change", fetchRecipes);

});
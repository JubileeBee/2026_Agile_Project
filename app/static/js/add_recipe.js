
document.addEventListener("DOMContentLoaded", () => {

    const container = document.getElementById("ingredients-container");
    const addBtn = document.getElementById("add-ingredient-btn");

    if(container && addBtn) {
        // Add ingredient row
        addBtn.addEventListener("click", () => {
            const row = document.createElement("div");
            row.classList.add("ingredient-row");

            row.textContent = `
                <input type="text" name="ingredient_name[]" placeholder="Ingredient" required>
                <input type="text" name="ingredient_quantity[]" placeholder="Qty">
                <input type="text" name="ingredient_unit[]" placeholder="Unit">
                <button type="button" class="remove-btn">X</button>
            `;

            container.appendChild(row);
        });

        // Remove ingredient (event delegation)
        container.addEventListener("click", (e) => {
            if (e.target.classList.contains("remove-btn")) {
                if (container.children.length > 1) {
                    e.target.parentElement.remove();
                } else {
                    alert("You need at least one ingredient.");
                }
            }
        });
    }


    const prepInput = document.getElementById("prep_time");
    const cookInput = document.getElementById("cook_time");
    const totalInput = document.getElementById("total_time");
    const totalDisplay = document.getElementById("total_display");

    function formatTime(minutes) {
        if (!minutes || minutes <= 0) return "";

        const hrs = Math.floor(minutes / 60);
        const mins = minutes % 60;

        if (hrs > 0 && mins > 0) return `${hrs} hr ${mins} mins`;
        if (hrs > 0) return `${hrs} hr`;
        return `${mins} mins`;
    }

    function updateTotalTime() {
        const prep = parseInt(prepInput.value) || 0;
        const cook = parseInt(cookInput.value) || 0;

        const total = prep + cook;

        if (totalInput) {
            totalInput.value = total;
        }
        
        if (totalDisplay) {
            totalDisplay.textContent = formatTime(total);
        }
    }

    if (prepInput && cookInput) {
        prepInput.addEventListener("input", updateTotalTime);
        cookInput.addEventListener("input", updateTotalTime);
    }

    const descInput = document.getElementById("description");
    const descCount = document.getElementById("desc-count");

    if (descInput && descCount) {
        descInput.addEventListener("input", () => {
            const length = descInput.value.length;
            descCount.textContent = `${length} / 300`;
        });
    }

});
document.addEventListener("DOMContentLoaded", function () {
    console.log("Checkbox persistence script loaded");
    const checkboxes = document.querySelectorAll("input[type='checkbox']");
    console.log("Found", checkboxes.length, "checkboxes");
    checkboxes.forEach(cb => {
        const server = cb.getAttribute("data-server");
        const saved = localStorage.getItem("checkbox_" + server);
        console.log("Loading state for", server, ":", saved);
        if (saved === "true") cb.checked = true;
        cb.addEventListener("change", function () {
            console.log("Saving state for", server, ":", this.checked);
            localStorage.setItem("checkbox_" + server, this.checked);
        });
    });
});

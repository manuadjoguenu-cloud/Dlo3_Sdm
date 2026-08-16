// Ouvre/ferme le menu mobile (hamburger) et referme automatiquement
// après le clic sur un lien, pour ne pas laisser le tiroir ouvert.
document.addEventListener("DOMContentLoaded", () => {
  const bouton = document.getElementById("nav-toggle");
  const menu = document.getElementById("nav-menu");
  if (!bouton || !menu) return;

  const icone = bouton.querySelector(".nav-toggle-icone");

  function fermer() {
    menu.classList.remove("ouvert");
    bouton.setAttribute("aria-expanded", "false");
    if (icone) icone.textContent = "☰";
  }

  function basculer() {
    const ouvert = menu.classList.toggle("ouvert");
    bouton.setAttribute("aria-expanded", ouvert ? "true" : "false");
    if (icone) icone.textContent = ouvert ? "✕" : "☰";
  }

  bouton.addEventListener("click", basculer);

  menu.querySelectorAll("a").forEach(lien => {
    lien.addEventListener("click", fermer);
  });

  document.addEventListener("keydown", e => {
    if (e.key === "Escape") fermer();
  });
});

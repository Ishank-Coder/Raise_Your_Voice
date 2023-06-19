const hamburger = document.querySelector('.hamburger');
const navlist = document.querySelector('.nav-list');

hamburger.addEventListener('click', () => {
    hamburger.classList.toggle('active');
    navlist.classList.toggle('active');
});
document.querySelectorAll(".nav-list li").forEach(n=> n.addEventListener("click", () => {
    hamburger.classList.remove('active');
    navlist.classList.remove('active');
}));
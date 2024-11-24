// frontend/src/index.js
//import './styles/style.scss'; // Asegúrate de tener un archivo SCSS

const btn = document.getElementById('hamburger-menu-btn')
const mobileMenu= document.getElementById('mobile-menu')

/* Hamburger Menu Listener  */

btn.addEventListener('click', navToggle)



/* Function navToggle */

function navToggle(){
btn.classList.toggle('open')
mobileMenu.classList.toggle('hidden')
mobileMenu.classList.toggle('flex')


}


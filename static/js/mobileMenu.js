const btn = document.querySelectorById('hamburger-menu-btn')
const  mobileMenu= document.querySelectorById('mobile-menu')

/* Hamburger Menu Listener  */

btn.addEventListener('click', navToggle)



/* Function navToggle */

function navToggle(){
btn.classList.toggle('open')
mobileMenu.classList.toggle('hidden')
mobileMenu.classList.toggle('flex')
alert('menu')

}
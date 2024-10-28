document.addEventListener("DOMContentLoaded", function () {
    alert('cart.js cargado');
}, { once: true });


// document.addEventListener("DOMContentLoaded", function () {
//     const cartCountElement = document.getElementById('cart-count');
//     let cartCount = parseInt(cartCountElement.textContent) || 0;

//     const addToCartButtons = document.querySelectorAll('.add-to-cart');
//     addToCartButtons.forEach(button => {
//         button.addEventListener('click', function () {
//             const productId = this.getAttribute('data-product-id');

//             // Hacer una solicitud para agregar el producto al carrito
//             fetch(`/agregar_al_carrito/${productId}/`, {
//                 method: 'POST',
//                 headers: {
//                     'X-CSRFToken': getCookie('csrftoken'), // Incluyendo el token CSRF
//                     'Content-Type': 'application/json'
//                 },
//                 body: JSON.stringify({ product_id: productId })
//             })
//             .then(response => {
//                 if (response.ok) {
//                     cartCount++;
//                     cartCountElement.textContent = cartCount; // Actualizar contador
//                     alert('Producto agregado al carrito');
//                 } else {
//                     alert('Error al agregar al carrito');
//                 }
//             })
//             .catch(error => {
//                 console.error('Error:', error);
//             });
//         });
//     });

//     // Función para obtener el token CSRF
//     function getCookie(name) {
//         let cookieValue = null;
//         if (document.cookie && document.cookie !== '') {
//             const cookies = document.cookie.split(';');
//             for (let i = 0; i < cookies.length; i++) {
//                 const cookie = cookies[i].trim();
//                 if (cookie.substring(0, name.length + 1) === (name + '=')) {
//                     cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
//                     break;
//                 }
//             }
//         }
//         return cookieValue;
//     }
// });

// Función para obtener el valor del token CSRF
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Comprobar si este cookie string comienza con el nombre que buscamos
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function isUserAuthenticated() {
    return document.getElementById("user-auth-status").value === "True";
}

// Función para agregar un producto al carrito
function addToCart(productId) {
    if (!isUserAuthenticated()) {
        return;
    }

    fetch(`/customers/add_to_cart/${productId}/`, {
        method: 'POST', // Usamos POST para agregar productos
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken') // Incluimos el token CSRF
        },
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Error en la respuesta del servidor');
        }
        return response.json();
    })
    .then(data => {
        console.log(data.message);
        updateCartDisplay(); // Actualiza la visualización del carrito
    })
    .catch(error => {
        console.error('Error:', error);
        console.log('Hubo un problema al agregar el producto al carrito.');
    });
}

function removeFromCart(productId) {
    fetch(`/customers/remove_from_cart/${productId}/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken') 
        }
    })
    .then(response => {
        if (!response.ok) throw new Error('Error al eliminar el producto del carrito');
        return response.json();
    })
    .then(() => updateCartDisplay())
    .catch(error => console.error('Error:', error));
}

function updateQuantity(productId, change) {
    const newQuantity = change === 1 ? 1 : -1; // Cambia 1 por -1 o viceversa
    fetch(`/customers/update_cart_item/${productId}/?quantity=${newQuantity}`, {
        method: 'GET', // Usamos GET para obtener la cantidad
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken') // Incluimos el token CSRF
        }
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Error al actualizar la cantidad del carrito');
        }
        return response.json();
    })
    .then(data => {
        console.log(data.message); // Mensaje de éxito
        updateCartDisplay(); // Actualiza la visualización del carrito
    })
    .catch(error => {
        console.error('Error:', error);
    });
}


function updateCartDisplay() {
    fetch('/customers/view_cart/')
    .then(response => {
        if (!response.ok) {
            throw new Error('Error en la respuesta del servidor');
        }
        return response.json();
    })
    .then(data => {
        const cartItemsContainer = document.getElementById("cart-items");
        const cartCount = document.getElementById("cart-count");
        const cartTotal = document.getElementById("cart-total");
        const checkoutButton = document.getElementById("checkout-button");

        // Limpiar el contenedor antes de insertar nuevos elementos
        cartItemsContainer.innerHTML = "";

        data.items.forEach(item => {
            const listItem = document.createElement("li");
            listItem.classList.add("cart-item", "d-flex", "justify-content-between", "align-items-center", "mb-2", "p-2", "border", "rounded");
        
            const formattedPrice = new Intl.NumberFormat('es-ES', {
                minimumFractionDigits: 0,
                maximumFractionDigits: 0
            }).format(item.total_price_amount);
        
            listItem.innerHTML = `
                <div class="cart-item-info">
                    <strong>${item.name}</strong><br>
                    <small>Precio: $${formattedPrice}</small>
                </div>
                <div class="quantity-controls">
                    <button class="remove-btn" onclick="removeFromCart(${item.product_id})">
                        <i class="bi bi-trash"></i>
                    </button>
                    <div class="quantity-row">
                        <button class="quantity-btn" onclick="updateQuantity(${item.product_id}, -1)">-</button>
                        <span class="quantity">${item.quantity}</span>
                        <button class="quantity-btn" onclick="updateQuantity(${item.product_id}, 1)">+</button>
                    </div>
                </div>
            `;
            cartItemsContainer.appendChild(listItem);
        });
        
        const formattedTotal = new Intl.NumberFormat('es-ES', {
            minimumFractionDigits: 0,
            maximumFractionDigits: 0
        }).format(data.totals_amount);
        
        // Actualizar el contador y el total del carrito
        cartCount.innerText = data.items.length > 0 ? data.items.length : "0"; // Asegura que se muestre 0 si está vacío
        cartTotal.innerText = formattedTotal;

        // Habilitar o deshabilitar el botón de pagar
        checkoutButton.disabled = data.items.length === 0; 

        // Mostrar u ocultar el contador en el ícono del carrito
        cartCount.style.display = data.items.length > 0 ? "inline" : "none";
    })
    .catch(error => {
        console.error('Error:', error);
    });
}

// Función para iniciar el proceso de pago
function checkout() {
    fetch('/customers/create_order/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken')
        }
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Error al crear el pedido');
        }
        return response.json();
    })
    .then(data => {
        console.log(data.message);
        window.location.href = data.redirect_url;
    })
    .catch(error => {
        console.error('Error:', error);
    });
}

// Función para alternar la visualización del dropdown del carrito
function toggleCartDropdown() {
    const cartDropdown = document.getElementById('cart-dropdown');
    const isVisible = cartDropdown.style.display === 'block';
    cartDropdown.style.display = isVisible ? 'none' : 'block';
}

// Consulta inicial al cargar la página
document.addEventListener("DOMContentLoaded", () => {
    if (!isUserAuthenticated()) {
        return;
    } else {
        updateCartDisplay();
    }
});

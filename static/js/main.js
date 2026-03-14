const api = {
    async getProducts(params = {}) {
        const query = new URLSearchParams(params).toString();
        const response = await fetch(`${API_URL}/products/?${query}`);
        return response.json();
    },

    async getProduct(id) {
        const response = await fetch(`${API_URL}/products/${id}/`);
        return response.json();
    },

    async getCategories() {
        const response = await fetch(`${API_URL}/categories/`);
        return response.json();
    },

    async getCart() {
        const response = await auth.apiFetch(`${API_URL}/cart/`);
        return response.json();
    },

    async addToCart(productId, quantity = 1) {
        const response = await auth.apiFetch(`${API_URL}/cart/add/`, {
            method: 'POST',
            body: JSON.stringify({ product_id: productId, quantity })
        });
        return response.json();
    },

    async updateCartItem(itemId, quantity) {
        const response = await auth.apiFetch(`${API_URL}/cart/items/${itemId}/`, {
            method: 'PUT',
            body: JSON.stringify({ quantity })
        });
        return response.json();
    },

    async removeFromCart(itemId) {
        const response = await auth.apiFetch(`${API_URL}/cart/items/${itemId}/delete/`, {
            method: 'DELETE'
        });
        return response.json();
    }
};

const ui = {
    showNotification(message, type = 'success') {
        const container = document.getElementById('notification-container') || this.createNotificationContainer();
        const notification = document.createElement('div');
        notification.className = `notification ${type}`;
        notification.style.backgroundColor = type === 'success' ? '#10b981' : '#ef4444';
        notification.innerText = message;
        container.appendChild(notification);
        setTimeout(() => notification.remove(), 3000);
    },

    createNotificationContainer() {
        const container = document.createElement('div');
        container.id = 'notification-container';
        document.body.appendChild(container);
        return container;
    },

    updateNavbar() {
        const user = auth.getUser();
        const navLinks = document.querySelector('.nav-links');
        if (user) {
            let links = `
                <li><a href="/">Home</a></li>
                <li><a href="/products/">Products</a></li>
                <li><a href="/cart/">Cart</a></li>
                <li><a href="/orders/">My Orders</a></li>
            `;
            if (user.role === 'admin') {
                links = `
                    <li><a href="/">Home</a></li>
                    <li><a href="/admin-dashboard/">Products</a></li>
                    <li><a href="/admin/orders/">Orders</a></li>
                `;
            }
            links += `<li><a href="#" onclick="auth.logout()">Logout (${user.username})</a></li>`;
            navLinks.innerHTML = links;
        } else {
            navLinks.innerHTML = `
                <li><a href="/">Home</a></li>
                <li><a href="/products/">Products</a></li>
                <li><a href="/login/">Login</a></li>
                <li><a href="/register/">Register</a></li>
            `;
        }
    }
};

window.api = api;
window.ui = ui;

document.addEventListener('DOMContentLoaded', () => {
    ui.updateNavbar();
});

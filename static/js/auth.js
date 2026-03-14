const API_URL = '/api';

const auth = {
    setToken(token, refresh) {
        localStorage.setItem('access_token', token);
        localStorage.setItem('refresh_token', refresh);
    },

    getToken() {
        return localStorage.getItem('access_token');
    },

    logout() {
        localStorage.removeItem('access_token');
        localStorage.removeItem('refresh_token');
        localStorage.removeItem('user');
        window.location.href = '/login/';
    },

    setUser(user) {
        localStorage.setItem('user', JSON.stringify(user));
    },

    getUser() {
        const user = localStorage.getItem('user');
        return user ? JSON.parse(user) : null;
    },

    isAuthenticated() {
        return !!localStorage.getItem('access_token');
    },

    isAdmin() {
        const user = this.getUser();
        return user && user.role === 'admin';
    },

    async register(data) {
        const response = await fetch(`${API_URL}/register/`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(data)
        });
        return response.json();
    },

    async login(username, password) {
        const response = await fetch(`${API_URL}/login/`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ username, password })
        });
        const data = await response.json();
        if (response.ok) {
            this.setToken(data.access, data.refresh);
            this.setUser(data.user);
        }
        return { ok: response.ok, data };
    },

    async apiFetch(url, options = {}) {
        const token = this.getToken();
        const headers = { ...options.headers };
        
        // Don't set Content-Type for FormData, let the browser do it with the boundary
        if (!(options.body instanceof FormData)) {
            headers['Content-Type'] = 'application/json';
        }
        
        if (token) {
            headers['Authorization'] = `Bearer ${token}`;
        }
        
        let response = await fetch(url, { ...options, headers });
        
        if (response.status === 401 && localStorage.getItem('refresh_token')) {
            // Token expired, attempt refresh
            const refreshResponse = await fetch(`${API_URL}/token/refresh/`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ refresh: localStorage.getItem('refresh_token') })
            });
            if (refreshResponse.ok) {
                const data = await refreshResponse.json();
                this.setToken(data.access, localStorage.getItem('refresh_token'));
                headers['Authorization'] = `Bearer ${data.access}`;
                response = await fetch(url, { ...options, headers });
            } else {
                this.logout();
            }
        }
        return response;
    }
};

window.auth = auth;

import axios from "axios";

export default defineNuxtPlugin((NuxtApp) => {
    if (process.client) {
        const csrfToken = document.cookie.match(/csrftoken=([^;]+)/);
        if (csrfToken) {
            axios.defaults.withCredentials = true;
            axios.defaults.headers.common['X-CSRFToken'] = csrfToken[1];
        } else {
            console.error("CSRF token not found");
        }
    }

    axios.defaults.baseURL = "http://localhost:8001/api/";

    return {
        provide: {
            axios: axios,
        },
    };
});

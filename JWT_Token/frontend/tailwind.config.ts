/** @type {import ('tailwindcss').Config }  */


module.exports = {
    content: [
        "./components/**/*.{js,vue,ts}",
        "./layouts/**/*.vue",
        "./pages/**/*.vue",
        "./plugins/**/*.{js,ts}",
        "./nuxt.config.{ts,js}", // Nuxt konfiguratsiya faylini qo‘shish
        "./app.vue", // `app.vue` faylini qo‘shish
        "./assets/**/*.{js,ts,vue}" // Agar assets'dan ham foydalanilsa, qo‘shish
    ],
    theme: {
        extend: {
            colors: {
                darkPrimary: '#1d2633',
                darkSecondary: '#2c384a',
                darkText : "white",
                lightPrimary: "#ffffff",
                lightSecondary: "#fefefe",
                lightText: "#000000"
            },
        },
    },
    darkMode: 'class',
    plugins: []
}
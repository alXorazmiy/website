import './assets/css/base.css'
import './assets/css/main.css'
import './assets/css/login.css'
import './assets/css/loader.css'
import './assets/css/info.css'
import './assets/css/home.css'

import { createApp } from 'vue'
import { createPinia } from 'pinia'

import { library } from '@fortawesome/fontawesome-svg-core'
import '@/axios'


import App from './App.vue'
import router from './router'

const app = createApp(App)

app.use(createPinia())
app.use(router)

app.mount('#app')

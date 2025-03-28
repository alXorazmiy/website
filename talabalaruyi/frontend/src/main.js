import './assets/css/base.css'
import './assets/css/main.css'
import './assets/css/home.css'
import './assets/css/modal.css'
import './assets/css/sidebar.css'
import './assets/css/table.css'
import './assets/css/info.css'
import 'swiper/css'
import 'swiper/css/navigation'
import 'vue3-easy-data-table/dist/style.css';

import { createApp } from 'vue'
import { createPinia } from 'pinia'
import Vue3EasyDataTable from 'vue3-easy-data-table';
import naive from 'naive-ui'
import '@/axios'


import App from './App.vue'
import router from './router'

const app = createApp(App)

app.use(createPinia())
app.use(naive)
app.use(router)
app.component('EasyDataTable', Vue3EasyDataTable);

app.mount('#app')


import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'
import router from './router'


import './assets/css/base.css'
import './assets/css/adminpage.css'
import './assets/css/sidebar.css'
import './assets/css/login.css'
import './assets/css/main.css'
import './assets/css/table.css'
import './assets/css/shop.css'
import './assets/css/menu.css'
import 'vue3-easy-data-table/dist/style.css';


import Vue3EasyDataTable from 'vue3-easy-data-table';
import { library } from '@fortawesome/fontawesome-svg-core'
import {createI18n} from 'vue-i18n'
import naive from 'naive-ui'
import '@/axios'



import UZ from './locale/uz.json'
import RU from './locale/ru.json'
import EN from './locale/en.json'


const i18n = createI18n({
    locale : localStorage.getItem('language'),
    messages : {
        UZ: UZ,
        RU: RU,
        EN: EN,
    }
})




const app = createApp(App)
app.use(createPinia())
app.use(router)
app.use(naive)
app.use(i18n)
app.component('EasyDataTable', Vue3EasyDataTable);
app.mount('#app')

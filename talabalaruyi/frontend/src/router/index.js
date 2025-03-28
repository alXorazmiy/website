import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/students',
      name: 'students',
      component: () => import('../views/StudentsView.vue')
    },
    {
      path: '/payments',
      name : 'payments',
      component: () => import ('../views/PaymentsView.vue')
    }
  ]
})

export default router

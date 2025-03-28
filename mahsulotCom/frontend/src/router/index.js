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
            path : '/login',
            name : 'login',
            component : ()=> import('../views/login/LoginView.vue')
        },
        {
            path: '/admin',
            name: 'admin',
            component : ()=> import('../views/admin/adminPage.vue')
        },
        {
            path: '/admin/shops',
            name : "adminshops",
            component : ()=> import('../views/admin/shops/shopsPage.vue')
        },
        {
            path: "/admin/shops/:id",
            name: "adminshopsdetail",
            component: ()=> import('../views/admin/shopDetail/ShopDetailPage.vue')
        },
        {
            path: '/admin/users',
            name : "adminusers",
            component : ()=> import('../views/admin/users/usersPage.vue')
        },
        // {
        //   path: '/about',
        //   name: 'about',
        //   // route level code-splitting
        //   // this generates a separate chunk (About.[hash].js) for this route
        //   // which is lazy-loaded when the route is visited.
        //   component: () => import('../views/AboutView.vue')
        // }
    ]
})

export default router

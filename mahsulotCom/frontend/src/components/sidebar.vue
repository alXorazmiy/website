<template>
    <div class="sidebar" :class = "sidebar_active == true? 'sidebar_active' : '' ">
        <div class="logo">
            <div class="logo-img">
                <img src="../assets/images/logo.png" alt="" @click="sidebar_open">
            </div>
            <div class="logo-title">
                <p>mahsulot.com</p>
                <i class="fa-solid fa-circle-chevron-left" @click="sidebar_close"></i>
            </div>
        </div>

        <div class="nav-links">
            <RouterLink to="/admin">
                <div class="nav-link" :class="sidebar_link == 1 ? 'active-link' : '' "  @click="sidebarLink(1)">
                    <div class="nav-link_icon"><i class="fa-solid fa-house"></i></div>
                    <div class="nav-link_name">{{ $t('Home') }}</div>
                    <span class = 'nav-link_span'>{{ $t('Home') }}</span>
                    <span class="nav-link_hover"></span>
                </div>
            </RouterLink>
            <RouterLink to="/admin/shops">
                <div class="nav-link " :class="sidebar_link == 2 ? 'active-link' : '' " @click="sidebarLink(2)">
                    <div class="nav-link_icon"><i class="fa-solid fa-shop"></i></div>
                    <div class="nav-link_name">{{ $t('Shops') }}</div>
                    <span class = 'nav-link_span'>{{ $t('Shops') }}</span>
                    <span class="nav-link_hover"></span>

                </div>
            </RouterLink>
            <!-- <RouterLink to="">
                <div class="nav-link"  :class="sidebar_link == 3 ? 'active-link' : '' " @click="sidebarLink(3)">
                    <div class="nav-link_icon"><i class="fa-solid fa-cart-shopping"></i></div>
                    <div class="nav-link_name">{{ $t('Products') }}</div>
                    <span class = 'nav-link_span'>{{ $t('Products') }}</span>
                    <span class="nav-link_hover"></span>

                </div>
            </RouterLink> -->
            <RouterLink to="/admin/users" v-show="userStore.admin == 'super_admin'">
                <div class="nav-link"  :class="sidebar_link == 4 ? 'active-link' : '' " @click="sidebarLink(4)">
                    <div class="nav-link_icon"><i class="fa-solid fa-users"></i></div>
                    <div class="nav-link_name">{{ $t('users') }}</div>
                    <span class = 'nav-link_span'>{{ $t('users') }}</span>
                    <span class="nav-link_hover"></span>

                </div>
            </RouterLink>
           
            
            
            <div class="logout" @click="logout">
          
                <div class="nav-link">
                    <div class="nav-link_icon"><i class="fa-solid fa-right-from-bracket"></i></div>
                    <div class="nav-link_name">{{ $t('logout') }}</div>
                    <span class = 'nav-link_span'>{{ $t('logout') }}</span>
                <span class="nav-link_hover"></span>

           
            </div>
        </div>
        </div>

       

    </div>
  
</template>

<script setup>
    import { ref } from "vue";
    import { useControllerStore } from "@/stores/controller";
import { useUserStore } from "@/stores/users";
import { useRouter } from "vue-router";
    const controllerStore = useControllerStore()
    const userStore = useUserStore()
    const sidebar_active = ref(false)
    const sidebar_link = ref(1)
    const router = useRouter()


    function sidebar_close(){
        controllerStore.mobile_sidebar = false
        controllerStore.sidebar_open = true
        sidebar_active.value = true
    }

    function sidebar_open(){
        controllerStore.sidebar_open = false
        sidebar_active.value = false
    }

    function sidebarLink(id){
        controllerStore.mobile_sidebar = false
        sidebar_link.value = id
    }

    function logout(){
        localStorage.removeItem('access_token')
        controllerStore.is_admin = false
        userStore.admin = ''
        router.push('/')
    }



</script>

<style>

</style>
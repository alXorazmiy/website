

<template>
 
    <div>
        <div class="loader-container" v-show="controllerStore.is_loader">
            <Loader />
        </div>
        <div class="sidebar-container" :class="controllerStore.sidebar_open == true ? 'sidebar-active': ''">
            <Sidebar />
        </div>
        <div class="menu" >
            <i class="fa-solid fa-bars" @click="sidebar_open(true)"></i>
        </div>
        <div class="info-container">
            <Info />
        </div>
        <div class="page-container" @click="sidebar_open(false)">
            <RouterView />
        </div>
    </div>  
</template>



<script setup>
    import { onMounted } from 'vue'
    import { RouterLink, RouterView } from 'vue-router'
    import Loader from './components/loader.vue'
    import Sidebar from './components/sidebar.vue'
    import Info from './components/info.vue'
    import {useControllerStore} from './stores/controller'

    const controllerStore = useControllerStore()
    function sidebar_open(if_){
        controllerStore.sidebar_open = if_
    }
    onMounted(()=>{
        // document.body.classList.add("dark-mode-variables")
        controllerStore.is_loader = false
    })

</script>


<style scoped>

</style>

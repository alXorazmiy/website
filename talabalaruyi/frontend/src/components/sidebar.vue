<template>
    <div class="sidebar">
        <div class="sidebar-logo">
            <img src="../assets/images/logo.png" alt="">
        </div>
        <div class="sidebar-links">
            <div class="sidebar-link">
                <RouterLink to="/" class="nav-link " @click = 'sidebar_close'>
                    <i class="fa-solid fa-building"></i>
                    <p>Xonalar</p>
                </RouterLink>
                
            </div>
            <div class="sidebar-link">
                <RouterLink to="/students" class="nav-link " @click = 'sidebar_close'>
                    <i class="fa-solid fa-graduation-cap"></i>
                    <p>Talabalar</p>
                </RouterLink>

            </div>
            <div class="sidebar-link">
                <RouterLink to="/payments" class="nav-link " @click = 'sidebar_close'>
                    <i class="fa-solid fa-money-check-dollar"></i>
                    <p>To'lovlar</p>
                </RouterLink>

            </div>
        </div>
    </div>
  
</template>

<script setup>
    
    import { useControllerStore } from '@/stores/controller';
    const controllerStore = useControllerStore()

    function sidebar_close(){
        controllerStore.sidebar_open = false
    }

</script>

<style>

</style>
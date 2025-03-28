<template>
    <div class="profilemenu">
        <div class="profilemenu-items">
            <img src="../assets/icons/user.png" alt="">
            <p @click="bodyshow">{{ userStore.user.email }}</p>
            <i class="fa-solid fa-caret-down" @click="bodyshow"></i>
            
            <div class="profilemenu-body" v-show="menubody_if">
                <p>Profile</p>
                <p @click="logout">Logout</p>
            </div>
        </div>
    </div>

</template>

<script setup>
    import { ref } from "vue";  
    import { useRouter } from "vue-router";
    import { useUserStore } from "../stores/user";
    const userStore = useUserStore()
    const menubody_if = ref(false)
    const router = useRouter()

    function bodyshow(){
        if(menubody_if.value == true) {
            menubody_if.value = false 
        }else {
            menubody_if.value = true
        }
    }

    function logout(){
        localStorage.removeItem('access_token')
        router.push('/login')
    }   

</script>

<style>

</style>
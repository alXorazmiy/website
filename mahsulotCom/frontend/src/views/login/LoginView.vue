<template>

    <div class="container">
        <div class="login">
            <form @submit.prevent="loginSubmit">
                <div class="login-form-logo">
                    <img src="../../assets/images/logo.png" alt="">
                    <p>mahsulotlarCom</p>
                </div>
                <div class="login-form-input">
                    <i class="fa-solid fa-user"></i>
                    <input type="text" placeholder="Username" v-model="username">
                </div>
                <div class="login-form-input">

                    <i class="fa-solid fa-lock"></i>
                    <input type="password" placeholder="Password" v-model="password">
                </div>
                <div class="login-form-checkbox">
                    <input type="checkbox" >
                    <p>{{ $t('rememberme') }}</p>
                </div>
                <div class="login-form-button">
                    <button type="submit" @click="loginSubmit">{{ $t('signin') }}</button>
                </div>
            </form>
        </div>
    </div>
  
</template>

<script setup>
    import { useMessage } from 'naive-ui'
    import { ref } from 'vue'
    import axios from 'axios'
    import {useControllerStore} from '../../stores/controller'
    import { useRouter } from 'vue-router'
import { useUserStore } from '@/stores/users'

    const username = ref('xorazmshox')
    const password = ref('932826557')
    const remember = ref()
    
    const controllerStore = useControllerStore()
    const userStore = useUserStore()
    const router = useRouter()


    function loginSubmit(){
        const request = {
            username : username.value,
            password : password.value
        }
     
        axios.post('login/', request)
            .then((data) =>{
                if (data.status ==200) {
                    localStorage.setItem("access_token", data.data.token)
                    controllerStore.is_admin = true
                    userStore.admin = data.data.user.role
                    router.push('admin')
                    console.log(userStore.admin)


                }
                else{
                    const message = useMessage()
                    message.error("Error")
                }
            })
            .catch((error)=>{

            })
        
    }




</script>

<style>

</style>
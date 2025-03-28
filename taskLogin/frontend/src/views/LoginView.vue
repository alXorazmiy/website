<template>
    <div class = "login-container">
        <div class="login-form">
            <form @submit.prevent="login">
                <p>LOGIN</p>
                <div class = 'form-email' :class = "formEmailController == 'uncorrect' ? 'uncorrect': formEmailController == 'correct' ? 'correct': 'empty'">
                    <input type="text" v-model="formController.email" placeholder="Email@gmail.com" @focus="focusEmail" @input = 'inputEmail'>
                    <i class="fa-solid fa-envelope" :class = "formEmailController == 'uncorrect' ? 'uncorrectIcon': formEmailController == 'correct' ? 'correctIcon': 'empty'"></i>
                </div>

                <div class = 'form-password' :class = "formPasswordController == 'uncorrect' ? 'uncorrect': formPasswordController == 'correct' ? 'correct': 'empty'">
                    <input type="text" v-model ="formController.password" placeholder="xx-xx-xx" @focus="focusPassword" @input = "inputPassword">
                    <i class="fa-solid fa-lock"  :class = "formPasswordController == 'uncorrect' ? 'uncorrectIcon': formPasswordController == 'correct' ? 'correctIcon': 'empty'"></i>
                </div>
                <div class = 'form-remember'>
                    <input type="checkbox">
                    <span>Remember me</span>
                </div>
                <div class = 'form-button' @click="login">
                    <button type="submit" v-show ="buttonController == false">Login</button>
                    <i class="fa-solid fa-spinner" v-show="buttonController"></i>
                </div>
            </form>
        </div>
    </div>
</template>

<script setup>  
    import { ref } from "vue";  
    import { useInfoStoreController } from "../stores/infos";
    import axios from 'axios'
    import { useRouter } from "vue-router";
    import { useUserStore } from "../stores/user";
    const infoStore = useInfoStoreController()
    const userStore = useUserStore()
    const router = useRouter()

    const formController = ref({
        email : "",
        password : ""
    })
    const formEmailController = ref('empty')
    const formPasswordController = ref('empty')
    const buttonController = ref(false)
    
    function focusEmail(){
        if (formController.value.password == ''){
            formPasswordController.value = 'empty'
        }
        if(formEmailController.value != 'correct'){
            formEmailController.value = 'uncorrect'
        }
    }

    function focusPassword(){
        if (formController.value.email == ''){
            formEmailController.value = 'empty'
        }
        if(formPasswordController.value != 'correct'){
            formPasswordController.value = 'uncorrect'
        }
    }

    function inputEmail(e) {
        if (formController.value.email.includes('@gmail.com')){
            formEmailController.value = 'correct'
        }
        else if (formController.value.email.includes('@mail.ru')){
            formEmailController.value = 'correct'
        }
        else {
            formEmailController.value = 'uncorrect'
        }
    }

    function inputPassword(e) {
        let password = formController.value.password.replaceAll('-', '')
        let pairs = password.match(/.{1,2}/g);
        let result = pairs.join('-')
        formController.value.password = result

        if (password.length > 5 && password.length % 2 == 0){
            formPasswordController.value = 'correct'
        }else{
            formPasswordController.value = 'uncorrect'
        }

    }
    
    function login(){

        const timestamp = Date.now()
        if (formEmailController.value == 'correct' && formPasswordController.value == 'correct'){
            buttonController.value = true
            let request = {
                email: formController.value.email,
                password: formController.value.password.replaceAll('-', '')
            }

            axios.post("login/", request)
                .then((data)=>{
                    if(data.status == 200){
                        localStorage.setItem('access_token', data.data.token)
                        buttonController.value = false
                        userStore.user.email = data.data.user[0].email

                        router.push('/')
                    }
                }).catch((err)=>{
                    infoStore.info_if = true
                    let error = {
                        id : timestamp,
                        type: "error",
                        text: "Email and password are incorrect"
                    }
                    infoStore.info_list.push(error)
                    buttonController.value = false

                })
        }
        else if (formEmailController.value != 'correct' && formPasswordController.value != 'correct') {
            infoStore.info_if = true
            let error = {
                id : timestamp,
                type: "error",
                text: "Email and password are incorrect"
            }
            infoStore.info_list.push(error)
        }
        else if (formEmailController.value != 'correct'){
            infoStore.info_if = true
            let error = {
                id : timestamp,
                type: "error",
                text: "Email is incorrect"
            }
            infoStore.info_list.push(error)
        }
        else if (formPasswordController.value != 'correct'){
            infoStore.info_if = true
            let error = {
                id : timestamp,
                type: "error",
                text: "Password is incorrect"
            }
            infoStore.info_list.push(error)
        }
    }

    

</script>

<style>

</style>
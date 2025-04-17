<template>
    <div class = "w-full h-[100vh] top-0 left-0 bg-[#1d2633]" >
        <div class="flex justify-center items-center h-full">
            <div class="w-[400px] h-[500px]  rounded ">
                <form @submit.prevent = "register" class="h-full w-full p-3 flex justify-around flex-col items-center relative ">
                    <span class = "text-white font-bold text-[24px]" >Sign in</span>
                    <div class = "w-[80%] mx-auto" >
                        <div class="bg-[#2c384a] mb-3 p-3 flex items-center rounded">
                            <Icon name = "material-symbols:person" size = "20" class="text-white" />
                            <input v-model="name" type="text" placeholder="Name" class=" bg-transparent outline-none ml-2 text-white">
                        </div>
                        <div class="bg-[#2c384a] mb-3 p-3 flex items-center rounded">
                            <Icon name = "material-symbols:mail-rounded" size = "20" class="text-white" />
                            <input v-model="email" type="email" placeholder="Email" class=" bg-transparent outline-none ml-2 text-white">
                        </div>
                        <div class="bg-[#2c384a] mb-3 p-3 flex items-center rounded">
                            <Icon name = "material-symbols:lock" size = "20" class="text-white" />
                            <input v-model="password" type="password" placeholder="Password" class=" bg-transparent outline-none ml-2 text-white">
                        </div>
                        <div class="bg-[#2c384a] mb-3 p-3 flex items-center rounded">
                            <Icon name = "material-symbols:lock" size = "20" class="text-white" />
                            <input v-model="confirmPassword" type="password" placeholder="Confirm password" class=" bg-transparent outline-none ml-2 text-white">
                        </div>
                        

                        <button type="submit" class="bg-[#0067fd] w-full h-10 p-2  flex items-center justify-center my-8 ">
                            <Icon v-if = "buttonLoading"  name = "ri:loader-2-fill" class = "text-white animate-spin duration-200" size = "20" />
                            <span v-else class = "text-white font-bold " >Sign in</span>
                        </button>
                        <hr class="border border-gray-500 mb-8">
                       
                        <NuxtLink to="/login">
                            <div class="text-white border py-2 flex items-center justify-center ">
                                Log in
                            </div>
                        </NuxtLink>
                    </div>
                   

                </form>
            </div>
        </div>
    </div>
</template>

<script setup>

import axios from "axios"
import {useRouter} from 'vue-router'

const router = useRouter()

const buttonLoading = ref(false)
const name = ref('')
const email = ref(null)
const password = ref(null)
const confirmPassword = ref(null)



const register = () =>{
    buttonLoading.value = true

    if (email.value == null) {
        // notification
    }
    else if (password.value == null) {
        // notification
    }
    else if (password.value != confirmPassword.value){
        // notification
    }

    else {
        let data = {
            name: name.value,
            email : email.value,
            password : password.value,
        }
        axios.post("http://localhost:8001/api/register/", data,{ withCredentials: true})
            .then((value)=>{
                if (value.status == 201){
                    buttonLoading.value = false
                    router.push("/")
                }
            })
            .catch((error)=>{
                buttonLoading.value = false
            })
    }


}

</script>


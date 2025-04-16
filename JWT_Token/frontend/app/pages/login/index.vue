<template>
    <div class = "w-full h-[100vh] top-0 left-0 bg-[#0d1117]" >
        <div class="flex justify-center items-center h-full">
            <div class="w-[400px] h-[400px] bg-[#151b23] rounded ">
                <form @submit.prevent = "login" class="h-full w-full p-3 flex justify-around flex-col items-center relative ">
                    <span class = "text-white font-bold text-[20px]" >Login</span>
                    <div class = "w-[80%] mx-auto" >
                        <div class="bg-[#1d2633] mb-3 p-3 flex items-center rounded">
                            <Icon name = "material-symbols:mail-rounded" size = "20" class="text-white" />
                            <input v-model="email" type="email" placeholder="Email" class=" bg-transparent outline-none ml-2 text-white">
                        </div>
                        <div class="bg-[#1d2633] mb-3 p-3 flex items-center rounded">
                            <Icon name = "material-symbols:lock" size = "20" class="text-white" />
                            <input v-model="password" type="password" placeholder="Password" class=" bg-transparent outline-none ml-2 text-white">
                        </div>
                        <div class="my-3 text-gray-400" >
                            <input v-model="remember"  type="checkbox" class="mr-3 cursor-pointer">
                            <span>Remember me</span>
                        </div>

                        <button type="submit" class="bg-[#238636] w-full h-10 p-2 rounded flex items-center justify-center mb-8 ">
                            <Icon v-if = "buttonLoading"  name = "ri:loader-2-fill" class = "text-white animate-spin duration-200" size = "20" />
                            <span v-else class = "text-white font-bold " >Login</span>
                        </button>
                    </div>
                    <div class = "absolute bottom-2" >
                        <span class="text-gray-400">You have not account?</span>
                        <NuxtLink to="/signup" class="ml-3 text-blue-400 cursor-pointer">Sign up</NuxtLink>
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
const email = ref('c@gmailc.om')
const password = ref('c123456789')
const remember = ref(true)


const login = () =>{
    buttonLoading.value = true

    let data = {
        email : email.value,
        password : password.value,
    }
    axios.post("http://localhost:8001/api/login/", data,{ withCredentials: true})
        .then((value)=>{
            console.log(value)
            if (value.status == 200){
                buttonLoading.value = false
                router.push("/")
            }
        })
        .catch((error)=>{
            buttonLoading.value = false
            console.log(error)
        })

}

</script>


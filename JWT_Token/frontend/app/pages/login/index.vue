<template>
    <div class = "w-full h-[100vh] top-0 left-0 dark:bg-darkPrimary bg-lightPrimary" >
        <div class="flex justify-center items-center h-full">
            <div class="w-[400px] h-[450px] rounded ">
                <form @submit.prevent = "login" class="h-full w-full p-3 flex justify-around flex-col items-center relative ">
                    <span class = "dark:text-white text-black font-bold text-[24px]" >Log in</span>
                    <div class = "w-[80%] mx-auto dark:text-white text-black" >
                        <div class="dark:bg-darkSecondary bg-lightSecondary mb-3 p-3 flex items-center rounded">
                            <Icon name = "material-symbols:mail-rounded" size = "20"  />
                            <input v-model="email" type="email" placeholder="Email" class=" bg-transparent outline-none ml-2 ">
                        </div>
                        <div class="dark:bg-darkSecondary bg-lightSecondary mb-3 p-3 flex items-center rounded">
                            <Icon name = "material-symbols:lock" size = "20"  />
                            <input v-model="password" type="password" placeholder="Password" class=" bg-transparent outline-none ml-2 ">
                        </div>
                        <div class="my-8 text-gray-400" >
                            <input v-model="remember"  type="checkbox" class="mr-3 cursor-pointer">
                            <span>Remember me</span>
                        </div>

                        <button type="submit" class="bg-[#0067fd] w-full h-10 p-2  flex items-center justify-center mb-8 ">
                            <Icon v-if = "buttonLoading"  name = "ri:loader-2-fill" class = "text-white animate-spin duration-200" size = "20" />
                            <span v-else class = "text-white  " >Login</span>
                        </button>
                        <hr class="border border-gray-500 mb-8">
                       
                        <NuxtLink to="/signup">
                            <div class="border dark:border-white border-black py-2 flex items-center justify-center " >
                                Sign up
                            </div>
                        </NuxtLink>

    
                    </div>

                </form>
            </div>
        </div>
    </div>
</template>

<script setup>

const {$axios} = useNuxtApp()
const router = useRouter()
const buttonLoading = ref(false)
const email = ref('b@gmail.com')
const password = ref('b123456')
const remember = ref(true)


const login = () =>{
    buttonLoading.value = true

    let data = {
        email : email.value,
        password : password.value,
    }
    try {
        $axios.post("login/", data)
            .then((value)=>{
                if (value.status == 200){
                    buttonLoading.value = false
                    
                    router.push("/")
                }
            })
            .catch((error)=>{
                buttonLoading.value = false
                console.log(error)
            })
    } catch{

    }

}

</script>


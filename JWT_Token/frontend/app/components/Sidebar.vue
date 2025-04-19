<template>
    <div class="fixed z-10 w-[250px] h-[100vh] top-0 left-0 dark:bg-darkSecondary bg-[#1d2d5b]">

        <div class="flex justify-start items-center  flex-col relative h-full w-full">
            <div class="h-[100px] mt-10 flex flex-col items-center text-white">
                    <img  v-if="$userStore.image == null" src="@/assets/images/user.jpeg" alt="" class = "rounded-full max-w-[100px]">
                    <NuxtImage v-else src="~/assets/images/user.jpeg"  format="webp" />
                    <p class = "mt-2 ">{{ $userStore.name }}</p>
                    <p class = "flex items-center" >
                        <Icon name = "material-symbols:mail-rounded" size = "20"  />
                        <span class="ml-2">{{ $userStore.email }}</span>
                    </p>
            </div>

            <div class="mt-[100px] w-full  text-white ">
                <div class="grid px-[30px]">
                    <NuxtLink to="/" class="flex items-center space-x-5  p-2 rounded-md cursor-pointer transition-all duration-200">
                        <Icon name="ic:round-home" size="24" />
                        <span>{{ $t('Home') }}</span>
                    </NuxtLink>
                    <NuxtLink to="/codes" class="flex items-center space-x-5  p-2 rounded-md cursor-pointer transition-all duration-200">
                        <Icon name="solar:code-bold-duotone" size="24" />
                        <span>{{ $t('codes') }}</span>
                    </NuxtLink>
                    <NuxtLink to="/settings" class="flex items-center space-x-5  p-2 rounded-md cursor-pointer transition-all duration-200">
                        <Icon name="material-symbols:settings-rounded" size="24" />
                        <span>{{ $t('settings') }}</span>
                    </NuxtLink>
                    <NuxtLink to="/about" class="flex items-center space-x-5  p-2 rounded-md cursor-pointer transition-all duration-200">
                        <Icon name="cib:about-me" size="24" />
                        <span>{{ $t('about') }}</span>
                    </NuxtLink>
                </div>
            </div>
            
            <div class="absolute bottom-20 left-0 right-0   text-white  text-center">
                    <button class = "flex items-center justify-center mx-auto" @click = "logout">
                        <Icon name = "line-md:log-out" size = "24"/>
                        <span class=" ml-3" >{{ $t('logout') }}</span>
                    </button>
            </div>

        </div>
    </div>
</template>

<script setup>
const {$axios, $userStore} = useNuxtApp()

const router = useRouter()


const logout = () =>{
    try {
        $axios.post("logout/")
            .then((value)=>{
                if (value.status == 200){

                    router.push("/login")
                }
            })
            .catch((error)=>{
                console.log(error)
            })
    } catch{

    }
}


</script>


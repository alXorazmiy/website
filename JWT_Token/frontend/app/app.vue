<template>
    <div  v-if ="loader" class="fixed z-50 w-full h-[100vh] flex items-center justify-center bg-[#1d2633]">
        <Loader />
    </div>
    <NuxtPage v-else />
</template>

<script setup>


const loader = ref(true)

const { setLocale } = useI18n()
const {$axios} = useNuxtApp()
const router = useRouter()
onMounted( async ()=> {
    try {
        const savedLocale = localStorage.getItem('locale')
        if (savedLocale) {
            await setLocale(savedLocale)
        }
        $axios.get("http://localhost:8001/api/user/")
            .then((value)=>{
                loader.value = false
                
            })
            .catch((error)=>{
                router.push("/login")    
                loader.value = false
            })
    }catch{

    }

})

</script>
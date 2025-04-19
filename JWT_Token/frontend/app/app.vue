<template>
    <div  v-if ="$generalStore.isLoader" class="fixed z-50 w-full h-[100vh] flex items-center justify-center dark:bg-darkPrimary bg-white">
        <Loader />
    </div>
    <NuxtPage v-else />
</template>

<script setup>
import { onBeforeMount, onMounted } from 'vue'
const {$axios, $generalStore, $userStore} = useNuxtApp()
const router = useRouter()


onBeforeMount( async () => {
    if ($generalStore.isDark) {
        document.documentElement.classList.add('dark')
    } else {
        document.documentElement.classList.remove('dark')
    }
})



onMounted( async ()=> {
    try {
        $generalStore.isLoader = true;
        $axios.get("http://localhost:8001/api/user/")
            .then((value) => {
                if (value.status == 200) {
                    $userStore.setData(value.data)
                    $generalStore.isLoader = false;
                    
                }
            })
            .catch((error) => {
                $generalStore.isLoader = false;
              
                router.push("/login");
            });
    }catch{
        setTimeout(() => {
            $generalStore.isLoader = false;
        }, 1000);
    }

})

</script>
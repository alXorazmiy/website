
<template>
    <div>
        <div class="loader-container" v-show = "storeController.loader">
            <Loader />
        </div>
        <div class="info-container" v-show = 'infoStore.info_if'>
            <Info />
        </div>
        <div>
            <RouterView />
        </div>
    </div>
</template>

<script setup>
    import Loader from './components/loader.vue'
    import Info from './components/info.vue'
    import { onMounted } from 'vue'
    import { RouterLink, RouterView, useRouter } from 'vue-router'
    import {useStoreController} from './stores/controller'
    import {useInfoStoreController} from './stores/infos'
    import {useUserStore} from './stores/user'
    import axios from 'axios'
    const router = useRouter()

    const userStore = useUserStore()
    const infoStore = useInfoStoreController()
    const storeController = useStoreController()

    onMounted(()=>{      
        storeController.loader = true
        axios.get('login/', {
            headers : {
                Authorization : `token ${localStorage.getItem('access_token')}`
            }
        }).then((data)=>{
            console.log(data)
            if(data.data.status == 200){
                userStore.user.email = data.data.user[0].email
            }else{
                router.push('/login')
            }
        }).catch((error)=>{
            router.push('/login')
        })
        
        storeController.loader = false
    })

</script>


<style scoped>

a.router-link-exact-active {
  color: var(--color-text);
}

a.router-link-exact-active:hover {
  background-color: transparent;
}

a {
  display: inline-block;
  padding: 0 1rem;
  border-left: 1px solid var(--color-border);
}


</style>

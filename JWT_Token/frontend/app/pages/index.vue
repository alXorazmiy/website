


<template>
    <div class = "w-full h-[100vh] top-0 left-0 bg-[#0d1117]" >

    </div>
</template>

<script setup>
import { onMounted } from 'vue';
import { useRouter } from 'vue-router';
import axios from 'axios'


const router = useRouter()
onMounted(()=>{
    axios.get("http://localhost:8001/api/user/", { withCredentials: true })
        .then((value)=>{
            console.log(value)
        })
        .catch((error)=>{
            router.push("/login")
        })
})

</script>


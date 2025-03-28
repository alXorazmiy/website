
<template>
    <div class="infos">
        <div class="info-items" v-for="item in infoStore.info_list" :key="item">
            <div   v-if = "item.type == 'error'" class = 'info-error'>
                <span></span>
                <i class="fa-solid fa-circle-exclamation"></i>
                <p>{{ item.text }}</p>
                <i class="fa-solid fa-xmark" @click="info_delete(item.id)"></i>
            </div>
            <div   v-if = "item.type == 'success'" class = 'info-success'>
                <span></span>
                <i class="fa-solid fa-circle-check"></i>
                <p>{{ item.text }}</p>
                <i class="fa-solid fa-xmark" @click="info_delete(item.id)"></i>
            </div>
            <div   v-if = "item.type == 'info'" class = 'info-info'>
                <span></span>
                <i class="fa-solid fa-circle-info"></i>
                <p>{{ item.text }}</p>
                <i class="fa-solid fa-xmark" @click="info_delete(item.id)"></i>
            </div>
            <div   v-if = "item.type == 'warning'" class = 'info-warning'>
                <span></span>
                <i class="fa-solid fa-triangle-exclamation"></i>
                <p>{{ item.text }}</p>
                <i class="fa-solid fa-xmark" @click="info_delete(item.id)"></i>
            </div>
        </div>
    </div>
  
</template>

<script setup>

    import { useInfoStore } from '@/stores/infos';
    import { onMounted } from 'vue';
    const infoStore = useInfoStore()

    function info_delete(id){
        let list = infoStore.info_list.filter(item =>  item.id != id)
        infoStore.info_list = list
    }

    function delete_info() {
        if(infoStore.info_if){
            let list = infoStore.info_list.slice(1)
            infoStore.info_list = list
        }
        
    }

    onMounted(()=>{
        // setInterval(delete_info, 4000);
    })

</script>

<style>

</style>

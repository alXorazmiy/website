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

    import { useInfoStoreController } from '@/stores/infos';
    const infoStore = useInfoStoreController()

    function info_delete(id){
        console.log('hello')
        let list = infoStore.info_list.filter(item =>  item.id != id)
        infoStore.info_list = list
    }

</script>

<style>

</style>
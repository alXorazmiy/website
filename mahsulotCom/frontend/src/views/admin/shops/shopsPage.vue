<template>
    <div class="table-container">
        <ShopHeader />
        <div class="table-search">
            <div>
                <i class="fa-solid fa-magnifying-glass"></i>
                <input type="text" v-model="searchValue" :placeholder="$t('search')">
            </div>
        </div>
        <EasyDataTable
            :headers="headers"
            :items="shopStore.shopList"
            table-class-name="customize-table"
            :search-value="searchValue"
        >
            <template #header-id="{}">
                        <p>{{ $t('id') }}</p>
            </template>
            <template #header-image="{}">
                        <p>{{ $t('image') }}</p>
            </template>
            <template #header-title="{}">
                        <p>{{ $t('title') }}</p>
            </template>
            <template #header-tools="{}">
                        <p><i class="fa-solid fa-ellipsis-vertical"></i></p>
            </template>
            <template #item-image="{image}">
                        <div class = 'table-image'>
                            <img :src="image" alt="">
                        </div>
            </template>
            <template #item-tools="{id}">
                <i class="fa-solid fa-right-to-bracket table-login"  @click="shopDetail(id)"></i>
            </template>
        </EasyDataTable>
          
    </div>
</template>

<script setup>

    import axios from 'axios';
    import { onMounted,ref } from 'vue';
    import ShopHeader from './widget/header.vue'
    import {useShopStore} from '@/stores/shop.js'
    import { useControllerStore } from '@/stores/controller';
    import { useRouter } from 'vue-router';

    const shopStore = useShopStore()
    const controllerStore = useControllerStore()
    const router = useRouter()

    const searchValue = ref()
    const headers = [
        { text: 'ID', value: "id", width : 50 },
        { text: "Image", value: "image", width: 60 },
        { text: "Title", value: "title",  },
        { text: "...", value: "tools", width : 70 }
    ]
    function shopDetail(id){
        router.push({name : "adminshopsdetail", params : { id: id }})
    }

    onMounted(()=>{
        controllerStore.page_loader = true
        axios.get('shops/', {
            headers: {
                'Authorization': `token ${localStorage.getItem('access_token')}`
            }
        })
        .then((data)=>{
            shopStore.shopList = data.data.shops
            controllerStore.page_loader = false
            console.log(shopStore.shopList)
        })
    })

</script>

<style>

</style>
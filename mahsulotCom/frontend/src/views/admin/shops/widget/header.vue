<template>
    <div class="shop-header">
        <div class="header-buttons">
            <!-- <div class = 'button-filter'>
                <i class="fa-solid fa-filter"></i>
                <p >{{ $t('filter') }}</p>
            </div> -->
            <div class = 'button-create' @click="shop_create">
                <i class="fa-solid fa-plus"></i>
                <p >{{ $t('createshop') }}</p>
            </div>
        </div>

        <n-modal
            v-model:show="create_if"
            :mask-closable="true"
            preset="dialog"
            title=""
            style="background-color: var(--color-white); width: 600px;margin-top: 30px; margin-bottom: 30px;"
            :positive-text="$t('createshop')"
            :negative-text="$t('cancel')"
            @positive-click="create"
            @negative-click="modal_close"
        >
                <div class = 'shop-create-modal'>
                    <div class="shop-create-input">
                        <input type="text" :placeholder="$t('name')" v-model="title">
                    </div>
                    <div class="shop-create-description">
                        <textarea cols="30" rows="5" :placeholder="$t('description')" v-model="description"></textarea>
                    </div>

                    <div class="shop-create-images">
                        <div class = 'image-file'>
                            <div>
                                <i class="fa-solid fa-image" v-if="image == ''"></i>
                                <img :src="image" alt="" v-if ="image != ''">
                            </div>
                            <input type="file"  @change="fileSelected">
                        </div>
                    </div>
                </div>
        </n-modal>
    </div>
  
</template>

<script setup>
    import axios from 'axios';
    import { ref } from 'vue';
    import {useShopStore} from '@/stores/shop.js'
import { useUserStore } from '@/stores/users';
    const shopStore = useShopStore()
    const userStore = useUserStore()
    const create_if = ref(false)
    const title = ref()
    const description = ref()
    const image = ref('')

    function shop_create(){
        if (userStore.admin == "super_admin"){
            create_if.value = true
        }
    }
    function fileSelected(e){
        const fd = new FormData()
        fd.append('image', e.target.files[0])
        axios.post('image/', fd, {
            headers : {
                'Authorization' : `token ${localStorage.getItem("access_token")}`
            }
        })
            .then((data)=>{
                if(data.status == 200) {
                    image.value = data.data.image
                }
            })
            .catch((error)=>{
                console.log(error)
            })
    }

    function create(){
        const fd = new FormData()
        fd.append('title', title.value)
        fd.append("description", description.value)
        fd.append('image', image.value)
        axios.post('shops/', fd, {
            headers : {
                'Authorization' : `token ${localStorage.getItem("access_token")}`
            }
        })
            .then((data)=>{
                if(data.status == 200) {
                    shopStore.shopList = data.data.shops
                }
            })
            .catch((error)=>{
                console.log(error)
            })

    }



</script>

<style>

</style>
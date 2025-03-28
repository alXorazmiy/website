<template>
    <div class = 'shop-detail-info'>
        <div class="shop-info">
            <div class="shop-image">
                <img :src="shopStore.shop.image" alt="">
            </div>
            <div class="shop-title">
                <p>{{ shopStore.shop.title }}</p>
            </div>
            <div class="shop-decsription">
                <p>{{ shopStore.shop.description }}</p>
            </div>
        </div>
        <div class="shop-tools">
           
            <i class="fa-solid fa-pen-to-square" @click="update_open"></i>
             
            <n-popconfirm  v-model:show="delete_if" :negative-text = 'null' :positive-text = 'null' :show-icon="false" style="background-color: var(--color-background);">
                <template #activator>
                    <i class="fa-solid fa-trash-can"></i>
                </template>
                <div>
                    <p class = "popconfirm-text"> {{ $t('want_delete') }}</p>
                    <div class="popconfirm-buttons">
                        <button class = 'button-no' @click="delete_cancel">{{ $t("no") }}</button>
                        <button class = 'button-yes'>{{ $t("yes") }}</button>
                    </div>
                </div>
            </n-popconfirm>
        </div>

        <n-modal
            v-model:show="update_if"
            :mask-closable="true"
            preset="dialog"
            title=""
            style="background-color: var(--color-white); width: 600px;margin-top: 30px; margin-bottom: 30px;"
            :positive-text="$t('update')"
            :negative-text="$t('cancel')"
            @positive-click="update"
            @negative-click="modal_close"
        >
                <div class = 'shop-create-modal'>
                    <div class="shop-create-input">
                        <input type="text" placeholder="Do'kon nomi" v-model="shopStore.shop.title">
                    </div>
                    <div class="shop-create-description">
                        <textarea cols="30" rows="5" placeholder="Tavsifi" v-model="shopStore.shop.description"></textarea>
                    </div>

                    <div class="shop-create-images">
                        <div class = 'image-file'>
                            <div>
                                <img :src="shopStore.shop.image" alt="" >
                            </div>
                            <input type="file"  @change="fileSelected">
                        </div>
                    </div>
                </div>
        </n-modal>


       
    </div>
  
</template>

<script setup>
    import { useShopStore } from '@/stores/shop';
    import axios from 'axios';
    import { ref } from 'vue';
    import { useRoute } from 'vue-router';
    import { useControllerStore } from '../../../../stores/controller';
import { useUserStore } from '@/stores/users';




    const delete_if = ref(false)
    const update_if = ref(false)
    const shopStore = useShopStore()
    const controllerStore = useControllerStore()
    const userStore = useUserStore()
    const route = useRoute()


    function update_open(){
        if(userStore.admin == "super_admin"){
            update_if.value = true
        }
        
    }
    function delete_cancel(){
        delete_if.value = false
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
                    shopStore.shop.image = data.data.image
                }
            })
            .catch((error)=>{
                console.log(error)
            })
    }

    function update(){
        controllerStore.page_loader = true
        const fd = new FormData()
        fd.append('title', shopStore.shop.title)
        fd.append('description', shopStore.shop.description)
        fd.append('image', shopStore.shop.image)

        axios.put(`shops/${route.params.id}/`, fd, {
            headers: {
                'Authorization': `token ${localStorage.getItem('access_token')}`
            }
        })
            .then((data)=>{
                if(data.status == 200){
                    // console.log(data.data)
                    shopStore.shop.id = data.data.id
                    shopStore.shop.title = data.data.title
                    shopStore.shop.description = data.data.description
                    shopStore.shop.image = data.data.image
                    controllerStore.page_loader = false
                    
                }
            })
            .catch((error)=>{
                console.log(error)
            })
            
    }


</script>

<style>

</style>
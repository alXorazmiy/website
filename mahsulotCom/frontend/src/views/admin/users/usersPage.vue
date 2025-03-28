<template>
    <div class="table-container">
        <div class="table-header">
            <div class = 'table-search'>
               <div>
                    <i class="fa-solid fa-magnifying-glass"></i>
                    <input type="text" v-model="searchValue" :placeholder="$t('search')">
               </div>
            </div>
            <div class="buttons">
                <div class = 'button-create' @click="create_user">
                    <i class="fa-solid fa-plus"></i>
                    <p >{{ $t('createUser') }}</p>
                </div>
            </div>

        </div>
        <EasyDataTable
            :headers="headers"
            :items="userStore.userList"
            table-class-name="customize-table"
            :search-value="searchValue"
        >
            <template #header-id="{}">
                        <p>{{ $t('id') }}</p>
            </template>
            <template #header-username="{}">
                        <p>{{ $t('username') }}</p>
            </template>
            <template #header-role="{}">
                        <p>{{ $t('role') }}</p>
            </template>
            <template #header-is_active="{}">
                        <p>{{ $t('active') }}</p>
            </template>
            <template #header-tools="{}">
                        <p><i class="fa-solid fa-ellipsis-vertical"></i></p>
            </template>
            <template #item-role="{role}">
                       <p class = "table-price" v-if = "role == 'product_admin'"><span class = 'role_active'>{{ $t('product_admin') }}</span></p>
                       <p class = "table-price" v-if = "role == 'super_admin'"><span class = 'role_unactive'>{{ $t('super_admin') }}</span></p>
            </template>
            <template #item-is_active="{is_active}">
                       <p class = "table-price" v-if = "is_active == true"><span class = 'active'>{{ $t('active_true') }}</span></p>
                       <p class = "table-price" v-if = "is_active == false"><span class = 'unactive'>{{ $t('active_false') }}</span></p>
            </template>
         
            <template #item-tools="{id}">
                <div class="table-tools">
                    <i class="fa-solid fa-pen-to-square " @click="update_user(id)"></i>
                    <n-popconfirm   :negative-text = 'null' :positive-text = 'null' :show-icon="false" style="background-color: var(--color-background);">
                        <template #activator>
                            <i class="fa-solid fa-trash-can"></i>
                        </template>
                        <div>
                            <p class = "popconfirm-text"> {{ $t('want_delete') }}</p>
                            <div class="popconfirm-buttons">
                                <!-- <button class = 'button-no' @click="delete_cancel">{{ $t("no") }}</button> -->
                                <button class = 'button-yes' @click = "delete_user(id)">{{ $t("yes") }}</button>
                            </div>
                        </div>
                    </n-popconfirm>
                </div>
            </template>
        </EasyDataTable>

        <n-modal
            v-model:show="create_if"
            :mask-closable="true"
            preset="dialog"
            title=""
            style="background-color: var(--color-white); width: 300px;margin-top: 30px; margin-bottom: 30px;"
            :positive-text="$t('create')"
            :negative-text="$t('cancel')"
            @positive-click="userCreate"
            @negative-click="modal_close"
        >
                <div class = 'shop-create-modal'>
                    <div class="shop-create-input">
                        <input type="text" :placeholder="$t('username')" v-model="userStore.user.username">
                    </div>
                    <div class="shop-create-input">
                        <input type="text" :placeholder="$t('password')" v-model="userStore.user.password">
                    </div>
                    <div class="shop-create-select2">
                        <select   v-model="userStore.user.role">
                            <option value = "product_admin">Admin</option>
                            <option value = "super_admin">Super Admin</option>
                        </select>
                        
                    </div>
                    <div class="shop-create-active" >
                        <input type="checkbox" v-model="userStore.user.active" >
                        <label for="">{{$t('active')}}</label>
                    </div>
                   
                </div>
        </n-modal>

        <n-modal
            v-model:show="update_if"
            :mask-closable="true"
            preset="dialog"
            title=""
            style="background-color: var(--color-white); width: 300px;margin-top: 30px; margin-bottom: 30px;"
            :positive-text="$t('update')"
            :negative-text="$t('cancel')"
            @positive-click="updateUser"
            @negative-click="modal_close"
        >
                <div class = 'shop-create-modal'>
                    <div class="shop-create-input">
                        <input type="text" :placeholder="$t('username')" v-model="userStore.user.username">
                    </div>
                    <div class="shop-create-input">
                        <input type="text" :placeholder="$t('password')" v-model="userStore.user.password">
                    </div>
                    <div class="shop-create-select2">
                        <select   v-model="userStore.user.role">
                            <option value = "product_admin">Admin</option>
                            <option value = "super_admin">Super Admin</option>
                        </select>
                        
                    </div>
                    <div class="shop-create-active" >
                        <input type="checkbox" v-model="userStore.user.active" >
                        <label for="">{{$t('active')}}</label>
                    </div>
                   
                </div>
        </n-modal>
          
    </div>
</template>

<script setup>

    import axios from 'axios';
    import { onMounted,ref } from 'vue';
    import { useRouter } from 'vue-router';
    import { useControllerStore } from '@/stores/controller';
    import {useUserStore} from '@/stores/users'
   
    const router = useRouter()
    const userStore = useUserStore()
    const controllerStore =  useControllerStore()
    const searchValue = ref()
    const create_if = ref(false)
    const update_if = ref(false)


    const headers = [
        { text: 'ID', value: "id", width : 50 },
        { text: "Image", value: "username"},
        { text: "Title", value: "role", width: 150 },
        { text: "price", value: "is_active", width: 150 },
        { text: "...", value: "tools", width : 70 }
    ]
    

    function create_user(){
        if(userStore.admin == 'super_admin'){
            create_if.value = true
        }
    }

    function userCreate(){
        const fd = new FormData()
        fd.append('username', userStore.user.username)
        fd.append('password', userStore.user.password)
        fd.append('role', userStore.user.role)
        fd.append('active', userStore.user.active)
        axios.post('users/',fd, {
            headers: {
                'Authorization': `token ${localStorage.getItem('access_token')}`
            }
        })
        .then((data)=>{
            userStore.userList = data.data
        })
        .catch((error)=>{
            console.log(error)
        })
    }

    function update_user(id){
        update_if.value = true

        let list = userStore.userList

        for( let i = 0; i< list.length; i++){
            if (list[i].id == id){
                userStore.user.id = list[i].id
                userStore.user.username = list[i].username
                userStore.user.password = '********'
                userStore.user.role = list[i].role
                userStore.user.active = list[i].is_active
            }
        }
        
    }

    function updateUser(){
        const fd = new FormData()
        fd.append('username', userStore.user.username)
        fd.append('password', userStore.user.password)
        fd.append('role', userStore.user.role)
        fd.append('active', userStore.user.active)
        axios.put(`users/${userStore.user.id}/`,fd, {
            headers: {
                'Authorization': `token ${localStorage.getItem('access_token')}`
            }
        })
        .then((data)=>{
            userStore.userList = data.data
        })
        .catch((error)=>{
            console.log(error)
        })
    }


    function delete_user(id){
        axios.delete(`users/${id}/`, {
            headers: {
                'Authorization': `token ${localStorage.getItem('access_token')}`
            }
        })
        .then((data)=>{
            userStore.userList = data.data
        })
        .catch((error)=>{
            console.log(error)
        })
    }
    onMounted(()=>{
        controllerStore.page_loader = true
        axios.get('users/', {
            headers: {
                'Authorization': `token ${localStorage.getItem('access_token')}`
            }
        })
        .then((data)=>{
            userStore.userList = data.data
            controllerStore.page_loader = false
            console.log(data.data)
        })
        .catch((error)=>{
            console.log(error)
        })
    })

</script>

<style>

</style>
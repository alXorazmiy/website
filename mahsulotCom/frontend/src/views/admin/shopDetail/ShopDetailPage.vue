<template>
    <div class = 'table-container'>
        <Header />
        <hr>
        <div class="table-header">
            <div class = 'table-search'>
               <div>
                    <i class="fa-solid fa-magnifying-glass"></i>
                    <input type="text" v-model="searchValue" :placeholder="$t('search')">
               </div>
            </div>
            <div class="buttons">
                <div class = 'button-filter' @click="product_filter">
                    <i class="fa-solid fa-filter"></i>
                    <p >{{ $t('filter') }}</p>
                </div>
                <div class = 'button-create' @click="product_create">
                    <i class="fa-solid fa-plus"></i>
                    <p >{{ $t('createProduct') }}</p>
                </div>
            </div>

        </div>
        <EasyDataTable
            :headers="headers"
            :items="ProductStore.productList"
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
            <template #header-category="{}">
                        <p>{{ $t('category') }}</p>
            </template>
            <template #header-price="{}">
                        <p>{{ $t('price') }}</p>
            </template>
            <template #header-amount="{}">
                        <p>{{ $t('amount') }}</p>
            </template>
            <template #header-active="{}">
                        <p>{{ $t('active') }}</p>
            </template>
            <template #header-tools="{}">
                        <p class = "table-header-tools"><i class="fa-solid fa-ellipsis-vertical"></i></p>
            </template>
            <template #item-image="{image}">
                        <div class = 'table-image'>
                            <img :src="image.split(',')[0]" alt="">
                        </div>
            </template>
            <template #item-price="{price}">
                       <p class = "table-price">{{(new Intl.NumberFormat('ru-RU').format(price))}} <span>  UZS</span> </p>
            </template>
            <template #item-amount="{amount}">
                       <p class = "table-price">{{(new Intl.NumberFormat('ru-RU').format(amount))}}</p>
            </template>
            <template #item-active="{active}">
                       <p class = "table-price" v-if = "active == true"><span class = 'active'>{{ $t('active_true') }}</span></p>
                       <p class = "table-price" v-if = "active == false"><span class = 'unactive'>{{ $t('active_false') }}</span></p>
            </template>
            <template #item-tools="{id}">
                <div class="table-tools">
                    <i class="fa-solid fa-pen-to-square" @click="update_product_open(id)"></i>
                    <n-popconfirm   :negative-text = 'null' :positive-text = 'null' :show-icon="false" style="background-color: var(--color-background);">
                        <template #activator>
                            <i class="fa-solid fa-trash-can"></i>
                        </template>
                        <div>
                            <p class = "popconfirm-text"> {{ $t('want_delete') }}</p>
                            <div class="popconfirm-buttons">
                                <!-- <button class = 'button-no' @click="delete_cancel">{{ $t("no") }}</button> -->
                                <button class = 'button-yes' @click = "delete_product(id.id)">{{ $t("yes") }}</button>
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
            style="background-color: var(--color-white); width: 600px;margin-top: 30px; margin-bottom: 30px;"
            :positive-text="$t('createProduct')"
            :negative-text="$t('cancel')"
            @positive-click="productCreate"
            @negative-click="modal_close"
        >
                <div class = 'shop-create-modal'>
                    <div class="shop-create-input">
                        <input type="text" :placeholder="$t('name')" v-model="ProductStore.product.title">
                    </div>
                    <div class="shop-create-description">
                        <textarea cols="30" rows="5" :placeholder="$t('description')" v-model="ProductStore.product.description"></textarea>
                    </div>
                    <div class="shop-create-input">
                        <input type="number" :placeholder="$t('price')" v-model="ProductStore.product.price">
                    </div>
                    <div class="shop-create-input">
                        <input type="number" :placeholder="$t('amount')" v-model="ProductStore.product.amount">
                    </div>
                    <div class="shop-create-active">
                        <input type="checkbox" :placeholder="$t('active')" v-model="ProductStore.product.active">
                        <label for="">{{$t('active')}}</label>
                    </div>
                    <div class="shop-create-select">
                        <select name="" id="" v-model="ProductStore.product.category">
                            <option :value="item.id" v-for="item in ProductStore.categoryList" :key = "item"> {{ item.title }} </option>
                        </select>
                        <n-popconfirm  v-model:show="create_category_if" :negative-text = 'null' :positive-text = 'null' :show-icon="false" style = "background-color: var(--color-white)">
                            <template #activator>
                                <i class="fa-solid fa-plus"></i>
                            </template>
                            <div>
                                <p class = 'popconfirm-body'>
                                    <input type="text" placeholder="Nomi" v-model="category_title">
                                    <textarea name="" id="" cols="30" rows="4" :placeholder="$t('description')" v-model="category_description"></textarea>
                                </p>
                                <div class="popconfirm-buttons">
                                    <button class = 'button-no' @click="category_cancel">{{ $t("cancel") }}</button>
                                    <button class = 'button-create' @click="category_create">{{ $t("create") }}</button>
                                </div>
                            </div>
                        </n-popconfirm>
                    </div>

                    <div class="shop-create-images">
                        <div class = 'image-files'>
                            <label for="123"><i class="fa-solid fa-image"></i></label>
                            <input type="file" id="123" @change="fileSelected">
                        </div>
                        <div class="image-list" v-for="item in ProductStore.imageList" :key = "item">
                            <!-- <p>{{ item }}</p> -->
                            <img :src="item" alt="">
                        </div>
                    </div>
                </div>
        </n-modal>

        <n-modal
            v-model:show="update_if"
            :mask-closable="true"
            preset="dialog"
            title=""
            style="background-color: var(--color-white); width: 600px;margin-top: 30px; margin-bottom: 30px;"
            :positive-text="$t('update')"
            :negative-text="$t('cancel')"
            @positive-click="updateProduct"
            @negative-click="modal_close"
        >
                <div class = 'shop-create-modal'>
                    <div class="shop-create-input">
                        <input type="text" :placeholder="$t('name')" v-model="ProductStore.product.title">
                    </div>
                    <div class="shop-create-description">
                        <textarea cols="30" rows="5" placeholder="Tavsifi" v-model="ProductStore.product.description"></textarea>
                    </div>
                    <div class="shop-create-input">
                        <input type="number" :placeholder="$t('price')" v-model="ProductStore.product.price">
                    </div>
                    <div class="shop-create-input">
                        <input type="number" :placeholder="$t('amount')" v-model="ProductStore.product.amount">
                    </div>
                    <div class="shop-create-active">
                        <input type="checkbox" :placeholder="$t('active')" v-model="ProductStore.product.active">
                        <label for="">{{$t('active')}}</label>
                    </div>
                    <div class="shop-create-select">
                        <select name="" id="" v-model="ProductStore.product.category">
                            <option :value="item.title" v-for="item in ProductStore.categoryList" :key = "item"> {{ item.title }} </option>
                        </select>
                        <n-popconfirm  v-model:show="create_category_if" :negative-text = 'null' :positive-text = 'null' :show-icon="false" style = "background-color: var(--color-white)">
                            <template #activator>
                                <i class="fa-solid fa-plus"></i>
                            </template>
                            <div>
                                <p class = 'popconfirm-body'>
                                    <input type="text" :placeholder="$t('title')" v-model="category_title">
                                    <textarea name="" id="" cols="30" rows="4" :placeholder="$t('description')" v-model="category_description"></textarea>
                                </p>
                                <div class="popconfirm-buttons">
                                    <button class = 'button-no' @click="category_cancel">{{ $t("cancel") }}</button>
                                    <button class = 'button-create' @click="category_create">{{ $t("create") }}</button>
                                </div>
                            </div>
                        </n-popconfirm>
                    </div>

                    <div class="shop-create-images">
                        <div class = 'image-files'>
                            <label for="123"><i class="fa-solid fa-image"></i></label>
                            <input type="file" id="123" @change="fileSelected">
                        </div>
                        <div class="image-list" v-for="item in ProductStore.imageList" :key = "item" >
                            <!-- <p>{{ item }}</p> -->
                            <img :src="item" alt="">
                            <div @click="delete_image(item)"><i class="fa-solid fa-xmark"></i></div>
                        </div>
                    </div>
                </div>
        </n-modal>

        <n-modal
            v-model:show="filter_if"
            :mask-closable="true"
            preset="dialog"
            title=""
            style="background-color: var(--color-white); width: 300px;margin-top: 30px; margin-bottom: 30px;"
            :positive-text="$t('filter2')"
            :negative-text="$t('cancel')"
            @positive-click="filterProduct"
            @negative-click="modal_close"
        >
                <div class = 'shop-create-modal'>
                    <div class="shop-create-select2">
                        <select  v-model="filter_active">
                            <option value="all">{{ $t('all') }}</option>
                            <option value="true">{{ $t('active_true') }}</option>
                            <option value="false">{{ $t('active_false') }}</option>
                        </select>
                    </div>
                    <div class="shop-create-input2">
                        <input type="number" :placeholder="$t('price') + ' 1'" v-model="filter_price1">
                        <input type="number" :placeholder="$t('price') + ' 2'" v-model="filter_price2">
                    </div>
                </div>
        </n-modal>



    </div>
</template>

<script setup>
    import axios from "axios";
    import { onMounted,ref } from "vue";
    import { useRoute, useRouter } from "vue-router";
    import { useControllerStore } from "../../../stores/controller";
    import Header from './widget/header.vue'
    import { useShopStore } from "@/stores/shop";
    import {useProductStore} from '@/stores/product'
import { formDark } from "naive-ui";


    const controllerStore = useControllerStore()
    const shopStore = useShopStore()
    const ProductStore = useProductStore()
    const router = useRouter()
    const route = useRoute()
    const create_if = ref(false)
    const update_if = ref(false)
    const filter_if = ref(false)

    const create_category_if = ref(false)
    const category_title = ref('')
    const category_description = ref('')
    const searchValue = ref()
    const delete_if =ref(false)

    const filter_active =ref('all')
    const filter_price1 = ref(null)
    const filter_price2 = ref(null)
    
    

    const headers = [
        { text: 'ID', value: "id", width : 50 },
        { text: "Image", value: "image", width: 60 },
        { text: "Title", value: "title",  },
        { text: "Category", value: "category", width: 150 },
        { text: "Price", value: "price", width: 100, sortable: true },
        { text: "Amount", value: "amount", width: 100,sortable: true },
        { text: "Active", value: "active", width: 100 },

        { text: "...", value: "tools", width : 70 }
    ]

    function clear(){
        ProductStore.product.title = ''
        ProductStore.product.description = ''
        ProductStore.product.category = ''
        ProductStore.product.price = ''
        ProductStore.product.amount = ''
        ProductStore.product.active = ''
        ProductStore.imageList = []

        create_if.value = false 
        update_if.value = false

    }

    function product_create(){
        clear()
        create_if.value = true
        axios.get('category/', {
            headers : {
                'Authorization' : `token ${localStorage.getItem('access_token')}`
            }
        })
            .then((data)=>{
                if (data.status == 200){
                    ProductStore.categoryList = data.data.categories
                }
            })
    }

    function category_cancel(){
        create_category_if.value = false
    }
    function category_create(){
        const fd = new FormData()
        fd.append('title', category_title.value)
        fd.append('description', category_description.value)
        axios.post('category/', fd, {
            headers : {
                'Authorization' : `token ${localStorage.getItem('access_token')}`
            }
        })
            .then((data)=>{
                if (data.status == 200){
                    create_category_if.value = false
                    ProductStore.categoryList = data.data.categories
                }
            })

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
                    let new_list = ProductStore.imageList
                    new_list.push(data.data.image)
                    console.log(new_list)

                    ProductStore.imageList = new_list
                }
            })
            .catch((error)=>{
                console.log(error)
            })
    }

    function productCreate(){
        let imageString = ''
        ProductStore.imageList.forEach((element) => {
            imageString = imageString + String(element) + ','
        })

        const fd = new FormData()
        fd.append('title', ProductStore.product.title)
        fd.append('description', ProductStore.product.description)
        fd.append('category', ProductStore.product.category)
        fd.append('price', ProductStore.product.price)
        fd.append('amount', ProductStore.product.amount)
        fd.append('active', ProductStore.product.active)
        fd.append('images', imageString)

        axios.post(`product/${route.params.id}/`, fd, {
            headers : {
                'Authorization' : `token ${localStorage.getItem("access_token")}`
            }
        })
            .then((data)=>{
                if(data.status == 200) {
                    ProductStore.productList = data.data
                    clear()
                }
            })
            .catch((error)=>{
                console.log(error)
            })

    }


    function delete_cancel (){
        delete_if.value = false
    }

    function delete_product(id){
        axios.delete(`productdetail/${id}/`, {
            headers: {
                'Authorization' : `token ${localStorage.getItem('access_token')}`
            }
        })
            .then((data)=>{
                if(data.status == 200){
                    ProductStore.productList = data.data  
                }
            })
            .catch((error)=>{
                console.log(error)
            })
    }

    function update_product_open(id){
        // console.log(item)
        update_if.value = 
        axios.get('category/', {
            headers : {
                'Authorization' : `token ${localStorage.getItem('access_token')}`
            }
        })
            .then((data)=>{
                if (data.status == 200){
                    ProductStore.categoryList = data.data.categories
                }
            })
        ProductStore.productList.forEach((value)=>{
         
            if (value.id == id){
                ProductStore.product.id = value.id
                ProductStore.product.title = value.title
                ProductStore.product.description = value.description
                ProductStore.product.category = value.category
                ProductStore.product.price = value.price
                ProductStore.product.amount = value.amount
                ProductStore.product.active = value.active
                let imagelist = value.image.split(',')
                ProductStore.imageList = imagelist
                ProductStore.imageList.pop()
                // console.log(ProductStore.imageList.pop())
            }
        })

    }

    function updateProduct(){
        let imageString = ''
        ProductStore.imageList.forEach((element) => {
            imageString = imageString + String(element) + ','
        })

        const fd = new FormData()
        fd.append('id', route.params.id)
        fd.append('title', ProductStore.product.title)
        fd.append('description', ProductStore.product.description)
        fd.append('category', ProductStore.product.category)
        fd.append('price', ProductStore.product.price)
        fd.append('amount', ProductStore.product.amount)
        fd.append('active', ProductStore.product.active)
        fd.append('images', imageString)

        axios.put(`productdetail/${ProductStore.product.id}/`, fd, {
            headers : {
                'Authorization' : `token ${localStorage.getItem("access_token")}`
            }
        })
            .then((data)=>{
                if(data.status == 200) {
                    ProductStore.productList = data.data
                    clear()
                }
            })
            .catch((error)=>{
                console.log(error)
            })
    }


    function delete_image(img){
        let new_list = []
        ProductStore.imageList.forEach((value)=>{
            if (value != img){
                new_list.push(value)
            }
        })

        ProductStore.imageList = new_list
    }


    function product_filter(){
        filter_if.value = true
    }

    function filterProduct(){
        const fd = new FormData()
        fd.append('active', filter_active.value)
       
        fd.append('price_1', filter_price1.value)
        fd.append('price_2', filter_price2.value)
        axios.put(`product/${route.params.id}/`, fd, {
            headers : {
                'Authorization' : `token ${localStorage.getItem('access_token')}`
            }
        })
            .then((data)=>{
                if(data.status == 200){
                    ProductStore.productList = data.data
                }
            })
            .catch((error)=>{
                console.log(error)
            })
    }

    onMounted(()=>{
        controllerStore.page_loader = true
        console.log(route.params.id)
        axios.get(`shops/${route.params.id}/`, {
            headers : {
                'Authorization' : `token ${localStorage.getItem('access_token')}`
            }
        })
            .then((data)=>{
                if(data.status == 200){
                    // console.log(data.data)
                    shopStore.shop.id = data.data.id
                    shopStore.shop.title = data.data.title
                    shopStore.shop.description = data.data.description
                    shopStore.shop.image = data.data.image
                    // controllerStore.page_loader = false
                    
                }
            })
            .catch((error)=>{
                console.log(error)
            })

        axios.get(`product/${route.params.id}/`, {
            headers : {
                'Authorization' : `token ${localStorage.getItem('access_token')}`
            }
        })
            .then((data)=>{
                if(data.status == 200){
                    console.log(data.data)
                    ProductStore.productList = data.data
                    controllerStore.page_loader = false
                    
                }
            })
            .catch((error)=>{
                console.log(error)
            })
    })

</script>

<style>

</style>
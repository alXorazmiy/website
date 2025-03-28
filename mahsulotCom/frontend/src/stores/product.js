import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

export const useProductStore = defineStore('productstore', () => {
    const productList = ref([])
    const product = ref({
        id : '',
        title: '',
        description : '',
        image : '',
        amount : '',
        price : '',
        category: '',
        active: ''
    })

    const categoryList = ref([])
    const imageList = ref([])
 
    return {productList, product,categoryList, imageList}
})

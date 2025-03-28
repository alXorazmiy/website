import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

export const useShopStore = defineStore('shopstore', () => {
    const shopList = ref([])
    const shop = ref({
        id : '',
        title: '',
        description : '',
        image : ''
    })
 
    return {shopList, shop}
})

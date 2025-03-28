
import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

export const useInfoStore = defineStore('infoStore', () => {
    const info_if = ref(false)
    const info_list = ref([])
    return { info_if, info_list}
})
    

import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

export const useStoreController = defineStore('controller', () => {
    const loader = ref(false)
    return {loader}
})

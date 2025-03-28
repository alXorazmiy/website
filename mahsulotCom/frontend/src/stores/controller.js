import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

export const useControllerStore = defineStore('controller', () => {
    const is_admin = ref(false)
    const sidebar_open = ref(false)
    const page_loader = ref(false)
    const mobile_sidebar = ref(false)

    return {is_admin, sidebar_open, page_loader,mobile_sidebar}
})

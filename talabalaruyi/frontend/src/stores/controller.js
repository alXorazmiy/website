import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

export const useControllerStore = defineStore('controller', () => {
    const is_loader = ref(false)
    const sidebar_open = ref(false)


    const floors = ref([])
    const rooms = ref([])
    const faculty = ref([])
    const payments = ref([])
    const students = ref([])
    const months = ref([])
 
    return { is_loader,sidebar_open, floors, rooms, faculty, payments , students, months}
})

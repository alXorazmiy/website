import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

export const useUserStore = defineStore('userstore', () => {
    const userList = ref([])
    const user = ref({
        id: "",
        username : '',
        password: '',
        role : '',
        active : true
    })

    const admin = ref()
 
    return {userList, user,admin}
})

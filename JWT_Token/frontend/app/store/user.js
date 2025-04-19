

import { defineStore } from "pinia";

export const useUserStore = defineStore("user", {
    state : ()=> (
        {
            email : '',
            name : '',
            id : null,
            image : '',
            is_active : false,
            is_superuser: false,
        }
    ),
    actions : {
        setData(data) {
            this.id = data.id
            this.name = data.name
            this.email = data.email
            this.image = data.image
            this.is_active = data.is_active
        }
    },
    persist : true
})

    import { defineStore } from "pinia";

    export const useGeneralStore = defineStore("general", {
        state: ()=>({
            isLogin : false,
            count: 0
        }),
        actions: {
            increment(){
                this.count--
            }
        },
        persist: true
    })
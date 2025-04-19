
import { defineStore } from "pinia";

export const useGeneralStore = defineStore("general", {
    state: ()=>({
        isLogin : false,
        isLoader: false,
        isDark : true,
        count: 0
    }),
    actions: {
        increment(){
            this.count--
        },
        toggleTheme() {
            this.isDark = !this.isDark;
        }
    },
    persist: {
        paths: ['isLogin', 'isDark']
    }
})
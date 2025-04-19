import { useGeneralStore } from "~/store/general";
import { useUserStore } from "~/store/user";


export default defineNuxtPlugin((NuxtApp)=>{
    return {
        provide : {
            generalStore: useGeneralStore(),
            userStore : useUserStore(),
        }
    }
})
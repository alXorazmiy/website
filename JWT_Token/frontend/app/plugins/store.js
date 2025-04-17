import { useGeneralStore } from "~/store/general";


export default defineNuxtPlugin((NuxtApp)=>{
    return {
        provide : {
            generalStore: useGeneralStore(),
        }
    }
})
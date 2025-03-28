<template>
    <div class ='menu'>
        <div class = 'sidebar-mobile-open'>
            <i class="fa-solid fa-bars" @click="mobile_sidebar_open"></i>
        </div>
        <div class="menu-buttons">
       
            <select v-model = "$i18n.locale" @change="change_language($i18n.locale)">
                <option value="UZ">UZ</option>
                <option value="RU">RU</option>
                <option value="EN">EN</option>
            </select>
            <select v-model = "theme" @change="change_theme">
                <option value="light">{{ $t('light_mode') }}</option>
                <option value="dark">{{ $t('dark_mode') }}</option>
            </select>
            
        
        </div>
    </div>
</template>

<script setup>
    import { onMounted, ref } from "vue";
import { useControllerStore } from "../stores/controller";


    const theme = ref()
    const controllerStore = useControllerStore()

    function change_language(lang){
        console.log(lang)
        localStorage.setItem('language', lang)
    }

    function change_theme(){
        if (theme.value == 'light'){
            document.body.classList.remove("dark-mode-variables")
            localStorage.setItem("themeMode", 'light')

        }else{
            document.body.classList.add("dark-mode-variables")
            localStorage.setItem("themeMode", 'dark')
        }   
    }

    function mobile_sidebar_open(){
        controllerStore.mobile_sidebar = true
    }
    onMounted(()=>{
        if(localStorage.getItem("themeMode") == 'light'){
            theme.value = 'light'
            document.body.classList.remove("dark-mode-variables")
        }
        else if (localStorage.getItem("themeMode") == 'dark') {
            console.log('dark')
            theme.value = 'dark'
            document.body.classList.add("dark-mode-variables")
        }
    })

</script>

<style>

</style>
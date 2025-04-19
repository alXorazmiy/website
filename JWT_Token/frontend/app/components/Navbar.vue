<template>
    <div class="fixed z-10 bg-transparent w-full h-[80px] top-0 left-0 right-0" >
        <div class="flex justify-end items-center h-full mx-10">
            <div class= "flex items-center justify-around text-gray-500 w-[40%]"  >

                <div class = "dark:bg-[#3e4857] bg-[#f1f1f1] px-5 py-2 rounded-full dark:text-white text-black " >
                    <input type="text" class = "bg-transparent outline-none text-[14px] " :placeholder="$t('search')">
                    <Icon name = "material-symbols:search"  />
                </div>

                <div class = "flex items-center">
                    <Icon class = "ml-10 mr-4 cursor-pointer" name = "mingcute:shopping-bag-2-fill"  size = "30"   />
                    <Icon class = "ml-1 mr-4 cursor-pointer " name = "fluent:comment-text-32-filled"  size = "30" />    
                    <Icon class = "mr-5 cursor-pointer" name = "material-symbols:notifications-rounded"  size = "30" />

                    <div class="cursor-pointer" @click = "setTheme">
                        <div class="dark:bg-darkSecondary bg-lightSecondary w-[70px] h-[32px] rounded-full relative flex items-center px-1 ">
                            <div class="absolute dark:right-1   dark:bg-darkPrimary bg-white w-[26px] h-[26px] rounded-full flex items-center justify-center transition-all duration-300">
                                <Icon v-if="!$generalStore.isDark" name="line-md:moon-filled-alt-to-sunny-filled-loop-transition" class="text-[#e89849]" size="20" />
                                <Icon v-else name="line-md:moon-filled-loop" class="text-white" size="20" />
                            </div>
                        </div>
                    </div>


                    <div class = "relative ml-3" >
                        <button class=  "mt-1 dark:text-darkText text-lightText flex items-center justify-around dark:bg-darkSecondary bg-lightSecondary px-5 py-2 rounded-full w-[160px]"  @click = "event => languageMenu = !languageMenu">
                            <span v-if="locale == 'en'"  >{{ $t('English') }}</span>
                            <span v-if="locale == 'ru'"  >{{ $t('Russian') }}</span>
                            <span v-if="locale == 'uz'"  >{{ $t('Uzbek tili') }}</span>
                            <Icon name = "material-symbols:arrow-drop-down" size = "20" class="ml-2" />
                        </button>

                        <div v-if = "languageMenu" id = "PopupMenu" class = " absolute dark:bg-darkSecondary bg-lightSecondary rounded-lg py-1.5 w-[160px] shadow-xl dark:text-darkText text-lightText top-[50px] right-0" >
                            <div class="flex m-2 px-2 cursor-pointer" @click="setLanguage('en')">
                                <img src="@/assets/images/en.png" alt="" class="w-[24px] h-[24px] object-cover">
                                <span class="ml-3" >English</span>
                            </div>
                            <div class="flex m-2 px-2 cursor-pointer" @click="setLanguage('uz')">
                                <img src="@/assets/images/uz.png" alt="" class="w-[24px] h-[24px] object-cover">
                                <span class="ml-3" >Uzbek</span>
                            </div>
                            <div class="flex m-2 px-2 cursor-pointer" @click="setLanguage('ru')">
                                <img src="@/assets/images/ru.png" alt="" class="w-[24px] h-[24px] object-cover">
                                <span class="ml-3" >Pусский</span>
                            </div>  
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
const {locale, setLocale } = useI18n()
const {$generalStore} = useNuxtApp()

const languageMenu = ref(false)



const setLanguage =(language) =>{
    setLocale(language)
    languageMenu.value = false
}

const setTheme  = () =>{
    $generalStore.toggleTheme()


    if ($generalStore.isDark) { 
        document.documentElement.classList.add('dark')
    } else {
        document.documentElement.classList.remove('dark')
    }

}



</script>


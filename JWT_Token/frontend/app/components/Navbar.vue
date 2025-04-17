<template>
    <div class="fixed z-10 bg-transparent w-full h-[80px] top-0 left-0 right-0" >
        <div class="flex justify-end items-center h-full mx-10">
            <div class= "flex items-center justify-around text-gray-500 w-[40%]"  >

                <div class = "bg-[#3e4857] px-5 py-2 rounded-full text-white " >
                    <input type="text" class = "bg-transparent outline-none text-[14px] " :placeholder="$t('search')">
                    <Icon name = "material-symbols:search"  />
                </div>

                <div class = "flex items-center">
                    <Icon class = "ml-10 mr-4 cursor-pointer" name = "mingcute:shopping-bag-2-fill"  size = "30"   />
                    <Icon class = "ml-1 mr-4 cursor-pointer " name = "fluent:comment-text-32-filled"  size = "30" />    
                    <Icon class = "mr-5 cursor-pointer" name = "material-symbols:notifications-rounded"  size = "30" />

                    <!-- <div>
                        <div>
                            <button v-for="locale in locales" @click="setLocale(locale.code)">
                                {{ locale.code }}
                            </button>
                            <h1>{{ $t('English') }}</h1>
                        </div>
                    </div> -->


                    <div class = "relative" >
                        <button class=  "mt-1 text-white flex items-center justify-around bg-[#2c384a] px-5 py-2 rounded-full w-[160px]"  @click = "event => languageMenu = !languageMenu">
                            <span v-if="locale == 'en'"  >{{ $t('English') }}</span>
                            <span v-if="locale == 'ru'"  >{{ $t('Russian') }}</span>
                            <span v-if="locale == 'uz'"  >{{ $t('Uzbek tili') }}</span>
                            <Icon name = "material-symbols:arrow-drop-down" size = "20" class="ml-2" />
                        </button>

                        <div v-if = "languageMenu" id = "PopupMenu" class = " absolute bg-[#2c384a] rounded-lg py-1.5 w-[160px] shadow-xl text-white top-[50px] right-0" >
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
const {locale, locales, setLocale } = useI18n()
const {$axios} = useNuxtApp()
const router = useRouter()
const languageMenu = ref(false)

onMounted(()=>{
    console.log(locale.value) 
})


const setLanguage =(language) =>{
    setLocale(language)
    languageMenu.value = false
    localStorage.setItem('locale', language)
}

// const logout = () =>{
//     try {
//         $axios.post("logout/")
//             .then((value)=>{
//                 if (value.status == 200){
//                     languageMenu.value = false
//                     router.push("/login")
//                 }
//             })
//             .catch((error)=>{
//                 console.log(error)
//             })
//     } catch{

//     }
// }

</script>





<template>
    <div :class="{ 'dark': isDark }">
        <div class = "w-full h-[100vh] top-0 left-0 dark:bg-darkPrimary bg-lightPrimary" >
            <Navbar />
            <div class="flex justify-center items-center w-full h-full text-white">
                <div class="flex flex-col items-center dark:text-darkText text-lightText ">
                    {{ count }}
                    <button class="mt-5 py-2 px-5 bg-[#f02c56] rounded text-white" @click = "increment" >Increment</button>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>

// import {useCounter} from "@/composables/useCounter.ts"
import { storeToRefs } from 'pinia';
const {$generalStore} = useNuxtApp()
const { count } = storeToRefs($generalStore)
const { increment } = $generalStore

const isDark = ref(true)



</script>


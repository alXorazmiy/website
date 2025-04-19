<template>
    <MainLayout>
        <div class="w-full h-[100vh] top-0 left-0 dark:bg-darkPrimary bg-lightPrimary">
            <div class="flex justify-center items-center w-full h-full text-white">
                <pre v-if="code" class="w-[50%] bg-[#151b23] p-3 rounded">
                    <code v-html="highlightedCode"></code>
                </pre>
            </div>
        </div>
    </MainLayout>
</template>

<script setup>
import MainLayout from "@/layouts/MainLayout.vue"
import hljs from 'highlight.js/lib/core'
import python from 'highlight.js/lib/languages/python'
import 'highlight.js/styles/atom-one-dark.css'

hljs.registerLanguage('python', python)

const code = ref(`
def hello_world():
    print("Hello, World!")
hello_world()
`)

const highlightedCode = ref('')

onMounted(() => {
  highlightedCode.value = hljs.highlight('python', code.value).value
})
</script>

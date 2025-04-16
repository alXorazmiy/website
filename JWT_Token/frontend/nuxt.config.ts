export default defineNuxtConfig(
    {
        compatibilityDate: '2024-11-01',
        devtools: { enabled: true },
        future : {
            compatibilityVersion : 4,
        },
        experimental: {
            scanPageMeta: 'after-resolve',
            sharedPrerenderData: false,
            compileTemplate: true,
            resetAsyncDataToUndefined: true,
            templateUtils: true,
            relativeWatchPaths: true,
            normalizeComponentNames: false,
            spaLoadingTemplateLocation: 'within',
            defaults: {
                useAsyncData: {
                    deep: true
                }
            }
        },

        features: {
            inlineStyles: true
        },
        css : ["./assets/css/main.css"],
        modules: [
          '@nuxt/fonts',
          '@nuxt/icon',
          '@nuxt/image',
          '@nuxtjs/tailwindcss'
        ]
    }
)
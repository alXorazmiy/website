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
          '@nuxtjs/tailwindcss',
          '@pinia/nuxt',
          '@nuxtjs/i18n'
        ],
        i18n: {

            defaultLocale: 'uz',  
            locales: [
                { code: 'en', file: 'en.json' },
                { code: 'ru', file: 'ru.json' },
                { code: 'uz', file: 'uz.json' },
            ],
            lazy: true,
            langDir: '../app/i18n/locales', 
         
            strategy: 'no_prefix'
          }
    }
)
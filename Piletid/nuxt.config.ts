// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  devtools: { enabled: true },
  css: ['~/assets/css/main.css'],
  plugins: ["~/plugins/preline.client.ts"],

  nitro: {
    firebase: {
      gen: 2
    }
  },

  modules: ["@nuxtjs/tailwindcss"]
})
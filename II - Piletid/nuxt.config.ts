// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  devtools: { enabled: true },
  css: ['~/assets/css/main.css'],
  plugins: ["~/plugins/preline.client.ts"],

  modules: ["@nuxtjs/tailwindcss", '@nuxtjs/supabase'],
  supabase: { redirect: false },

})
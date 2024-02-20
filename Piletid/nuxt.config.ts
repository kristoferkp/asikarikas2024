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

  modules: ["@nuxtjs/tailwindcss", 'nuxt-vuefire'],

  vuefire: {
    config: {
      apiKey: "AIzaSyBQv7Bd17jkpky5h5xj4nmc9wirmtKzbf0",
      authDomain: "piletid-b625c.firebaseapp.com",
      projectId: "piletid-b625c",
      storageBucket: "piletid-b625c.appspot.com",
      messagingSenderId: "190813899233",
      appId: "1:190813899233:web:f6d49ee6896a36de992aa0",
      measurementId: "G-FCJXKM3DP6"
    },
    auth: {
      enabled: false
    },
  },
})
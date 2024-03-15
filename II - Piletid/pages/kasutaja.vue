<script setup>
const user = useSupabaseUser();
</script>

<template>
  <div class="mx-auto">
    <Account v-if="user" />
    <Auth v-else />
  </div>
</template>


<template>
    <RouterView />
</template>

<script setup>
    import { RouterLink, RouterView } from 'vue-router'

</script>




<style scoped>

a.router-link-exact-active {
    color: var(--color-text);
}
a.router-link-exact-active:hover {
    background-color: transparent;
}

</style>

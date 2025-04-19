<template>
    <section class="flex min-h-screen flex-col items-center justify-center dark:bg-darkPrimary bg-white dark:text-white text-black">
      <h1 class="mb-2 text-9xl font-bold">
        {{ error?.statusCode }}
      </h1>
      <p class="mb-10 text-xl sm:text-3xl">{{ error?.statusMessage }}</p>
      <NuxtLink class="bg-danger px-5 py-3 rounded-md cursor-pointer text-white " to="/"> Go home </NuxtLink>
    </section>
  </template>


<script setup lang="ts">
    import type { NuxtError } from "#app";

    defineProps({
        error: Object as () => NuxtError,
    });
</script>
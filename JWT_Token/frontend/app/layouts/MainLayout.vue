<template>
    <div class = "relative" >
        <Navbar />
        <Sidebar />
        <div class="absolute left-[250px] w-[calc(100%-250px)]">
            <slot />
        </div>
    </div>
</template>

<script setup>



</script>


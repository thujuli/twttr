<template>
    <div class="rounded-lg border-2 bg-gray-300 border-gray-500 mt-4">
        <h3 class="text-gray-800 text-xl font-semibold px-2 pt-2">Tweet From {{ username }}</h3>
        <img :src="imagePath" class="w-full mt-2 border-y-2 border-gray-500">
        <div class="bg-gray-900 p-2">
            <p class="text-lg text-gray-300">{{ content }}</p>
            <button class="rounded-md bg-gray-200 px-4 text-lg font-semibold border border-sky-500 text-sky-500 mt-2">Like</button>
        </div>
    </div>
</template>

<script setup>
defineProps(["username", "content", "imagePath"])
</script>
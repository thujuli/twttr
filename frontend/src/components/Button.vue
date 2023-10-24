<template>
    <button :type="buttonType" class="bg-sky-500 hover:bg-sky-600 rounded-md text-gray-200 font-bold text-lg p-2" @click="$emit('handleClick')">{{ buttonName }}</button>
</template>

<script setup>
defineProps(["buttonName", "buttonType"])
defineEmits(["handleClick"])
</script>
<template>
    <button :type="buttonType" :disabled="disabled" @click="$emit('handleClick')"
        class="bg-sky-500 p-2 mt-2 rounded-xl font-bold text-gray-200 hover:bg-sky-800 disabled:bg-gray-500">{{ buttonName }}
    </button>
</template>

<script setup>
defineProps(["buttonName", "buttonType", "disabled"])
defineEmits(["handleClick"])
</script>
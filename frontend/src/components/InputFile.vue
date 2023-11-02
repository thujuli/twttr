<template>
    <input type="file" :id="id" @change="handleFileChange" class="block w-full text-lg text-gray-900 border border-gray-300 rounded-lg cursor-pointer bg-gray-50 dark:text-gray-400 focus:outline-none dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400">
</template>

<script setup>
const { id, modelValue } = defineProps(['id', 'modelValue']);
const emits = defineEmits(['update:modelValue']); // Use defineEmits to declare the emit function


const handleFileChange = (event) => {
    const file = event.target.files[0];
    emits('update:modelValue', file); // Emit the event with the selected file
}

</script>
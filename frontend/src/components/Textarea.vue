<template>
    <textarea :id="id" rows="5" :placeholder="placeholder"  :value="modelValue" @input="$emit('update:modelValue', $event.target.value)" class="rounded-md bg-gray-800 text-gray-300 text-lg font-semibold p-2" style="resize: none;"></textarea>
</template>

<script setup>
defineProps(["id", "rows", "placeholder", "modelValue"])
defineEmits(['update:modelValue'])
</script>
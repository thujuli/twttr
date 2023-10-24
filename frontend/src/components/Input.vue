<template>
    <label :for="id" class="text-2md text-gray-300">{{ labelName }}</label>
    <input :id="id" :type="inputType" :value="modelValue" @input="$emit('update:modelValue', $event.target.value)" class="rounded-md h-10 bg-gray-800 focus:bg-gray-700 focus:border-b-2 focus:border-sky-500 focus:outline-none text-gray-300 font-semibold p-2">

</template>

<script setup>
defineProps(["labelName", "inputType", "id", "placeholder", "modelValue"])
defineEmits(["update:modelValue"])
</script>
<template>
    <Dialog :open="isOpen"  @close="$emit('toggleModal')" class="relative z-50">
         <!-- The backdrop, rendered as a fixed sibling to the panel container -->
        <div class="fixed inset-0 bg-gray-900/30" aria-hidden="true" />

        <!-- Full-screen container to center the panel -->
        <div class="fixed inset-0 flex w-screen items-center justify-center p-4 ">
            <DialogPanel class="bg-gray-900 p-5 rounded-md w-2/5">
                <slot></slot>
            </DialogPanel>
        </div>
    </Dialog>
</template>

<script setup>
import {
    Dialog,
    DialogPanel,
} from "@headlessui/vue"

defineProps(["isOpen"])
defineEmits(["toggleModal"])

</script>
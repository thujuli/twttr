<template>
    <div class="bg-gray-800 border-2 border-sky-800 rounded-md overflow-hidden shadow-lg">
        <img class="w-full" :src="imagePath">
        <div class="px-6 py-2">
            <h3 class="text-gray-300 text-lg">{{ content }}</h3>
            <h2 class="font-semibold text-gray-200 text-lg text-left md:text-right"> <span class="border-b-2">{{ username }}</span></h2>
        </div>
        <div class="flex flex-row px-4 gap-3 pt-2 border-t-2 border-sky-800 bg-gray-300">
            <!-- <h2 class="bg-gray-200 rounded-md px-3 pt-2 font-semibold text-gray-700 mb-2">{{ username }}</h2> -->
            <button class="bg-sky-400 hover:bg-sky-600 text-gray-800 text-sm font-bold py-2 px-4 rounded inline-flex items-center mb-2">
                <svg class="fill-current w-4 h-4 mr-2" viewBox="0 0 15 15" version="1.1" id="heart" xmlns="http://www.w3.org/2000/svg">
                    <path d="M13.91,6.75c-1.17,2.25-4.3,5.31-6.07,6.94c-0.1903,0.1718-0.4797,0.1718-0.67,0C5.39,12.06,2.26,9,1.09,6.75&#xA;&#x9;C-1.48,1.8,5-1.5,7.5,3.45C10-1.5,16.48,1.8,13.91,6.75z"/>
                </svg>
                <span>Like</span>
            </button>
        </div>
    </div>
</template>

<script setup>
defineProps(["username", "content", "imagePath"])
</script>
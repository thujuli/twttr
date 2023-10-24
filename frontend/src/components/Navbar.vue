<template>
    <header class="bg-gray-950 text-gray-100">
        <nav class="flex justify-between items-center mx-4 py-5">
            <h3 class="uppercase font-bold text-xl">twttr</h3>
            <ul class="flex text-lg">
                <li class="px-2 ">
                    <router-link to="/" active-class="border-b-2 border-gray-100">Home</router-link>
                </li>
                <li class="px-2">
                    <router-link to="/register" active-class="border-b-2 border-gray-100">Register</router-link>
                </li>
                <li class="px-2">
                    <router-link to="/login" active-class="border-b-2 border-gray-100">Login</router-link>
                </li>
            </ul>
        </nav>
    </header>
    
</template>
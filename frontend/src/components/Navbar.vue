<template>
    <header class="bg-gray-950 text-gray-100">
        <nav class="flex justify-between items-center mx-4 py-5">
            <h3 class="uppercase font-bold text-xl">twttr</h3>
            <ul class="flex text-lg">
                <li class="px-2 ">
                    <router-link to="/" active-class="border-b-2 border-gray-100" class="hover:border-b-2 border-gray-100">Home</router-link>
                </li>
                <li class="px-2 ">
                    <router-link to="/leaderboard" active-class="border-b-2 border-gray-100" class="hover:border-b-2 border-gray-100">Leaderboard</router-link>
                </li>
                <li class="px-2 ">
                    <a :href="urlAdmin" class="hover:border-b-2 border-gray-100" target="_blank">Admin</a>
                </li>
                <li class="px-2">
                    <router-link to="/register" active-class="border-b-2 border-gray-100" class="hover:border-b-2 border-gray-100">Register</router-link>
                </li>
                <li class="px-2">
                    <router-link to="/login" active-class="border-b-2 border-gray-100" class="hover:border-b-2 border-gray-100">Login</router-link>
                </li>
                <li class="px-2">
                    <button class="hover:border-b-2 border-gray-100" @click="handleLogout">Logout</button>
                </li>
            </ul>
        </nav>
    </header>
    
</template>

<script setup>
import Swal from "sweetalert2"
import { useRouter } from "vue-router";
import { ref } from "vue";
import { useAuth } from "../composable/useAuth";
import { useAuthStore } from "../stores/authStore" 


const urlAdmin = import.meta.env.VITE_API_BASEURL + "/admin"
const success = ref(false)
const successMessage = ref(null)

const router = useRouter()
const { tryLogout } = useAuth() 
const { removeToken, accessToken } = useAuthStore()

const handleLogout =  () => {
    Swal.fire({
        title: 'Logout',
        text: "Apakah anda yakin mau logout!",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Ya'
        }).then( async (result) => {
            if (result.isConfirmed) {
                const res = await tryLogout(import.meta.env.VITE_API_BASEURL + "/api/auth/logout", accessToken)
                console.log(res)
                success.value = res.data.data.success
                successMessage.value = res.data.data.message
                removeToken()
                router.push('/login')
                if(success.value){
                Swal.fire(
                    'Logout!',
                    successMessage.value,
                    'success'
                )
            }
        }
    })
}
</script>
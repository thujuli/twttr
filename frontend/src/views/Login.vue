<template>
    <div class="flex flex-col h-screen">
        <Navbar/>
        <div class="flex flex-col mt-32 w-6/12 mx-auto">
            <h2 class="text-3xl font-bold text-gray-200">Login</h2>
            <p class="mt-2 mb-4 text-gray-400 text-lg">Please sign in to continue</p>
            <p v-show="showMessage" class="text-white p-3 mt-2 mb-2" :class="{'bg-red-500': status.error, 'bg-green-500': status.success}">{{ message }}</p>
            <Form>
                <Input id="email" label-name="Email" input-type="text" v-model="userData.email"/>
                <Input id="password" label-name="Password" input-type="password" v-model="userData.password"/>
                <Button button-name="LOGIN" button-type="submit" @handle-click="handleLogin"/>
            </Form>
        </div>
        <div class="flex justify-center items-center">
                <p class="mt-3 text-gray-400">Don't have an account? <router-link to="/register" class="text-sky-500 hover:underline">Register</router-link></p>
        </div>
    </div>
</template>

<script setup>
import Navbar from "../components/Navbar.vue";
import Form from "../components/Form.vue";
import Input from "../components/Input.vue"
import Button from "../components/Button.vue";
import { reactive, ref } from "vue";
import { useRouter } from "vue-router"
import { useAuth } from "../composable/useAuth"
import { useAuthStore } from "../stores/authStore";

const { setToken } = useAuthStore()
const { tryAuth } = useAuth()
const router = useRouter()
const showMessage = ref(false)
const message = ref("")
const status = reactive({
    success: false,
    error: false,
})

const userData = reactive({
    email: "",
    password: ""
})

const handleLogin = async () => {
    const response = await tryAuth(import.meta.env.VITE_API_BASEURL + "/api/auth/login", userData)

    if (response.data.success) {
        setToken(response.data.data.access_token, response.data.data.refresh_token, response.data.data.user_id)
        router.push("/")
    } else if (response.status == 422) {
            message.value = "Invalid input data"
            showMessage.value = true
            status.error = true
    } else if (response.status == 401) {
            message.value = response.data.message
            showMessage.value = true
            status.error = true
    } else{
            message.value = "Something went wrong"
            showMessage.value = true
            status.error = true
    }
}
</script>
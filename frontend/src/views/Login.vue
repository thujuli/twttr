<template>
    <div class="flex flex-col h-screen">
        <Navbar/>
        <div class="flex flex-col mt-32 w-6/12 mx-auto">
            <h2 class="text-3xl font-bold text-gray-200">Login</h2>
            <p class="mt-2 mb-4 text-gray-400 text-lg">Please sign in to continue</p>
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

const { tryAuth } = useAuth()
const router = useRouter()
const success = ref(false)
const accessToken = ref("")
const refreshToken = ref("")

const userData = reactive({
    email: "",
    password: ""
})

const handleLogin = async () => {
    const response = await tryAuth(import.meta.env.VITE_API_BASEURL + "/api/auth/login", userData)
    success.value = response.data.success
    accessToken.value = response.data.data.access_token
    refreshToken.value = response.data.data.refresh_token

    if (success.value) {
        localStorage.setItem("accessToken", accessToken.value)
        localStorage.setItem("refreshToken", refreshToken.value)

        router.push("/")
    }
}
</script>
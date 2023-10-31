<template>
    <div class="flex flex-col h-screen">
        <Navbar/>
        <div class="flex flex-col mt-4 w-6/12 mx-auto">
            <h2 class="text-3xl font-bold text-gray-200">Create Account</h2>
            <p class="mt-2 mb-4 text-gray-400 text-lg">Please fill the input blow here</p>
            <p v-show="showMessage" class="text-white p-3 mt-2 mb-2" :class="{'bg-red-500': status.error, 'bg-green-500': status.success}">{{ message }}</p>
            <Form>
                <Input id="email" label-name="Email" input-type="text" v-model="userData.email"/>
                <Input id="username" label-name="Username" input-type="text" v-model="userData.username"/>
                <Input id="passoword" label-name="Password" input-type="password" v-model="userData.password"/>
                <Input id="confirm-password" label-name="Confirm Password" input-type="password" v-model="confirmPassword"/>
                <Button button-name="REGISTER" button-type="submit" @handle-click="handleRegister"/>
            </Form>
            <div class="flex justify-center items-center">
                <p class="mt-3 text-gray-400">Already have an account? <router-link to="/login" class="text-sky-500 hover:underline">Login</router-link></p>
            </div>
        </div>
    </div>
</template>

<script setup>
import Navbar from "../components/Navbar.vue";
import Form from "../components/Form.vue";
import Input from "../components/Input.vue";
import Button from "../components/Button.vue";
import { ref, reactive} from "vue";
import { RouterLink } from "vue-router"
import { useAuth } from "../composable/useAuth"

const { tryAuth } = useAuth()
const userData = reactive({
    username: "",
    email: "",
    password: ""
})
const confirmPassword = ref("")
const message = ref("")
const showMessage = ref(false)
const status = reactive({
    success: false,
    error: false,
})

const handleRegister = async () => {
    if (confirmPassword.value === userData.password) {
        const response = await tryAuth(import.meta.env.VITE_API_BASEURL + "/api/users/", userData)
        if (response.data.success) {
            message.value = response.data.message
            showMessage.value = true
            status.success = true
        }
        else if (response.status == 422) {
            message.value = "Invalid input data"
            showMessage.value = true
            status.error = true
        } else if (response.status == 409) {
            message.value = response.data.message
            showMessage.value = true
            status.error = true
        } else{
            message.value = "Something went wrong"
            showMessage.value = true
            status.error = true
        }
    }
    else {
        message.value = "Password don't match"
        showMessage.value = true
        status.error = true
    }
}

</script>
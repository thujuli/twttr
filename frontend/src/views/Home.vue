<template>
    <div class="flex flex-col">
        <Navbar/>
        <div class="flex flex-col mt-14 w-6/12 mx-auto">
            <Form>
                <Textarea id="tweet" placeholder="What's happening?" rows="5" v-model="content"/>
                <div class="flex gap-5">
                    <Button button-name="SUBMIT" button-type="submit" @handle-click="handleSubmit"/>
                    <Button button-name="UPLOAD FILE" button-type="button" @handle-click="toggleModal"/>
                </div>
            </Form>
            <div class="flex flex-col space-y-3 mt-4">
                <Card v-for="data in dataUser" :key="data.id" :username="data.user.username" :content="data.content" :image-path="data.image_path"/>
                <!-- pagination -->
                <div class="pagination flex justify-center gap-5 items-center">
                    <button @click="prevItem" :disabled="page === 1"
                        class="bg-sky-500 p-2 mt-2 rounded-xl font-bold text-gray-200 hover:bg-sky-800 disabled:bg-gray-500">Previous</button>
                    <span class="text-xl text-gray-200">{{ page }} of {{ pagination.totalPages }}</span>
                    <button @click="nextItem" :disabled="page === pagination.totalPages"
                        class="bg-sky-500 p-2 mt-2 rounded-xl font-bold text-gray-200 hover:bg-sky-800 disabled:bg-gray-500">Next</button>
                </div>
            </div>
        </div>
        <!-- <div v-show="showModal"> -->
        <Modal :is-open="showModal" @toggle-modal="toggleModal">
            <Form>
                <Textarea id="uploadFile" placeholder="What's happening?" rows="5" v-model="formData.content"/>
                <InputFile id="uploadBtn" v-model="formData.file"/>
                <div class="flex flex-row gap-3 mt-2">
                    <Button @handle-click="toggleModal" button-name="CLOSE" button-type="button"/>
                    <Button @handle-click="handleUpload" button-name="SUBMIT" button-type="submit"/>
                </div>
            </Form>
        </Modal>
        <!-- <Modal :is-open="showModal" @close-modal="toggleModal" @upload-button="handleUpload"/> -->
        <!-- </div> -->
    </div>
</template>

<script setup>
import Navbar from "../components/Navbar.vue";
import Form from "../components/Form.vue";
import Button from "../components/Button.vue";
import Card from "../components/Card.vue";
import Modal from "../components/Modal.vue";
import Textarea from "../components/Textarea.vue";
import InputFile from "../components/InputFile.vue";
import { ref, onMounted, reactive, watch} from "vue";
import { useAxios} from "../composable/useAxios"
import Swal from "sweetalert2"

const { tryFetch, tryPost, tryUpload } = useAxios()
const showModal = ref(false)

const dataUser = ref([])
const apiTweet = import.meta.env.VITE_API_BASEURL + "/api/tweets/"
const content = ref("")
const formData = reactive({
    content: "",
    file: "",
})

const page = ref(1)
const per_page = ref(3)
const pagination = reactive({
    totalItems: 0,
    totalPages: 0,
})

const prevItem = () => {
    page.value --
    console.log(page.value)
}

const nextItem = () => {
    page.value ++ 
    console.log(page.value)
}

watch(page, (newPage) => {
    handleFetching(newPage, per_page.value)
})

const toggleModal = () => {
    showModal.value = !showModal.value
}

const handleFetching = async (page, per_page) => {
    const response = await tryFetch(apiTweet, page, per_page)
    dataUser.value = response.data.data
    pagination.totalItems = response.data.total_items
    pagination.totalPages = response.data.total_pages
}

const handleSubmit = async () => {
    const response = await tryPost(apiTweet, {"content": content.value})
    if (response.data.success) {
        Swal.fire({
            icon: 'success',
            title: 'Good job!',
            text: response.data.message
        })
        content.value = ""
        handleFetching()
    }
    else if (response.status == 422) {
        Swal.fire({
            icon: 'error',
            title: 'Invalid data',
            text: 'Please check your input!'
        })
    } else {
        Swal.fire({
            icon: 'error',
            title: 'Oops...',
            text: 'Something went wrong!'
        })
    }
}

const handleUpload = async () => {
    const response = await tryUpload(apiTweet, formData)
    try {
        if (response.status == 415) {
            Swal.fire({
                icon: 'error',
                title: 'Invalid data',
                text: 'Please check your input!'
            })
        } else if (response.status == 500) {
            Swal.fire({
                icon: 'error',
                title: 'Oops...',
                text: response.data.message
            })
        }     
    } catch {
        Swal.fire({
            icon: 'success',
            title: 'Good job!',
            text: 'Tweet has been successfully created'
        })
        toggleModal()
        handleFetching()
    }
}

onMounted(async ()=> {
    handleFetching()
})

</script>
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
                <!-- <Card v-for="data in dataUser" :key="data.id" :username="data.user.username" :content="data.content" :image-path="data.image_path"/> -->
                <Card v-for="data in dataUser" :key="data.id">
                    <img class="w-full" :src="data.image_path" :alt="data.image_name">
                    <div class="px-6 py-2">
                        <h3 class="text-gray-300 text-lg">{{ data.content }}</h3>
                        <h2 class="font-semibold text-gray-200 text-lg text-left md:text-right"> <span class="border-b-2">{{ data.user.username }}</span></h2>
                    </div>
                    <div class="flex flex-row px-4 gap-3 pt-2 border-t-2 border-sky-800 bg-gray-300">
                        <BtnLike button-type="submit" @handle-click="likeTweet(data.id)" :likes="data.likes.length"/>
                    </div>
                </Card>
                <!-- pagination -->
                <div class="pagination flex justify-center gap-5 items-center">
                    <BtnPagination @handle-click="prevItem" button-name="Previous" button-type="button" :disabled="page ===1"/>
                    <span class="text-xl text-gray-200">{{ page }} of {{ totalPages }}</span>
                    <BtnPagination @handle-click="nextItem" button-name="Next" button-type="button" :disabled="page === totalPages"/>
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
import BtnLike from "../components/BtnLike.vue";
import BtnPagination from "../components/BtnPagination.vue";
import { ref, onMounted, reactive, watch} from "vue";
import { useAxios } from "../composable/useAxios"
import Swal from "sweetalert2"

const { tryFetch, tryPost, tryUpload, tryLike } = useAxios()
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
const totalPages = ref(1)


const likeTweet = async (tweet_id) => {
    await tryLike(`${apiTweet}${tweet_id}/likes`)
    handleFetching(page.value, per_page.value)
}

const prevItem = () => {
    page.value --
}

const nextItem = () => {
    page.value ++ 
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
    if (response.data.total_pages !== 0) {
        totalPages.value = response.data.total_pages
    }
    console.log(dataUser.value)
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
        handleFetching(page.value, per_page.value)
        toggleModal()
    }
}

onMounted(async ()=> {
    handleFetching(page.value, per_page.value)
})

</script>
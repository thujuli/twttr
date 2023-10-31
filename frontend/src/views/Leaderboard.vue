<template>
    <div class="flex flex-col">
        <Navbar/>
        <div class="mx-auto w-1/2 mt-14 bg-gray-200 p-2 rounded-md">
            <h1 class="text-2xl mb-3 text-center">Leaderboard</h1>
            <DataTable class="display" :columns="columns" :data="data" :options="options"/>
        </div>
    </div>
</template>

<script setup>
import Navbar from '../components/Navbar.vue';
import DataTable from 'datatables.net-vue3';
import DataTablesCore from 'datatables.net-dt';
import { onMounted, ref } from 'vue';
import { useAxios } from '../composable/useAxios';
DataTable.use(DataTablesCore);

const data = ref([])
const { tryFetch } = useAxios()
const columns = [
    { data: 'username', title: 'Username' },
    { data: 'count', title: 'Tweet Count' },
];
const options = {
    searching: false,
    responsive:true,
    select:true,
}

const handleFetch = async() => {
    const response = await tryFetch(import.meta.env.VITE_API_BASEURL + "/api/leaderboard/")
    data.value = response.data.data
}

onMounted(async () => {
    handleFetch()
})
</script>

<style>
@import 'datatables.net-dt';
</style>
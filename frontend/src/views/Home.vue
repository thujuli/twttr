<template>
    <div class="flex flex-col">
        <Navbar/>
        <div class="flex flex-col mt-14 w-6/12 mx-auto">
            <Form>
                <textarea name="tweet" id="tweet" rows="5" placeholder="What's happening?" class="rounded-md bg-gray-800 text-gray-300 text-lg font-semibold p-2" style="resize: none;"></textarea>
                <div class="flex items-center justify-center mt-2">
                    <input class="block w-full text-lg font-bold text-gray-900 border border-gray-300 rounded-lg cursor-pointer bg-gray-50 dark:text-gray-400 focus:outline-none dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 mr-2 basis-3/4" id="default_size" type="file">
                    <div class="flex-1">
                        <Button button-name="Tweet" button-type="submit "/>
                    </div>
                </div>
            </Form>
            <Card username="admin" image-path="https://picsum.photos/id/237/1080/720" content="Lorem ipsum dolor sit amet consectetur adipisicing elit. Explicabo aliquam molestias cupiditate vero, alias, quia eum atque nihil repellendus voluptatibus sapiente cum? Sed at distinctio iure. Autem sunt aspernatur voluptas!
"/>
<Card username="admin" image-path="https://picsum.photos/id/237/1080/720" content="Lorem ipsum dolor sit amet consectetur adipisicing elit. Explicabo aliquam molestias cupiditate vero, alias, quia eum atque nihil repellendus voluptatibus sapiente cum? Sed at distinctio iure. Autem sunt aspernatur voluptas!
"/>
<Card username="admin" image-path="https://picsum.photos/id/237/1080/720" content="Lorem ipsum dolor sit amet consectetur adipisicing elit. Explicabo aliquam molestias cupiditate vero, alias, quia eum atque nihil repellendus voluptatibus sapiente cum? Sed at distinctio iure. Autem sunt aspernatur voluptas!
"/>
        </div>
    </div>
</template>

<script setup>
import Navbar from "../components/Navbar.vue";
import Form from "../components/Form.vue";
import Button from "../components/Button.vue";
import Card from "../components/Card.vue";
</script>
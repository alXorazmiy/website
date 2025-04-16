<template>
    <div class="h-screen w-full bg-[#0d1117] flex flex-col">
        <!-- TOP (Username input) -->
        <div class="h-[100px] w-full bg-[#0d1117] flex justify-center items-center">
            <input v-model="username" type="text" class="w-[300px] outline-none p-2 bg-[#151b23] rounded text-white" placeholder="Username">
        </div>

        <!-- MESSAGES (scrollable area) -->
        <div class="flex-1 overflow-y-auto px-4 py-6 flex flex-col-reverse ">
            <div v-for="(message, index) in messages" :key="index" class="w-[50%] mx`-auto" :id="`message-${message.id}`">
                <div v-if="username != message.username" class="flex items-center w-full mb-8">
                    <div class="flex flex-col items-center">
                        <div class="h-[50px] w-[50px] rounded-full bg-teal-700 flex justify-center items-center text-[30px] text-white">
                            {{ message.username.charAt(0).toUpperCase() }}
                        </div>
                    </div>
                    <div class="ml-8 p-3 w-[400px] bg-green-500 rounded text-white">
                        <div class="flex justify-between pb-3">
                            <span class="font-bold">{{ message.username }}</span>
                            <span>{{ message.date }}</span>
                        </div>
                        <span>{{ message.message }}</span>
                    </div>
                </div>

                <div v-else class="flex items-center justify-end w-full mb-8">
                    <div class="mr-8 p-3 w-[400px] bg-[#010409] rounded text-white">
                        <div class="flex justify-between pb-3">
                            <span class="font-bold">{{ message.username }}</span>
                            <span>{{ message.date }}</span>
                        </div>
                        <span>{{ message.message }}</span>
                    </div>
                    <div class="flex flex-col items-center">
                        <div class="h-[50px] w-[50px] rounded-full bg-teal-700 flex justify-center items-center text-[30px] text-white">
                            {{ message.username.charAt(0).toUpperCase() }}
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- BOTTOM (Message input) -->
        <div class="h-[100px] w-full bg-[#0d1117] flex justify-center items-center">
            <div class="flex justify-center items-center w-[700px] mx-auto">
                <form @submit.prevent="submit" class="w-[90%]">
                    <input v-model="message" type="text" class="w-full h-[80px] outline-none p-2 bg-[#151b23] rounded text-white" placeholder="Message">
                </form>
                <button class="rounded-full bg-[#f02c56] ml-5 flex justify-center items-center w-[60px] h-[60px]" @click="submit">
                    <Icon name="mynaui:send-solid" size="40" class="text-white" />
                </button>
            </div>
        </div>
    </div>
</template>

<script setup>
import { ref, onMounted, nextTick, watch } from 'vue';
import Pusher from 'pusher-js';
import axios from 'axios';

const username = ref('');
const message = ref('');
const messages = ref([]);

function submit() {
    if (message.value.trim() !== '') {
        const newMessage = {
            id: Date.now(), 
            username: username.value,
            message: message.value, 
            date: new Date().toLocaleTimeString(),
        };
        axios.post("http://127.0.0.1:8001/api/v1/messages/", newMessage);
        message.value = ''; // Clear input after submit
    }
}
onMounted(() => {
    Pusher.logToConsole = true;

    const pusher = new Pusher('a1dd35e4fe0e49e62d9b', { cluster: 'us2' });
    const channel = pusher.subscribe('chat');
    channel.bind('message', function (data) {
        // Yangi xabarni messages massiviga qo'shish
        messages.value.unshift(data);
        console.log(data)

        // nextTick(() => {
        //     const container = document.querySelector('.overflow-y-scroll');
        //     const scrollHeight = container.scrollHeight;
        //     const clientHeight = container.clientHeight;

        //     // Container to'liq to'ldirilganidan keyin skroll qilish
        //     if (scrollHeight > clientHeight) {
        //         const lastMessage = messages.value[messages.value.length - 1];
        //         const lastMessageElement = document.getElementById(`message-${lastMessage.id}`);
        //         if (lastMessageElement) {
        //             lastMessageElement.scrollIntoView({ behavior: 'smooth' });
        //         }
        //     }
        // });
    });
});


</script>


<style>
::-webkit-scrollbar {
    width: 0; 
    height: 0;
}
</style>
<template>
  
    <div class = "table">
        <EasyDataTable
                buttons-pagination
                :headers="headers"
                :items="controllerStore.students"
                table-class-name="customize-table"
                :search-value="searchValue"
                >
                <template #item-image="{image}">
                    <img class = "table-student-image" :src="image" alt="">
                </template>
                <template #item-first_name="{first_name, last_name}">
                    <p class = 'name' >{{ last_name }} {{first_name}}</p>
                </template>
                <template #item-faculty="{faculty}">
                    <p  >{{faculty.name}}</p>
                </template>
                <template #item-course="{course, }">
                    <p  >{{course}} - kurs</p>
                </template>
            </EasyDataTable>
    </div>
</template>

<script setup>
    import axios from "axios";
    import { onMounted, ref } from "vue";
    const searchValue = ref('')

    const headers = [
        { text: "Id", value: "id", width : 30},
        { text: "Rasm", value: "image", width: 50},
        { text: "Talaba", value: "first_name", width: 150},
        // { text: "Familiya", value: "last_name", width: 150},
        { text: "Fakultet", value: "faculty", width: 100},
        { text: "Kurs", value: "course", width: 70},
        { text: "Qavat", value: "floor", width: 70},
        { text: "Xona", value: "room", width: 70},
        { text: "Joy", value: "bed", width: 70},
        { text: "...", value: "detail", width: 20 },
        
        
    ]

    import {useControllerStore} from '../stores/controller'

    const controllerStore = useControllerStore()


    onMounted(()=>{
        axios.get('allstudents/')
            .then((data)=>{
                controllerStore.students = data.data
            })
    })

</script>

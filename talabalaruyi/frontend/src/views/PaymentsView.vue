<template>
  
    <div class = "table">
        <div class="buttons">
            <button @click="payment_open">To'lov</button>
        </div>

        <EasyDataTable
                buttons-pagination
                :headers="headers"
                :items="controllerStore.payments"
                table-class-name="customize-table"
                :search-value="searchValue"
                >
                <template #item-student="{student}">
                    <p class = 'name' > {{student.last_name}} {{student.first_name}}</p>
                </template>
                <template #item-amount="{amount}">
                    <p class = 'payment' >{{(new Intl.NumberFormat('ru-RU').format(amount))  }} <span>UZS</span> </p>
                </template>
                <template #item-date="{date}">
                    <p class = 'payment' >{{(new Date(date).toLocaleDateString('RU-ru'))  }}</p>
                </template>
            </EasyDataTable>

            

            <n-modal
                v-model:show="payment_if"
                :mask-closable="true"
                @keydown.enter = "payment"

            >
            <div class = 'modal' style = "width: 300px; min-height: 180px !important">
                <div class ='payment'>
                    <n-select
                        v-model:value="select_student"
                        filterable tag
                        
                        :options="select_options"
                    />
                    <div class = "modal-payment">
                        <input type="number" placeholder="summa" v-model="select_summa">
                    </div>  
                </div>
                <div class="buttons">
                    <button type="submit" class = 'payment' @click="payment">To'lov</button>
                </div>
            </div>

        </n-modal>

    </div>
</template>

<script setup>
    import axios from "axios";
    import { onMounted, ref } from "vue";
    import { useWindowSize } from 'vue-window-size'
    import {useInfoStore} from '../stores/infos'
    import {useControllerStore} from '../stores/controller'


    const controllerStore = useControllerStore()
    const infoStore = useInfoStore()

    const searchValue = ref('')
    const payment_if = ref(false)
    const select_options = ref([])
    const select_student = ref('')
    const select_summa = ref('')
    let headers = []



  


    function payment_open(){
        payment_if.value = true
        axios.get('allstudents/')
            .then((data)=>{
                let list = data.data
                let new_list = []
                for (let i = 0; i < list.length; i ++){
                    let new_items = {
                        label : `${list[i].last_name} ${list[i].first_name}`,
                        value: list[i].id
                    }
                    new_list.push(new_items)
                }

                select_options.value = new_list
            })
    }
    function payment(){
        let request = {
            student : select_student.value,
            amount: select_summa.value
        }
        axios.post('payments/', request)
            .then((data)=>{
                const timestamp = Date.now()

                infoStore.info_if = true
                let error = {
                    id : timestamp,
                    type: "success",
                    text: `${(new Intl.NumberFormat('ru-RU').format(select_summa.value))} to'landi`
                }
                infoStore.info_list.push(error)
                controllerStore.payments = data.data.reverse()
                payment_if.value = false
            })
    }

    onMounted(()=>{
        const screen_size =  useWindowSize()

        if (Number(screen_size.width.value) < 600) {
            headers = [
                { text: "Talaba", value: "student", width: 300},
                { text: "Summa", value: "amount", width: 150},
                { text: "Sana", value: "date", width: 150},
                
            ]
        }else{
            headers = [
                { text: "Talaba", value: "student", },
                { text: "Summa", value: "amount", width: 150},
                { text: "Sana", value: "date", width: 150},
                
            ]
        }
        axios.get('payments/')
            .then((data)=>{
                controllerStore.payments = data.data.reverse()
            })
    })

</script>

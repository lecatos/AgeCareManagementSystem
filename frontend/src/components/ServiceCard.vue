

<script setup lang="ts">
import type { StringMappingType } from 'typescript';
import ServiceForm from './ServiceForm.vue';
import { ref } from 'vue';
let props = defineProps<{
    id: number
    image: string,
    name: string,
    type: string,
    location: string,
    duration: string,
    category: string,
    staff_associated: any[],
    client_associated: any[]
}>()
const serviceform: any = ref(null);
function openModal(){
    serviceform.value.openModal();
}
const emit = defineEmits(["updateService"])
</script>

<template>
    <ServiceForm @updateService="emit('updateService')" ref="serviceform" type="edit" :obj="{id: id, image: image, name: name, type: type, location: location, duration: duration, category: category, staff_associated: staff_associated, client_associated: client_associated}"/>
    <div @click=openModal class="col-lg-4 my-3" style="width: 500px; border: 1px solid black; background-color: white;">
        <div class="mb-4" style="height: 150px; background-color: lightblue;">
            <img height=150 width=500 :src="props.image">
        </div>
        <div>
            <h3 class="px-4">{{ props.name }}</h3>
            <ul style="list-style-type:none;">
                <li><b>Type:</b> {{ props.type }}</li>
                <li><b>Location:</b> {{ props.location }}</li>
                <li><b>Duration:</b> {{ props.duration }}</li>
                <li><b>Category:</b> {{ props.category }}</li>
                <li><b>Staff Associated:</b> |<span v-for="n in props.staff_associated">&nbsp;{{ `${n.first_name} ${n.last_name}` }} |</span></li>
                <li><b>Client Associated:</b> |<span v-for="n in props.client_associated">&nbsp;{{ `${n.first_name} ${n.last_name}` }} |</span></li>
                <li><b>Status:</b> Running</li>
            </ul>  
        </div>
    </div>
</template>

<style>
</style>
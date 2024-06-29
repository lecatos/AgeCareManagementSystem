<script setup lang="ts">
import axios from "axios";
import * as bootstrap from 'bootstrap';
import {ref, reactive, onMounted, computed } from 'vue'
import { serviceStore } from "@/stores/serviceStore";

type type = "add" | "edit"

const state = reactive({
    modal_demo: null as null | bootstrap.Modal,
})
const users: any = computed(()=>{
    return serviceStore.value.users
})
const clients: any = computed(()=>{
    return serviceStore.value.clients
})
defineExpose({ openModal })
const emit = defineEmits(["updateService"])
let props = defineProps<{
    type: type
    obj: any
}>()
const objref = ref(props.obj)
const is_group = computed(()=>objref.value.type == "Group")
objref.value.client_associated = props.obj.client_associated?.map((d: any)=>d.id)
objref.value.staff_associated = props.obj.staff_associated?.map((d: any)=>d.id)
function openModal()
{
    state.modal_demo?.show()
}
const servicemodal: any = ref(null);
onMounted(() => {
    state.modal_demo = new bootstrap.Modal(servicemodal.value)
    //axios.get("/api/user/list?limit=10000")
    //    .then((res) => {users_tmp.value = res.data.results;console.log(users_tmp.value)});
    //axios.get("/api/client/list?limit=10000")
    //    .then((res) => {clients_tmp.value = res.data.results;console.log(clients_tmp.value)})

})

function closeModal()
{
    state.modal_demo?.hide()
}
function submits(e: any){
    if (e.target){
        let formData = new FormData(e.target);
        console.log(Array.from(formData.entries()))
        axios.post(e.target.action, formData)
        .then((res) => {closeModal();emit("updateService")})
        .catch((res)=>{
            console.log(res);
            //closeModal();
            alert("Failed!\nReason:" + JSON.stringify(res.response.data, null, "\t"))
        });
    }
    if (props.type == "add"){
        reset(e.target)
    }
}
function deletes(){
    axios.post("/api/service/remove", {id: props.obj.id})
        .then((res) => {closeModal();emit("updateService")})
        .catch((res)=>{
            console.log(res);
            //closeModal();
            alert("Failed!\nReason:" + JSON.stringify(res.response.data, null, "\t"))
        });
}
function reset(formele: any){
    objref.value = {};
    formele.reset()
}
</script>

<template>

<!-- Popup Form -->
<div class="modal fade" ref="servicemodal" id="ServiceModal" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
  <div class="modal-dialog modal-dialog-centered" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title" id="exampleModalLabel">{{ type == "add" ? "Add" : "Edit" }} Service</h5>
      </div>
        <!-- Modal Body -->
    <form @submit.prevent="submits" id="serviceedit" method="post" :action='type == "add" ? "/api/service/add" : "/api/service/update"'>
        <div class="modal-body">
            <!-- Service ID-->
            <input type="hidden" id="serviceId" name="id" :value=objref.id>
            <div class="form-group">
              <label>Service Banner</label>
              <input id="photo" type="file" name="image">
            </div>
            <!-- Service Name -->
            <div class="form-group">
                <label for="name">Service Name</label>
                <input v-model=objref.name required type="text" class="form-control" name="name" placeholder="Enter name">
            </div>

            <!-- Type -->
            <div class="form-group">
                <label for="type">Type</label>
                <fieldset id="group1">
                    <div class="form-check">
                        <input v-model=objref.type required class="form-check-input" type="radio" name="type" id="option1" value="Individual">
                        <label class="form-check-label" for="option1">
                            Individual
                        </label>
                    </div>
                    <div class="form-check">
                        <input v-model=objref.type required class="form-check-input" type="radio" name="type" id="option2" value="Group">
                        <label class="form-check-label" for="option2">
                            Group
                        </label>
                    </div>
                </fieldset>
            </div>
            <!-- Location -->
            <div class="form-group">
                <label for="location">Location</label>
                <input v-model=objref.location required type="text" class="form-control" id="location" name="location">
            </div>
            <div class="form-group">
                <label for="duration">Duration</label>
                <input v-model=objref.duration required type="time" class="form-control" id="duration" name="duration">
            </div>
            <!-- Category -->
            <div class="form-group">
                <label for="category">Category</label>
                <select required v-model="objref.category" name="category">
                <option disabled value="undefined">Please select one
                </option>
                <option>
                <label class="form-check-label">
                    Health & Wellbeing
                </label>
                </option>
                <option>
                <label class="form-check-label">
                    Rehabiliation
                </label>
                </option>
                <option>
                <label class="form-check-label">
                    Pain Management
                </label>
                </option>
                <option>
                <label class="form-check-label">
                    Psychological
                </label>
                </option>
                <option>
                <label class="form-check-label">
                    Physical
                </label>
                </option>
                <option>
                <label class="form-check-label">
                    Others
                </label>
                </option>
            </select>
            </div>

            <!-- Staff Associate -->
            <div class="form-group">
                <label for="staff">+ Staff</label>
                <select multiple v-model="objref.staff_associated" required id="staff" class="form-control" name="staff_associated">
                    <option type="number" v-for="(staff, i) in users" :key=i :value=staff.id>{{`${staff.first_name} ${staff.last_name}`}}</option>
                </select>
            </div>
            <!-- Client Associate -->
            <div class="form-group">
                <label for="member">+ Member</label>
                <select multiple v-model="objref.client_associated" required id="member" class="form-control" name="client_associated">
                    <option type="number" v-for="(client, i) in clients" :key=i :value=client.id>{{`${client.first_name} ${client.last_name}`}}</option>
                </select>
            </div>
        </div>
        <div class="modal-footer">
            <template v-if="type == 'edit'">
                <input type="submit" class="btn btn-primary" value="Update"></input>
                <input @click=deletes type="button" class="btn btn-danger" value="Delete"></input>
            </template>
            <template v-else-if="type == 'add'">
                <input type="submit" class="btn btn-primary" value="Add"></input>
            </template>
            <button type="button" class="btn btn-secondary" @click=closeModal>Close</button>
        </div>
    </form>
    </div>
  </div>
</div>
</template>

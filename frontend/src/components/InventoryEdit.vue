<script setup lang="ts">
import axios from "axios";
import * as bootstrap from 'bootstrap';
import {watch, ref, reactive, onMounted } from 'vue'

let props = defineProps<{
    inv: any,
}>()
const state = reactive({
    modal_demo: null as null | bootstrap.Modal,
})
defineExpose({ openModal })
const emit = defineEmits(["updateInv"])
function openModal()
{
   
    state.modal_demo?.show()
}
onMounted(() => {
    state.modal_demo = new bootstrap.Modal('#modal_demo', {})
})

function closeModal()
{
    state.modal_demo?.hide()
}
function submits(e: any){
    if (e.target){
        let formData = new FormData(e.target);
        
        axios.post(e.target.action, formData)
        .then((res) => {closeModal();emit("updateInv")})
        .catch((res)=>{
            console.log(res);
            alert("Failed!\nReason:" + JSON.stringify(res.response.data, null, "\t"))
        });
    }
    reset(e.target)
}
function reset(form: any){
    form.reset()
}
function deletes(){
    axios.post(`/api/inventory/${props.inv.item_name}/remove`)
        .then((res) => {closeModal();emit("updateInv")})
        .catch((res)=>{
            console.log(res);
            alert("Failed!\nReason:" + JSON.stringify(res.response.data, null, "\t"))
        });
}
</script>

<template>
<!-- Modal -->
<div class="modal fade" id="modal_demo" tabindex="-1" aria-labelledby="modal_demo_label" aria-hidden="true">
  <div class="modal-dialog modal-dialog-centered">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title" id="modal_demo_label">Inventory Stock Manager</h5>
        <button type="button" class="btn-close" aria-label="Close" @click="closeModal"></button>
      </div>
      <form v-on:submit.prevent="submits" id="invform" method="post" :action="'/api/inventory/'+inv.item_name+'/update'">
      <div class="modal-body">
          <!-- Stock -->
          <div class="form-group">
              <label for="qty">Quantity</label>
              <input :value=inv.qty type="number" id="qty" name="qty">
          </div>
          
        </div>
        <div class="modal-footer">
            <input type="submit" class="btn btn-primary" value="Update Stock">
            <button @click=deletes type="button" class="btn btn-danger">Delete</button>
            <button type="button" class="btn btn-secondary" @click="closeModal">Close</button>
        </div>
    </form>
    </div>
  </div>
</div>
</template>

<style>
</style>

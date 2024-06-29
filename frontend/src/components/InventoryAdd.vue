<script setup lang="ts">
import {reactive, ref, onMounted} from "vue";
import * as bootstrap from 'bootstrap';
import axios from 'axios';

const state = reactive({
    modal_demo: null as null | bootstrap.Modal,
})
defineExpose({ openModal })
const emit = defineEmits(["updateInv"])
function openModal()
{
   
    state.modal_demo?.show()
}
const addinv: any = ref(null)
onMounted(() => {
    state.modal_demo = new bootstrap.Modal(addinv.value, {})
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
}
</script>
<template>
    <div class="contain row my-1 mb-3">
        <div class="row d-flex justify-content-center">
        <button @click=openModal  class="btn btn-primary">Add Inventory</button>
        </div>
    </div>

    <!-- Modal -->
<div ref="addinv" class="modal fade" id="modal_demo" tabindex="-1" aria-labelledby="modal_demo_label" aria-hidden="true">
  <div class="modal-dialog modal-dialog-centered">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title" id="modal_demo_label">Inventory Stock Manager</h5>
        <button type="button" class="btn-close" aria-label="Close" @click="closeModal"></button>
      </div>
      <form v-on:submit.prevent="submits" id="invform" method="post" :action="'/api/inventory/add'">
      <div class="modal-body">
        <!-- Image -->
        <div class="form-group">
              <label for="image">Image</label>
              <input type="file" id="image" name="image">
          </div>
        <!-- Name -->
        <div class="form-group">
              <label for="item_name">Item Name</label>
              <input required type="text" id="item_name" name="item_name">
          </div>
            <!-- Desc -->
            <div class="form-group">
                <label for="desc">Description</label>
                <input type="text" id="desc" name="desc">
            </div>
            <!-- crit Point -->
          <div class="form-group">
              <label for="critical_point">Critical Point</label>
              <input required type="number" id="critical_point" name="critical_point">
          </div>
          <!-- Stock -->
          <div class="form-group">
              <label for="qty">Quantity</label>
              <input required type="number" id="qty" name="qty">
          </div>
          
        </div>
        <div class="modal-footer">
            <input type="submit" class="btn btn-primary" value="Add Inventory">
            <button type="button" class="btn btn-secondary" @click="closeModal">Close</button>
        </div>
    </form>
    </div>
  </div>
</div>
</template>
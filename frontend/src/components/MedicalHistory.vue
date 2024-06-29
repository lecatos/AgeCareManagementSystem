<script setup lang="ts">
import axios from "axios";
import * as bootstrap from 'bootstrap';
import {watch, ref, reactive, onMounted } from 'vue'

let props = defineProps<{
    is_user: boolean,
    user: any
}>()
let user_type = props.is_user ? "user" : "client";
const state = reactive({
    modal_hist: null as null | bootstrap.Modal,
})
defineExpose({ openModal })
const emit = defineEmits(["updateList"])
function openModal()
{

    state.modal_hist?.show()
}
onMounted(() => {
    state.modal_hist = new bootstrap.Modal('#modal_hist', {})
})

function closeModal()
{
    state.modal_hist?.hide()
}

function submits(e: Event) {
    e.preventDefault();
    let myForm = document.getElementById('medHistForm') as HTMLFormElement;
    let formData = new FormData(myForm);
    const apiUrl = '/api/client/'+props.user.id+'/medhist/add';

    axios.post(apiUrl, formData).then(function (response) {
        closeModal();
        emit("updateList");
    }).catch((error) => {
        console.error(error);
        alert("Failed!\nReason:" + JSON.stringify(error.response.data, null, "\t"));
    });
}
</script>

<template>
<!-- Modal -->
<div class="modal fade" id="modal_hist" tabindex="-1" aria-labelledby="modal_demo_label" aria-hidden="true">
  <div class="modal-dialog modal-dialog-centered">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title" id="modal_demo_label">{{is_user ? "Staff" : "Member"}} Edit</h5>
        <button type="button" class="btn-close" aria-label="Close" @click="closeModal"></button>
      </div>
      <form v-on:submit.prevent="submits" id="medHistForm" method="post" :action="'/api/client/'+user.id+'/medhist/add'">
      <div class="modal-body">
        <!-- File Upload -->
        <div class="form-group">
            <label>{{user.first_name}} {{user.last_name}}</label>
            <img :src=user.avatar alt="" border=3 height=100 width=100></img>
        </div>
        <div class="row my-1">
          <table class="table table-striped table-hover">
            <thead class="table-dark">
              <tr>
                <th scope="col" class="col-1">Date</th>
                <th scope="col" class="col-1">Facility</th>
                <th scope="col" class="col-1">Description</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="entry in user.medhist" scope="row">
                <td>{{entry.date}}</td>
                <td>{{entry.facility}}</td>
                <td>{{entry.description}}</td>
              </tr>
            </tbody>
          </table>
        </div>

        <div class="form-group">
          <label for="date">Date</label>
          <input id="date" type="date" name="date">
        </div>
        <div class="form-group">
          <label for="facility">Facility</label>
          <input id="facility" type="text" name="facility">
        </div>
        <div class="form-group">
          <label for="description">Description</label>
          <input id="description" type="text" name="description">
        </div>
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-secondary" @click="closeModal">Close</button>
        <input type="submit" class="btn btn-primary" value="Add Entry">
      </div>
      </form>
    </div>
  </div>
</div>
</template>

<style>
</style>

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
    modal_demo: null as null | bootstrap.Modal,
})
defineExpose({ openModal })
const emit = defineEmits(["updateList"])
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
        .then((res) => {closeModal();emit("updateList")})
        .catch((res)=>{
            console.log(res);
            alert("Failed!\nReason:" + JSON.stringify(res.response.data, null, "\t"));
            closeModal();
        });
    }
}
</script>

<template>
<!-- Modal -->
<div class="modal fade" id="modal_demo" tabindex="-1" aria-labelledby="modal_demo_label" aria-hidden="true">
  <div class="modal-dialog modal-dialog-centered">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title" id="modal_demo_label">{{is_user ? "Staff" : "Member"}} Edit</h5>
        <button type="button" class="btn-close" aria-label="Close" @click="closeModal"></button>
      </div>
      <form v-on:submit.prevent="submits" id="staffadd" method="post" :action="'/api/'+user_type+'/'+user.id+'/update'">
      <div class="modal-body">
          <!-- File Upload -->
          <div class="form-group">
              <label>{{user.first_name}} {{user.last_name}}</label>
              <img :src=user.avatar alt="" border=3 height=100 width=100></img>
              <label for="photo">Upload Photo</label>
              <input id="photo" type="file" name="avatar">
          </div>
          <!-- Full Name -->
          <div class="form-group">
              <label for="fname">First Name</label>
              <input :value=user.first_name id="fname" type="text" name="first_name">
          </div>
          <div class="form-group">
              <label for="lname">Last name</label>
              <input :value=user.last_name id="lname" type="text" name="last_name">
          </div>
          <!-- Gender Selection -->
          <div class="form-group gender">
                <span>Gender:</span>
                <div>
                    <input type="radio" id="male" name="sex" value="M" class="gender-radio" :checked="user.sex == 'M' ? true : false">
                    <label for="male" class="gender-label">Male</label>
                    
                    <input type="radio" id="female" name="sex" value="F" class="gender-radio" :checked="user.sex == 'F' ? true : false">
                    <label for="female" class="gender-label">Female</label>
                </div>
          </div>
          <div v-if=is_user>
            <div class="form-group">
              <label for="username">Username</label>
              <input :value=user.username id="username" type="text" placeholder="david@hotmail.com" name="usename">
            </div>
          </div>
          <!-- Email -->
          <div class="form-group">
              <label for="email">Email</label>
              <input :value=user.email id="email" type="text" placeholder="david@hotmail.com" name="email">
          </div>
          <!-- Phone Number -->
          <div class="form-group">
              <label for="phoneno">Phone Number</label>
              <input :value=user.tel id="phoneno" type="text" name="tel">
          </div>
          <!-- Date of Birth -->
          <div class="form-group">
              <label for="DoB">Date of Birth</label>
              <input :value=user.dob type="date" id="DoB" name="dob">
          </div>
          
        </div>
        <div class="modal-footer">
            <button type="button" class="btn btn-secondary" @click="closeModal">Close</button>
            <input type="submit" class="btn btn-primary" value="Save Changes">
        </div>
    </form>
    </div>
  </div>
</div>
</template>

<style>
</style>

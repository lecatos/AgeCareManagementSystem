<script lang="ts">
import axios from 'axios';
import { defineComponent, ref } from 'vue';
import ProfileEdit from "./ProfileEdit.vue";
import MedicalHistory from "./MedicalHistory.vue";
interface Client {
  id: number
  first_name: string;
  last_name: string;
  dob: string;
  sex: string;
  tel: string;
  email: string;
  avatar: string;
}
export default defineComponent({
    components: {ProfileEdit, MedicalHistory},
    data() {
      return {
        offset: 1,
        limit: 10,
        current: null as string | null,
        next: null as string | null,
        previous: null as string | null,
        count: null,
        clients: [] as Client[],
        selected_client: {} as Client,
        loading: true as boolean
      }
    },
    methods: {
      nextPage(){
        if (this.next !== null){
          axios.get(this.next)
          .then(res => {
            this.clients = res.data.results;
            this.current = this.next;
            this.next = res.data.next,
            this.previous = res.data.previous,
            this.count = res.data.count
          });
        }
      },
      previousPage(){
        if (this.previous !== null){
          axios.get(this.previous)
          .then(res => {
            this.clients = res.data.results;
            this.current = this.previous;
            this.next = res.data.next,
            this.previous = res.data.previous,
            this.count = res.data.count
          });
        }
      },
      search(e: any){
        axios.get("/api/client/list?limit=10000")
        .then(res => {
          this.clients = res.data.results.filter((client: Client)=>{
            return (client.first_name + " " + client.last_name).toLowerCase().includes(e.target.value.toLowerCase())
          });
        });
        console.log(e);
      },
      showEdit(){
        let profileedit: any = this.$refs.profileedit;
        profileedit.openModal();
      },
      showMedHist(){
        let medicalhistory: any = this.$refs.medicalhistory;
        medicalhistory.openModal();
      },
      updateClients(){
        let req;
        if (!this.current){
          req = axios.get("/api/client/list", { params: { limit:this.limit }})
        } else {
          req = axios.get(this.current)
        }
        req.then(res => {
          this.clients = res.data.results;
          this.next = res.data.next,
          this.previous = res.data.previous,
          this.count = res.data.count
        }).catch(function (error: any) {
          console.log(error.message);
        })
      }
    },
    mounted () {
      this.updateClients()
    }
  });
</script>

<template>
    <ProfileEdit @updateList=updateClients ref="profileedit" :is_user=false :user=selected_client></ProfileEdit>
    <MedicalHistory @updateList=updateClients ref="medicalhistory" :is_user=false :user=selected_client></MedicalHistory>
    <div class="member">
      <div class="container-fluid">
        <h2 class="row">This is a Member Table page</h2>
        <div class="row my-1 btn-holder">
          <input type="text" @input="search" placeholder="Search Name" class="mx-1 col-lg-2"> 
          <router-link to="/search/member-add" class="mx-1 col-lg-2 float-right btn btn-secondary">Add Member</router-link>
        </div>
        <div class="row my-1">
          <table class="table table-striped table-hover">
            <thead class="table-dark">
              <tr>
                <th scope="col" class="col-1">Profile</th>
                <th scope="col" class="col-1">Name</th>
                <th scope="col" class="col-1">Surname</th>
                <th scope="col" class="col-1">Sex</th>
                <th scope="col" class="col-1">DOB</th>
                <th scope="col" class="col-1">Tel</th>
                <th scope="col" class="col-1">Email</th>
                <th scope="col" class="col-1"></th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="client in clients" scope="row">
                <td><button class="p-0" @click="selected_client = client;showEdit();"><img  :src=client.avatar alt="" border=3 height=80 width=80></img></button></td>
                <td>{{client.first_name}}</td>
                <td>{{client.last_name}}</td>
                <td>{{client.sex}}</td>
                <td>{{client.dob}}</td>
                <td>{{client.tel}}</td>
                <td>{{client.email}}</td>
                <td><button class="btn btn-secondary" @click="selected_client = client;showMedHist();" width="fit-content">Medical History</button></td>
              </tr>
            </tbody>
          </table>
        </div>
        <div class="row d-flex justify-content-center">
          <button class="btn btn-primary col-1 mx-2" v-on:click="previousPage()"> < </button> <button class="btn btn-primary col-1 mx-2" v-on:click="nextPage()"> > </button>
        </div>
      </div>
    </div>
</template>

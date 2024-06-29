<script lang="ts">
  import axios from "axios"
  import { defineComponent } from 'vue';
  import ProfileEdit from "./ProfileEdit.vue";
  export interface User {
  first_name: string;
  last_name: string;
  dob: string;
  sex: string;
  tel: string;
  email: string;
  avatar: string;
}
  export default defineComponent({
    components: {ProfileEdit},
    data() {
      return {
        offset: 1,
        limit: 10,
        current: null as string | null,
        next: null as string | null,
        previous: null as string | null,
        count: null,
        selected_user: {} as User,
        users: [] as User[]
      }
    },
    methods: {
      nextPage(){
        if (this.next !== null){
          axios.get(this.next)
          .then(res => {
            this.users = res.data.results;
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
            this.users = res.data.results;
            this.current = this.previous;
            this.next = res.data.next,
            this.previous = res.data.previous,
            this.count = res.data.count
          });
        }
      },
      search(e: any){
        axios.get("/api/user/list?limit=10000")
        .then(res => {
          this.users = res.data.results.filter((user: User)=>{
            return (user.first_name + " " + user.last_name).toLowerCase().includes(e.target.value.toLowerCase())
          });
        });
        console.log(e);
      },
      showEdit(){
        let profileedit: any = this.$refs.profileedit;
        profileedit.openModal();
      },
      updateUsers(){
        let req;
        if (!this.current){
          req = axios.get("/api/user/list", { params: { limit:this.limit }})
        } else {
          req = axios.get(this.current)
        }
        req.then(res => {
          this.users = res.data.results;
          this.next = res.data.next,
          this.previous = res.data.previous,
          this.count = res.data.count
        }).catch(function (error: any) {
          console.log(error.message);
        })
      }
    },
    mounted () {
      this.updateUsers()
    }
});
</script>

<template>
    <ProfileEdit @updateList=updateUsers ref="profileedit" :is_user=true :user=selected_user></ProfileEdit>
    <div class="staff">
      <div class="container-fluid">
        <h2 class="row">This is a Staff Table page</h2>
        <div class="row my-1 btn-holder">
          <input type="text" @input="search" placeholder="Search Name" class="mx-1 col-lg-2"> 
          <router-link to="/search/staff-add" class="mx-1 col-lg-2 float-right btn btn-secondary">Add Staff</router-link>
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
              </tr>
            </thead>
            <tbody>
              <tr v-for="user in users" scope="row">
                <td><button class="p-0" @click="selected_user=user;showEdit()"><img :src=user.avatar alt="" border=3 height=80 width=80></img></button></td>
                <td>{{user.first_name}}</td>
                <td>{{user.last_name}}</td>
                <td>{{user.sex}}</td>
                <td>{{user.dob}}</td>
                <td>{{user.tel}}</td>
                <td>{{user.email}}</td>
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

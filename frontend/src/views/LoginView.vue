<script setup lang="ts">
import Hero from '../components/Hero.vue'
</script>

<script lang="ts">
import axios from "axios"
import {logged_user} from "../stores/logged_user"
export default {
  methods: {
    submits(e: any){
      let formData = new FormData(e.target);
       
      axios.post(e.target.action, formData).then((res)=>{
        logged_user.value.is_logged = true;
        logged_user.value.username = e.target.username.value;
        e.target.reset();
        this.$router.push("/");
      }).catch((res)=>{alert("Failed!\nReason:" + JSON.stringify(res.response.data, null, "\t"))})
    },
  }

};
</script>

<template>
  <main>
    <Hero><h1>Login</h1></Hero>
    <div class="login-container">
      <div class="login-box">
        <h2>Login</h2>
        <form v-on:submit.prevent="submits" id="loginform" method="post" action="/api/user/login">
          <div class="input-group">
            <label for="username">Username</label>
            <input type="text" id="username" name="username" placeholder="Type your username">
          </div>
          <div class="input-group">
            <label for="password">Password</label>
            <input type="password" id="password" name="password" placeholder="Type your password">
          </div>

          <input type="checkbox"><span> Remember me</span>
          <button class="login-button">LOGIN</button>
          
          <div class="forgot-password">
            <a href="/">Forgot password?</a>
          </div>
          <div class="additional-links">
            <a href="/">Look for FAQs</a>
            <a href="/">Report an issue?</a>
          </div>
        </form>
      </div>
    </div>
  </main>
</template>

<style scoped>
.login-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
}

.login-box {
  background-color: #ffffff;
  border-radius: 8px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
  padding: 40px;
  width: 400px;
}

h2 {
  text-align: center;
  margin-bottom: 30px;
  color: #333333;
}

.input-group {
  margin-bottom: 20px;
}

label {
  display: block;
  font-weight: bold;
  margin-bottom: 5px;
  color: #555555;
}

input[type="text"],
input[type="password"] {
  width: 100%;
  padding: 10px;
  border: 1px solid #dddddd;
  border-radius: 4px;
}

.forgot-password {
  text-align: left;
  margin-bottom: 20px;
}

.login-button {
  width: 100%;
  padding: 12px;
  background-color: #007bff;
  color: #ffffff;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-size: 16px;
  transition: background-color 0.3s ease;
}

.login-button:hover {
  background-color: #0056b3;
}

.signup-options {
  text-align: center;
  margin-top: 20px;
}

.social-buttons {
  display: flex;
  justify-content: center;
  margin-top: 10px;
}

.social-button {
  padding: 10px 20px;
  margin: 0 10px;
  border-radius: 4px;
  text-decoration: none;
  color: #ffffff;
}

.facebook {
  background-color: #3b5998;
}

.google {
  background-color: #dd4b39;
}

.linkedin {
  background-color: #0077b5;
}

.additional-links {
  text-align: center;
  margin-top: 20px;
}

.additional-links a {
  margin: 0 10px;
  color: #777777;
  text-decoration: none;
}
</style>
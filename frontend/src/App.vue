<script lang="ts">
import { RouterLink, RouterView } from 'vue-router'
import NavBar from './components/NavBar.vue'
import Banner from './components/Banner.vue'
import FootBar from './components/FootBar.vue'
import ProfileEdit from "./components/ProfileEdit.vue"
import HeroVue from "./components/Hero.vue"
import axios from "axios"
import {logged_user} from "./stores/logged_user"


export default {
  components: {NavBar, Banner, FootBar, ProfileEdit, HeroVue},
  methods: {
    getToken(){
      return this.$cookies.get('csrftoken');
    }
  },
  mounted(){
    const self = this;
    axios.interceptors.request.use(function(config) {
        const token = self.getToken();
        config.headers["X-Csrftoken"] = self.getToken();
        return config;
    }, (error) => {
        return Promise.reject(error);
    });
    axios.interceptors.response.use(null, (error) => {
        if (error.response.status == 403){
          this.$router.push("/login");
        }
        return Promise.reject(error);
    });
    axios.get("/api/user/whoami").then((res) => {
      if (res.data.is_authenticated){
        logged_user.value.is_logged = true;
        logged_user.value.username = res.data.user.username;
      }
    })
  }
}
</script>

<template>
  <header>
    <NavBar/>
  </header>
  <Banner />
  <div>
    <RouterView />
  </div>
  <footer>
    <FootBar />
  </footer>
</template>

<style scoped>
  a{
    color: white;
  }
</style>

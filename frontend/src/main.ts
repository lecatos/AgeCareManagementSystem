import './assets/bootstrap.min.css'
import './assets/bootstrap.bundle.min.js'

// Import Bootstrap and BootstrapVue CSS files (order is important)
import 'bootstrap/dist/css/bootstrap.css'


import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import VueCookies from "vue-cookies";
import axios from "axios";
const app = createApp(App)
app.config.globalProperties.$axios = axios
axios.defaults.withCredentials = true
app.use(router)
app.use(VueCookies)
app.mount('#app')

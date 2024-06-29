<script lang="ts">
import {logged_user} from "../stores/logged_user"
export default {
    data(){
        return {
            username: "Guest"
        }
    },
    computed:{
        logged_user(){
            return logged_user
        }
    }
}
</script>

<template>
    <nav class="navbar navbar-expand navbar-dark bg-dark">
        <div class="container">
            <RouterLink class="navbar-brand" to="/">System</RouterLink>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navtarget" aria-controls="navtarget" aria-expanded="false">
                <span class="navbar-toggler-icon"></span>
            </button>

            <div class="collapse navbar-collapse" id="navtarget">
                <ul class="navbar-nav me-auto">
                    <li class="nav-item">
                        <RouterLink class="nav-link" to="/search">Search</RouterLink>
                    </li>
                    <li class="nav-item">
                        <RouterLink class="nav-link" to="/service">Service</RouterLink>
                    </li>
                    <li class="nav-item">
                        <RouterLink class="nav-link" to="/inventory">Inventory</RouterLink>
                    </li>
                    <li class="nav-item">
                        <RouterLink class="nav-link" to="/login">Login</RouterLink>
                    </li>
                    <li class="nav-item">
                        <RouterLink class="nav-link" to="/logout">Logout</RouterLink>
                    </li>
                </ul>
            </div>
        </div>
        <label class="mx-5 text-white">Logged as: {{logged_user.value.username}}</label>
    </nav>
</template>
<script setup lang="ts">
import {logged_user} from "../stores/logged_user";
import {useRouter} from "vue-router";

logged_user.value.logout();
if (logged_user.value.is_logged){
    const router = useRouter();
    router.push("/");
}
</script>
<template></template>
<script setup lang="ts">
  import Hero from '../components/Hero.vue'
</script>

<template>
  <Hero><h1>Search Individual</h1></Hero>
  <main>
    <div class="search container">
      <div class="contain row my-1 mb-3">
        <div class="row d-flex justify-content-center">
          <RouterLink class="col-lg-2 btn btn-secondary mx-1" to="/search/member">Member</RouterLink>
          <RouterLink class="col-lg-2 btn btn-secondary mx-1" to="/search/staff">Staff</RouterLink>
        </div>
      </div>
      <div class="row my-1">
        <RouterView />
      </div>
    </div>
  </main>
</template>

<style>
.adjust{
  width: fit-content;
}

</style>
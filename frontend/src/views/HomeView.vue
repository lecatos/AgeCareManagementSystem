<script setup lang="ts">
  import Hero from '../components/Hero.vue'
</script>

<template>
  <main>
    <Hero><h1>Home page</h1></Hero>

    <div class="grid-container">
      <div class="grid-item">
        <RouterLink to="/service"><img class="image" src="./../../images/booking.jpg" alt="Booking"></RouterLink>
        <p>Service</p>
      </div>
      <div class="grid-item">
        <RouterLink to="/search/member"><img class="image" src="./../../images/member.jpg" alt="Member"></RouterLink>
        <p>Member</p>
      </div>
      <div class="grid-item">
        <RouterLink to="/search/staff"><img class="image" src="./../../images/staff.webp" alt="Staff"></RouterLink>
        <p>Staff</p>
      </div>
      <div class="grid-item">
        <RouterLink to="/commingsoon"><img class="image" src="./../../images/facility.png" alt="Facility"></RouterLink>
        <p>Facility</p>
      </div>
      <div class="grid-item">
        <RouterLink to="/commingsoon"><img class="image" src="./../../images/scheduling.webp" alt="Scheduling"></RouterLink>
        <p>Scheduling</p>
      </div>
      <div class="grid-item">
        <RouterLink to="/inventory"><img class="image" src="./../../images/inventory.jpg" alt="Inventory"></RouterLink>
        <p>Inventory</p>
      </div>
    </div>
  </main>


</template>

<style>
main {
  margin-bottom: 10%;
}
.grid-container {
  margin-top: 5%;
  display: grid;
  grid-template-columns: repeat(3, 1fr); 
  grid-gap: 10px; 
}

.grid-item {
  text-align: center; 
}

.image {
  width: 300px; 
  height: 200px; 
  object-fit: cover; 
  object-position: center;
}
</style>
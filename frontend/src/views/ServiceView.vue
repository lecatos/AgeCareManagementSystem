<script lang="ts">
  import Hero from '../components/Hero.vue'
  import Card from '../components/ServiceCard.vue'
  import ServicePopUp from '../components/ServiceAdd.vue';
  import ServiceAdd from '../components/ServiceAdd.vue';
  import axios  from 'axios';
  import { serviceStore } from '@/stores/serviceStore';
  export default {
    components: {
      Hero, Card, ServicePopUp, ServiceAdd
    },
    data (){
      return {
        services: [] as any
      }
    },
    methods : {
      updateService(){
        serviceStore.value.refresh()
        axios.get("/api/service/list").then((res)=>{
        console.log(res.data)
        this.services = res.data;
      })
      }
    },
    mounted () {
      this.updateService()
    }
  };
  </script>


<!--TODO: SWAP TABLE OUT FOR CARD COMPONENT-->
<template>
    <Hero><h1>Services</h1></Hero>
    <div class="staff">
      <div class="container">
        <div class="row my-1 pb-5">  
          <div v-for="s in services" class="col-lg-6 d-flex justify-content-center">
            <Card @updateService="updateService" :id=s.id :name=s.name :type=s.type :category=s.category :image=s.image :client_associated=s.client_associated :staff_associated=s.staff_associated :duration=s.duration :location=s.location></Card>
          </div>
          <div class="col-lg-6 d-flex justify-content-center">
            <ServiceAdd @updateService="updateService"/>
          </div>
        </div>
      </div>
    </div>
</template>


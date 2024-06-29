<script lang="ts">
  import InventoryEdit from '@/components/InventoryEdit.vue';
  import InventoryAdd from '@/components/InventoryAdd.vue';
import Hero from '../components/Hero.vue'
import { defineComponent, ref } from 'vue';
import axios from "axios";
export default defineComponent({
    components: {InventoryEdit, Hero, InventoryAdd},
    data() {
      return {
        invs: [] as any[],
        selected_inv: {} as any
      }
    },
    methods: {
      showStockManager(){
        let updateinv: any = this.$refs.updateinv;
        updateinv.openModal();
      },
      updateInvs(){
        axios.get("/api/inventory/list").then((res)=>{
          this.invs = res.data 
        })
      }
    },
    mounted () {
      this.updateInvs()
    }
  });
</script>

<template>
  <Hero><h1>Inventory</h1></Hero>
  <InventoryEdit @updateInv=updateInvs ref="updateinv" :inv=selected_inv></InventoryEdit>
  <main>
    <div class="staff">
      <div class="container">
        <InventoryAdd @updateInv=updateInvs />
        <div class="row my-1">
          <table class="table table-striped table-hover">
            <thead class="table-dark">
              <tr>
                <th scope="col" class="col-1">Stock</th>
                <th scope="col" class="col-1">Name</th>
                <th scope="col" class="col-1">Desc</th>
                <th scope="col" class="col-1">Crit Point</th>
                <th scope="col" class="col-1">Qty</th>
                <th scope="col" class="col-1">Last Restock</th>
                <th scope="col" class="col-1">Status</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="inv in invs" scope="row">
                <td><button class="p-0" @click="selected_inv = inv;showStockManager();"><img  :src=inv.image alt="" border=3 height=80 width=80></img></button></td>
                <td>{{inv.item_name}}</td>
                <td>{{inv.desc}}</td>
                <td>{{inv.critical_point}}</td>
                <td>{{inv.qty}}</td>
                <td>{{inv.last_restock}}</td>
                <td>
                  <svg v-if="inv.qty>inv.critical_point*1.2" xmlns="http://www.w3.org/2000/svg" width="50px" height="50px" viewBox="0 0 24 24" fill="none">
                  <path d="M12 22C17.5 22 22 17.5 22 12C22 6.5 17.5 2 12 2C6.5 2 2 6.5 2 12C2 17.5 6.5 22 12 22Z" stroke="green" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
                  <path opacity="0.34" d="M7.75 11.9999L10.58 14.8299L16.25 9.16992" stroke="green" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
                  </svg>
                  <svg v-else-if="inv.qty>=inv.critical_point" fill="#ffae00" width="50px" height="50px" viewBox="0 0 32 32" version="1.1" xmlns="http://www.w3.org/2000/svg" stroke="#fae500"><g id="SVGRepo_bgCarrier" stroke-width="0"></g><g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g><g id="SVGRepo_iconCarrier"> <path d="M15 21.063v-15.063c0-0.563 0.438-1 1-1s1 0.438 1 1v15.063h-2zM15 23.031h2v1.875h-2v-1.875zM0 16c0-8.844 7.156-16 16-16s16 7.156 16 16-7.156 16-16 16-16-7.156-16-16zM30.031 16c0-7.719-6.313-14-14.031-14s-14 6.281-14 14 6.281 14 14 14 14.031-6.281 14.031-14z"></path> </g></svg>
                  <svg v-else fill="#ff0000" width="50px" height="50px" viewBox="0 0 16 16" xmlns="http://www.w3.org/2000/svg" stroke="#ff0000" transform="matrix(1, 0, 0, 1, 0, 0)"><g id="SVGRepo_bgCarrier" stroke-width="0"></g><g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g><g id="SVGRepo_iconCarrier"><path d="M15.35 12.81 9 2.08a1.22 1.22 0 0 0-2 0L.65 12.81a1.14 1.14 0 0 0 1 1.69h12.66a1.14 1.14 0 0 0 1.04-1.69zm-13.66.55L8 2.64l6.31 10.72z"></path><path d="M7.32 5.45h1.25V10H7.32z"></path><ellipse cx="7.95" cy="11.9" rx=".67" ry=".7"></ellipse></g></svg>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
  </main>
</template>
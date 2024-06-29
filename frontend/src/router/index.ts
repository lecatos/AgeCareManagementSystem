import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import SearchView from '../views/SearchView.vue'
import LoginView from '../views/LoginView.vue'
import LogoutView from '../views/LogoutView.vue'
import MemberView from '../components/MemberView.vue'
import StaffView from '../components/StaffView.vue'
import MemberAdd from '../components/MemberAdd.vue'
import StaffAdd from '../components/StaffAdd.vue'
import CommingSoon from '../components/CommingSoon.vue'
import ServiceView from '../views/ServiceView.vue'
import InventoryView from '@/views/InventoryView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/search',
      name: 'search',
      component: SearchView,
      children: [
        { path: 'member', name: 'Member', component: MemberView },
        { path: 'staff', name: 'Staff', component: StaffView },
        { path: 'member-add', name: 'MemberAdd', component: MemberAdd },
        { path: 'staff-add', name: 'StaffAdd', component: StaffAdd }
      ]
    },
    {
      path: '/login',
      name: 'login',
      component: LoginView
    },
    {
      path: '/logout',
      name: 'logout',
      component: LogoutView
    },
    {
      path: '/service',
      name: 'service',
      component: ServiceView
    },
    {
      path: '/inventory',
      name: 'inventory',
      component: InventoryView
    },
    {
      path: '/commingsoon',
      name: 'commingsoon',
      component: CommingSoon
    },
  ]
})

export default router

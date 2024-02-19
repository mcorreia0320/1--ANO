import { createRouter, createWebHistory } from 'vue-router'
import CabulasView from '@/views/CabulasView.vue'
import StatsView from '@/views/StatsView.vue'
import EditCabulasView from '@/views/EditCabulasView.vue'
import AuthView from '@/views/AuthView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'apontamentos',
      component: CabulasView
    },
    {
      path: '/stats',
      name: 'stats',
      component: StatsView
    },
    {
      path: '/editApontamento/:id',
      name: 'edit-apontamento',
      component: EditCabulasView
    },
    {
      path: '/auth',
      name: 'auth',
      component: AuthView
    }
  ]
})

export default router

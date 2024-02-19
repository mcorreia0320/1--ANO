import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/msgs',
      name: 'msgs',
      component: () => import('../views/MsgsView.vue')
    },
    {
      path: '/:pathMatch(.*)',
      name: 'erro',
      component: () => import('../views/Erro.vue')
    },
    {
      path: '/msgs/:id',
      name: 'msg',
      component: () => import('../views/MsgView.vue')
    },
    {
      path: '/modals',
      name: 'modals',
      component: () => import('../views/ModalsView.vue')
    }
  ]
})

export default router

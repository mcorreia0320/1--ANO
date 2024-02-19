import { createRouter, createWebHistory } from 'vue-router'
import SignUp from '../views/SignUp.vue';
import Profile from '../views/Profile.vue';
import Login from '../views/Login.vue';
import Home from '../views/Home.vue'
import Categorias from '../views/Categorias.vue'
import CategoriaIndividual from '../views/CategoriaIndividual.vue'
import ErroView from '../views/ErroView.vue'
import PegadaCarbono from '../views/PegadaCarbono.vue'
import PegadaAdmin from '../views/PaginaAdmin.vue'
import CreateProfile from '../views/CreateProfile.vue'

function isAuthenticated() {
  const token = localStorage.getItem('jwt');
  return token && token !== '';
}

function isAdminUser() {
  const userId = localStorage.getItem('userID');
  return userId ==='1';
}


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home
    },
    {
      path: '/signUp',
      name: 'signup',
      component: SignUp
    },
    {
      path: '/createProfile',
      name: 'CreateProfile',
      component: CreateProfile,
      meta: { requiresAuth: true }
    },
    {
      path: '/login',
      name: 'login',
      component: Login
    },
    {
      path: '/profile',
      name: 'profile',
      component: Profile,
      meta: { requiresAuth: true }
    },
    {
      path: '/categorias',
      name: 'categorias',
      component: Categorias
    },
    {
      path: '/categoria_individual/:id',
      name: 'categoria_individual',
      component: CategoriaIndividual
    },
    {
      path: '/calculadora',
      name: 'calculadora',
      component: PegadaCarbono
    },
    {
      path: '/administrador',
      name: 'administrador',
      component: PegadaAdmin,
      meta: { requiresAuth: true }
    },
    {
      path: '/:catchAll(.*)',
      meta: { hideComponents: true},
      component: ErroView
    }
  ]
})

router.beforeEach((to, from, next) => {
  if (to.meta.requiresAuth && !isAuthenticated()) {
    next('/login'); 
  } else if (to.name === 'administrador' && (!isAuthenticated() || !isAdminUser())) {
    next('/'); 
  } else {
    next();
  }
});

export default router

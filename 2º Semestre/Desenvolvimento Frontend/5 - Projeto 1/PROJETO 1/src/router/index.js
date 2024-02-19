import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import Pesquisar_CocktailsView from '../views/Pesquisar_CocktailsView.vue'
import CocktailView from '../views/CocktailView.vue'
import ErroView from '../components/ErroView.vue'
import ComentariosView from '../views/ComentariosView.vue'
import CarrinhoView from '../views/CarrinhoView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/pesquisar_cocktails',
      name: 'pesquisar_cocktails',
      component: Pesquisar_CocktailsView
    },
    {
      path: '/cocktail/:name/:id',
      name: 'cocktail',
      component: CocktailView
    },
    {
      path: '/testemunho',
      name: 'comentarios',
      component: ComentariosView
    },
    {
      path: '/shop',
      name: 'shopping car',
      component: CarrinhoView
    },
    {
      path: '/:catchAll(.*)',
      meta: { hideComponents: true},
      component: ErroView
    }
  ]
})

export default router

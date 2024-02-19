
<template>
  <div class="fixed-top" id="header" v-if="!$route.meta.hideComponents">
    <header class="container" >
      <div
        class="botões-header d-flex align-items-center"
        id="navbarNavAltMarkup"
      >
        <nav class="navbar navbar-expand-md px-0 w-100 gap-1">
          <div class="animation-logo gap-1">
            <div class="logo">
              <i class="fa-solid fa-martini-glass-citrus"></i>
            </div>
            <div class="text-logo">
              <p class="logo-text h-100 pt-2 fw-bolder">
                House of the Cocktail's
              </p>
            </div>
          </div>
          <button
            class="navbar-toggler"
            type="button"
            data-bs-toggle="collapse"
            data-bs-target="#navbarNavAltMarkup"
            aria-controls="navbarNavAltMarkup"
            aria-expanded="false"
            aria-label="Toggle navigation"
          >
            <span class="navbar-toggler-icon"></span>
          </button>
          <div class="collapse navbar-collapse gap-3" id="navbarNavAltMarkup">
            <ul
              class="main-nav-list navbar-nav ms-auto">
              <li class="nav-item" v-for="botao in navbarStore.botoes">
                <RouterLink :to="botao.path"
                  class="nav-link header-link text-decoration-none px-3 py-2 mx-0"
                  @click="navbarStore.closeMenuMobile()"
                  >{{ botao.name }}</RouterLink>
              </li>
              <li class="nav-item shop">
                <RouterLink :to="navbarStore.shop_path" class="icon-shop">
                  <i class="fa-solid fa-cart-shopping fs-4 py-2 px-3"></i>
              </RouterLink>
              </li>
              <li class="nav-item theme-mode header-link">
                <fieldset class="d-flex px-3 gap-2 align-items-center py-2">
                  <label for="tema">Light</label>
                  <input checked type="radio" name="tema" id="light-mode"/>
                  &emsp;
                  <label for="tema">Dark</label>
                  <input type="radio" name="tema" id="dark-mode"/>
                </fieldset>
              </li>
              <!-- <li v-if="authStore.user != null" class="fw-light ps-3 pt-2"><p class="subtitle-modal text-justify">Logged as</p></li> -->
              <li v-if="authStore.user != null"><button class="btn button-logout ms-2" type="button" @click="logoutUser">Logout</button></li>
            </ul>
          </div>
        </nav>
      </div>
    </header>
    <hr class="mt-0 fixed" v-if="!$route.meta.hideComponents">
  </div>
    <div v-if="!$route.meta.hideComponents">
      <p class="fs-4 fw-lighter w-100 text-center color-text" v-if="authStore.user != null && authStore.user.displayName != null "> &lt;-- Logged with {{ authStore.user.displayName }} --&gt; </p>
      <p class="fs-4 fw-lighter w-100 text-center color-text" v-else-if="authStore.user != null"> &lt;-- Logged with {{ authStore.user.email }} --&gt; </p>
    </div>
  <RouterView/>
  <hr class="mt-5" v-if="!$route.meta.hideComponents">
  <section class="container px-0" id="footer" v-if="!$route.meta.hideComponents">
        <div class="container-info-footer mt-5 d-flex flex-column align-items-center">
            <div class="container-logo-footer-social d-flex flex-column align-items-center">
                <div class="animation-logo">
                    <i class="fa-solid fa-martini-glass-citrus"></i>
                </div>
                <div class="social-media py-3">
                    <a href="https://www.facebook.com/miguel.correia.33865854/"><i class="fa-brands fa-square-facebook px-2"></i></a>
                    <a href="https://www.instagram.com/mcorreia0320/"><i class="fa-brands fa-square-instagram px-2"></i></a>
                </div>  
            </div>
            <div class="container-info-nav-footer ">
                <a data-bs-toggle="modal" data-bs-target="#signupModal" class="nav-footer" type="button" v-if="authStore.user == null"><span class="nav-footer">Sign in</span></a>
                <a data-bs-toggle="modal" data-bs-target="#loginModal" class="nav-footer" type="button" v-if="authStore.user == null"><span class="nav-footer">Login</span></a>
                <RouterLink to="/"><span class="nav-footer">Home</span></RouterLink>
            </div>
            <p>Copyright © UMa 2023</p>
        </div>
  </section>


  <modals />
</template>

<script setup>
  import { RouterLink, RouterView } from "vue-router";
  import { useNavbarStore } from "./stores/navbarStore";
  import modals from "./components/modals.vue";
  import { useAuthStore } from "./stores/authStore";
  import { onAuthStateChanged } from 'firebase/auth';
  import { auth } from "./firebase";

  const authStore = useAuthStore();
  const navbarStore = useNavbarStore();

  onAuthStateChanged(auth, async (user)=>{
    authStore.setUser(user);
  })

  const logoutUser = ()=>{
    authStore.logout(auth)
  }


</script>
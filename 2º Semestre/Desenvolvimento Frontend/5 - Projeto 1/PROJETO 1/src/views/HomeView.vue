<template>
  <section class="container" id="apresentacao">
        <div class="container-info">
            <div class="container-img-apresentacao">
                <img src="../assets/images/home-img.png" alt="Cocktail">
            </div>
            <div class="container-text-apresentacao px-5 py-5">
                <h4>By Miguel Peñaranda</h4>
                <h1>Discover The Best Cocktails of the World</h1>
                <p class="mb-4">The best cocktail shop thanks to our wide variety of cocktails prepared by the best bartenders with high quality ingredients, in a modern and cozy environment with exceptional service and constant promotions and special events.</p>
                <div class="botoes-apresentação d-flex gap-4 justify-content-center">
                    <button class="botao1 fs-4 py-1" data-bs-toggle="modal" data-bs-target="#signupModal" type="button" v-if="authStore.user == null">Sign In</button>
                    <button class="botao2 fs-4 py-1" data-bs-toggle="modal" data-bs-target="#loginModal" type="button" v-if="authStore.user == null">Login</button>
                </div>
            </div>
        </div>
    </section>
</template>

<script setup>
import { useAuthStore } from "../stores/authStore";

const authStore = useAuthStore();
</script>
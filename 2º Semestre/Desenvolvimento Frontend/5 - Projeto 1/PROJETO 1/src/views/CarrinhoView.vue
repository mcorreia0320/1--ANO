<template>
    <div class="container d-flex justify-content-center" id="carrinho">
        <div class="carrinho-card">
            <header class="d-flex gap-3 align-items-center py-3">
                <i class="fa-solid fa-cart-shopping fs-1 ps-3"></i>
                <h1 class="fw-bolder">SHOPPING CART</h1>
            </header>
            <div class="produtos">
                <div class="produto ps-5 pe-5" v-for="item in shoppingStore.shopCar" :key="item.nameCocktail">
                    <img :src="item.imageSource" :alt="item.nameCocktail">
                    <p>Cocktail name:<span>{{item.nameCocktail}}</span></p>
                    <p>Quantity:<span>{{ item.quantity }}</span></p>
                    <p>Price:<span>{{ item.price }} €</span></p>
                    <div class="text-end">
                        <button class="botao1" @click="deletefromShopcar(item.nameCocktail)">-</button>
                    </div>
                </div>
            </div>
            <div class="payment-section d-flex justify-content-between pe-4">
                <p>Total Price:<span>{{ totalPay }} €</span></p>
                <button class="botao1 py-2 px-3" type="button" v-if="authStore.user != null">Finish Payment</button>
                <button class="botao1 py-2 px-3" type="button" data-bs-toggle="modal" data-bs-target="#loginModal" v-else>Faça Login</button>
            </div>
        </div>
    </div>
</template>

<script setup>
import { useShoppingStore } from '../stores/shoppingStore';
import { ref } from 'vue';
import { useAuthStore } from '../stores/authStore';

const authStore = useAuthStore();
const shoppingStore = useShoppingStore();
const totalPay = ref(0)

shoppingStore.shopCar.forEach(item => {
    totalPay.value += item.price * item.quantity;
});

const deletefromShopcar = (name)=>{

    for (let i = 0; i < shoppingStore.shopCar.length; i++) {
        var objeto = shoppingStore.shopCar[i];
        for (let properity in objeto) {
            if (objeto[properity] == name) {
                objeto['quantity'] -= 1;
                if (objeto['quantity'] == 0) {
                    shoppingStore.shopCar.splice(i,1);
                }
                totalPay.value = 0
                shoppingStore.shopCar.forEach(item => {
                totalPay.value += item.price * item.quantity;
                });
                break
            }
        }
    }
}
</script>
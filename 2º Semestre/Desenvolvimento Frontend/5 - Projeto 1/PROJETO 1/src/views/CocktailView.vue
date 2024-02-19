<template>
    <div class="container" id="cocktail">
        <div class="cocktail-description d-flex gap-3 p-4 align-items-center" v-for="item in cocktailsStore.array_cocktails">
            <div class="img-cocktail d-flex flex-column align-items-center">
                <div class="img-cocktail d-flex flex-column align-items-center">
                    <h3 class="fw-bolder">{{ item.strDrink }}</h3>
                    <img :src="item.strDrinkThumb" :alt="item.strDrink">
                </div>
                <div id="counter" class="d-flex mt-3 gap-3" v-if="authStore.user != null">
                    <button class="botao1" @click="acreaseCounter">+</button>
                    <h1 class="text-center h-100 pt-1">{{ counter }}</h1>
                    <button class="botao1" @click="decreaseCounter"> - </button>
                </div>
            </div>
            <div class="info-cocktail">
                <h3 class="fw-bolder mb-3">Ingredients</h3>
                <div class="ingredients gap-4" >
                    <div class="ingrediente" v-for="item in cocktailsStore.array_ingredients">
                        <p class="text-center fw-normal">{{ item.strIngredient }}</p>
                        <img :src="item.imageSource" :alt="item.strIngredient">
                        <p v-if="item.measure != undefined" class="fw-lighter">{{ item.measure }}</p>
                        <p v-else class="fw-lighter">Preference</p>
                    </div>
                </div>
                <h3 class="fw-bolder mb-3 mt-3">Description</h3>
                <p>{{ item.strInstructions }}</p>
                <button class="botao1 mb-2" @click="adicionar" v-if="authStore.user != null">Add to Shopping Car</button>
                <button class="botao1 mb-2" @click="$router.push('/pesquisar_cocktails')" v-else>Voltar a Pesquisar Cocktails</button>
                <p class="fw-bolder">{{ erro }}</P>
            </div>
        </div>
    </div>
</template>

<script setup>
import {useRoute, useRouter } from 'vue-router';
import { useCocktailsStore } from '../stores/cocktailsStore';
import { useShoppingStore} from '../stores/shoppingStore';
import { ref } from 'vue';
import { onMounted } from 'vue';
import { useAuthStore } from "../stores/authStore";


const authStore = useAuthStore();
const cocktailsStore = useCocktailsStore();
const shoppingStore = useShoppingStore();
const route = useRoute();
const router = useRouter();

const counter = ref(0);
const erro = ref('');

onMounted( async ()=>{
    await cocktailsStore.getCocktailByID(cocktailID);
    var object = cocktailsStore.array_cocktails[0];
    cocktailsStore.array_ingredients = [];
    for (let properity in object) {
        let ingrediente = await cocktailsStore.getIngredients(object[properity]);
        if (ingrediente != null) {
            for (let lista in ingrediente) {
                cocktailsStore.array_ingredients.push(ingrediente[lista])
            }
        }
    }
    for (let i = 0; i < cocktailsStore.array_ingredients.length; i++) {
        const ingredientObject = cocktailsStore.array_ingredients[i];
        ingredientObject['imageSource'] = 'https://www.thecocktaildb.com/images/ingredients/' + ingredientObject.strIngredient + '.png';
    }
    for (const cocktail of cocktailsStore.array_cocktails) {
        let noNulo = 0;
        for (let j = 1; j < 15; j++) {
            let measure = cocktail[`strMeasure${j}`];
            if (measure != null){
                let measureIngrediente = cocktailsStore.array_ingredients[noNulo];
                measureIngrediente['measure'] = measure;
                noNulo += 1;
            }
        }
    }

})

const cocktailID = route.params.id;

const adicionar = ()=>{
    cocktailsStore.array_cocktails.forEach(item => {
       if (counter.value != 0) {
            shoppingStore.shopCar.push({
           nameCocktail: item.strDrink,
           quantity: counter.value,
           price: Math.floor(Math.random() * (15 - 8)) + 8,
           imageSource: item.strDrinkThumb
          })
          counter.value = 0;
          erro.value = '';
          router.push('/pesquisar_cocktails');
       }
       else{
            erro.value = '*MINIMO UM COCKTAIL*'
       }
    });
}

const acreaseCounter = ()=>{
    counter.value += 1;
}
const decreaseCounter = ()=>{
    if (counter.value > 0) {
        counter.value -= 1;
    }
}


</script>
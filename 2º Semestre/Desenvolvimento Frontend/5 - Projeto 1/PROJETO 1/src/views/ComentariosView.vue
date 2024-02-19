<template>
    <div class="container" id="testemunhos">
        <h1 class="text-center fw-bolder mb-5">Comments of the Restaurant</h1>
        <div class="container-testemunhos ">
            <div class="review" v-for="opiniao in testemunhoStore.array_testemunhos">
                <div class="img-name">
                    <img src="../assets/images/profile.png" alt="">
                    <h4>{{ opiniao.nome }}<br><span>{{ opiniao.cocktail }}</span></h4>
                </div>
                <p>{{ opiniao.description }}</p>
            </div>
        </div>
        <div class="form-testemunhos mt-5 d-flex justify-content-center" v-if="authStore.user != null">
            <div class="card-form p-5">
                <h3 class="fw-bolder">Write your Opinion</h3>
                <div class="input-info d-flex gap-5">
                    <div class="input">
                        <h5 class="mt-4">Name</h5>
                        <input type="text" placeholder="Your Name..." class="ps-3 input-size" v-model="firstName">
                    </div>
                    <div class="input">
                        <h5 class="mt-4">Cocktail</h5>
                        <select v-model="selectedCocktail" class="text-color ps-3">
                            <option :value="cocktail.strDrink" v-for="cocktail in cocktailsStore.array_cocktails">{{ cocktail.strDrink }}</option>
                        </select>
                    </div>
                </div>
                <div class="input-description mt-4">
                    <textarea name="description" id="" cols="30" rows="10" placeholder="Your Opinion..." class="ps-2 py-2" v-model="description"></textarea>
                    <div class="d-flex align-items-center justify-content-between">
                        <button class="botao1 fs-4 py-1 mt-3" type="button" @click="addTestemunho()">Submit</button> <span class="mt-2 text-config">{{ erro }}</span>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
import { ref } from 'vue'
import { useCocktailsStore } from '../stores/cocktailsStore';
import { useTestemunhoStore } from '../stores/testemunhoStore';
import { onMounted } from 'vue';
import { useAuthStore } from "../stores/authStore";


const authStore = useAuthStore();

onMounted(()=> {
        cocktailsStore.getCocktails(search.value);
        testemunhoStore.getTestemunho();
    })

const testemunhoStore = useTestemunhoStore();
const cocktailsStore = useCocktailsStore();

const search = ref('')

const selectedCocktail = ref(null);

const firstName = ref(null);

const description = ref(null);

const erro = ref('');

const addTestemunho = ()=> {
    if (selectedCocktail.value && firstName.value && description.value != null) {
        testemunhoStore.addTestemunho(firstName.value,selectedCocktail.value,description.value);
        firstName.value = null;
        description.value = null;
        selectedCocktail.value = null;
        erro.value = '';
    }
    else{
        erro.value = '*TODOS OS CAMPOS SÃO OBRIGATORIOS*'
    }
}
</script>
<template>
  <div class="container" id="pesquisa">
        <div class="barra_pesquisa">
            <input type="search" name="" id="" placeholder="Cocktail name..." class="barra ps-3" v-model="search" @keyup="searchCocktail">
            <button type="submit" class="botao-pesquisa"><i class="fa-solid fa-magnifying-glass mx-0 lupa"></i></button>
        </div>
        <h5 class="text-center mt-5 fw-bolder title-pesquisa">Popular Drinks <small class="fw-light fs-6 text-secondary">({{ cocktailsStore.totalCocktails }})</small></h5>
        <div class="alguns-cocktails mt-4 col-md-4">
            <div class="cocktails-pesquisa" v-for="item in cocktailsStore.array_cocktails" :key="item.strDrink" @click="selectCocktail(item.strDrink,item.idDrink)">
                <img v-bind:src="item.strDrinkThumb" :alt="item.strDrink">
                <p>{{ item.strDrink }}</p>
            </div>
        </div>
    </div>
</template>

<script setup>
    import { useCocktailsStore } from "../stores/cocktailsStore";
    import { onMounted, ref } from 'vue';
    import { useRouter } from 'vue-router'
    

    const router = useRouter();
    const cocktailsStore = useCocktailsStore();
    const search = ref('');
    
    onMounted(()=> {
        cocktailsStore.getCocktails(search.value);
    })

    const searchCocktail = ()=>{
        cocktailsStore.getCocktails(search.value)
    }

    const selectCocktail = (name, id)=>{
        let cocktailName = encodeURIComponent(name);
        router.push('/cocktail/' + cocktailName + '/' + id)
    }
</script>


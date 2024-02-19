import { defineStore } from "pinia";

export const useCocktailsStore = defineStore('cocktailsStore',{
    state: ()=> {
        return {
           array_cocktails: [],
           array_ingredients: []
        }
    },
    actions: {
        async getCocktails(name) {
            if ( name != '') {
                let res = await fetch('https://www.thecocktaildb.com/api/json/v1/1/search.php?s=' + name);
                let result = await res.json();
                this.array_cocktails = await result.drinks
            }
            else {
                let res = await fetch('https://www.thecocktaildb.com/api/json/v1/1/search.php?s=');
                let result = await res.json();
                this.array_cocktails = await result.drinks
            } 
        },
        async getCocktailByID(id) {
            let res = await fetch('https://www.thecocktaildb.com/api/json/v1/1/lookup.php?i=' + id);
            let result = await res.json();
            this.array_cocktails = await result.drinks
        },
        async getIngredients(name) {
            let res = await fetch('https://www.thecocktaildb.com/api/json/v1/1/search.php?i=' + name);
            let result = await res.json();
            return result.ingredients
        }
    },
    getters: {
        totalCocktails: state => {
            if (state.array_cocktails != null) {
                return state.array_cocktails.length
            } else return 0
        }
    }
})
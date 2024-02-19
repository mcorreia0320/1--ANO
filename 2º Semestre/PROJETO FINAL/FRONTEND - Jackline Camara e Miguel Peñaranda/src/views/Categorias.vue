<template>
    <div class="container w-100 my-5">
        <h1 class="text-center w-100 text-success mb-4">PESQUISA DE CATEGORIAS ECOLÓGICAS:</h1>
        <div class="input-group w-100 d-flex justify-content-center">
            <div id="search-autocomplete" class="form-outline w-50">
                <input type="search" v-model="search" id="form1" class="form-control custom-placeholder" placeholder="Categoria ecologica..." @keyup.enter="categoriasEcologias.getCategoriasBinding(search)"/>
            </div>
            <button type="button" class="btn btn-success" @click="categoriasEcologias.getCategoriasBinding(search)">
                <i class="fas fa-search"></i>
            </button>
        </div>
        <hr class="text-success mt-5" />
        <div class="container cards-grid mt-5 justify-content-center mb-5" v-if="array.length != 0">
            <div class="card-categoria card d-flex flex-column p-4" v-for="categoria in categoriasEcologias.array_categorias">
                <div class="card-img-top d-flex justify-content-center">
                    <img :src="categoria.image" alt="">
                </div>
                <h4 class="mt-2 text-uppercase text-categoria w-100 text-center text-success text-opacity-50">{{ categoria.nome }}</h4>
                <h1 class="text-uppercase w-100 text-center text-success">{{ categoria.categoria }}</h1>
                <div class="button-container w-100 text-center">
                    <button class="btn btn-success" @click="$router.push('/categoria_individual/' + categoria.id)">Mais informação...</button>
                </div>
            </div>
        </div>
        <div v-else class="text-center mb-5">
            <h3 class="w-100 text-center text-success mt-5">ESCREVA O NOME COMPLETO DA CATEGORIA</h3>
            <button class="btn btn-success" @click="categoriasEcologias.getAllCategorias()"> Refresh </button>
        </div>
        <hr class="text-success" />
    </div>
</template>

<script setup>
import { useCategoriasEcologicasStore } from '../stores/categoriasEcologiasStore';
import { onMounted, ref, watch } from 'vue';

const search = ref('');

const categoriasEcologias = useCategoriasEcologicasStore();

const array = ref(categoriasEcologias.array_categorias)

watch(()=> categoriasEcologias.array_categorias, (newStatus) =>{
        array.value = newStatus;
    })

onMounted(async ()=>{
    categoriasEcologias.getAllCategorias();
})


</script>
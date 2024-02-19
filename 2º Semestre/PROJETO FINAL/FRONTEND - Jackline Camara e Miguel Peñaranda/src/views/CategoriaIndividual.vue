<template>
    <div class="container">
        <div class="categoria container w-100 my-5 p-4 shadow">
            <div class="content-categoria w-100 h-100 d-flex p-5">
                <div class="img-tittle w-50 h-100  d-flex flex-column justify-content-center p-5 gap-5">
                    <div class="w-100 p-4 rounded border border-2 border-success bg-success bg-opacity-50">
                        <img :src="categoria.image" alt="" class="img-categoria">
                    </div>
                    <div class="bg-success p-4 rounded-pill">
                        <h1 class="text-center text-light text-uppercase">{{ categoria.nome }}</h1>
                    </div>
                </div>
                <div class="description px-4 d-flex flex-column justify-content-center">
                    <h1 class="text-uppercase text-success">{{ categoria.categoria }}</h1>
                    <p class="text-description text-success text-justify">{{ categoria.descricao }}</p>
                    <p class="text-description text-success text-justify">Se cumprires com esta ação ecologica, consegues:</p>
                    <ul class="text-description text-success text-justify">
                        <li>Reciclagem de vidro: {{ categoria['recicled-glass'] }}</li>
                        <li>Reciclagem de metal: {{ categoria['recicled-metal'] }}</li>
                        <li>Reciclagem de papel: {{ categoria['recicled-paper']}}</li>
                        <li>Reciclagem de plastico {{ categoria['recicled-plastic'] }}</li>
                    </ul>
                    <p class="text-description text-success text-justify">Consegue-se descontar da tua pegada de carbono: {{ categoria.CO2 }} emissiones de CO2</p>
                    <button class="btn btn-outline-success btn-lg" v-if="userStatus != null" @click="$router.push('/calculadora')">Calcular a sua Pegada</button>
                    <button class="btn btn-outline-success btn-lg" v-else @click="$router.push('/login')">Login para Calcular a sua Pegada</button>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
    import { useCategoriasEcologicasStore } from '../stores/categoriasEcologiasStore';
    import { useUserStore } from '../stores/userStore';
    import { onMounted, ref, watch } from 'vue';
    import { useRoute } from 'vue-router';

    const route = useRoute();

    onMounted(()=>{
        CategoriasEcologicasStore.getCategoriaById(route.params.id)
    })

    const userStore = useUserStore();
    const CategoriasEcologicasStore = useCategoriasEcologicasStore();

    const categoria = ref(CategoriasEcologicasStore.indiviualCategory);

    watch(()=> CategoriasEcologicasStore.indiviualCategory, (newStatus) =>{
        categoria.value = newStatus;
    })

    const userStatus = ref(userStore.user);

    watch(()=> userStore.user, (newStatus) =>{
        userStatus.value = newStatus;
    })


</script>
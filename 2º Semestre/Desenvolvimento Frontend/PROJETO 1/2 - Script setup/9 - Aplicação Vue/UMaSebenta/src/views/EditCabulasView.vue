<template>
    <div class="cabulas">
        <AddEditApontamento v-model="contentApontamento" ref="contentApontamentoRef">
            <template #buttons>
                <button class="button is-link is-light mr-3"
                            @click="$router.back()">
                        Cancel
                </button>
                <button class="button is-link has-background-success"
                        :disabled="!contentApontamento"
                        @click="handleSaveClicked">
                    Save
                </button>
            </template>
        </AddEditApontamento>
    </div>
</template>

<script setup>
    import { ref } from 'vue';
    import AddEditApontamento from '@/components/AddEditCabula.vue';
    import { useCabulasStore } from '@/stores/cabulasStore';
    import { useRoute, useRouter } from 'vue-router';

    const cabulasStore = useCabulasStore();
    const contentApontamento = ref('texto para gravar');
    const contentApontamentoRef = ref(null);

    const route = useRoute();
    const router = useRouter();
    const handleSaveClicked = () => {
            var id = route.params.id;
            cabulasStore.updateApontamento(id.toString(), contentApontamento.value.trim());
            router.push('/');
        }
    contentApontamento.value = cabulasStore.getApontamentoContent(route.params.id); 
</script>
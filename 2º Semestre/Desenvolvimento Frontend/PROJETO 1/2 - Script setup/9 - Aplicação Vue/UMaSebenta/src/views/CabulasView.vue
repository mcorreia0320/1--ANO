<template>
    <div class="cabulas">
        <AddEditApontamento v-model="newApontamento" ref="newApontamentoRef">
            <template #buttons>
                <button class="button is-link has-background-success"
                        @click="addApontamento"
                        :disabled="!newApontamento">
                        Adicionar
                </button>
            </template>
        </AddEditApontamento>
        <!-- <div class="card has-background-success-dark p-4 mb-5">
            <div class="field">
                <div class="control">
                    <textarea ref="newApontamentoRef" class="textarea" placeholder="Adicionar apontamento" v-model="newApontamento" @keyup.enter="addApontamento"></textarea>
                </div>
            </div>
            
            <div class="field is-grouped is-grouped-right">
                <div class="control">
                    <button class="button is-link has-background-success"
                            @click="addApontamento"
                            :disabled="!newApontamento">Adicionar</button>
                </div>
            </div>
        </div> -->
        <Apontamento v-for="cabula in cabulasStore.apontamentos" 
                    :key="cabula.id" 
                    :cabula="cabula" />
                    <!-- @deleteClicked="deleteApontamento" -->
    </div>
</template>

<script setup>
    import { ref, onMounted } from 'vue'
    import Apontamento from '@/components/cabula.vue'
    import { useCabulasStore } from '@/stores/cabulasStore'
    import  AddEditApontamento from '@/components/AddEditCabula.vue'

    const cabulasStore = useCabulasStore();
    const newApontamento = ref('')
    const newApontamentoRef = ref(null)

    onMounted(() => {
            cabulasStore.getApontamentos()
        })

    const addApontamento = () => {
        cabulasStore.addApontamento(newApontamento.value)
        // let newId = 1;

        // if (apontamentos.value.length != 0) {
        //     newId = apontamentos.value[0].id + 1
        // }
        
        // apontamentos.value.unshift({
        //     id: newId,
        //     content: newApontamento.value.trim()
        // })
        newApontamento.value = ''
        newApontamentoRef.value.focusTextarea()
    }
    // const deleteApontamento = idToDelete => {
    //     apontamentos.value = apontamentos.value.filter(cabula => { return cabula.id !== idToDelete })
    //     }
</script>
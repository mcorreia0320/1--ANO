<template>
    <div class="stats">
        <table class="table is-fullwidth">
            <thead>
                <tr>
                    <th>Estatísticas</th>
                    <th>Total</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>Número de Apontamentos</td>
                    <td>{{ cabulasStore.totalApontamentos }}</td>
                </tr>
                <tr>
                    <td>Número de Carateres</td>
                    <td>{{ cabulasStore.totalCaracteres }}</td>
                </tr>
            </tbody>
        </table>
    </div>
</template>

<script setup>
    import { useCabulasStore } from '../stores/cabulasStore';
    const cabulasStore = useCabulasStore();
</script>
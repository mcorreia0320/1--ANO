<template>
    <div class="modals">
        <h1>Modals</h1>
        <button @click="showModal = true">Show Modal</button>
        <Modal 
            title="My modal title (via props)"
            @hideModal="showModal = false"
            v-model="showModal">
            <p>Lorem ipsum dolor sit amet consectetur, adipisicing elit. Temporibus, dolorum? Voluptatem odit odio a saepe vitae quod accusantium, sit eos eius, natus suscipit libero animi, in impedit?</p>
        </Modal>
    </div>
</template>

<style>
    .modal {
        background-color: beige;
        padding: 10px;
        position: absolute;
        left: 0;
        top: 0;
        color: black;
        width: 100%;
        height: 100%;
        z-index: 1;
    }
</style>

<script setup>
    import { ref } from 'vue'
    import  Modal  from '@/components/Modal.vue'
    
    const showModal = ref(false);

</script>


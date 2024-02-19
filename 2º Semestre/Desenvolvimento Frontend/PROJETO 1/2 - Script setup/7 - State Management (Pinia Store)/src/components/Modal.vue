<template>
    <teleport to=".modals-container">
        <div class="modal"
             v-if="modelValue">
            <h1>{{ title }}</h1>
            <slot />
            <button @click="handleButtonClick">Hide Modal</button>
        </div>
    </teleport>
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
    const props = defineProps({
        title: {
            type: String,
            default: "No tittle specified"
        },
        modelValue: {
            type: Boolean,
            default: false
        }
    })

    const emit = defineEmits(['update:modelValue','hideModal'])


    const handleButtonClick = ()=> {
        emit('update:modelValue', false)
    }
</script>


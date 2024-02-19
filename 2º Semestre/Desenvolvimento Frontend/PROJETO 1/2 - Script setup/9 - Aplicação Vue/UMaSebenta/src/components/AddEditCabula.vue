<template>
    <div class="card has-background-success-dark p-4 mb-5">
        <div class="field">
            <div class="control">
                <textarea ref="textareaRef" class="textarea" placeholder="Adicionar apontamento"
                            :value="modelValue"
                            @input="$emit('update:modelValue', $event.target.value)">
                </textarea>
            </div>
        </div>
            
        <div class="field is-grouped is-grouped-right">
            <div class="control">
                <slot name="buttons"></slot>
            </div>
        </div>
    </div>
</template>

<script setup>
import { ref } from 'vue';

const emit = defineEmits(['update:modelValue']);

const props = defineProps({
    modelValue: {
        type: String,
        required: true
    }
})

const textareaRef = ref(null);

const focusTextarea = () => {
    textareaRef.value.focus();
}

defineExpose({
    focusTextarea
})
</script>
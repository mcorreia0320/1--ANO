<template>
  <div class="about">
    <h1>Mensagens</h1>
    <ul>
      <li v-for="item in msgs" :key="item.id">
        <RouterLink :to="`/msgs/${ item.id }`">{{ item.text }}</RouterLink>
      </li>
    </ul>
    <textarea name="" id="" cols="30" rows="10"></textarea>
    <div>
      <button class="counter-button" @click="increaseCounter(1)">
            {{ counterData.count }}
      </button>
    </div>
  </div>
</template>
<style>
  .counter-button{
    width: 150px;
    height: 50px;
    font-size: xx-large;
  }
</style>
<script setup>
  import { ref } from 'vue'
  import { useCounter } from '@/use/useCounter'
    

    const msgs = ref([
      {
        id: '1',
        text: 'Mensagem 1'
      },
      {
        id: '2',
        text: 'Mensagem 2'
      },
      {
        id: '3',
        text: 'Mensagem 3'
      },
    ])

    const { counterData, increaseCounter } = useCounter();

</script>

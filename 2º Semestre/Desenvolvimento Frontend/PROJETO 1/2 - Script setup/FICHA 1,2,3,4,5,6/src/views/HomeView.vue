<template>
  <div class="home">
    
    <div>
      <button class="btn" @click="dividirCounter()">--</button>
      <button class="btn" @click="decreaseCounter()">-</button>
      <span class="counter">{{counterData.count}}</span>
      <button class="btn" @click="increaseCounter()">+</button>
      <button class="btn" @click="duplicarCounter()">++</button>
    </div>

    <div>
      <h4>Edit counter tittle:</h4>
      <input type="number" v-model="counterData.count">
      <p>This counter is {{ oddOrEven }}</p>
    </div>

  </div>
</template>

<style>
.home {
  text-align: center;
  padding: 20px;
}
.btn, .counter {
  font-size: 40px;
  margin: 10px;
}
</style>

<script setup>
import { ref, computed, watch, onMounted, nextTick } from 'vue'
import { useCounter } from '@/use/useCounter'

const { counterData, oddOrEven, increaseCounter, decreaseCounter, dividirCounter, duplicarCounter } = useCounter();

</script>
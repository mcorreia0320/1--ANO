<template>
  <div class="home">
    
    <div>
      <button class="btn" @click="counter.decreaseCounter(2)">--</button>
      <button class="btn" @click="counter.decreaseCounter(1)">-</button>
      <span class="counter">{{counter.count}}</span>
      <button class="btn" @click="counter.increaseCounter(1)">+</button>
      <button class="btn" @click="counter.increaseCounter(2)">++</button>
    </div>

    <div>
      <h4>Edit counter tittle:</h4>
      <input type="number" v-model="counter.count">
      <p>This counter is {{ counter.oddOrEven }}</p>
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
import { useCounterStore } from '@/stores/counter';

const counter = useCounterStore();
const { counterData, oddOrEven, increaseCounter, decreaseCounter, dividirCounter, duplicarCounter } = useCounter();

</script>
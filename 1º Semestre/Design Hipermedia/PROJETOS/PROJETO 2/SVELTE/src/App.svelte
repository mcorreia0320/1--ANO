<script>
import { onMount } from 'svelte';
import svelteLogo from './assets/svelte.svg'
import Counter from './lib/Counter.svelte'

let resultado = {};
let refeicoes = [];

onMount(
  async ()=>{
  const res = await fetch('https://www.themealdb.com/api/json/v1/1/filter.php?a=Portuguese')
  resultado = await res.json()
  refeicoes = await resultado.meals
  }
 
)

</script>



<div class="d-flex flex-wrap gap-4 mobile-refeicoes">
  
  {#each refeicoes as refeicao}
  <div class="card">
    <div class="top-card overflow-hidden">
      <img src={refeicao.strMealThumb} alt="" class="img-card animation2-img">
    </div>
    <div class="card-text px-5 py-3">
      <p class="category1 p-1">PALEO</p>
      <h4 class="fw-bold titulo-card texto-black">{refeicao.strMeal}</h4>
      <div class="container-info-card">
        <div class="info calorias d-flex gap-2">
          <i class="fa-solid fa-scale-balanced icon-card"></i>
          <p class="texto-info-card texto-black">650 calorias</p>
        </div>
        <div class="info nutriscore d-flex gap-2">
          <i class="fa-solid fa-utensils utensilios icon-card"></i>
          <p class="texto-info-card texto-black">NutriScore ® 74</p>
        </div>
        <div class="info rating d-flex gap-2">
          <i class="fa-regular fa-star icon-card"></i>
          <p class="texto-info-card pb texto-black">4.9 rating (537)</p>
        </div>
      </div>
    </div>
  </div>
  {/each}
</div>


<template>
  <div class="container">
    <div id="carouselExample" class="carousel slide">
      <div class="carousel-inner">
        <div class="carousel-item active"><img class="carousel-img" src="https://www.thecocktaildb.com/images/media/drink/3pylqc1504370988.jpg" alt=""/></div>
        <div class="carousel-item" v-for="imagem in listaBebidas">
          <img :src="imagem.strDrinkThumb" class="d-block carousel-img" alt="...">
        </div>
      </div>
      <button class="carousel-control-prev" type="button" data-bs-target="#carouselExample" data-bs-slide="prev">
        <span class="carousel-control-prev-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Previous</span>
      </button>
      <button class="carousel-control-next" type="button" data-bs-target="#carouselExample" data-bs-slide="next">
        <span class="carousel-control-next-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Next</span>
      </button>
    </div>
    <br>
    <div class="input">
      <input type="text" v-model="pesquisa" @keyup="getLista(pesquisa)" placeholder="Pesquisa cocktail....">
    </div>
    <div class="container-card">
      <div class="card" v-for="item in listaBebidas">
        <img :src="item.strDrinkThumb" :alt="item.strDrink" class="img">
        <p>{{ item.strDrink }}</p>
      </div>
    </div>
  </div>
</template>

<script setup>
  
  import { ref, onMounted } from 'vue';

  const listaBebidas= ref([]);
  const pesquisa = ref('');

  onMounted(()=>{
    getLista(pesquisa.value);
  })

  const getLista = (pesquisa)=>{
   
    if (pesquisa == '') {
      fetch('https://www.thecocktaildb.com/api/json/v1/1/filter.php?c=Ordinary_Drink')
      .then(data=>data.json())
      .then(res=>res.drinks)
      .then(final => listaBebidas.value = final.map(dados => dados) )
    } else {
      fetch('https://www.thecocktaildb.com/api/json/v1/1/search.php?s=' + pesquisa)
      .then(data=>data.json())
      .then(res=>res.drinks)
      .then(final => listaBebidas.value = final.map(dados => dados) )
    }

  }
  
</script>

<style>
.container-card{
  display: grid;
  grid-template-columns: repeat(4,300px);
  grid-template-rows: repeat(auto, 300px);
  justify-content: center;
  gap:1rem;
}
.img{
  object-fit: cover;
  width: 100%;
  height: 100%;
}
.input{
  width: 100%;
  text-align: center;
  margin-bottom: 1rem;
}
input{
  width: 500px;
  height: 2rem;
}
.card{
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  padding: 1rem;
  border: solid 1px black;
  border-radius: 1rem;
  background-color: blueviolet;
  color: white;
}
.carousel-img{
  object-fit: contain !important;
  width: 100%;
  height: 20rem;
}
body{
  background-color: black;
  margin-top: 5rem;
}
</style>
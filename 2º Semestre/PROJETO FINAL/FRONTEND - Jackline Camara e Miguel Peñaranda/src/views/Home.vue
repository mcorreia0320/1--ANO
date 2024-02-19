<template>
   <div id="home">
    <div class="background-overlay"></div>
        <div class="content container d-flex align-items-center justify-content-center py-5 container-md gap-5">
            <div class="box w-100 h-100 d-flex flex-md-row p-2 bg-success p-2 bg-opacity-50">
                <div class="w-75 overflow-scroll p-3 container">
                    <h1 class="text-center">Alguma vez te questionaste como é que as nossas ações afetam o meio ambiente?</h1>
                    <p class="text-content">A pegada de carbono representa a quantidade de gases de efeito estufa que emitimos para a atmosfera através das nossas atividades diárias. Desde ligar uma lâmpada até conduzir um carro ou desfrutar das nossas comidas favoritas, todas as nossas ações deixam uma marca no nosso planeta. No entanto, não há motivo para preocupação! Existem diversas formas emocionantes e criativas de reduzir a nossa pegada de carbono e proteger o nosso ambiente.</p>
                    <p class="text-content">Sabemos que criar consciência é fundamental para alcançar mudanças significativas. Ao calcular a tua pegada de carbono, poderás ter uma visão clara das emissões geradas pelas tuas atividades diárias</p>
                    <p class="text-content">Disponibilizaremos ferramentas e recursos para ajudar-te a reduzi-la de forma prática e divertida. Vamos partilhar conselhos incríveis sobre como poupar energia, oferecer opções de transporte sustentável, ideias para uma alimentação mais amiga do ambiente e truques para evitar o desperdício de recursos.</p>
                    <button class="btn btn-outline-light btn-lg" v-if="userStatus != null" @click="$router.push('/calculadora')">Calcular a sua Pegada</button>
                    <button class="btn btn-outline-light btn-lg" v-else @click="$router.push('/login')">Login para Calcular a sua Pegada</button>
                </div>
                <div class="w-50 container"><img src="https://www.huelladecarbono.info/wp-content/uploads/2022/02/compensar-hc-3d-5.png" alt="" class="img-box2"/></div>
            </div>
        </div>
    </div>
    <div class=" box2 w-100 py-4 my-5 bg-light">
        <div class="container w-100">
            <h1>Cuidemos o Meio Ambiente</h1>
            <p class="fs-5 text-objetive">O nosso objetivo é ser o teu aliado nesta aventura. Queremos motivar-te, apoiar-te e tornar todo este processo divertido enquanto cuidas do planeta. Lembra-te de que cada pequena mudança conta e, juntos, podemos fazer a diferença na construção de um futuro mais sustentável</p>
            <div class="container-img-counter w-100 d-flex gap-5 align-items-center">
                <div class="w-75">
                    <img src="https://www.huelladecarbono.info/wp-content/uploads/2022/02/1.-emisiones-directas.png" alt="" class="img-objetive ">
                </div>
                <div class="counter d-flex py-5 justify-content-center align-items-center flex-column w-50">
                    <h4 class="w-100 text-center">QUANTIDADE DE PEGADAS DE CARBONO REDUZIDAS:</h4>
                    <h1 class="w-100 text-center ">----&gt;  {{ counter }}  &lt;----</h1>
                </div>
            </div>
        </div>
    </div>
    <h2 class="container text-description text-success text-uppercase w-100 text-center mb-4">Ultimas pegadas de carbono calculadas</h2>
    <div class="container historial_pegadas mb-5 px-0 overflow-scroll" style="height: 39.5vh;">
        <ol class="list-group list-group-numbered">
            <li class="list-group-item d-flex justify-content-between align-items-start" v-for="historial in HistoricHomeStore.array_historial">
                <div class="ms-2 me-auto">
                    <div class="fw-bold">Anonimo</div>
                       --&gt; {{ historial.totalEmissions }} &lt;-- CO2 emission
                </div>
                <span class="badge bg-success bg-opacity-75 rounded-pill">Caculado en: {{ HistoricHomeStore.datetimeToDate(historial.createdAt) }}</span>
            </li>
        </ol>
    </div>
</template>

<script setup>
    import { useUserStore } from '../stores/userStore';
    import { onMounted, ref, watch } from 'vue';
    import { useHistoricHomeStore } from '../stores/historicHomeStore'
    import axios from 'axios';

    const HistoricHomeStore = useHistoricHomeStore();
    
    const instanceAxios = axios.create({
        baseURL: "http://backendprojectapimj.azurewebsites.net"
    })

    onMounted(()=>{
        instanceAxios.get('/landingpage/counter').then(count =>{
            counter.value = count.data.counter;
        }).catch(err =>{
            counter.value = err.response.data.message
        })

        HistoricHomeStore.getHistorial()

    })

    const counter = ref(null)

    const userStore = useUserStore();

    const userStatus = ref(userStore.user);

    watch(()=> userStore.user, (newStatus) =>{
        userStatus.value = newStatus;
    })
</script>
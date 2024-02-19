<template>
    <section>
        <div class="container py-5">
            <div class="row">
                <div class="col">
                    <nav aria-label="breadcrumb" class="bg-light rounded-3 p-3 mb-4 border border-2 border-success">
                        <ol class="breadcrumb mb-0">
                            <li class="breadcrumb-item"><a href="/" class="link link-success">Home</a></li>
                            <li class="breadcrumb-item active" aria-current="page">Perfil de Usuario</li>
                        </ol>
                    </nav>
                </div>
            </div>
            <div>
                <div class="card mb-4">
                    <div class="card-body border border-2 border-success rounded">
                        <div class="row">
                            <div class="col-sm-3">
                                <p class="mb-0 text-success">Nome Completo</p>
                            </div>
                            <div class="col-sm-9">
                                <p class="text-muted mb-0">{{ firstName + ' ' + lastName }}</p>
                            </div>
                        </div>
                        <hr>
                        <div class="row">
                            <div class="col-sm-3">
                                <p class="mb-0 text-success">Email</p>
                            </div>
                            <div class="col-sm-9">
                                <p class="text-muted mb-0">{{ email }}</p>
                            </div>
                        </div>
                        <hr>
                        <div class="row">
                            <div class="col-sm-3">
                                <p class="mb-0 text-success">Data de Nascimento</p>
                            </div>
                            <div class="col-sm-9">
                                <p class="text-muted mb-0">{{ bornDate }}</p>
                            </div>
                        </div>
                        <hr>
                        <div class="d-flex container justify-content-center gap-5 flex-md-row flex-column">
                            <button class="btn btn-success btn-lg text-uppercase fw-bold" data-bs-toggle="modal" data-bs-target="#updatePass" type="button">Update Password</button>
                            <button class="btn btn-success btn-lg text-uppercase fw-bold" data-bs-toggle="modal" data-bs-target="#updateProfile" type="button">Update Profile</button>
                        </div>
                    </div>
                </div>
                <div class="row">
                    <div class="col-md-6">
                        <div class="card mb-4 mb-md-0">
                            <div class="card-body border border-2 border-success rounded container">
                                <div class="header-card">
                                    <h3 class="text-description text-success w-100 text-center">Resultados da tua Pegada de Carbono</h3>
                                </div>
                                <hr>
                                <div class="habitsFeeding" v-for="habito in profileStore.feedingHabitsUser">
                                    <h4 class="text-description text-success w-100 text-center mb-3">Habitos alimenticios</h4>
                                    <ul class="text-success">
                                        <li><p class="text-success">Consumo de Produtos Locais: <span class="text-description ps-2">{{ habito.local_products ? 'Sim': 'Não' }}</span></p></li>
                                        <li><p class="text-success">Tipo de dieta: <span class="text-description ps-2">{{ habito.diet.diet_type }}</span></p></li>
                                        <li><p class="text-success">Emssiones de CO2, segundo os teus habitos alimenticios: <span class="text-description ps-2">{{ habito.co2_emissions }}</span></p></li>
                                    </ul>
                                </div>
                                <hr>
                                <div class="habitsTransporte" v-for="habito in profileStore.transportHabitUser">
                                    <h4 class="text-description text-success w-100 text-center mb-3">Habitos de Transporte</h4>
                                    <ul class="text-success">
                                        <li><p class="text-success">Distancia aproximada que percorre mensualmente: <span class="text-description ps-2">{{ habito.distance_traveled + ' Km' }}</span></p></li>
                                        <li><p class="text-success">Tipo de dieta: <span class="text-description ps-2">{{ habito.transport.type_transport }}</span></p></li>
                                        <li><p class="text-success">Emssiones de CO2, segundo os teus habitos de transporte: <span class="text-description ps-2">{{ habito.CO2_emissions }}</span></p></li>
                                    </ul>
                                </div>
                                <hr>
                                <div class="habitsHome" v-for="habito in profileStore.homeHabitsUser">
                                    <h4 class="text-description text-success w-100 text-center mb-3">Habitos do Hogar</h4>
                                    <ul class="text-success">
                                        <li><p class="text-success">Quantidade de pessoas que moram no teu hogar: <span class="text-description ps-2">{{ habito.amount_people }}</span></p></li>
                                        <li><p class="text-success">Tamanho do hogar: <span class="text-description ps-2">{{ habito.size + ' m2' }}</span></p></li>
                                        <li><p class="text-success">Reciclam em casa: <span class="text-description ps-2">{{ habito.recycling ? 'Sim':'Não' }}</span></p></li>
                                        <li><p class="text-success">Consumo aprox. de electricidade: <span class="text-description ps-2">{{ habito.electricity_consumption.monthly_consumption }}</span></p></li>
                                        <li><p class="text-success">Total de emissoes de CO2, segundo o teu consumo de electricidade: <span class="text-description ps-2">{{ habito.electricity_consumption.co2_emissions }}</span></p></li>
                                        <li><p class="text-success">Consumo aprox. de gas: <span class="text-description ps-2">{{ habito.gas_consumption.monthly_consumption }}</span></p></li>
                                        <li><p class="text-success">Total de emissoes de CO2, segundo o teu consumo de gas: <span class="text-description ps-2">{{ habito.gas_consumption.co2_emissions }}</span></p></li>
                                    </ul>
                                </div>
                                <hr>
                                <div class="result" v-for="habito in profileStore.homeHabitsUser">
                                    <h4 class="text-description text-success w-100 text-center mb-3">Resultado Total de Emissiones de CO2</h4>
                                     <h3 class="text-success w-100 text-center">{{ habito.total_co2_emissions }}</h3>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="col-md-6">
                        <div class="card mb-4 mb-md-0">
                            <div class="card-body border border-2 border-success rounded container overflow-scroll" style="height: 70vh;">
                                <div class="header-card">
                                    <h3 class="text-description text-success w-100 text-center">Historial das tuas Pegada de Carbono</h3>
                                </div>
                                <hr>
                                <div v-for="historial in profileStore.userHistorial">
                                    <ul>
                                        <li><p class="text-success">Total de emissiones: <span class="text-description ps-2">{{ historial.totalEmissions }}</span></p></li>
                                        <li><p class="text-success">Fecha do Calculo da Pegada: <span class="text-description ps-2">{{ historicHomeStore.datetimeToDate(historial.createdAt) }}</span></p></li>
                                    </ul>
                                    <hr>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>
    <modals />
</template>

<script setup>
    import { onMounted, ref } from 'vue';
    import axios from 'axios';
    import { useRoute } from 'vue-router';
    import modals from '../components/modals.vue'
    import { useProfileStore } from '../stores/profileStore';
    import { useHistoricHomeStore } from '../stores/historicHomeStore';

    const historicHomeStore = useHistoricHomeStore();
    const profileStore = useProfileStore();
    const route = useRoute();

    const instanceAxios = axios.create({
        baseURL: "http://backendprojectapimj.azurewebsites.net"
    })

    var email = ref('')
    var id = ref('');
    var firstName = ref('')
    var lastName = ref('')
    var bornDate = ref('')

    onMounted(async ()=>{
        const token = localStorage.getItem('jwt');
        const userId = localStorage.getItem('userID');
        verifyAccess();
        profileStore.getInfoUser(token, userId);
        profileStore.getHistorialUser(token,userId)
    });

    const verifyAccess = async ()=>{
        
        try {
            const token = localStorage.getItem('jwt');
            instanceAxios.get("/account", {
                headers: {
                    'user-id': localStorage.getItem('userID'),
                    Authorization: "Bearer " + token
                }
            }).then(user =>{
                var data = user.data.user
                email.value = data.email
                id.value = data.account_id
                firstName.value = data.user.firstName
                lastName.value = data.user.lastName

                var date = new Date(data.user.born_date)
                var year = date.getFullYear()
                var month = date.getMonth() + 1
                var day = date.getDate()

                if (month < 10) {
                    month = '0' + month
                }
                bornDate.value = day + '-' + month + '-' + year
            })
        } catch (err) {
           console.log(err)
        }
    }

   


</script>
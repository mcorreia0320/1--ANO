<template>
    <div class="container">
        <div id="carouselExampleControls" class="carousel slide my-5">
            <div class="carousel-inner text-center">
                <div class="carousel-item active">
                    <div class="row d-flex justify-content-center align-items-center h-100">
                        <div class="col col-xl-10">
                            <div class="card" style="border-radius: 1rem;">
                                <div class="d-flex justify-content-center container">
                                    <div class="col-md-6 col-lg-7 d-flex align-items-center">
                                        <div class="card-body p-4 p-lg-5 text-black">
                                            <div class="d-flex align-items-center justify-content-center mb-3 pb-1">
                                                <img src="../assets/image/logo.svg" width="70" height="70" alt="" style="filter: invert(36%) sepia(95%) saturate(377%) hue-rotate(100deg) brightness(94%) contrast(88%);"/>
                                                <span class="h1 fw-bold mb-0 text-success me-5">Calculadora de Carbono</span>
                                            </div>
                                            <h5 class="text-success text-opacity-75 mb-3 pb-3 text-description" style="letter-spacing: 1px;">VAMOS A CALCULAR A TUA PEGADA!</h5>
                                            <div class="pt-1 mb-4 align-items-center gap-4">
                                                <button class="btn btn-success btn-lg w-100 text-uppercase fw-bold" style="height: 3.7rem;" data-bs-target="#carouselExampleControls" data-bs-slide="next" v-if="token != null">COMEZAR</button>
                                                <button class="btn btn-success btn-lg w-100 text-uppercase fw-bold" @click="$router.push('/login')" v-else>Login</button>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="carousel-item">
                        <div class="row d-flex justify-content-center align-items-center h-100">
                            <div class="col col-xl-10">
                                <div class="card" style="border-radius: 1rem;">
                                    <div class="d-flex justify-content-center container">
                                        <div class="col-md-6 col-lg-7 d-flex align-items-center">
                                            <div class="card-body p-4 p-lg-5 text-black">
                                                <form @submit.prevent="">
                                                    <div class="d-flex align-items-center justify-content-center mb-3 pb-1">
                                                        <img src="../assets/image/logo.svg" width="70" height="70" alt="" style="filter: invert(36%) sepia(95%) saturate(377%) hue-rotate(100deg) brightness(94%) contrast(88%);"/>
                                                        <span class="h1 fw-bold mb-0 text-success me-5">Calculadora de Carbono</span>
                                                    </div>
                                                    <h5 class="text-success text-opacity-75 mb-3 pb-3 text-description" style="letter-spacing: 1px;">Habitos Alimenticios</h5>
                                                    <div class="form-outline mb-4 d-flex flex-column align-items-center">
                                                        <div class="d-flex gap-3 justify-content-center text-success border border-1 border-success rounded p-2 w-50">
                                                            <div class="form-check">
                                                                <input class="form-check-input" type="radio" name="localProdutos" id="Não" value="Não" v-model="selectOption">
                                                                <label class="form-check-label text-description" for="Não">Não</label>
                                                            </div>
                                                                <div class="form-check">
                                                                <input class="form-check-input" type="radio" name="flexRadioDefault" id="flexRadioDefault2" value="Sim" v-model="selectOption">
                                                                <label class="form-check-label text-description" for="flexRadioDefault2">Sim</label>
                                                            </div>
                                                        </div>
                                                        <label for="question" class="text-success text-description mt-4">Costumas consumir produtos locais?</label>
                                                    </div>
                                                    <div class="form-outline mb-4">
                                                        <select class="text-success text-opacity-75 form-select form-select-lg" v-model="selectedDiet" required>
                                                            <option value="Selecione um tipo de dieta..." disabled selected>Selecione um tipo de dieta...</option>
                                                            <option :value="diet.diet_type" v-for="diet in calculadoraStore.listDiets">{{ diet.diet_type }}</option>
                                                        </select>
                                                        <label class="form-label text-success pt-2 text-description" for="Diet">Qual é o teu tipo de dieta?</label>
                                                    </div>
                                                    <div class="pt-1 mb-4 align-items-center gap-4 fw-bold d-flex">
                                                        <button class="btn btn-dark w-50 btn-lg fw-bold text-uppercase" style="height: 3.7rem;" @click="calculadoraStore.getUserInfo(token, userId)" data-bs-target="#carouselExampleControls" data-bs-slide="prev">Voltar</button>
                                                        <button class="btn btn-success btn-lg w-50 text-uppercase fw-bold" @click="$router.push('/login')" v-if="token == null">Login</button>
                                                        <button class="btn btn-success btn-lg w-50 text-uppercase fw-bold" data-bs-target="#carouselExampleControls" data-bs-slide="next" style="height: 3.7rem;" type="submit" v-else-if="calculadoraStore.feedingHabits.length == 0" @click="FillHabitsFeeding" :disabled="selectedDiet === 'Selecione um tipo de dieta...' || selectOption === ''">SEGUINTE</button>
                                                        <button class="btn btn-success btn-lg w-50 text-uppercase fw-bold" data-bs-target="#carouselExampleControls" data-bs-slide="next" style="height: 3.7rem;" type="submit" v-else @click="UpdateHabitsFeeding" :disabled="selectedDiet === 'Selecione um tipo de dieta...' || selectOption === ''">SEGUINTE</button>
                                                    </div>
                                                    <p class="text-success">{{ errorMsg }}</p>
                                                </form>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                </div>
                <div class="carousel-item">
                    <div class="row d-flex justify-content-center align-items-center h-100">
                            <div class="col col-xl-10">
                                <div class="card" style="border-radius: 1rem;">
                                    <div class="d-flex justify-content-center container">
                                        <div class="col-md-6 col-lg-7 d-flex align-items-center">
                                            <div class="card-body p-4 p-lg-5 text-black">
                                                <form @submit.prevent="">
                                                    <div class="d-flex align-items-center justify-content-center mb-3 pb-1">
                                                        <img src="../assets/image/logo.svg" width="70" height="70" alt="" style="filter: invert(36%) sepia(95%) saturate(377%) hue-rotate(100deg) brightness(94%) contrast(88%);"/>
                                                        <span class="h1 fw-bold mb-0 text-success me-5">Calculadora de Carbono</span>
                                                    </div>
                                                    <h5 class="text-success text-opacity-75 mb-3 pb-3 text-description" style="letter-spacing: 1px;">Habitos de Transporte</h5>
                                                    <div class="form-outline mb-4">
                                                        <select class="text-success text-opacity-75 form-select form-select-lg" v-model="selectTransport" placeholder="Selecione um tipo de transporte..." required>
                                                            <option value="Selecione um tipo de transporte..." disabled selected>Selecione um tipo de transporte...</option>
                                                            <option  v-for="transport in calculadoraStore.listTransports" :value="transport.type_transport">{{ transport.type_transport }}</option>
                                                        </select>
                                                        <label class="form-label text-success text-opacity-75 pt-2 text-description" for="transporte">Qual é o tipo de transporte que usas habitualmente?</label>
                                                    </div>
                                                    <div class="form-outline mb-4">
                                                        <input type="number"  id="km" class="form-control form-control-lg text-success text-opacity-75 homeMany" placeholder="Ex. 920" v-model="distanceKm" required/>
                                                        <label class="form-label text-success pt-2 text-description" for="kilometros">Aproximadamente quantos kilometros percorre por mes?</label>
                                                    </div>
                                                    <div class="pt-1 mb-4 align-items-center gap-4 d-flex">
                                                        <button class="btn btn-dark w-50 btn-lg fw-bold text-uppercase" style="height: 3.7rem;" @click="calculadoraStore.getUserInfo(token, userId)" data-bs-target="#carouselExampleControls" data-bs-slide="prev">Voltar</button>
                                                        <button class="btn btn-success btn-lg w-50 text-uppercase fw-bold" @click="$router.push('/login')" v-if="token == null">Login</button>
                                                        <button class="btn btn-success btn-lg w-50 text-uppercase fw-bold" data-bs-target="#carouselExampleControls" data-bs-slide="next" style="height: 3.7rem;" type="submit" v-else-if="calculadoraStore.transportHabits.length == 0" @click="FillHabitsTransports" :disabled="distanceKm === null || selectTransport === 'Selecione um tipo de transporte...'">SEGUINTE</button>
                                                        <button class="btn btn-success btn-lg w-50 text-uppercase fw-bold" data-bs-target="#carouselExampleControls" data-bs-slide="next" style="height: 3.7rem;" type="submit" v-else @click="UpdateHabitsTransports" :disabled="distanceKm === null || selectTransport === 'Selecione um tipo de transporte...'">SEGUINTE</button>
                                                    </div>
                                                    <p class="text-success">{{ errorMsg }}</p>
                                                </form>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                </div>
                <div class="carousel-item">
                    <div class="row d-flex justify-content-center align-items-center h-100">
                            <div class="col col-xl-10">
                                <div class="card" style="border-radius: 1rem;">
                                    <div class="d-flex justify-content-center container">
                                        <div class="col-md-6 col-lg-7 d-flex align-items-center">
                                            <div class="card-body p-4 p-lg-5 text-black">
                                                <form @submit.prevent="">
                                                    <div class="d-flex align-items-center justify-content-center mb-3 pb-1">
                                                        <img src="../assets/image/logo.svg" width="70" height="70" alt="" style="filter: invert(36%) sepia(95%) saturate(377%) hue-rotate(100deg) brightness(94%) contrast(88%);"/>
                                                        <span class="h1 fw-bold mb-0 text-success me-5">Calculadora de Carbono</span>
                                                    </div>
                                                    <h5 class="text-success text-opacity-75 mb-3 pb-3 text-description" style="letter-spacing: 1px;">Habitos do Hogar</h5>
                                                    <div class="form-outline mb-4">
                                                        <input type="number" id="homePeople" class="form-control form-control-lg homeMany text-success text-opacity-75" placeholder="Ex. 4" v-model="amountPeople" required/>
                                                        <label class="form-label text-success text-opacity-75 pt-2 text-description" for="homePeople">Quantas pessoas moram na tua casa/apartamento?</label>
                                                    </div>
                                                    <div class="form-outline mb-4">
                                                        <input type="number"  id="tamanho" class="form-control form-control-lg homeMany text-success text-opacity-75" placeholder="Ex. 120" v-model="m2Home" required/>
                                                        <label class="form-label text-success pt-2 text-description" for="tamahno">Qual é o tamanho em m2 da tua casa/apartamento?</label>
                                                    </div>
                                                    <div class="form-outline mb-4 d-flex flex-column align-items-center">
                                                        <div class="d-flex gap-3 justify-content-center text-success border border-1 border-success rounded p-2 w-50">
                                                            <div class="form-check">
                                                                <input class="form-check-input" type="radio" name="localProdutos" id="Não" value="Não" v-model="selectReciclying">
                                                                <label class="form-check-label text-description" for="Não">Não</label>
                                                            </div>
                                                                <div class="form-check">
                                                                <input class="form-check-input" type="radio" name="flexRadioDefault" id="flexRadioDefault2" value="Sim" v-model="selectReciclying">
                                                                <label class="form-check-label text-description" for="flexRadioDefault2">Sim</label>
                                                            </div>
                                                        </div>
                                                        <label for="question" class="text-success text-description mt-2">Costumam fazer reciclagem?</label>
                                                    </div>
                                                    <div class="form-outline mb-4">
                                                        <select class="text-success text-opacity-75 form-select form-select-lg" v-model="selectGas" required>
                                                            <option value="Selecione uma opção..." disabled selected>Selecione uma opção...</option>
                                                            <option :value="value.monthly_consumption" v-for="value in calculadoraStore.betweenValues">{{ value.monthly_consumption }}</option>
                                                        </select>
                                                        <label class="form-label text-success pt-2 text-description" for="Gas">Aproximadamente, quanto costumam gastar em gas mensualmente?</label>
                                                    </div>
                                                    <div class="form-outline mb-4">
                                                        <select class="text-success text-opacity-75 form-select form-select-lg" v-model="selectElectricity" required>
                                                            <option value="Selecione uma opção..." disabled selected>Selecione uma opção...</option>
                                                            <option :value="value.monthly_consumption" v-for="value in calculadoraStore.betweenValues">{{ value.monthly_consumption }}</option>
                                                        </select>
                                                        <label class="form-label text-success pt-2 text-description" for="Electricidade">Aproximadamente, quanto costumam gastar em electricidade mensualmente?</label>
                                                    </div>
                                                    <div class="pt-1 mb-4 align-items-center gap-4 d-flex">
                                                        <button class="btn btn-dark w-50 btn-lg fw-bold text-uppercase" style="height: 3.7rem;" @click="calculadoraStore.getUserInfo(token, userId)" data-bs-target="#carouselExampleControls" data-bs-slide="prev">Voltar</button>
                                                        <button class="btn btn-success btn-lg w-50 text-uppercase fw-bold" @click="$router.push('/login')" v-if="token == null">Login</button>
                                                        <button class="btn btn-success btn-lg w-50 text-uppercase fw-bold" style="height: 3.7rem;" type="submit" v-else-if="calculadoraStore.homeHabits.length == 0" @click="FillInfoHome" :disabled="disabled === true || selectReciclying === '' || amountPeople === null || m2Home === null || selectGas === 'Selecione uma opção...' || selectElectricity === 'Selecione uma opção...'">OBTER PEGADA</button>
                                                        <button class="btn btn-success btn-lg w-50 text-uppercase fw-bold" style="height: 3.7rem;" type="submit" v-else @click="UpdateInfoHome" :disabled="disabled === true || selectReciclying === '' || amountPeople === null || m2Home === null || selectGas === 'Selecione uma opção...' || selectElectricity === 'Selecione uma opção...'">OBTER PEGADA</button>
                                                    </div>
                                                    <p class="text-success">{{ errorMsg }}</p>
                                                </form>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                </div>
            </div>  
        </div>
    </div>
</template>


<script setup>
    import {ref, onMounted } from 'vue'
    import { useCalculadoraStore } from '../stores/calculadoraStore';
    import { useRouter } from 'vue-router';
    import axios from 'axios';

    const router = useRouter();

    const disabled = ref(false);

    const selectedDiet = ref('Selecione um tipo de dieta...');
    const selectOption = ref('');
    const distanceKm = ref(null);
    const selectTransport = ref('Selecione um tipo de transporte...');
    const selectReciclying = ref('');
    const amountPeople = ref(null)
    const m2Home = ref(null);
    const selectGas = ref('Selecione uma opção...');
    const selectElectricity = ref('Selecione uma opção...');

    const errorMsg = ref('');
    
    const calculadoraStore = useCalculadoraStore();
    const token = localStorage.getItem('jwt');
    const userId = localStorage.getItem('userID');

    onMounted( async ()=>{
        calculadoraStore.getUserInfo(token, userId);
        calculadoraStore.getListDiets();
        calculadoraStore.getAllTransports();
        calculadoraStore.getAllValues();
    })

    const instanceAxios = axios.create({
       baseURL: "http://backendprojectapimj.azurewebsites.net"
    })

    const FillHabitsFeeding = async () =>{
        const token = localStorage.getItem('jwt');
        
        const headers = {
            'user-id': localStorage.getItem('userID'),
            Authorization: 'Bearer ' + token
        }

        const data = {
            localProducts: selectOption.value,
            typeDiet: selectedDiet.value
        }

        if (selectOption.value == '' || selectedDiet.value == 'Selecione um tipo de dieta...') {
            errorMsg.value = 'Por favor preencha todos os campos!'
        } else {
            try{
                await instanceAxios.post('/calculator/habits', data, {headers}).then(()=>{
                    errorMsg.value = '';
                })
            }
            catch (err) {return err}
        }
    }

    const UpdateHabitsFeeding = async () =>{
        const token = localStorage.getItem('jwt');
        
        const headers = {
            'user-id': localStorage.getItem('userID'),
            Authorization: 'Bearer ' + token
        }

        const data = {
            localProducts: selectOption.value,
            typeDiet: selectedDiet.value
        }

        if (selectOption.value == '' || selectedDiet.value == 'Selecione um tipo de dieta...') {
            errorMsg.value = 'Por favor preencha todos os campos!'
        } else {
            try{
                await instanceAxios.put('/calculator/habits', data, {headers}).then(()=>{
                    errorMsg.value = ''
                })
                errorMsg.value = ''
            }
            catch (err) {return err}
        }
    }

    const FillHabitsTransports = async ()=>{
        const token = localStorage.getItem('jwt');
        
        const headers = {
            'user-id': localStorage.getItem('userID'),
            Authorization: 'Bearer ' + token
        }

        const data = {
            distanceTraveled: distanceKm.value,
            typeTransport: selectTransport.value
        }

        if (distanceKm.value == null || selectTransport.value == 'Selecione um tipo de transporte...') {
            errorMsg.value = 'Por favor preencha todos os campos!'
        }else {
            try {
                await instanceAxios.post('/calculator/transport', data, {headers}).then(()=>{
                    errorMsg.value = ''
                })
            } catch (error) {
                return error
            }
        }
    }
    const UpdateHabitsTransports = async ()=>{
        const token = localStorage.getItem('jwt');
        
        const headers = {
            'user-id': localStorage.getItem('userID'),
            Authorization: 'Bearer ' + token
        }

        const data = {
            distanceTraveled: distanceKm.value,
            typeTransport: selectTransport.value
        }

        if (distanceKm.value == null || selectTransport.value == 'Selecione um tipo de transporte...') {
            errorMsg.value = 'Por favor preencha todos os campos!'
        } else {
            try {
                await instanceAxios.put('/calculator/transport', data, {headers}).then(()=>{
                    errorMsg.value = ''
                })
            } catch (error) {
                return error
            }
        }

    }

    const FillInfoHome = async () =>{
        const token = localStorage.getItem('jwt');
        
        const headers = {
            'user-id': localStorage.getItem('userID'),
            Authorization: 'Bearer ' + token
        }

        const data = {
            amountPeople: amountPeople.value,
            sizeHome: m2Home.value,
            recycling: selectReciclying.value,
            consumptionsGas: selectGas.value,
            consumptionsElectricity: selectElectricity.value
        }

        if (amountPeople.value == null || m2Home.value == null || selectReciclying.value == '' || selectGas.value == 'Selecione uma opção...' == selectElectricity.value == 'Selecione uma opção...') {
            errorMsg.value = 'Por favor preencha todos os campos!'
        } else {
            try {
                disabled.value = true;
                await instanceAxios.post('/calculator/home', data, {headers}).then(()=>{
                    errorMsg.value = ''
                })
            } catch (error) {
                disabled.value = false;
            }
        }

        
        router.push('/profile')

        selectedDiet.value = 'Selecione um tipo de dieta...';
        selectOption.value = '';
        distanceKm.value = null;
        selectTransport.value = 'Selecione um tipo de transporte...';
        selectReciclying.value = '';
        amountPeople.value = null;
        m2Home.value = null;
        selectGas.value = 'Selecione uma opção...';
        selectElectricity.value ='Selecione uma opção...';

    }

    const UpdateInfoHome = async () =>{
        const token = localStorage.getItem('jwt');
        
        const headers = {
            'user-id': localStorage.getItem('userID'),
            Authorization: 'Bearer ' + token
        }

        const data = {
            amountPeople: amountPeople.value,
            sizeHome: m2Home.value,
            recycling: selectReciclying.value,
            consumptionsGas: selectGas.value,
            consumptionsElectricity: selectElectricity.value
        }

        if (amountPeople.value == null || m2Home.value == null || selectReciclying.value == '' || selectGas.value == 'Selecione uma opção...' == selectElectricity.value == 'Selecione uma opção...') {
            errorMsg.value = 'Por favor preencha todos os campos!'
        } else {
            try {
                disabled.value = true;
                await instanceAxios.put('/calculator/home', data, {headers}).then(()=>{
                    errorMsg.value = ''
                })
            } catch (error) {
                disabled.value = false;
            }
        }


        router.push('/profile')

        selectedDiet.value = 'Selecione um tipo de dieta...';
        selectOption.value = '';
        distanceKm.value = null;
        selectTransport.value = 'Selecione um tipo de transporte...';
        selectReciclying.value = '';
        amountPeople.value = null;
        m2Home.value = null;
        selectGas.value = 'Selecione uma opção...';
        selectElectricity.value ='Selecione uma opção...';
    }


</script>
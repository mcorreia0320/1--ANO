<template>
     <div class="container py-5 h-100">
        <div class="row d-flex justify-content-center align-items-center h-100">
            <div class="col col-xl-10">
                <div class="card" style="border-radius: 1rem;">
                    <div class="row g-0">
                        <div class="col-md-6 col-lg-5 d-none d-md-block">
                            <img src="https://www.padima.es/wp-content/uploads/elementor/thumbs/Eco-pxcu3v3hdxty0sdmy9krntrprtmmx5cle9ww4h6xc0.jpg" class="img-fluid" />
                        </div>
                        <div class="col-md-6 col-lg-7 d-flex align-items-center">
                            <div class="card-body p-4 p-lg-5 text-black">
                                <form @submit.prevent="createProfile">
                                    <div class="d-flex align-items-center mb-3 pb-1">
                                        <img src="../assets/image/logo.svg" width="70" height="70" alt="" style="filter: invert(36%) sepia(95%) saturate(377%) hue-rotate(100deg) brightness(94%) contrast(88%);"/>
                                        <span class="h1 fw-bold mb-0 ps-1 text-success">Save the World</span>
                                    </div>
                                    <h5 class="text-success text-opacity-75 mb-3 pb-3 text-description" style="letter-spacing: 1px;">Create a profile...</h5>
                                    <div class="form-outline mb-4">
                                        <input type="text" id="firstname" class="form-control form-control-lg" v-model="profile.firstname" required/>
                                        <label class="form-label text-success text-opacity-75 pt-1 text-description" for="Firstname">Primeiro Nome</label>
                                    </div>
                                    <div class="form-outline mb-4">
                                        <input type="text"  id="lastname" class="form-control form-control-lg" v-model="profile.lastname" required/>
                                        <label class="form-label text-success pt-1 text-description" for="Lastname">Ultimo Nome</label>
                                    </div>
                                    <div class="form-outline mb-4">
                                        <input type="date" class="form-control form-control-lg text-success text-opacity-75" v-model="profile.bornDate" required>
                                        <label for="date" class="form-label text-success pt-1 text-description">Data de Nascimento</label>
                                    </div>
                                    <div class="pt-1 mb-4 align-items-center gap-4">
                                        <button class="btn btn-success btn-lg w-100 text-uppercase fw-bold" style="height: 3.7rem;" type="submit" :disabled="disabled">Criar Perfil</button>
                                        <p class="text-danger text-opacity-75 pt-2 text-center">{{ errorMsg }}</p>
                                    </div>
                                </form>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
import { ref, reactive} from 'vue';
import axios from 'axios';
import { useRouter } from 'vue-router';
import { useUserStore } from '../stores/userStore';

const UserStore = useUserStore();
const router = useRouter();
const errorMsg = ref('')

const profile = reactive({
    firstname: '',
    lastname: '',
    bornDate: ''
})

const disabled = ref(false);


const instanceAxios = axios.create({
       baseURL: "http://backendprojectapimj.azurewebsites.net"
    })


const createProfile = async ()=>{
    const token = localStorage.getItem('jwt');
    const headers = {
        'user-id': localStorage.getItem('userID'),
        Authorization: 'Bearer ' + token
    }
    
    const data = {
        firstname: profile.firstname,
        lastname: profile.lastname,
        bornDate: profile.bornDate
    }
    try {
        disabled.value = true
        await instanceAxios.post('/account/user', data, { headers }).then(()=>{
            profile.bornDate = ''
            router.push('/')
            UserStore.messageAuthentication("Bem vindo, " + profile.firstname + ' ' + profile.lastname);
            profile.firstname = ''
            profile.lastname = ''
        }).catch((error)=>{
            errorMsg.value = '* ' + error.response.data.message + ' *';
        })
    } catch (err) {
        if (err) {
            errorMsg.value = '* Something went wrong! *';
            disabled.value = false
        }
    }
}



</script>
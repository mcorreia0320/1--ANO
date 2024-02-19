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
                                <form @submit.prevent="registerUser">
                                    <div class="d-flex align-items-center mb-3 pb-1">
                                        <img src="../assets/image/logo.svg" width="70" height="70" alt="" style="filter: invert(36%) sepia(95%) saturate(377%) hue-rotate(100deg) brightness(94%) contrast(88%);"/>
                                        <span class="h1 fw-bold mb-0 ps-1 text-success">Save the World</span>
                                    </div>
                                    <h5 class="text-success text-opacity-75 mb-3 pb-3 text-description" style="letter-spacing: 1px;">Create a account...</h5>
                                    <div class="form-outline mb-4">
                                        <input type="email" v-model="credenciais.email" id="email" class="form-control form-control-lg" required/>
                                        <label class="form-label text-success text-opacity-75 pt-1 text-description" for="email">Email</label>
                                    </div>
                                    <div class="form-outline mb-4">
                                        <input type="password" v-model="credenciais.password" id="password" class="form-control form-control-lg" required/>
                                        <label class="form-label text-success text-opacity-75 pt-1 text-description" for="password">Password</label>
                                    </div>
                                    <div class="pt-1 mb-4 d-flex align-items-center gap-4">
                                        <button class="btn btn-success btn-lg btn-block w-25" type="submit" :disabled="disable">Sign-up</button>
                                        <p class="text-danger text-opacity-75 pt-2 text-center">{{ errorMsg }}</p>
                                    </div>
                                    <p class="mb-5 pb-lg-2 text-success text-opacity-75 text-description" >Já tens uma conta? <a href="/login"
                                        class="link-success text-description button-register">Login aqui</a></p>
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

const userStore = useUserStore();
const router = useRouter();

const instanceAxios = axios.create({
       baseURL: "https://backendprojectapimj.azurewebsites.net"
    })

const errorMsg = ref('')

const credenciais = reactive({
    email: '',
    password: ''
})

const disable = ref(false);

const registerUser = async ()=> {
    try {
        disable.value = true;
        await instanceAxios.post("/account/signup", {
            email: credenciais.email,
            password: credenciais.password
        }).then(user => {
            const userData = user.data;
            localStorage.setItem("jwt", userData.token);
            localStorage.setItem("userID", userData.user.account_id);
            userStore.setUser(userData.user);
            credenciais.email = ''
            credenciais.password = ''
            errorMsg.value = ''
            router.push('/createProfile');
        }).catch((error)=>{
            errorMsg.value = '* ' + error.response.data.message + ' *';
        })
    } catch (err) {
        if (err) {
            errorMsg.value = '* Something went wrong! *';
            disable.value = false;
        }
    }
}
</script>
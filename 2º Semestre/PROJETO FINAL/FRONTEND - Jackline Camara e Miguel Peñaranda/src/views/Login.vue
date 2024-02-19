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
                <form @submit.prevent="loginUser">
                  <div class="d-flex align-items-center mb-3 pb-1">
                    <img src="../assets/image/logo.svg" width="70" height="70" alt="" style="filter: invert(36%) sepia(95%) saturate(377%) hue-rotate(100deg) brightness(94%) contrast(88%);"/>
                    <span class="h1 fw-bold mb-0 ps-1 text-success">Save the World</span>
                  </div>
                  <h5 class="text-success text-opacity-75 mb-3 pb-3 text-description" style="letter-spacing: 1px;">Sign into your account...</h5>
                  <div class="form-outline mb-4">
                    <input type="email" id="Email" class="form-control form-control-lg" required v-model="credenciais.email"/>
                    <label class="form-label text-success text-opacity-75 pt-1 text-description" for="Email">Email</label>
                  </div>
                  <div class="form-outline mb-4">
                    <input type="password" id="Password" class="form-control form-control-lg" required v-model="credenciais.password"/>
                    <label class="form-label text-success text-opacity-75 pt-1 text-description" for="Password">Password</label>
                  </div>
                  <div class="pt-1 mb-4 d-flex align-items-center gap-4">
                    <button class="btn btn-success btn-lg btn-block w-25" type="submit">Login</button>
                    <p class="text-danger text-opacity-75 pt-2 text-center">{{ errorMsg }}</p>
                  </div>

                  <p class="mb-5 pb-lg-2 text-success text-opacity-75 text-description" >Ainda não tens conta? <a href="/signup"
                    class="link-success text-description button-register">Regista-te aqui</a></p>
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
import { ref, reactive } from 'vue';
import axios from 'axios';
import { useRouter } from 'vue-router';
import { useUserStore } from '../stores/userStore';

const router = useRouter();
const userStore = useUserStore();


const instanceAxios = axios.create({
        baseURL: "http://backendprojectapimj.azurewebsites.net"
    })

const errorMsg = ref('')

const credenciais = reactive({
    email: '',
    password: ''
})

const loginUser = async ()=> {
    try {
        await instanceAxios.post("/account/login", {
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
            router.push('/');
            userStore.messageAuthentication("Bem vindo, " + userData.user.user.firstName + " " + userData.user.user.lastName)
        }).catch((error)=>{
            errorMsg.value = '* ' + error.response.data.message + ' *';
        })
    } catch (err) {
        if (err) {
            errorMsg.value = '* Something went wrong! *';
        }
    }
}
</script>
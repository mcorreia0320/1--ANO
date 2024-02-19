<template>
    <div class="modal fade" tabindex="-1" role="dialog" id="signupModal">
        <div class="modal-dialog" role="document">
            <div class="modal-content">
                <div class="modal-header">
                    <h5 class="modal-title subtitle-modal fw-bolder">Sign In</h5>
                    <button type="button" class="close" data-bs-dismiss="modal" arialabel="Close" @click="cancelar">
                        <span aria-hidden="true">&times;</span>
                    </button>
                </div>
                <div class="modal-body">
                    <form id="signup-form" @submit.prevent="submitRegister">
                        <div class="form-group py-2">
                            <label for="username" class="subtitle-modal">Nome de Usuario:</label>
                            <input type="text"  class="form-control" placeholder="Miguel Peñaranda ou mcorreia0320" v-model="credencias.username" required>
                        </div>
                        <div class="form-group py-2">
                            <label for="email" class="subtitle-modal">Email:</label>
                            <input type="email" id="signin-email" class="form-control" placeholder="example@gmail.com" v-model="credencias.email" required>
                        </div>
                        <div class="form-group py-2">
                            <label for="password" class="subtitle-modal">Password:</label>
                            <input type="password" id="signin-password" class="form-control" placeholder="*******" v-model="credencias.password" required>
                        </div>
                        <div class="d-flex justify-content-between">
                            <p class="fw-bold text-center w-50 color-text">{{ status }}</p>
                            <div>
                                <button type="button" class="botao botao-modal-1" data-bs-dismiss="modal" @click="cancelar">Cancelar</button>
                                <button type="submit" class="botao botoao-modal-2 ms-2">Register</button>
                            </div>
                        </div>
                    </form>
                </div>
            </div>
        </div>
    </div>
    <div class="modal fade" tabindex="-1" role="dialog" id="loginModal">
        <div class="modal-dialog" role="document">
            <div class="modal-content">
                <div class="modal-header">
                    <h5 class="modal-title subtitle-modal fw-bolder">Login</h5>
                    <button type="button" class="close" data-bs-dismiss="modal" arialabel="Close" @click="cancelar">
                        <span aria-hidden="true">&times;</span>
                    </button>
                </div>
                <div class="modal-body">
                    <form id="login-form" @submit.prevent="submitLogin">
                        <div class="form-group py-3">
                            <label for="email" class="subtitle-modal">Email:</label>
                            <input type="email" class="form-control" placeholder="example@gmail.com" v-model="credencias.email" required>
                        </div>
                        <div class="form-group py-3">
                            <label for="password" class="subtitle-modal">Password:</label>
                            <input type="password" class="form-control" placeholder="*******" v-model="credencias.password" required>
                        </div>
                        <div class="d-flex justify-content-between">
                            <p class="fw-bolder text-center w-50 color-text">{{ status }}</p>
                            <div>
                                <button type="button" class="botao botao-modal-1" data-bs-dismiss="modal" @click="cancelar">Cancelar</button>
                                <button type="submit" class="botao botoao-modal-2 ms-2">Login</button>
                            </div>
                        </div>
                    </form>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
import {reactive, ref} from 'vue';
import { useAuthStore } from '@/stores/authStore';
import { auth } from '../firebase';
import { createUserWithEmailAndPassword, signInWithEmailAndPassword, updateProfile } from 'firebase/auth';

const authStore = useAuthStore();

const status = ref('');

const cancelar = ()=>{
    status.value = '';
    credencias.email = '';
    credencias.password = '';
    credencias.username = '';
}

const credencias = reactive({
    username: '',
    email: '',
    password: ''
})


const submitRegister = async ()=> {
    
    try {

            // FUNÇÃO DE FIREBASE PARA FAZER O REGISTO
        
        const userCredentials = await createUserWithEmailAndPassword(auth,credencias.email,credencias.password)
        
        await updateProfile(userCredentials.user, {
            displayName: credencias.username
        })

        // FECHA O MODAL APÓS O REGISTO COM EXITO

        const signupModal = document.querySelector('#signupModal')  // Seleciona o div do modal
        const modal = bootstrap.Modal.getInstance(signupModal)      // Aplicação do codigo da documentação do bootstrap
        modal.hide()                                                // Usa-se o metodo hide do bootstrap para fechar o modal

        // Mensagem de successo usando a framework toastefy desde a store authStore
        if (userCredentials.user.displayName == null){
            authStore.messageAuthentication("Bem vindo, " + userCredentials.user.email)
        } else authStore.messageAuthentication("Bem vindo, " + userCredentials.user.displayName)
        
        credencias.email = '';
        credencias.password = ''
        status.value = '';
        credencias.username = '';
    } 
    catch (error) {

        if (error.code === 'auth/invalid-email') {
            status.value = 'Email Invalido';
        }
        else if (error.code === 'auth/weak-password' ) {
            status.value = 'O password deve ter no minimo 6 caracteres';
        }
        else if (error.code === 'auth/email-already-in-use') {
            status.value = 'O email introduzido já esta em uso'
        }
        else if (error.code) {
            alert('Something went wrong')
        }
    }
 }

  const submitLogin = async ()=> {
    
    try{
        
            // FUNÇÃO DE FIREBASE PARA FAZER O LOGIN

        const userCredentials = await  signInWithEmailAndPassword(auth, credencias.email, credencias.password)
        
        // FECHA O MODAL APÓS O LOGIN COM EXITO

        const loginModal = document.querySelector('#loginModal')  // Seleciona o div do modal
        const modal = bootstrap.Modal.getInstance(loginModal)      // Aplicação do codigo da documentação do bootstrap
        modal.hide()                                                // Usa-se o metodo hide do bootstrap para fechar o modal

        // Mensagem de successo usando a framework toastefy desde a store authStore
        if (userCredentials.user.displayName == null){
            authStore.messageAuthentication("Bem vindo, " + userCredentials.user.email)
        } else authStore.messageAuthentication("Bem vindo, " + userCredentials.user.displayName)
        
        
        credencias.email = '';
        credencias.password = ''
        status.value = '';
        credencias.username = '';

        }
    catch (error) {

        if (error.code === 'auth/user-not-found') {
            status.value = 'O email inserido não se encontra registado'
        }
        else if (error.code === 'auth/wrong-password') {
            status.value = 'O password inserido é incorreto, tente novamente'
        }
        else if (error.code) {
            alert('Something went wrong')
        }

    }
 }




</script>
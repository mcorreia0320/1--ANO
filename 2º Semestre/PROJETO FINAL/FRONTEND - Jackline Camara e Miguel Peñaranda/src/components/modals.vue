<template>
    <div class="modal fade" tabindex="-1" role="dialog" id="updatePass">
        <div class="modal-dialog" role="document">
            <div class="modal-content border border-5 border-success text-success">
                <div class="modal-header">
                    <h5 class="modal-title subtitle-modal fw-bolder">Update Password</h5>
                    <button type="button" class="close btn rounded bg-success text-light border border-transparent" data-bs-dismiss="modal" arialabel="Close" @click="resetUpdateForm">
                        <span aria-hidden="true">&times;</span>
                    </button>
                </div>
                <div class="modal-body container">
                    <form @submit.prevent="updatePassword">
                        <div class="form-group py-2">
                            <label for="oldpassword" class="subtitle-moda mb-2l">Palavra-passe Antiga:</label>
                            <input type="password"  class="form-control" placeholder="*******" v-model="oldPassword" required>
                        </div>
                        <div class="form-group py-2">
                            <label for="newPassoword" class="subtitle-modal mb-2">Palavra-passe Nova:</label>
                            <input type="password"  v-model="newPassword" class="form-control" placeholder="*******" required>
                        </div>
                        <div class="form-group py-2">
                            <label for="newPasswordConfirm" class="subtitle-modal mb-2">Confirmar Palavra-passe:</label>
                            <input type="password" v-model="newPasswordConfirm" class="form-control" placeholder="*******" required>
                        </div>
                        <div class="d-flex justify-content-between">
                            <p class="fw-bold text-center w-50 color-text">{{ errorMsg }}</p>
                            <div>
                                <button type="button" class="btn btn-dark" data-bs-dismiss="modal" @click="resetUpdateForm">Cancelar</button>
                                <button type="submit" class="btn btn-success ms-2">Update</button>
                            </div>
                        </div>
                    </form>
                </div>
            </div>
        </div>
    </div>
    <div class="modal fade" tabindex="-1" role="dialog" id="updateProfile">
        <div class="modal-dialog" role="document">
            <div class="modal-content border border-5 border-success text-success">
                <div class="modal-header">
                    <h5 class="modal-title subtitle-modal fw-bolder">Update Profile</h5>
                    <button type="button" class="close btn rounded bg-success text-light border border-transparent" data-bs-dismiss="modal" arialabel="Close" @click="resetUpdateForm">
                        <span aria-hidden="true">&times;</span>
                    </button>
                </div>
                <div class="modal-body container">
                    <form @submit.prevent="updateProfile">
                        <div class="form-group py-2">
                            <label for="oldpassword" class="subtitle-moda mb-2l">Primeiro Nome:</label>
                            <input type="text" class="form-control" v-model="formProfile.firstName" required>
                        </div>
                        <div class="form-group py-2">
                            <label for="newPassoword" class="subtitle-modal mb-2">Ultimo Nome:</label>
                            <input type="text" v-model="formProfile.lastName" class="form-control" required>
                        </div>
                        <div class="form-group py-2">
                            <label for="newPasswordConfirm" class="subtitle-modal mb-2">Data de Nascimento:</label>
                            <input type="date" v-model="formProfile.bornDate" class="form-control" required>
                        </div>
                        <div class="d-flex justify-content-between">
                            <div>
                                <button type="button" class="btn btn-dark" data-bs-dismiss="modal" @click="resetUpdateForm">Cancelar</button>
                                <button type="submit" class="btn btn-success ms-2">Update</button>
                            </div>
                        </div>
                    </form>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
import { ref, onMounted, reactive } from 'vue';
import axios from 'axios';
import { useRouter } from 'vue-router';

const router = useRouter();

const instanceAxios = axios.create({
        baseURL: "http://backendprojectapimj.azurewebsites.net"
    })

const oldPassword = ref('');
const newPassword = ref('')
const newPasswordConfirm = ref('');

const errorMsg = ref('');

const firstName = ref('')
const lastName = ref('')
const bornDate = ref('')

const formProfile = reactive({
    firstName: '',
    lastName: '',
    bornDate: ''
})


const resetUpdateForm = ()=>{
    oldPassword.value = ''
    newPassword.value = ''
    newPasswordConfirm.value = ''
    formProfile.bornDate = ''
    getProfile();
}

onMounted(async ()=>{
        getProfile();
    });

const getProfile = async ()=>{
        try {
            const token = localStorage.getItem('jwt');
            instanceAxios.get("/account", {
                headers: {
                    'user-id': localStorage.getItem('userID'),
                    Authorization: "Bearer " + token
                }
            }).then(user =>{
                var data = user.data.user
                firstName.value = data.user.firstName
                lastName.value = data.user.lastName
                formProfile.firstName = data.user.firstName
                formProfile.lastName = data.user.lastName

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

    const updatePassword = ()=>{
        const token = localStorage.getItem('jwt');
        
        const headers = {
            'user-id': localStorage.getItem('userID'),
            Authorization: 'Bearer ' + token
        }

        const data = {
            oldPassword: oldPassword.value,
            newPassword: newPassword.value
        }


        if (newPassword.value != newPasswordConfirm.value) {
            errorMsg.value = 'Por favor confirma a palavra passe, são diferentes!'
        }
        else {
            try{
                instanceAxios.put('/account/updatePassword', data, {headers}).then(() =>{
                    resetUpdateForm();
                    const formModal = document.querySelector('#updatePass');  
                    const modal = bootstrap.Modal.getInstance(formModal);      
                    modal.hide(); 
                }).catch(err =>{
                   errorMsg.value = err.response.data.message;
                })
            }catch (err) {
                return err
            }
        }
    }

    const updateProfile = ()=>{
        const token = localStorage.getItem('jwt');
        
        const headers = {
            'user-id': localStorage.getItem('userID'),
            Authorization: 'Bearer ' + token
        }

        const data = {
            firstname: formProfile.firstName,
            lastname: formProfile.lastName,
            bornDate: formProfile.bornDate
        }

        try {
            instanceAxios.put('/account/user', data, {headers}).then(()=>{
                resetUpdateForm();
                const formModal = document.querySelector('#updateProfile');  
                const modal = bootstrap.Modal.getInstance(formModal);   
                modal.hide(); 
                router.go(0);
            })
        } catch (error) {
            return error
        }
    }
</script>
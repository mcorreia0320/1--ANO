<template>
    <div class="container">
        <div class="row d-flex justify-content-center align-items-center h-100 my-5">
            <div class="col col-xl-10">
                <div class="card" style="border-radius: 1rem;">
                    <div class="d-flex justify-content-center container">
                        <div class="col-md-6 col-lg-7 d-flex align-items-center">
                            <div class="card-body p-4 p-lg-5 text-black">
                                <div class="d-flex align-items-center justify-content-center mb-3 pb-1">
                                    <h1 class="h1 fw-bold mb-0 text-success">Menu de Administrador</h1>
                                </div>
                                <hr>
                                <h3 class="text-description text-success w-100 text-center mb-4">Lista de Utilizadores</h3>
                                <ol class="list-group list-group-numbered border border-1 border-success overflow-scroll" style="height: 50vh;">
                                    <li class="list-group-item d-flex justify-content-between align-items-start" v-for="user in adminStore.ListUsers">
                                        <div class="ms-2 me-auto">
                                            <div class="fw-bold">{{ user.user.firstName + ' ' + user.user.lastName }}</div>
                                            <span class="ms-3">{{ 'Data de Nascimento: ' + historicHomeStore.datetimeToDate(user.user.born_date) }}</span>
                                        </div>
                                        <span class="badge bg-success bg-opacity-75 rounded-pill">{{ user.email}}</span>
                                    </li>
                                </ol>
                                <hr class="my-5">
                                <form action="Delete Users" class="container d-flex justify-content-center - align-items-center flex-column" @submit.prevent="deleteUser">
                                    <h3 class="text-description text-success w-100 text-center mb-4">Eliminar Usuarios</h3>
                                    <input type="email" v-model="email" class="form-control form-control-lg text-success text-opacity-75 homeMany" placeholder="example@gmail.com" required/>
                                    <button type="submit" class="btn btn-success btn-lg mt-4 w-75">Eliminar Utilizador</button>
                                    <h5 class="text-description text-success text-opacity-75 mt-4">{{ Msg }}</h5>
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
    import { ref, onMounted} from 'vue'
    import { useAdministradorStore } from '../stores/administradorStore';
    import { useHistoricHomeStore } from '../stores/historicHomeStore';
    import axios from 'axios';
    import { useRouter } from 'vue-router';

    const router = useRouter();
    const historicHomeStore = useHistoricHomeStore();
    const adminStore = useAdministradorStore();

    const email = ref('')

    const Msg = ref('');

    onMounted(()=>{
        const token = localStorage.getItem('jwt');
        const userId = localStorage.getItem('userID');
        
        adminStore.getAllUsers(token, userId);
    })

    const deleteUser = ()=>{
        const token = localStorage.getItem('jwt');
        const headers = {
        'user-id': localStorage.getItem('userID'),
        Authorization: 'Bearer ' + token
        };

        const config = {
        headers: headers,
        data: { email: email.value }
        };

        try {
        axios.delete('https://backendprojectapimj.azurewebsites.net/admin', config)
            .then(result => {
                Msg.value = result.data.message
                email.value = '';
                router.go(0);
            })
            .catch(err => {
                if (err) {
                    Msg.value = 'A conta inserida não existe!'
                }
            });
        } catch (error) {
        return error;
        }
    }
</script>
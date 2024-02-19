<template>
    <Header v-if="!$route.meta.hideComponents"/>
    <div class="text-light">
        <RouterView />
    </div>
    <Footer v-if="!$route.meta.hideComponents"/>
</template>

<script setup>
import { RouterView } from 'vue-router'
import Header from './components/Header.vue'
import Footer from './components/Footer.vue'
import { onMounted, ref, watch } from 'vue';
import { useUserStore } from './stores/userStore';
import axios from 'axios';

const UserStore = useUserStore();
const instanceAxios = axios.create({
        baseURL: "http://backendprojectapimj.azurewebsites.net"
    })

const userStatus = ref(UserStore.user);

onMounted( async ()=>{
    if (localStorage.getItem('jwt') != null) {
        const token = localStorage.getItem('jwt');
        instanceAxios.get('/account',{
            headers: {
                        'user-id': localStorage.getItem('userID'),
                        Authorization: "Bearer " + token
                    }
        }).then(userInfo =>{
            var data = userInfo.data.user
            UserStore.setUser(data);
        })
    }
    watch(()=> UserStore.user, (newStatus) =>{
    userStatus.value = newStatus;
})
})



</script>


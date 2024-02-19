<template>
    <h1>Mensagem Individual</h1>
    <p>Conteúdo da mensagem com o ID: {{ $route.params.id }}</p>
    <p> <RouterLink to="/msgs">&lt; Voltar</RouterLink></p>
    <button @click="showMsgId" class="msg-btn">ID</button>
    <div class="msg-btn">
        <button @click="goFirstMsg">Primeira Mensagem</button>
        <button @click="goMsgs">Todas as Mensagens</button>
        <button @click="goHome">Home</button>
    </div>
</template>
<style>
    .msg-btn {
        display: flex;
        gap: 5px;
        margin-top: 15px;
        width: fit-content;
        padding-left: 0.8rem;
        padding-right: 0.8rem;
    }
</style>
<script setup>
    import {useRouter, useRoute}  from 'vue-router'

    const router = useRouter();
    const route = useRoute();

    const showMsgId = ()=> {
        alert('O id da mensagem é: ' + route.params.id)
    }
    const goMsgs = ()=> {
        router.push('/msgs')
    }
    const goHome = ()=> {
        router.push({name:'home'})
    }
    const goFirstMsg = ()=> {
        router.push({
            name: 'msg',
            params: {
                id: '1'
            }
        })
    }
</script>
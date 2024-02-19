<template>
    <div>
        <footer class="d-flex flex-wrap justify-content-between align-items-center py-3 border-top bg-light ps-2 pe-2" id="footer">
        <p class="col-md-4 mb-0 text-muted">© 2023 MJ, Inc</p>

        <a href="/" class="col-md-4 d-flex align-items-center justify-content-center mb-3 mb-md-0 me-md-auto link-dark text-decoration-none">
            <img src="../assets/image/logo.svg" width="70" height="70" alt="" style="filter: invert(36%) sepia(95%) saturate(377%) hue-rotate(100deg) brightness(94%) contrast(88%);">
        </a>

        <ul class="nav col-md-4 justify-content-end">
            <li v-for="item in navbarStore.array_buttons"><RouterLink class="nav-link link-success" :to="item.route">{{ item.title }}</RouterLink></li>
            <li><a href="/login" class="nav-link link-success" v-if="userStatus == null">Login</a></li>
            <li><a href="/signUp" class="nav-link link-success" v-if="userStatus == null">Sign Up</a></li>
        </ul>
    </footer>
    </div>
</template>

<script setup>
    import { RouterLink } from 'vue-router';
    import { useNavbarStore } from '../stores/navbarStore';
    import { useUserStore } from '../stores/userStore';
    import { ref, watch } from 'vue'

    const userStore = useUserStore();
    const navbarStore = useNavbarStore();
    
    const userStatus = ref(userStore.user);

    watch(()=> userStore.user, (newStatus) =>{
        userStatus.value = newStatus;
    })

</script>
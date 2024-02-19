<template>
<header class="p-3 border-bottom bg-light" id="header">
    <div class="ms-2 me-2">
      <div class="d-flex flex-wrap align-items-center justify-content-center justify-content-lg-start">
        <a href="/" class="d-flex align-items-center mb-2 mb-lg-0 text-dark text-decoration-none me-3">
            <img src="../assets/image/logo.svg" width="50" height="50" alt="" style="filter: invert(36%) sepia(95%) saturate(377%) hue-rotate(100deg) brightness(94%) contrast(88%);">
        </a>

        <ul class="nav col-12 col-lg-auto me-lg-auto mb-2 justify-content-center mb-md-0 gap-1">
          <li v-for="item in navbarStore.array_buttons"><RouterLink class="nav-link px-2 link-success" :to="item.route">{{ item.title }}</RouterLink></li>
        </ul>

        <div class="col-md-3 text-end" v-if="userStatus == null">
            <button type="button" class="btn btn-outline-success me-2" @click="$router.push('/login')">Login</button>
            <button type="button" class="btn btn-success" @click="$router.push('/signUp')">Sign-up</button>
        </div>
        
        <div class="dropdown text-end" v-else>
          <a class="d-block link-success text-decoration-none dropdown-toggle text-success" id="dropdownUser1" data-bs-toggle="dropdown" aria-expanded="false">
            <img src="../assets/image/profile.svg" width="40" height="40"  alt="" style="filter: invert(36%) sepia(95%) saturate(377%) hue-rotate(100deg) brightness(94%) contrast(88%);">
          </a>
          <ul class="dropdown-menu text-small" aria-labelledby="dropdownUser1" style="">
            <li><RouterLink class="dropdown-item" to="/profile">Profile</RouterLink></li>
            <li><RouterLink class="dropdown-item" to="/administrador" v-if="userStatus.account_id == 1">Administrador</RouterLink></li>
            <li><hr class="dropdown-divider"></li>
            <li><a class="dropdown-item" @click="logout()">Sign out</a></li>
          </ul>
        </div>
      </div>
    </div>
  </header>
</template>

<script setup>
    import { RouterLink } from 'vue-router';
    import { useNavbarStore } from '../stores/navbarStore';
    import { useUserStore } from '../stores/userStore';
    import { ref, watch } from 'vue'
    import { useRouter } from 'vue-router';

    const router = useRouter();
    
    const userStore = useUserStore();
    const navbarStore = useNavbarStore();

    const userStatus = ref(userStore.user);

    watch(()=> userStore.user, (newStatus) =>{
        userStatus.value = newStatus;
    })

    const logout = ()=>{
      userStore.logout();
      router.push('/');
    }
</script>
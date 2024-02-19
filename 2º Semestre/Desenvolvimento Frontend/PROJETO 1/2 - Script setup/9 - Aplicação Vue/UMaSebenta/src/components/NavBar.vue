<template>
    <nav class="navbar is-success" role="navigation" aria-label="main navigation">
        <div class="container is-max-desktop">
            <div class="navbar-brand">
                <div class="navbar-item is-size-4 is-family-monospace">
                    UMaSebenta
                </div>
                <a @click.prevent="showMobileNav = !showMobileNav" :class="{'is-active': showMobileNav }" role="button" class="navbar-burger" aria-label="menu" aria-expanded="false" data-target="navbarBasicExample">
                <span aria-hidden="true"></span>
                <span aria-hidden="true"></span>
                <span aria-hidden="true"></span>
                </a>
            </div>
            <div id="navbarBasicExample" class="navbar-menu" :class="{'is-active': showMobileNav}">
                <div class="navbar-end">
                    <RouterLink class="navbar-item" active-class="is-active" to="/">Apontamentos</RouterLink>
                    <RouterLink class="navbar-item" active-class="is-active" to="/stats">Estatíticas</RouterLink>
                    <RouterLink class="navbar-item" active-class="is-active" to="/auth">Authenticacion</RouterLink>
                </div>
                <button class="button is-small is-warning mt-3 ml-3">Logout</button>
            </div>
        </div>
    </nav>
</template>

<script setup>

    import { ref } from 'vue'
    const showMobileNav = ref(false);
    
</script>

<style>
    @media (max-width: 1023px) {
        .navbar-menu{
            position: absolute;
            width: 100%;
            left: 0;
        }
    }
</style>
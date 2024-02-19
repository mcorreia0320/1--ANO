<template>
        <div class="w-100  d-flex justify-content-center align-items-center bg-error">
            <div class="container-error d-flex align-items-center">
                <img src="../assets/images/Error-img.png" alt="" class="img-error">
                <div class="text-error">
                    <h2>OOPS!</h2>
                    <h5>PAGE NOT FOUND</h5>
                    <h1>ERROR 404</h1>
                    <div class="boton-error">
                         <a><button @click="$router.push('/')">GO BACK</button></a>
                    </div>
                </div>
            </div>
        </div>
</template>

<script>
    export default {
        mounted(){
            document.body.style.paddingTop = '0';
        }
        
    }
</script>
<template>
     <div class="w-100  d-flex justify-content-center align-items-center bg-error">
            <div class="container-error d-flex align-items-center">
                <img src="../assets/image/pngegg.png" alt="" class="img-error">
                <div class="">
                    <h1 class="text-error">OOPS!</h1>
                    <h5 class="text-error2">PAGE NOT FOUND</h5>
                    <h1 class="text-error2">ERROR 404</h1>
                    <div class="boton-error w-100">
                         <button @click="$router.push('/')" class="btn btn-dark w-100 py-3">GO BACK</button>
                    </div>
                </div>
            </div>
        </div>
</template>
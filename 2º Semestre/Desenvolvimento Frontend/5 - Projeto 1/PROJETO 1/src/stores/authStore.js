import { defineStore } from 'pinia';
import { signOut  } from 'firebase/auth';



export const useAuthStore = defineStore('authStore', {
    state: ()=>{
        return {
            user: null
        }
    },
    actions: {
        setUser(dados) {
            this.user = dados;
        },

        messageAuthentication(message) {
            Toastify({
                text: message,
                duration: 5000,
                destination: "https://github.com/apvarun/toastify-js",
                newWindow: true,
                close: true,
                gravity: "bottom", // `top` or `bottom`
                position: "right", // `left`, `center` or `right`
                stopOnFocus: true, // Prevents dismissing of toast on hover
                style: {
                    background: "orangered",
                    color: "white",
                    fontWeight: "Bolder",
                    borderRadius: "2rem"
                },
                onClick: function(){} // Callback after click
                }).showToast();
        },
        
        logout(user) {
            signOut(user)
        }
    }
})
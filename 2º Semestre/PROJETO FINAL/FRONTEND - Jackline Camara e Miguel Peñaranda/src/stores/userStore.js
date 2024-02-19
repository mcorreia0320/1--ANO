import { defineStore } from "pinia";

export const useUserStore = defineStore('UserStore', {
    state: ()=>{
        return {
            user: null
        }
    },
    actions: {
        setUser(dataUser) {
            this.user = dataUser;
        },
        logout(){
            localStorage.removeItem('jwt');
            localStorage.removeItem('userID');
            this.user = null;
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
                    background: "green",
                    color: "white",
                    fontWeight: "Bolder",
                    borderRadius: "2rem"
                },
                onClick: function(){} // Callback after click
                }).showToast();
        }
    }
})
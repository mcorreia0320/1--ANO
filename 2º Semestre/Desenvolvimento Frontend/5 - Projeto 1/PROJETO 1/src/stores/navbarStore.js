import { defineStore } from 'pinia'

export const useNavbarStore = defineStore('navbarStore', {
    state: ()=> {
        return {
            botoes: [
                {
                    name: 'Home',
                    path: '/'
                },
                {
                    name: 'Pesquisar Cocktails',
                    path: '/pesquisar_cocktails'
                },
                {
                    name: 'Testemunhos',
                    path: '/testemunho'
                }
            ],
            shop_path : '/shop' 
        }
    },
    actions: {
        closeMenuMobile(){
            
            var navbarToggler = document.querySelector('.navbar-toggler');
            var navbarCollapse = document.querySelector('.navbar-collapse');

            
            var navbarOptions = navbarCollapse.querySelectorAll('.nav-link');

            
            navbarOptions.forEach(function(option) {
                
                option.addEventListener('click', function() {
                
                    navbarCollapse.classList.remove('show');
                    navbarToggler.setAttribute('aria-expanded', 'false');
                    
                    });

            });
        }
    }
})
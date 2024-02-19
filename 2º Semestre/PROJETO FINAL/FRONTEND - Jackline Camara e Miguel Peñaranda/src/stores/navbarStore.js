import { defineStore } from 'pinia'

export const useNavbarStore = defineStore('navBarStore', {
    state: ()=>{
        return {
            array_buttons: [
                {
                    title: 'Home',
                    route: '/'
                },
                {
                    title: 'Categorias Ecológicas',
                    route: '/categorias'
                },
                {
                    title: 'Calculadora de Carbono',
                    route: '/calculadora'
                }
            ]
        }
    }
})
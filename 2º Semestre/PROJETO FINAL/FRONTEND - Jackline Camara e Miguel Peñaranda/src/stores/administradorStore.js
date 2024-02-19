import { defineStore } from 'pinia'
import axios from 'axios';

export const useAdministradorStore = defineStore('AdministradorStore', {
    state: ()=>{
        return {
            ListUsers: []
        }
    },
    actions: {
        async getAllUsers(token, id) {
        
        const headers = {
            'user-id': id,
            Authorization: 'Bearer ' + token
        }
            
        axios.get('http://backendprojectapimj.azurewebsites.net/admin', {headers}).then( users => {
            this.ListUsers = users.data;
        })
        },

        async getHistorialUser(token, id) {
            const headers = {
                'user-id': id,
                Authorization: 'Bearer ' + token
            }

            axios.get('http://backendprojectapimj.azurewebsites.net/account/historial', {headers}).then((result =>{
                var historial = result.data.result;
                this.userHistorial = historial;
            }))
        }
    }
    
})
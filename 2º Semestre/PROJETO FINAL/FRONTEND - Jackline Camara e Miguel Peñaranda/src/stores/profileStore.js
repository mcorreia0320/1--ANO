import { defineStore } from 'pinia'
import axios from 'axios';

export const useProfileStore = defineStore('ProfileStore', {
    state: ()=>{
        return {
            userHistorial: [],
            feedingHabitsUser: [],
            transportHabitUser: [],
            homeHabitsUser: []
        }
    },
    actions: {
        async getInfoUser(token, id) {
        
        const headers = {
            'user-id': id,
            Authorization: 'Bearer ' + token
        }
            
        axios.get('http://backendprojectapimj.azurewebsites.net/account', {headers}).then((user)=>{
            var userData = user.data.user;
            var userHabits = userData.user;
            this.feedingHabitsUser = userHabits.feedingHabits;
            this.transportHabitUser = userHabits.user_transports;
            this.homeHabitsUser = userHabits.userHomes 
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
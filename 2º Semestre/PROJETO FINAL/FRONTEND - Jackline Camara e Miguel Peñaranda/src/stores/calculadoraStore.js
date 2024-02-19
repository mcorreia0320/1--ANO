import { defineStore } from 'pinia'
import axios from 'axios';

export const useCalculadoraStore = defineStore('CalculadoraStore', {
    state: ()=>{
        return {
            feedingHabits: [],
            transportHabits: [],
            homeHabits: [],
            listDiets: [],
            listTransports: [],
            betweenValues: []
        }
    },
    actions: {
        async getUserInfo(token, id) {
            axios.get('http://backendprojectapimj.azurewebsites.net/account', {
                headers: {
                    'user-id': id,
                    Authorization: "Bearer " + token
                }
            }).then(userData =>{
                 var feeding = userData.data.user.user.feedingHabits;
                 var transports = userData.data.user.user.user_transports;
                 var home = userData.data.user.user.userHomes
                 this.feedingHabits = feeding;
                 this.transportHabits = transports;
                 this.homeHabits = home;
            })
        },
        async getListDiets(){
            axios.get('http://backendprojectapimj.azurewebsites.net/landingpage/diets').then(diets => {
                this.listDiets = diets.data;
            })
        },
        async getAllTransports() {
            axios.get('http://backendprojectapimj.azurewebsites.net/landingpage/transports').then(transports =>{
                this.listTransports = transports.data;
            })
        },
        async getAllValues() {
            axios.get('http://backendprojectapimj.azurewebsites.net/landingpage/gasValues').then(values =>{
                this.betweenValues = values.data;
            })
        }
    }
})
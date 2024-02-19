import { defineStore } from 'pinia'
import axios from 'axios';

export const useHistoricHomeStore = defineStore('HistoricHomeStore', {
    state: ()=>{
        return {
            array_historial: []
        }
    },
    actions: {
         async getHistorial() {
            axios.get('http://backendprojectapimj.azurewebsites.net/landingpage/historial').then(historial =>{
                this.array_historial = historial.data;
            })
        },
        datetimeToDate(datetime) {
            var date = new Date(datetime)
            var year = date.getFullYear()
            var month = date.getMonth() + 1
            var day = date.getDate()

            if (month < 10) {
                month = '0' + month
            }
            return day + '-' + month + '-' + year
        }
    }
})
import { defineStore } from 'pinia'


export const useShoppingStore = defineStore('shoppingStore', {
      state: ()=>{
        return {
          shopCar:[]
        }
      }
  })

import { defineStore } from 'pinia'
import axios from 'axios';

export const useCategoriasEcologicasStore = defineStore('useCategoriasEcologicasStore', {
    state: ()=>{
        return {
            array_categorias: [],
            indiviualCategory: []
        }
    },
    actions: {
         async getAllCategorias() {
            axios.get('https://umacarbono-default-rtdb.firebaseio.com/acoes.json').then(result =>{
            const data = result.data;
            
            const objNotNulls = data.filter( obj => obj !== null);

            this.array_categorias = objNotNulls;
            })
         },
         async getCategoriasBinding(name) {
            axios.get(`https://umacarbono-default-rtdb.firebaseio.com/acoes.json?orderBy="categoria"&equalTo="${name}"`)
                .then(result =>{
                    var data = result.data;
                    let list = [];
                    for (const obj in data) {
                        if (Object.hasOwnProperty.call(data, obj)) {
                            const element = data[obj];
                            list.push(element);
                        }
                    }
                    this.array_categorias = list;
                })
         },
         async getCategoriaById(id) {
            axios.get(`https://umacarbono-default-rtdb.firebaseio.com/acao/${id}.json`).then(result =>{
                var data = result.data;
                this.indiviualCategory = data;
            })
         }
    }
})
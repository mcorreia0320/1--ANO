import { defineStore } from "pinia";
import { onSnapshot, collection, doc, setDoc } from "firebase/firestore";
import { db } from '@/firebase';

export const useTestemunhoStore = defineStore('testemunhoStore', {
    state: ()=>{
        return{
            array_testemunhos: []
        }
    },
    actions: {
        async getTestemunho() {
            onSnapshot(collection(db, 'testemunhos'), (QuerySnapshot)=> {
                let testemunhos = [];
                QuerySnapshot.forEach((doc)=>{
                    let review = {
                        person_id: doc.id,
                        nome: doc.data().nome,
                        cocktail: doc.data().cocktail,
                        description: doc.data().description
                    }
                    testemunhos.push(review);
                })
                this.array_testemunhos = testemunhos;
            })
        },
        async addTestemunho(nome,cocktail,description) {
            let id = 1;
            
            if (this.array_testemunhos.length != 0) {
                 id = this.array_testemunhos.length + 1;
            }

            await setDoc(doc(db,'testemunhos',"id" + id.toString()), {
                nome: nome,
                cocktail: '"' + cocktail +'"',
                description: description
            })
        }
    }
})
import { defineStore } from 'pinia'
import { collection, onSnapshot, doc, setDoc, deleteDoc, updateDoc } from 'firebase/firestore';
import { db } from '../firebase';

export const useCabulasStore = defineStore('cabulasStore', {
    state: () => {
        return {
            apontamentos: [
                {
                    id: 3,
                    content: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus nec iaculis mauris.'
                },
                {
                    id: 2,
                    content: 'Consectetur adipiscing elit, lorem ipsum dolor sit amet. Amer consectetur elit.'
                },
                {
                    id: 1,
                    content: 'Phasellus nec iaculis mauris. Lorem ipsum dolor sit amet'
                },
            ]
        }
    },
    actions: {
        async addApontamento(newApontamento) {
            let newId = 1;

            if (this.apontamentos.length != 0) {
                newId = this.apontamentos.length + 1;
            }
            
            // this.apontamentos.unshift({
            //     id: newId,
            //     content: newApontamento.trim()
            // })
            await setDoc(doc(db, 'apontamentos', newId.toString()), {
                content: newApontamento
            })
        },
        async deleteApontamento(idToDelete) {
            // this.apontamentos = this.apontamentos.filter(cabula => { return cabula.id !== idToDelete})
            await deleteDoc(doc(db,'apontamentos',idToDelete))
        },
        async updateApontamento(id, content) {
            // let index = this.apontamentos.findIndex(cabula => cabula.id == id);
            // this.apontamentos[index].content = content;
            await updateDoc(doc(db, 'apontamentos', id), {
                content
            })
        },
        async getApontamentos() {
            onSnapshot(collection(db, 'apontamentos'), (QuerySnapshot) => {
                let apontamentos = [];
                QuerySnapshot.forEach((doc) => {
                    let cabula = {
                        id: doc.id,
                        content: doc.data().content
                    }
                    apontamentos.push(cabula)
                })
                this.apontamentos = apontamentos;
            })
        }
    },
    getters: {
        getApontamentoContent: state => {
            return (id) => {
                return state.apontamentos.filter(cabula => cabula.id == id)[0].content
            }
        },
        totalApontamentos: (state) => {
            return state.apontamentos.length
        },
        totalCaracteres: (state) => {
            let contador = 0;

            state.apontamentos.forEach(cabula => {
                contador += cabula.content.length;
            })
            
            return contador
        }
    }
})
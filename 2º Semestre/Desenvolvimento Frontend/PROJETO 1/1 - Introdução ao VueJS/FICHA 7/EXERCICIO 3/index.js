const app = Vue.createApp(
    {
        setup() {
            const number = Vue.ref(0)
            const soma = ()=>{
                number.value++;
            }
            const resta = ()=>{
                number.value--;
            }

            return {
                number,
                resta,
                soma
            }
        }
    }
)
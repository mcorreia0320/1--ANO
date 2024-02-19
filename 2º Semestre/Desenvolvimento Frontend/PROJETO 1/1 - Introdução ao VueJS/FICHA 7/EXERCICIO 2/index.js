const app = Vue.createApp(
    {
        setup() {
            const texto = Vue.ref('Hello World!')
            const reverse_text = ()=>{
                texto.value = texto.value.split("").reverse().join("")
            }

            return {
                texto,
                reverse_text
            }
        }
    }
)
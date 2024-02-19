const app = Vue.createApp(
    {
        setup() {
            const graus = Vue.ref()
            const fahrenheit = Vue.ref()
            const calcular_fahrenheit = (graus) => {
                fahrenheit.value = graus * (9 / 5) + 32
            }
            const calcular_celsius = (fahrenheit) => {
                graus.value = (fahrenheit - 32) * (5/9)
            }
            

            return {
                graus,
                fahrenheit,
                calcular_fahrenheit,
                calcular_celsius
            }
        }
    }
)
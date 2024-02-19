const app = Vue.createApp(
    {
        data() {
            return {
                horas: '',
                minutos: '',
                minutos_2: '',
                segundos: '',
            }
        },
        methods: {
            horasToMinutes(horas) {
                this.minutos = horas * 60
            },
            minuteToSeconds(minutos_2) {
                this.segundos = minutos_2 * 60
            }
        }
    }
);
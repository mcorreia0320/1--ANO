const app = Vue.createApp({
    data() {
        return {
            numero: '',
            result: '',
            win: Math.round(Math.random() * 100),
            tentativas: 1
        }
    },
    methods: {
        verifica(numero) {
            if (this.numero == this.win) {
                this.result = "ACERTASTE!!! com " + this.tentativas + " tentativas "
            }
            else {
                if (this.win > this.numero) {
                    this.result = "Tenta um valor maior"
                }
                else {
                    this.result = "Tenta um valor menor"
                }
                this.tentativas++;
            }
        }

    }
});
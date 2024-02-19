const app = Vue.createApp(
    {
        data() {
            return {
                nome: '',
                cumprimento:'',
            }
        },
        methods:{
            cumprimento_nome(nome) {
                    if (nome == "Marco" || nome == "António") {
                        this.cumprimento = 'Hola Professor ' + nome
                    }
                    else {
                         this.cumprimento = 'Hola ' + nome
                    }
            }
        }
    }
);
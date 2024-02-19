const app = Vue.createApp(
    {
        data() {
            return {
                productName: 'Reserve um cruzeiro para a lua',

                productDescription: 'Navegue até à lua na nossa luxuosa nave espacial e assista aos astronautas trabalhando no espaço.',

                imageSource: './barco_galaxia.png',
                
                styleObject: {
                    'width': '600px'
                }

            }
        }
    },
);
const app = Vue.createApp(
    {
        setup() {
            const playerHealth = Vue.ref(100);
            const enemyHealth = Vue.ref(100);
            const usedCavalry = Vue.ref(false);
            const winner = Vue.ref('');
            const statusGame = Vue.ref('Crónica do Combate')
            const newGame = Vue.ref(false);
            const logMessages = Vue.ref([
                {
                    name: "Portugueses",
                    action: "",
                    value: 0,
                    log__player: true
                },
                {
                    name: "Beligirantes",
                    action: "",
                    value: 0,
                    log__enemy: true
                }
            ])
            const logStart = Vue.ref(false);
            const dano_pt = Vue.ref(0);
            const dano_bg = Vue.ref(0);
            const log__damage = Vue.ref(false);
            const log__heal = Vue.ref(false);
            const anim = Vue.ref(false);
            
            const damage = (min, max) => {
                return Math.floor(Math.random() * (max - min)) + min;
            }
            const attackEnemy = () => {
                dano_pt.value = damage(5, 12);
                enemyHealth.value -= dano_pt.value;
                attackPlayer();
                logMessages.value[0].action = "atacam";
                logMessages.value[0].value = dano_pt.value;
                log__damage.value = true;
                log__heal.value = false;
                logStart.value = true;
                animImg();
                checkWinner();

            }
            const attackPlayer = ()=> {
                dano_bg.value = damage(8, 15);
                playerHealth.value -= dano_bg.value;
                logMessages.value[1].action = "atacam";
                logMessages.value[1].value = dano_bg.value;
                
            }
            const cavalryCharge = () => {
                dano_pt.value = damage(10, 25);
                enemyHealth.value -= dano_pt.value;
                attackPlayer();
                usedCavalry.value = true;
                log__damage.value = true;
                log__heal.value = false;
                logStart.value = true;
                checkWinner();
            }
            const healPlayer = () => {
                if (playerHealth.value >= 90 && playerHealth.value < 100) {
                    dano_pt.value = damage(1, 10);
                    playerHealth.value += dano_pt.value;
                    logMessages.value[0].action = "curam-se";
                    logMessages.value[0].value = dano_pt.value;
                    log__damage.value = true;
                    log__heal.value = true;
                }
                else {
                    dano_pt.value = damage(8, 20);
                    playerHealth.value += dano_pt.value;
                    logMessages.value[0].action = "curam-se";
                    logMessages.value[0].value = dano_pt.value;
                    log__damage.value = true;
                    log__heal.value = true;
                }
                attackPlayer();
                logStart.value = true;
            }
            const surrender = () => {
                statusGame.value = "Game Over";
                playerHealth.value = 0;
                newGame.value = true;
                logStart.value = false;
                checkWinner();
            }
            const checkWinner = () => {
                if (playerHealth.value <= 0 && enemyHealth.value <= 0) {
                    playerHealth.value = 0;
                    enemyHealth.value = 0;
                    logStart.value = false;
                    statusGame.value = "Game Over";
                    winner.value = "EMPATEEEE!!!!";
                    newGame.value = true;
                }
                else if (enemyHealth.value <= 0) {
                     logStart.value = false;
                    statusGame.value = "Game Over";
                    winner.value = "Portugal!!!!! Portugal!!!!! Portugal!!!!!";
                    enemyHealth.value = 0;
                    newGame.value = true;
                }
                else if (playerHealth.value <= 0) {
                    logStart.value = false;
                    statusGame.value = "Game Over";
                    winner.value = "errr... acho que não era isto que estava no livro de historia";
                    playerHealth.value = 0;
                    newGame.value = true;
                }
            }
            const reset = () => {
                newGame.value = false;
                playerHealth.value = 100;
                enemyHealth.value = 100;
                usedCavalry.value = false;
                winner.value = '';
                statusGame.value = "Crónica do Combate";
                logStart.value = false;
            }
            const animImg = () => {
                anim.value = true;
                setTimeout(() => {
                    anim.value = false;
                },3500)
            }


            return {
                playerHealth,
                enemyHealth,
                damage,
                attackEnemy,
                attackPlayer,
                cavalryCharge,
                usedCavalry,
                healPlayer,
                winner,
                checkWinner,
                surrender,
                statusGame,
                newGame,
                reset,
                logMessages,
                logStart,
                dano_pt,
                dano_bg,
                log__damage,
                log__heal,
                anim,
                animImg
            }
        }
    }
) 
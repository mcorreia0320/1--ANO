import { ref, reactive, computed, watch, onMounted, nextTick } from 'vue'

export function useCounter() {
    const counterData = reactive({
        count: 0,
        tittle: 'My Counter'
    })


    const increaseCounter = () => {
    counterData.count++
    }
    const decreaseCounter = () => {
    counterData.count--
    }
    const duplicarCounter = () => {
    counterData.count += 2;
    }
    const dividirCounter = () => {
    counterData.count -= 2;
    }
    const oddOrEven = computed(() => {
    if (counterData.count % 2 == 0) return 'even'
    else return 'odd'
    })

    watch(() => counterData.count, (newCount) => {
    if (newCount == 20) {
        alert('Way go to! You made it to 20!!')
    }
    })
        
        return {
            counterData,
            oddOrEven,
            increaseCounter,
            decreaseCounter,
            duplicarCounter,
            dividirCounter
        }
};
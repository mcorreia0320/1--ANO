import { defineStore } from 'pinia'

export const useCounterStore = defineStore({
  id: 'counter',
  state: () => ({
    count: 0,
    tittle: 'My Counter Tittle'
  }),
  actions: {
    increaseCounter(x) {
      this.count += x;
    },
    decreaseCounter(x) {
      this.count -= x;
    }
  },
  getters: {
    oddOrEven: (state) => {
      if (state.count % 2 == 0) return 'even'
      return 'odd'
    }
  }
})

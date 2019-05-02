import Vue from 'vue'
import App from './App.vue'
import axios from 'axios'
import { library } from '@fortawesome/fontawesome-svg-core'
import { faArrowAltCircleUp as faArrowAltCircleUpSl , 
          faCoffee, faSearch, faSyncAlt, faTimes, faHeart
        } from '@fortawesome/free-solid-svg-icons'
import { faArrowAltCircleUp as faArrowAltCircleUpRg } from '@fortawesome/free-regular-svg-icons'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'


library.add([
    faCoffee, faSearch, faSyncAlt,
    faArrowAltCircleUpSl, faArrowAltCircleUpRg,
    faTimes, faHeart
])
Vue.component('font-awesome-icon', FontAwesomeIcon)
require('../node_modules/natuive/index.js')

var store = {
  state: {
    notification: 'Hello!',
    searchWord: '',
  },
  mutations: {
    setNotificationAction (newValue) {
      this.state.message = newValue
    },
    clearNotificationAction () {
      this.state.message = ''
    },
    setSearchWord (setValue) {
      this.state.searchWord = setValue
    },
    clearSearchWord () {
      this.state.searchWord = ''
    }
  }
}

// global variables
Vue.prototype.$searchFunction = null;
Vue.prototype.$axios = axios;

new Vue({
  el: '#app',
  store: store,
  render: h => h(App)
})

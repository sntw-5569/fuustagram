import Vue from 'vue'
import App from './App.vue'
import axios from 'axios'
import { library } from '@fortawesome/fontawesome-svg-core'
import { faArrowAltCircleUp as faArrowAltCircleUpSl , 
          faCoffee, faSearch, faSyncAlt, faTimes,
          faHeart, faPaw
        } from '@fortawesome/free-solid-svg-icons'
import { faArrowAltCircleUp as faArrowAltCircleUpRg } from '@fortawesome/free-regular-svg-icons'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'


library.add([
    faCoffee, faSearch, faSyncAlt,
    faArrowAltCircleUpSl, faArrowAltCircleUpRg,
    faTimes, faHeart, faPaw
])
Vue.component('font-awesome-icon', FontAwesomeIcon)
require('../node_modules/natuive/index.js')

// global variables
Vue.prototype.$searchFunction = null;
Vue.prototype.$axios = axios;
Vue.prototype.$apiUrl = 'https://10lbouggqi.execute-api.ap-northeast-1.amazonaws.com/prd/fuustagram-api'
Vue.prototype.$apiKey = 'qlNVoIKO986yi9cJ1cSSi7fFMObov0dk3EfCAWdJ'

new Vue({
  el: '#app',
  render: h => h(App)
})

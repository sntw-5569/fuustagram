import Vue from 'vue'
import App from './App.vue'
import { library } from '@fortawesome/fontawesome-svg-core'
import { 
        faArrowAltCircleUp as faArrowAltCircleUpSl , faCoffee, faSearch, faSyncAlt 
      } from '@fortawesome/free-solid-svg-icons'
import { faArrowAltCircleUp as faArrowAltCircleUpRg } from '@fortawesome/free-regular-svg-icons'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'

library.add([faCoffee, faSearch, faSyncAlt, faArrowAltCircleUpSl, faArrowAltCircleUpRg])

Vue.component('font-awesome-icon', FontAwesomeIcon)
require('../node_modules/natuive/index.js')

new Vue({
  el: '#app',
  render: h => h(App)
})

import Vue from 'vue'
import ElementUI from 'element-ui'
import Cookies from 'js-cookie'
import enLang from 'element-ui/lib/locale/lang/en'

import './icons'
import '@/styles/index.scss'
import 'normalize.css/normalize.css'
import App from './App.vue'
import store from './store'
import router from './router'


Vue.use(ElementUI, { size: Cookies.get('size') || 'medium', locale: enLang })

Vue.config.productionTip = false

new Vue({
  el: '#app',
  router,
  store,
  render: h => h(App),
})

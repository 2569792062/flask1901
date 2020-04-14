import Vue from 'vue/dist/vue.js'
import VueMathPlugin from  './VueMathPlugin.js'
import VueX from 'vuex'

Vue.use(VueMathPlugin)
Vue.use(VueX)

var store = new VueX.Store({
    state:{message:'hello'},
    mutations:{}
})

new Vue({
    el:'#app',
    data:{
        item:20
    },
    comments:"",
    store:store
})
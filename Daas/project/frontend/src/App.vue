<template>
  <div id="app">
    <!-- <img src="./assets/logo.png"> -->
    <HeadFirst></HeadFirst>
    <manageLeft></manageLeft>
    <div class="body-right">
      <router-view></router-view>
    </div>
    <x-footer></x-footer>
  </div>
</template>

<script>
// import API from './fetch/api'

import HeadFirst from './components/header.vue';
import manageLeft from "./components/manageLeft.vue";
import XFooter from './components/footer'
export default {
  name: 'App',
   components: { 
    HeadFirst,
    manageLeft,
    XFooter
   },
   mounted() {
      var self = this;
      // self.getData();
  },
  methods:{
    // getData(){
    //   API.getData({name:'li'}).then(res=>{
    //     console.log(res)
    //   })
    // }
  }
}


</script>

<style lang="scss">
 @import "./assets/css/common";
</style>


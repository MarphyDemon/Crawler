<template>
  <div id="app">
    <!-- <img src="./assets/logo.png"> -->
    <router-view/>
  </div>
</template>

<script>
// import API from './fetch/api'
export default {
  name: 'App',
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

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>

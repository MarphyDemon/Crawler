<template>
    <div class="common-header">
      <div class="pull-left logo-wrap">
          <img :src="require('../assets/img/icon.png')">
      </div>
      <div class="right-header">
        <span>{{username}}</span>
        <span class="quit" v-on:click="loginOut">退出</span>
      </div>
    </div>
</template>
<script>
import API from "../fetch/api.js";
import * as common from '../assets/js/common';
export default {
  data() {
    return {
      username: '',
    };
  },
  created() {
      var self = this;
      self.username = common.GetCookie('username');
  },
  methods: {
    loginOut(){
      document.cookie='username'+"="+"";
      this.$router.push({path: '/login'})
    },
  }
};
</script>

<template>
    <div class="body-left">
        <div class="side-nav">
            <ul class="nav-list nav-sass" >
                <li>
                    <ul class="sub-nav">
                        <li>
                            <a class="last-nav" v-bind:class="{'current': currentPath == '/'}" href="/#/">
                                 <i class="shebao-icon">
                                    <img src="../assets/img/money.png" alt="">
                                </i>
                                <span>职业薪酬报告</span>
                            </a>
                            <a class="last-nav" v-bind:class="{'current': currentPath == '/need'}" href="/#/need">
                                 <i class="shebao-icon">
                                    <img src="../assets/img/need.png" alt="">
                                </i> 
                                <span>职业需求报告</span>
                            </a>
                            <a class="last-nav" v-bind:class="{'current': currentPath == '/count'}" href="/#/count">
                                 <i class="shebao-icon">
                                    <img src="../assets/img/count.png" alt="">
                                </i> 
                                <span>统计报告</span>
                            </a>
                        </li>
                    </ul>
                </li>
            </ul>
        </div>
    </div>
</template>
<script>
import API from "../fetch/api.js";
import $ from "jquery";

export default {
  data() {
    return {
    };
  },
  created() {
    var self = this;
  },
  beforeMount() {
  },
  computed: {
    currentPath() {
        return this.$route.path
      },
  },
  mounted() {
  },
  methods: {
    
  }
};
</script>


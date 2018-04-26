<template>
    <div>
        <HeadFirst></HeadFirst>
        <manageLeft></manageLeft>
        <div class="body-right">
            <div class="dass-page" ref="abc">
                <div>
                    <h1>统计报告</h1>
                </div>
                <p-job></p-job>
                <p-city></p-city>
                <p-company></p-company> 
                <div class="download">
                    <div class="download-div">
                        <span v-on:click="downloadReport">下载统计报告</span>
                    </div>
                </div>
                <div class="back-top" v-if="backBtnFlag" v-on:click="backtop">
                    <p>
                        <i class="back-icon"></i>
                    </p>
                    <span>顶部</span>
                </div>
                <div class="download-module" v-if="moduleFlag">
                    <div class="module-title">
                        <span>下载统计报告</span>
                        <img src="../assets/img/close.png" alt="" v-on:click="moduleBack">
                    </div>
                    <div class="module-check">
                        <p>下载当前统计内容</p>
                    </div>
                    <div class="module-font">
                        <p>下载更多统计内容，请联系我，18846183249</p>
                    </div>
                    <div class="module-button">
                        <span class="backBtn" v-on:click="moduleBack">取消</span>
                        <span class="sureBtn" v-on:click="sureDown">确定</span>
                    </div>
                </div>
            </div>
        </div>
        <x-footer></x-footer> 
    </div>
</template>


<script>
import * as common from '../assets/js/common';
import API from "../fetch/api.js";
import canvg from "canvg-browser";
import html2canvas from "html2canvas";
import $ from "jquery";

import PJob from '../components/pJob';
import PCompany from '../components/pCompany';
import PCity from '../components/pCity'

import HeadFirst from '../components/header.vue';
import manageLeft from "../components/manageLeft.vue";
import XFooter from '../components/footer'
export default {
  name: "count",
  components: {
    PJob,
    PCompany,
    PCity,
    HeadFirst,
    manageLeft,
    XFooter
  },
  data() {
    return {
      backBtnFlag: false,
      moduleFlag: false,
      selectmod: false,
    };
  },
  mounted() {
      var self = this;
      if(common.GetCookie('username')){
        $(window).scroll(function() {
            self.scroll =
            document.body.scrollTop ||
            document.documentElement.scrollTop ||
            window.pageYOffset;
            self.backBtnFlag = self.scroll > 700;
        });
      }else{
            console.log("未登录！")
            this.$router.push({path: '/login'})
      }
  },
  methods: {
    downloadReport() {
      var that = this;
      this.moduleFlag = true;
    },
    moduleBack() {
      this.moduleFlag = false;
    },
    sureDown() {
        this.moduleFlag = false;
        this.downFlag = false;
        this.$nextTick(()=>{
            print()
        })
    },
     // 返回顶部按钮
    backtop() {
      var c = document.documentElement.scrollTop || document.body.scrollTop;
      $("html,body").animate(
        {
          scrollTop: (c = 0)
        },
        1000
      );
    },
    
  }
};
</script>

<style lang="scss">
@import "../assets/css/index";
</style>
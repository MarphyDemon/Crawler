<template>
    <div class="dass-page" ref="abc">
        <div>
            <h1>统计报告</h1>
        </div>
        <p-job></p-job>
        <p-company></p-company>
        <p-city></p-city>
        <div v-if="downFlag" class="download">
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
</template>


<script>
import API from "../fetch/api.js";
import canvg from "canvg-browser";
import html2canvas from "html2canvas";
import $ from "jquery";

import PJob from '../components/pJob';
import PCompany from '../components/pCompany';
import PCity from '../components/pCity'
export default {
  name: "count",
  components: {
      PJob,PCompany,PCity
  },
  data() {
    return {
      backBtnFlag: false,
      downFlag: false,
      moduleFlag: false,
    };
  },
  mounted() {
      var self = this;
    $(window).scroll(function() {
        self.scroll =
        document.body.scrollTop ||
        document.documentElement.scrollTop ||
        window.pageYOffset;
        self.backBtnFlag = self.scroll > 700;
    });
  },
  methods: {
    downloadReport() {
      var that = this;
      that.selectmod = true;
    },
    moduleBack() {
      this.moduleFlag = false;
      this.selectmod = false;
    },
    sureDown() {
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
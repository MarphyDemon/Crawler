<template>
    <div>
        <HeadFirst></HeadFirst>
        <manageLeft></manageLeft>
        <div class="body-right">
            <div class="dass-page" ref="abc" v-loading.fullscreen="loading">
                <div>
                    <h1>需求数据分析</h1>
                </div>
                <div class="search-data">
                    <div class="iCountUp">
                        <span class="search-text">本站目前共采集</span>
                        <count :countN = "count" :speed = "speed"></count>
                        <span class="search-text">条数据，清洗</span>
                        <count :countN = "failCount" :speed = "1"></count>
                        <span class="search-text">条无效数据，目前有效数据</span>
                        <count :countN = "vaildCount" :speed = "speed"></count>
                        <span class="search-text">条</span>
                    </div>
                </div>
                <div class="search">
                    <el-input v-model="positionName" placeholder="请输入职业,不能为空！！！"></el-input>
                </div>
                <div class="search-btn">
                    <el-button type="primary" plain v-on:click="getChart">生成薪酬报告</el-button>
                </div>
                
                <six-chart ref="six" v-if="firstChartFlag"></six-chart>
                <seven-chart ref="seven" v-if="firstChartFlag"></seven-chart>
                <eight-chart ref="eight" v-if="firstChartFlag"></eight-chart>
                <nine-chart ref="nine" v-if="firstChartFlag"></nine-chart>

                <div v-if="downFlag" class="download">
                    <div class="download-div">
                        <span v-on:click="downloadReport">下载分析报告</span>
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
                        <span>下载分析报告</span>
                        <img src="../assets/img/close.png" alt="" v-on:click="moduleBack">
                    </div>
                    <div class="module-check">
                        <p>下载当前分析内容</p>
                    </div>
                    <div class="module-font">
                        <p>下载更多分析内容，请联系我，18846183249</p>
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
import $ from "jquery";
import Count from "../components/count-Animate";
import canvg from "canvg-browser";
import html2canvas from "html2canvas";
import SixChart from '../components/sixChart';
import SevenChart from '../components/sevenChart';
import EightChart from '../components/eightChart';
import NineChart from '../components/nineChart';

import HeadFirst from '../components/header.vue';
import manageLeft from "../components/manageLeft.vue";
import XFooter from '../components/footer'
export default {
  name: "index",
  components: {
    Count,
    SixChart,
    SevenChart,
    EightChart,
    NineChart,

    HeadFirst,
    manageLeft,
    XFooter
  },
  data() {
    return {
      positionName: "",
      speed: 111,
      count: 0,
      interNum: 0,
      failCount: 0,
      vaildCount: 0,
      backBtnFlag: false,
      downFlag: false,
      moduleFlag: false,
      firstChartFlag: false,
      loading: false,
      yearList: [2018],
      cityList: [],
      gradeList: ['入门','初级','中级','高级','专家','不限'],
      companySizeList: ['少于15人','10-50人','15-50人','50-150人','150-500人','500-2000人','2000人以上'],
      companyStageList: ['天使轮','A轮','B轮','C轮','D轮','上市公司','不需要融资','未融资'],
      industryList: [],
    };
  },
  mounted() {
      var self = this;
        if(common.GetCookie('username')){
            self.getCount();
            self.getCitylist();
            self.getIndustryList();
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
    getCitylist(){
        var self = this;
        self.loading=true;
        API.getCityList().then(res => {
            if(res.success){
                self.cityList = res.body.citylist
            }else{
                console.log(res.body)
            }
            self.loading=false;
        })
    },
    getIndustryList(){
        var self = this;
        self.loading=true;
        API.getIndustryList().then(res => {
            if(res.success){
                self.industryList = res.body.industryList
            }else{
                console.log(res.body)
            }
            self.loading=false;
        })
    },
    getChart(){
        var self = this;
        self.firstChartFlag=true;
        self.downFlag = true;
        self.$nextTick(() => {
          self.$refs.six.getMonthData();
          self.$refs.seven.getCityNeedData();
          self.$refs.eight.getComSizeNeedData();
          self.$refs.nine.getStageNeedData();
        })

    },
    getCount(){
        var self = this;
        self.loading=true;
        API.getCountData().then(res => {
            if(res.success){
                self.count = res.body.count;
                self.failCount = res.body.failCount;
                self.interNum = res.body.interNum;
                self.vaildCount = res.body.vaildCount;
            }else{
                console.log(res.body);
            }
            self.loading=false;
        })
    },
    downloadReport() {
      var that = this;
      that.moduleFlag = true;
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
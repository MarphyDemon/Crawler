<template>
    <div id="chart" v-loading="loading">
        <div class="city-salary" id="city-salary">
            <div class="city-salary-title">
                <h2>公司融资阶段薪酬分析</h2>
            </div>
            <div class="city-salary-font">
                <div class="city-salary-det">
                    <h3>根据公司融资阶段不同分析不同城市不同职级薪资的高低</h3>
                    <span>为清晰显示数据的基本趋势，以下为市场回归数据</span>
                </div>
                <div class="svg-select">
                  <el-select v-model="stage" placeholder="请选择">
                      <el-option
                          v-for="item in $parent.companyStageList"
                          :key="item"
                          :label="item"
                          :value="item">
                      </el-option>
                  </el-select>
                </div>
                <div class="svg-select">
                  <el-select v-model="city" placeholder="请选择">
                      <el-option
                          v-for="item in $parent.cityList"
                          :key="item"
                          :label="item"
                          :value="item">
                      </el-option>
                  </el-select>
                </div>
            </div>
            <div id="five-container" style="min-width: 800px; height: 400px;"></div>
        </div>
    </div>
    
</template>

<script>
import * as Highcharts from "highcharts";
import API from '../fetch/api'
export default {
  name: "fivechar",
  data() {
    return {
      xAxisData: [],
      series: [],
      city: '北京',
      stage: '天使轮',
      loading: false,
    };
  },
  mounted(){
      var self = this;
      // self.getStageData();
  },
  watch:{
    city(value){
      this.city = value;
      this.getStageData();
    },
    stage(value){
      this.stage = value;
      this.getStageData();
    }
  },
  methods: {
    getStageData(){
        var self=this;
        self.loading=true;
        var option={
            positionName: self.$parent.positionName,
            city: self.city,
            Stage: self.stage
        }
        API.getStageData(option).then(res => {
            if(res.success){
                self.xAxisData = res.body.gradeName;
                self.series = res.body.series;
                self.firstChart()
            }else{
                console.log(res.body)
            }
            self.loading=false;
        })
    },
    firstChart() {
      var self = this;
      // highcharts
      var chartsOne = new Highcharts.Chart("five-container", {
        chart: {
          type: "column"
        },
        title: {
          text: ""
        },
        xAxis: [
          {
            categories: self.xAxisData,
            tickWidth: 0
          }
        ],
        yAxis: {
          title: {
            text:
              "—                                    月收入(¥)                                    —",
            margin: 30,
            style: {
              color: "#AFB7CA"
            },
            y: -10
          },
          labels: {
            formatter: function() {
              var b = parseInt(this.value).toString();
              var len = b.length;
              if (len <= 3) {
                return b;
              }
              var r = len % 3;
              return r > 0
                ? b.slice(0, r) +
                    "," +
                    b
                      .slice(r, len)
                      .match(/\d{3}/g)
                      .join(",")
                : b
                    .slice(r, len)
                    .match(/\d{3}/g)
                    .join(",");
            }
          },
          allowDecimals: false
        },
        legend: {
          enabled: true,
          align: "left", //程度标的目标地位
          verticalAlign: "top", //垂直标的目标地位
          x: 0, //间隔x轴的间隔
          y: 0, //间隔Y轴的间隔
          itemMarginBottom: 20, //图例底部外边距
          symbolHeight: 8,
          symbolWidth: 8,
          itemStyle: {
            color: "#606068",
            fontWeight: "normal"
          }
        },
        navigation: {
          buttonOptions: {
            enabled: false
          }
        },
        credits: { enabled: false }, //隐藏highcharts的站点标志
        tooltip: {
          backgroundColor: "rgba(112,126,161,0.80)", // 背景颜色
          borderColor: "#526084", // 边框颜色
          // borderRadius:2,             // 边框圆角
          borderWidth: 2, // 边框宽度
          shadow: false, // 是否显示阴影
          animation: true, // 是否启用动画效果
          useHTML: true,
          split: true,
          enabled: true,
          style: {
            // 文字内容相关样式
            color: "#7b8390",
            fontSize: "12px",
            textalign: "center"
          },
          backgroundColor: "#485465",
        //   formatter: function(params) {
        //     var relVal = this.points[0].point.index;
        //     var str = "";
        //     var Arr = [];
        //     var value = this.points[0].point.y;
        //     for (var i = 0; i < that.disValueArr.length; i++) {
        //       str =
        //         "<div class='high-font'><p class='first-p'>一线城市高于约</p><p class='percent'>" +
        //         (that.disValueArr[i] * 100).toFixed(2) +
        //         "%</p></div>";
        //       Arr.push(str);
        //     }
        //     if (this.points.length == 1) {
        //       return (
        //         "<div class='high-font'><p class='first-p'>" +
        //         that.sequence +
        //         "城市薪酬50分位</p><p class='percent'>" +
        //         value +
        //         "</p></div>"
        //       );
        //     }
        //     if (relVal % 2 == 0 && this.points.length == 2) {
        //       return Arr[relVal / 2];
        //     }
        //   }
        },
        plotOptions: {
          series: {
            lineWidth: 2,
            events: {
              mouseOver: function() {
                this.options.lineWidth = 1;
              },
              mouseOut: function() {
                this.options.lineWidth = 2;
              }
            },
            hoverseries: {
              lineWidth: 0
            }
          }
        },
        series: self.series
        // series: [
        //   {
        //     name: "一线城市",
        //     type: "area",
        //     stack: "总量1",
        //     connectNulls: true,
        //     color: "#5399F5",
        //     fillOpacity: 0.1,
        //     lineColor: "#5399F5",
        //     marker: {
        //       fillColor: "white",
        //       lineColor: "#5399F5",
        //       lineWidth: 2,
        //       symbol: "circle",
        //       states: {
        //         hover: {
        //           fillColor: "#5399F5",
        //           radius: 4
        //         }
        //       }
        //     },
        //     data: that.firstCityList
        //   },
        //   {
        //     name: "非一线城市",
        //     type: "area",
        //     stack: "总量2",
        //     connectNulls: true,
        //     color: "#FFBC68",
        //     fillOpacity: 0.1,
        //     lineColor: "#FFBC68",
        //     marker: {
        //       fillColor: "white",
        //       lineColor: "#FFBC68",
        //       lineWidth: 2,
        //       symbol: "circle",
        //       states: {
        //         hover: {
        //           fillColor: "#FFBC68",
        //           radius: 4
        //         }
        //       }
        //     },
        //     data: that.otherCityList
        //   }
        // ]
      });
    }
  }
};
</script>


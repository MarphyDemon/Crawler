// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'

Vue.config.productionTip = false
import { Select, Option, OptionGroup, Alert, Loading,Input,Button} from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
Vue.use(Select);
Vue.use(Option);
Vue.use(OptionGroup);
Vue.use(Alert);
Vue.use(Loading);
Vue.use(Input);
Vue.use(Button);

// import * as Highcharts from "highcharts";
// 加载导出模块
// import * as Exporting from "highcharts/modules/exporting";
// // 初始化导出模块
// Exporting(Highcharts);
/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})

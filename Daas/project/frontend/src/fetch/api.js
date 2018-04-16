import axios from 'axios'
import qs from 'qs'

// import * as _ from '../util/tool'
var domain = process.env.NODE_ENV !== 'production'?'':'';
//全局 axios 默认配置
// axios.defaults.timeout = 5000;
axios.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded;charset=UTF-8';
axios.defaults.baseURL = '';

//POST传参序列化
axios.interceptors.request.use((config) => {
     config.headers["X-Requested-With"] = 'XMLHttpRequest'
     
    if(config.method  === 'post'){
        config.data = qs.stringify(config.data);
    }
    return config;
},(error) =>{
    return Promise.reject(error);
});

//返回状态判断
axios.interceptors.response.use((res) =>{
    if (res.headers.loginurl) {
        // alert(res)
        // window.location.replace(res.headers.loginurl);
        // window.location.href ='/sso/user/toLogin';
        window.location.href ='/#/login';
    }
    if(!res.data.success){
        // _.toast(res.data.msg);
        // return Promise.reject(res);
    }
    return res;
}, (error) => {
    if (error.response.headers.loginurl) {
        // window.location.href = error.response.headers.loginurl
        // window.location.href ='/sso/user/toLogin';
        window.location.href ='/#/login';
        // https://dev.xinfushe.com/sso/login
    }
    return Promise.reject(error);
});

export function fetch(url, params) {
    return new Promise((resolve, reject) => {
        axios.post(url, params)
            .then(response => {
                resolve(response.data);
            }, err => {
                reject(err);
            })
            .catch((error) => {
               reject(error)
            })
    })
}
// var domain = '/salary'

export default {
    /**
     * Daas    接口
     */
    // 薪酬数据接口
    // 图一接口    获取根据职级不同得到的薪酬分析数据
    getGradeData(params){
        return fetch(domain + '/api/get_Grade',params);
    },
    // 获取统计数据接口
    getCountData(params){
        return fetch(domain + '/api/get_Count',params);
    },
    getSGradeData(params){
        return fetch(domain + '/api/get_SGrade',params);
    },
    // 图二接口    获取根据城市不同得到的不同职级薪酬分析数据
    getCityData(params){
        return fetch(domain + '/api/get_City',params);
    },
    // 图三接口     获取根据城市以及行业不同得到的不同职级薪酬数据
    getIndustryData(params){
        return fetch(domain + '/api/get_Industry',params)
    },
    // 图四接口     获取根据公司规模城市不同得到的不同职级的薪酬数据
    getComSizeData(params){
        return fetch(domain + '/api/get_ComSize',params)
    },
    // 图五接口     获取根据公司融资阶段不同得到的不同职级的薪酬数据
    getStageData(params){
        return fetch(domain + '/api/get_Stage',params)
    },
    // 需求数据接口
    // 根据月份不同获取需求数据接口
    getMonthData(params){
        return fetch(domain + '/api/get_Month',params)
    },
    //根据月份以及城市不同获取需求数据接口
    getCityNeedData(params){
        return fetch(domain + '/api/get_CityNeed',params)
    },
    // 获取月份以及公司大小不同获取需求数据接口
    getComSizeNeedData(params){
        return fetch(domain + '/api/get_ComNeed',params)
    },
    // 根据公司融资情况以及月份获取需求数据接口
    getStageNeedData(params){
        return fetch(domain + '/api/get_Sneed',params)
    },
    // 统计报告分析
    // 获取职位热度信息  招聘职位数>100
    getPJobData(params){
        return fetch(domain + '/api/get_PJob',params)
    },
    // 获取招聘数量多的公司    招聘数>100
    getPComData(params){
        return fetch(domain + '/api/get_PCom',params)
    },
    // 获取招聘数量多的城市    招聘数>500
    getPCityData(params){
        return fetch(domain + '/api/get_PCity',params)
    },
    getCityList(params){
        return fetch(domain + '/api/get_CList',params)
    },
    getIndustryList(params){
        return fetch(domain + '/api/get_IList',params)
    },
    login(params){
        return fetch(domain + '/api/login',params)
    },
    regist(params){
        return fetch(domain + '/api/regist',params)
    },
    logout(params){
        return fetch(domain + '/api/logout',params)
    },
    index(params){
        return fetch(domain + '/api/index',params)
    },
}


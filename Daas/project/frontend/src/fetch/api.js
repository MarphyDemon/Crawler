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
    getGradeData(params){
        return fetch(domain + '/api/get_Grade',params);
    },
    getCountData(params){
        return fetch(domain + '/api/get_Count',params);
    },
}

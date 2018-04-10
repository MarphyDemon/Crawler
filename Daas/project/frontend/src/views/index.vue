<template>
    <div>
        <input type="text" v-model="job">
        <button v-on:click="getGradeData"></button>
    </div>
</template>

<script>
import API from '../fetch/api'
export default {
    name: 'index',
    data(){
        return{
            job: ''
        }
    },
    mounted(){
        var self = this;
        self.init();
    },
    methods:{
        init(){
            var self = this;
        },
        getGradeData(){
            var self = this;
            var options = {
                jobName: self.job
            }
            API.getGradeData(options).then(res => {
                if(res.success){
                    console.log(res.body.data)
                }else{
                    alert(res.body.msg);
                }
            })
        }
    },
}
</script>

<style>

</style>


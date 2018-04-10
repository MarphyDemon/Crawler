<template>
  <div>
      <button v-on:click="getCount">getCount</button>
  </div>
</template>

<script>
import API from '../fetch/api'
export default {
    name: 'test',
    data(){
        return {

        }
    },
    mounted(){

    },
    methods:{
        getCount(){
            var self = this;
            API.getCountData().then(res => {
                if(res.success){
                    console.log(res.body)
                }else{
                    console.log(res.body)
                }
            })
        }
    }
}
</script>


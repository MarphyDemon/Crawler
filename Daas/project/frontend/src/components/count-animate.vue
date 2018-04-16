<template>
    <div class="count">
        <transition
            v-on:enter="enter">
            <span class="count-span" v-if="show">{{count}}</span>
        </transition>
    </div>
</template>

<script>
export default {
    name: 'countAnimate',
    props: ['countN','speed'],
    data() {
        return {
            show: false,
            count: 0,
            // countN: 3223,
            // speed: 4
        }
    },
    created(){
    },
    mounted(){
        var that = this;
        this.show=true;
    },
    methods:{
        countUp(){
            var that = this;
            var timer;
            // var str = that.countN.toString().length;
            clearInterval(timer);
            timer = setInterval(function(){
                var i = 0;
                var m = parseInt(that.countN%that.speed);
                that.count = that.count + that.speed;
                 if(that.count == (that.countN-m)){
                    that.count = that.count + m;
                    clearInterval(timer);
                }
            },1);
            
        },
        enter(){
            this.countUp();
        }
    }
}
</script>

<style>
.count{
    display: inline-block;
}
.count-span{
    color: #040;
    font-size: 16px;
    font-weight: 500;
}
</style>

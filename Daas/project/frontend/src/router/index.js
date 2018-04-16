import Vue from 'vue'
import Router from 'vue-router'
import index from '@/views/index'
import test from '@/views/test'
import need from '@/views/need'
import count from '@/views/count'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'index',
      component: index
    },
    {
      path: '/test',
      name: 'test',
      component: test
    },
    {
      path: '/need',
      name: 'need',
      component: need
    },
    {
      path: '/count',
      name: 'count',
      component: count
    }
  ]
})

import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Login from '../components/Login.vue'
import NavList from '@/components/NavList.vue'
import TestCase from '@/components/TestCase.vue'
import Report from '@/components/Report.vue'


Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/login',
    name: 'Login',
    component: Login
  },
  {
    path: '/navlist',
    name: 'NavList',
    component: NavList,
    children: [
        {
            path: 'testcase',
            name: 'TestCase',
            component: TestCase,
        },
        {
            path: 'report',
            name: 'Report',
            component: Report,
        }
        
        
    ]
  },
  {
    path: '/about',
    name: 'About',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router

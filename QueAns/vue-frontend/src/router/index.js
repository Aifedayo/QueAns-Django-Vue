import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
   {
     path: '/question/:slug/',
     name: 'question',
  //   // route level code-splitting
  //   // this generates a separate chunk (about.[hash].js) for this route
  //   // which is lazy-loaded when the route is visited.
  component: () => import(/* webpackChunkName: "question" */ '../views/QuestionDetail.vue'),
  props: true,
  },
  {
    path: '/ask/',
    name: 'question-editor',
    component: () => import(/* webpackChunkName: "questioneditor" */ '../views/QuestionEditor.vue'),
 }
]

const router = createRouter({
  history: createWebHistory('/'),
  routes
})

export default router

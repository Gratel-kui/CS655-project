import { createApp } from 'vue'
import App from './App.vue'
import 'bootstrap'

import './assets/main.css'
import '../node_modules/bootstrap/dist/css/bootstrap.min.css';
import DatePicker from 'ant-design-vue';
import 'ant-design-vue/dist/antd.css'; // or 'ant-design-vue/dist/antd.less'




const app = createApp(App)
app.use(DatePicker)
app.mount('#app')

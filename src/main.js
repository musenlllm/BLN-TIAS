import Vue from 'vue';
import App from './App.vue';
// import SvgIcon from '@/components/SvgIcon';
import router from './router';
import ElementUI from 'element-ui';
import VueI18n from 'vue-i18n';
import  'lib-flexible'
import { messages } from './components/common/i18n';
import 'element-ui/lib/theme-chalk/index.css'; // 默认主题
// import './assets/css/theme-green/index.css'; // 浅绿色主题
import './assets/css/icon.css';
import './assets/icon/iconfont.css';
// import './assets/unicodeicon/Uiconfont.css';
// import './assets/svgicon/SVGiconfont.css';
// import './assets/svgicon/iconfont.js';
import './components/common/directives';
import 'babel-polyfill';
// import "@/assets/icon";
import "./assets/icon/index";

// requires and returns all modules that match
const requireAll = requireContext => requireContext.keys().map(requireContext);

// import all svg
const req = require.context('./assets/icon/svg', true, /\.svg$/);
requireAll(req);



Vue.config.productionTip = false;
Vue.use(VueI18n);
Vue.use(ElementUI, {
    size: 'small'
});
const i18n = new VueI18n({
    locale: 'zh',
    messages
});

//使用钩子函数对路由进行权限跳转
router.beforeEach((to, from, next) => {
    document.title = `${to.meta.title} | LDMC-智能文本分析系统`;
    const role = localStorage.getItem('ms_username');
    //展示的首页不需要登陆即可看见
    if (!role && to.path !== '/login' && to.path !== '/entry') {
        next('/entry');
    } else if (to.meta.permission) {
        // 如果是管理员权限则可进入，这里只是简单的模拟管理员权限而已
        role === 'admin' ? next() : next('/403');
    } else {
        // 简单的判断IE10及以下不进入富文本编辑器，该组件不兼容
        if (navigator.userAgent.indexOf('MSIE') > -1 && to.path === '/editor') {
            Vue.prototype.$alert('vue-quill-editor组件不兼容IE10及以下浏览器，请使用更高版本的浏览器查看', '浏览器不兼容通知', {
                confirmButtonText: '确定'
            });
        } else {
            next();
        }
    }
});

new Vue({
    router,
    i18n,
    render: h => h(App)
}).$mount('#app');

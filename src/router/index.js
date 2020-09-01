import Vue from 'vue';
import Router from 'vue-router';

Vue.use(Router);

export default new Router({
    mode: 'history',//Add this to delete "#" in URL
    routes: [
        {
            // Default page is entry page
            path: '/',
            redirect: '/dashboard'
        },
        {
            path: '/',
            component: () => import(/* webpackChunkName: "home" */ '../components/common/Home.vue'),
            meta: { title: '自述文件' },
            children: [
                {
                    path: '/dashboard',
                    component: () => import(/* webpackChunkName: "dashboard" */ '../components/page/Dashboard.vue'),
                    meta: { title: '系统首页' }
                },
                {
                    path: '/relation',
                    component: () => import(/* webpackChunkName: "icon" */ '../components/page/RelationExtraction.vue'),
                    meta: { title: '关系抽取' }
                },
                {
                    path: '/summary',
                    component: () => import(/* webpackChunkName: "table" */ '../components/page/BaseTable.vue'),
                    meta: { title: '自动摘要' }
                },
                {
                    path: '/recognition',
                    component: () => import(/* webpackChunkName: "tabs" */ '../components/page/Tabs.vue'),
                    meta: { title: '实体识别' }
                },

                // 二级三级表单的示范（留着没删
                {
                    path: '/form',
                    component: () => import(/* webpackChunkName: "form" */ '../components/page/BaseForm.vue'),
                    meta: { title: '基本表单' }
                },
                {
                    // 富文本编辑器组件
                    path: '/editor',
                    component: () => import(/* webpackChunkName: "editor" */ '../components/page/VueEditor.vue'),
                    meta: { title: '富文本编辑器' }
                },
                {
                    // markdown组件
                    path: '/markdown',
                    component: () => import(/* webpackChunkName: "markdown" */ '../components/page/Markdown.vue'),
                    meta: { title: 'markdown编辑器' }
                },
                {
                    // 图片上传组件
                    path: '/upload',
                    component: () => import(/* webpackChunkName: "upload" */ '../components/page/Upload.vue'),
                    meta: { title: '文件上传' }
                },
                {
                    // 热点挖掘
                    path: '/hotspot',
                    component: () => import(/* webpackChunkName: "chart" */ '../components/page/BaseCharts.vue'),
                    meta: { title: '热点挖掘' }
                },
                {
                    // 文本主题分类
                    path: '/classification',
                    //component: () => import(/* webpackChunkName: "drag" */ '../components/page/DragList.vue'),
                    //meta: { title: '文本主题分类' }
                    component: () => import(/* webpackChunkName: "drag" */ '../components/page/TopicClassification.vue'),
                    meta: { title: '文本主题分类' }
                },
                // {
                //     // 拖拽Dialog组件
                //     path: '/dialog',
                //     component: () => import(/* webpackChunkName: "dragdialog" */ '../components/page/DragDialog.vue'),
                //     meta: { title: '拖拽弹框' }
                // },
                {
                    // 国际化组件
                    path: '/i18n',
                    component: () => import(/* webpackChunkName: "i18n" */ '../components/page/I18n.vue'),
                    meta: { title: '国际化' }
                },
                {
                    // 权限页面
                    path: '/permission',
                    component: () => import(/* webpackChunkName: "permission" */ '../components/page/Permission.vue'),
                    meta: { title: '权限测试', permission: true }
                },
                {
                    path: '/404',
                    component: () => import(/* webpackChunkName: "404" */ '../components/page/404.vue'),
                    meta: { title: '404' }
                },
                {
                    path: '/403',
                    component: () => import(/* webpackChunkName: "403" */ '../components/page/403.vue'),
                    meta: { title: '403' }
                },
            ]
        },
        {
            path: '/login',
            component: () => import(/* webpackChunkName: "login" */ '../components/page/Login.vue'),
            meta: { title: '登录' }

        },
        {
            path: '*',
            redirect: '/404'
        },
        {
            path: '/entry',
            component: () => import(/* webpackChunkName: "entrypage" */ '../components/page/entrypage.vue'),
            meta: { title: 'LDMC-NLP' }
        }
    ]
});

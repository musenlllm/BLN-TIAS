<template>
    <div class="sidebar">

        <el-menu
            class="sidebar-el-menu"
            :default-active="onRoutes"
            :collapse="collapse"
            :collapse-transition="true"
            text-color="#bfcbd9"
            background-color="#324157"
            active-text-color="#bfcbd9"
            unique-opened
            router
        >
            <template v-for="item in items">
                <!--<template v-if="item.subs">-->
                    <!--<el-submenu :index="item.index" :key="item.index">-->
                        <!--<template slot="title">-->
                            <!--<i :class="item.icon"></i>-->
                            <!--<span slot="title">{{ item.title }}</span>-->
                        <!--</template>-->
                        <!--<template v-for="subItem in item.subs">-->
                            <!--<el-submenu-->
                                <!--v-if="subItem.subs"-->
                                <!--:index="subItem.index"-->
                                <!--:key="subItem.index"-->
                            <!--&gt;-->
                                <!--<template slot="title">{{ subItem.title }}</template>-->
                                <!--<el-menu-item-->
                                    <!--v-for="(threeItem,i) in subItem.subs"-->
                                    <!--:key="i"-->
                                    <!--:index="threeItem.index"-->
                                <!--&gt;{{ threeItem.title }}</el-menu-item>-->
                            <!--</el-submenu>-->
                            <!--<el-menu-item-->
                                <!--v-else-->
                                <!--:index="subItem.index"-->
                                <!--:key="subItem.index"-->
                            <!--&gt;{{ subItem.title }}</el-menu-item>-->
                        <!--</template>-->
                    <!--</el-submenu>-->
                <!--</template>-->
                <!--<template v-else>-->
                    <el-menu-item :index="item.index" :key="item.index">
                        <i :class="item.icon"></i>
                        <span slot="title">{{ item.title }}</span>
                    </el-menu-item>
                <!--</template>-->
            </template>
        </el-menu>


    </div>
</template>

<script>
import bus from '../common/bus';
import ElementUI from 'element-ui';
// import 'element-ui/lib/theme-chalk/index.css'
export default {
    data() {
        return {
            collapse: false,
            items: [
                {
                    icon: 'iconfont icon2_shitishibie',
                    index: 'ner',
                    title: '实体识别'
                },
                {
                    icon: 'iconfont icon3_qingganfenxi',
                    index: 'emotion',
                    title: '情感分析'
                },
                {
                    icon: 'iconfont icon4_guanxichouqu',
                    index: 'relation',
                    title: '关系抽取'
                },
                {
                    icon: 'iconfont icon5_wajue',
                    index: 'hotspot',
                    title: '热点挖掘'
                },
                {
                    icon: 'iconfont icon6_fenlei',
                    index: 'classification',
                    title: '文本主题分类',
                },
                {
                    icon: 'iconfont icon1_wenbenzhaiyao',
                    index: 'summary',
                    title: '自动摘要'
                },
            ],

        };
    },
    computed: {
        onRoutes() {
            return this.$route.path.replace('/', '');
        }
    },
    created() {
        // 通过 Event Bus 进行组件间通信，来折叠侧边栏
        bus.$on('collapse', msg => {
            this.collapse = msg;
            bus.$emit('collapse-content', msg);
        });
    }
};
</script>

<style scoped>
    @import url("//unpkg.com/element-ui@2.13.2/lib/theme-chalk/index.css");

.sidebar {
    /*display: block;*/
    position: absolute;
    left: 0;
    top: 70px;
    bottom: 0;
    overflow-y: scroll;
}
.sidebar::-webkit-scrollbar {
    width: 0;
    display: none;
}
.sidebar-el-menu:not(.el-menu--collapse) {
    width: 250px;
}
.sidebar > ul {
    height: 100%;
}
</style>
<style>
  /*sidebar-el-menu el-menu*/
.el-menu-item.is-active{
    background-color: rgb(38,47,64) !important;
}
</style>

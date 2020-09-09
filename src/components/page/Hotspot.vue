<template>
    <!--<link rel="stylesheet" type="text/css" href="http://at.alicdn.com/t/font_2015036_ral7di9rm4.css">-->
    <div>
        <el-container>
            <el-header style="height: max-content;text-align: center">
                <h1 style="margin-top: 20px;letter-spacing: 10px; font-weight: normal; font-size: 25px; margin-bottom: -1%">
                  热点挖掘
                </h1>

                <!--<h1 style="color: gray;font-size: 30px">热点挖掘</h1>-->

                <!--<el-row style="margin-top: 30px; display: flex; justify-content: center">-->
                    <!--<el-button v-on:click="getData" type="primary" style="background: #242f42; border: 0px">开始分析</el-button>-->
                    <!--<el-button >随机样例</el-button>-->
                <!--</el-row>-->
            </el-header>
            <el-main  style="margin-left: 1px; margin-top: 10px; text-align: center">
                <el-row :gutter="20" >
                    <el-col :span="8">
                        <!--<el-card shadow="always" class="box-card" :body-style="{padding: '0px'}" style="min-height: 458px;font-size: 18px">-->
                      <el-card class="noBorderInput" :body-style="{padding: '0px'}" style="min-height: 466px;border: 0px;border-radius: 0;background-color: #fff;box-shadow: 0 0px 0px 0 rgba(0,0,0,.1);">
                      <div slot="header" class="clearfix" style="font-size: 18px;height: 30px;">

                            <span style="">
                                <!--<link rel="icon" href="../../assets/icon/news.icon" type="image/x-icon">-->
                                <!--<svg class="icon" aria-hidden="true">-->
                                    <!--<use xlink:href="#iconxinwen"></use>-->
                                <!--</svg>-->
                                <i class="iconfont iconxinwen"></i>
                                <!--<i class="ldmcxinwen" style="font-size: 21px;"></i>-->
                                热点新闻
                            </span>
                        </div>
                        <div class="tag-group" style=" display: flex; justify-content: center; flex-direction: row; flex-wrap: wrap;">
                            <el-table
                                    :data="this.hotspotRes.hot_event"
                                    style="width: 100%; text-align: center; "
                                    stripe
                                    :row-class-name="tableRowClassName"
                                    @sort-change="changeSort"
                                    :default-sort="{prop: 'rank', order: 'ascending'}"
                                    :show-overflow-tooltip=true
                                    max-height="400px"
                            >
                                <el-table-column align='center'
                                    header-align="center"
                                    prop="rank"
                                    label="排序"
                                    sortable
                                    :sort-orders="['ascending', 'descending']"
                                    width="80%"
                                >

                                  <div slot-scope="scope" v-if="scope.row.rank<4">

                                    <i class="iconfont iconmingcheng-huobao-t"></i>
                                  </div>
                                  <div slot-scope="scope" v-else>
                                    {{scope.row.rank}}

                                  </div>
                                </el-table-column>
                                <el-table-column align='left'
                                    header-align="center"
                                    prop="event"
                                    label="新闻话题"
                                    :show-overflow-tooltip=true
                                                 width="200%"
                                >
                                      <template slot-scope="scope">

                                        <a :href="scope.row.url" target="_blank" class="buttonText" >{{scope.row.event}}</a>
                                      </template>
                                </el-table-column>
                                <el-table-column align='center'
                                    prop="popularity"
                                    label="阅读量"
                                    :show-overflow-tooltip=true
                                >
                                </el-table-column>
                            </el-table>
                        </div>
                    </el-card>
                    </el-col>
                    <el-col :span="8">
                        <!--<el-card shadow="always" :body-style="{padding: '0px'}" style="min-height: 458px;">-->
                      <el-card class="noBorderInput" :body-style="{padding: '0px'}" style="min-height: 466px;border: 0px;border-radius: 0;background-color: #fff;box-shadow: 0 0px 0px 0 rgba(0,0,0,.1);">
                        <div slot="header" class="clearfix" style="font-size: 18px;height: 30px">
                            <span>

                                <i class="el-icon-chat-line-square" style="font-size: 21px"></i>

                                <!--<i class="iconfont iconhuati"></i>-->
                                热点话题
                            </span>
                        </div>
                        <div class="tag-group" style=" display: flex; justify-content: center; flex-direction: row; flex-wrap: wrap;">
                            <el-table
                                    :data="hotspotRes.hot_topic"
                                    style="width: 100%; text-align: center;"
                                    header-cell-style="font-weight:500"
                                    @sort-change="changeSort"
                                    :default-sort="{prop: 'rank', order: 'ascending'}"
                                    :row-class-name="tableRowClassName"
                                    stripe
                                    :show-overflow-tooltip=true
                                    max-height="400px"
                            >
                                  <el-table-column align='center'
                                    prop="rank"
                                    label="排序"
                                    sortable
                                    :sort-orders="['ascending', 'descending']"
                                    width="80%">
                                      <div slot-scope="scope" v-if="scope.row.rank<4">

                                        <i class="iconfont iconmingcheng-huobao-t"></i>
                                      </div>
                                      <div slot-scope="scope" v-else>
                                        {{scope.row.rank}}

                                  </div>

                                  </el-table-column>
                                  <el-table-column align='left'
                                    header-align="center"
                                    prop="topic"
                                    label="新闻话题"
                                    :show-overflow-tooltip=true
                                  >
                                       <template slot-scope="scope">
                                           <a :href="scope.row.url" target="_blank" class="buttonText" >{{scope.row.topic}}</a>
                                       </template>
                                  </el-table-column>
                                  <el-table-column align='center'
                                    prop="view_number"
                                    label="阅读量"
                                    width="100%"
                                  >
                                  </el-table-column>
                                  <!--<el-table-column-->
                                    <!--prop="url"-->
                                    <!--label="链接"-->
                                    <!--sortable="custom">-->
                                  <!--</el-table-column>-->

                                <!--{{ item.label }}-->
                            </el-table>
                        </div>
                    </el-card>
                    </el-col>
                    <el-col :span="8">
                        <!--<el-card shadow="always" :body-style="{padding: '0px'}" style="min-height: 458px;">-->
                      <el-card class="noBorderInput" :body-style="{padding: '0px'}" style="min-height: 466px;border: 0px;border-radius: 0;background-color: #fff;box-shadow: 0 0px 0px 0 rgba(0,0,0,.1);">
                            <div slot="header" class="clearfix" style="font-size: 18px;height: 30px">
                                <span>
                                    <i class="iconfont iconzengchang1" ></i>
                                <!--</div>-->
                                    最近半小时增长新闻
                                </span>
                            </div>
                            <el-table
                                    :data="this.recent_half_hour_increase_news"
                                    style="width: 100%; text-align: center;"
                                    stripe
                                    @sort-change="changeSort"
                                    :default-sort="{prop: 'publish_time', order: 'descending'}"
                                    :row-class-name="tableRowClassName"
                                    :show-overflow-tooltip=true
                                    max-height="400px"
                            >
                                <el-table-column align='left'
                                    type="index"
                                    header-align="center"
                                    prop="news"
                                    label="新闻话题"
                                     :show-overflow-tooltip=true
                                    width="220%"
                                >
                                    <template slot-scope="scope" v-if="scope.row.url">
                                        <i :href="scope.row.url" class="iconfont iconzuixin" ></i>
                                        <a :href="scope.row.url" target="_blank" class="buttonText" >【{{scope.row.news_type}}】{{scope.row.news}}</a>
                                    </template>
                                </el-table-column>
                                <el-table-column align='center'
                                    prop="publish_time"
                                    label="发布时间"
                                    sortable
                                    :sort-orders="['ascending', 'descending']"
                                     :show-overflow-tooltip=true
                                >
                                    <template slot-scope="scope">
                                          <span >{{scope.row.publish_time}}</span>
                                    </template>
                                </el-table-column>
                            </el-table>
                        </el-card>
                    </el-col>
                </el-row>
                <!--<el-card class="box-card" style="min-height:200px; margin-top: 20px;text-align: center">-->
                <el-card class="noBorderInput" :body-style="{padding: '0px'}" style="text-align: center;margin-top: 30px;min-height: 200px;border: 0px;border-radius: 0;background-color: #fff;box-shadow: 0 0px 0px 0 rgba(0,0,0,.1);">
                    <el-tabs type="card" v-model="activeName" @tab-click="handleClick" style="border: 0px;border-radius: 0">
                        <el-tab-pane label="今日" name="first">

                            <div class="wrap" v-if="isChildUpdate1">
                                <div id = "hot_freq_words1" style="width:100%;min-height:400px;" ></div>
                                <div id = "hot_key_words1" style="width:100%;min-height:400px;"></div>
                                <!--<div>{{this.freq_words2_list}}</div>-->
                            </div>
                        </el-tab-pane>
                        <el-tab-pane label="近七日" name="third">
                            <div class="wrap" v-if="isChildUpdate3">
                                <div id = "hot_freq_words3" style="width:100%;min-height:400px;" ></div>
                                <div id = "hot_key_words3" style="width:100%;min-height:400px;" ></div>
                                <!--<div>{{this.key_words2_list}}</div>-->
                            </div>
                        </el-tab-pane>
                    </el-tabs>

                </el-card>
            <!--</el-main>-->
            <!--<el-main style="text-align: center; margin-top: 10px; ">-->
                <!--<el-card class="box-card" style="min-height: 400px;margin-top: 20px;text-align: center">-->
                <el-card class="noBorderInput" :body-style="{padding: '0px'}" style="text-align: center;margin-top: 30px;min-height: 200px;border: 0px;border-radius: 0;background-color: #fff;box-shadow: 0 0px 0px 0 rgba(0,0,0,.1);">
                    <div slot="header" class="clearfix" style="font-size: 18px">
                        <span>新闻主题分布图</span>
                    </div>
                    <div id="today_hot_distribution" style="width:100%;height:600px;"></div>
                    <div id="week_hot_distribution" style="width:100%;height:600px;">近七日</div>
                  <!--{{this.recent_half_hour_increase_news}}-->
                  <!--{{this.nearly_one_week_news_dis}}-->
                  <!--{{this.nearly_three_days_news_dis}}-->
                  <!--{{this.today_news_dis}}-->
                </el-card>
                <!--<el-card class="box-card" style="min-height: 50px; margin-top: 20px">-->
                <el-card class="noBorderInput" :body-style="{padding: '0px'}" style="text-align: center;margin-top: 30px;min-height: 200px;border: 0px;border-radius: 0;background-color: #fff;box-shadow: 0 0px 0px 0 rgba(0,0,0,.1);">
                    <div slot="header" class="clearfix" style="font-size: 18px">
                        <span>近7日各主题新闻的每天增长数</span>
                    </div>
                    <!--折线图-->
                    <div id="hot_trend" style="width:100%;min-height: 600px;"></div>
                    <!--<div>{{this.hot_statistics}}</div>-->
                </el-card>
            </el-main>

        </el-container>
    </div>
</template>
<script>
import echarts from 'echarts'
import { fetchData } from '../../api/index';
// import resize from "./mixins/resize";
import "echarts-wordcloud/dist/echarts-wordcloud";
import "echarts-wordcloud/dist/echarts-wordcloud.min";
const hotspoturl = "http://49.234.217.110:5000/api/hotspot";

export default {
    name: 'basetable',
    data() {
        return {
            hotspotRes:{},
            items: [],
            // 柱状图
            charts: "",
            view_number: "",
            hot_event:[],
            hot_topic:[],
            freq_words:[],
            freq_words_list:[],
            freq_words1_list:[],
            freq_words2_list:[],
            freq_words3_list:[],
            key_words:[],
            key_words_list:[],
            key_words1_list:[],
            key_words2_list:[],
            entData:[],
            activeName: 'third',
            isChildUpdate1:false,
            isChildUpdate2:false,
            isChildUpdate3:true,
            recent_half_hour_increase_news:[],
            test:{"name":"Liza", "password":"123"},
            hot_statistics:{},
            today_news_distribution:{},
            today_news_dis:[],
            nearly_three_days_news_distribution:{},
            nearly_three_days_news_dis:[],
            nearly_one_week_news_distribution:{},
            nearly_one_week_news_dis:[],

            one_week_time : [],
            news_info:[],
            name:["Domestic国内","World世界","Sports体育","Society社会","History历史","Entertainment娱乐",
                        "Military军事","Government政府","Education教育","Finance经济","Comment评论","Other其他"],
            source:[['topic','今日','近七日'],['Comment评论'],['Domestic国内'], ['Education教育'], ['Entertainment娱乐'], ['Finance经济'],['Government政府'],
              ['History历史'], ['Military军事'], ['Other其他'], ['Society社会'], ['Sports体育'], ['World世界']]
        };
    },
    created() {
    },
    mounted() {
        this.init()
        // this.WordCloud('hot_freq_words');
        this.ResultofHospot();
        this.init()
    },
    methods: {
        handleClick(tab) {
            if(tab.name == "first") {
                this.isChildUpdate1 = true;
                this.getKeyWords("hot_key_words1",this.key_words.today,'今日新闻高影响力词分布词云');
                this.getFreqWords("hot_freq_words1",this.freq_words.today,'今日新闻高频词分布词云');
                this.isChildUpdate2 = false;
                this.isChildUpdate3 = false;
            } else if(tab.name == "third") {
                this.isChildUpdate1 = false;
                this.isChildUpdate2 = false;
                this.isChildUpdate3 = true;
                this.getKeyWords("hot_key_words3",this.key_words.nearly_one_week,'近七日新闻高影响力词分布词云');
                this.getFreqWords("hot_freq_words3",this.freq_words.nearly_one_week,'近七日新闻高频词分布词云');
            }
        },
        // 获取高频词列表
        getFreqWords(id,freq_words,title){
            for(let i = 0; i < 100; i++){
                let obj = {};
                obj.name = freq_words[i].word;
                obj.value = freq_words[i].frequency;
                this.freq_words_list[i] = obj;
            }
            this.$nextTick(() => {
                this.WordCloud(id,this.freq_words_list,title);
            })

        },
        // 获取关键词列表
        getKeyWords(id,key_words,title){
            for(let i = 0; i < 100; i++){
                let obj = {};
                obj.name = key_words[i].word;
                obj.value = key_words[i].influence;
                this.key_words_list[i] = obj;
            }
            this.$nextTick(() => {
                this.WordCloud(id,this.key_words_list,title);
            })

        },
        // 获取热点挖掘的数据
        ResultofHospot(){
            fetch(hotspoturl, {
                method: "POST",
                body: JSON.stringify({
                  // docs: [{
                  //       "id":0,
                  //       "doc":this.summaryText,
                  // }]
                }),
                headers: {
                  "Content-Type": "application/json",
                },
            })
            .then((res) => res.json())
            .catch((error) => console.error("Error:", error))
            .then((response) => {
                this.hotspotRes = response.results;
                // this.hot_event = hotspotRes.hot_event;
                // this.hot_topic = hotspotRes.hot_topic;
                // this.hot_freq_words = hotspotRes.hot_freq_words;
                // this.hot_key_words = hotspotRes.hot_key_words;
                // this.hot_statistics = hotspotRes.hot_statistics;
                this.recent_half_hour_increase_news = this.hotspotRes.hot_statistics.recent_half_hour_increase_news;
                this.today_news_distribution = this.hotspotRes.hot_statistics.today_news_distribution;
                this.today_news_dis = Object.values(this.today_news_distribution);
                this.nearly_one_week_news_distribution = this.hotspotRes.hot_statistics.nearly_one_week_news_distribution;
                this.nearly_one_week_news_dis = Object.values(this.nearly_one_week_news_distribution);
                // console.log(this.today_news_dis);
                //柱状图
                var i = 1

                for(i;i < 13;i++){
                     this.source[i].push(this.today_news_dis[i-1]);
                       // .push(this.nearly_three_days_news_dis[i-1]).push(this.nearly_one_week_news_dis[i-1])
                     this.source[i].push(this.nearly_one_week_news_dis[i-1]);
                     console.log(i)
                     // this.source = a.concat(b);
                }
                setTimeout(()=>{
                    this.drawDistribution("today_hot_distribution",this.today_news_distribution,'今日');
                    // this.drawDistribution("today_hot_distribution",this.nearly_one_week_news_dis,'近七日');
                })
                console.log("success")
                //折线图
                this.hot_statistics = this.hotspotRes.hot_statistics;
                this.news_info[0] = {
                    name: 'Domestic国内',
                    type: 'bar',
                    stack: '总量',
                    // label: {
                    //     show: true,
                    //     position: 'right'
                    // },
                    data: this.hot_statistics.domestic_trend
                },
                this.news_info[1] = {
                    name: 'World世界',
                    type: 'bar',
                    stack: '总量',
                    // label: {
                    //     show: true,
                    //     position: 'right'
                    // },
                    data: this.hot_statistics.world_trend
                },
                this.news_info[2] = {
                    name: 'Sports体育',
                    type: 'bar',
                    stack: '总量',
                    // label: {
                    //     show: true,
                    //     position: 'right'
                    // },
                    data: this.hot_statistics.sports_trend.map((item, index, arr)=> item * -1 )
                },
                this.news_info[3] = {
                    name: 'Society社会',
                    type: 'bar',
                    stack: '总量',
                    // label: {
                    //     show: true,
                    //     position: 'right'
                    // },
                    data: this.hot_statistics.society_trend
                },
                this.news_info[4] = {
                    name: 'History历史',
                    type: 'bar',
                    stack: '总量',
                    // label: {
                    //     show: true,
                    //     position: 'right'
                    // },
                    data: this.hot_statistics.history_trend.map((item, index, arr)=> item * -1 )
                },
                this.news_info[5] = {
                    name: 'Entertainment娱乐',
                    type: 'bar',
                    stack: '总量',
                    // label: {
                    //     show: true,
                    //     position: 'right'
                    // },
                    data: this.hot_statistics.entertainment_trend.map((item, index, arr)=> item * -1 )
                },
                this.news_info[6] = {
                    name: 'Military军事',
                    type: 'bar',
                    stack: '总量',
                    // label: {
                    //     show: true,
                    //     position: 'right'
                    // },
                    data: this.hot_statistics.military_trend.map((item, index, arr)=> item * -1 )
                },
                this.news_info[7] = {
                    name: 'Government政府',
                    type: 'bar',
                    stack: '总量',
                    // label: {
                    //     show: true,
                    //     position: 'right'
                    // },
                    data: this.hot_statistics.government_trend.map((item, index, arr)=> item * -1 )
                },
                this.news_info[8] = {
                    name: 'Education教育',
                    type: 'bar',
                    stack: '总量',
                    // label: {
                    //     show: true,
                    //     position: 'right'
                    // },
                    data: this.hot_statistics.education_trend.map((item, index, arr)=> item * -1 )
                },
                this.news_info[9] = {
                    name: 'Finance经济',
                    type: 'bar',
                    stack: '总量',
                    // label: {
                    //     show: true,
                    //     position: 'right'
                    // },
                    data: this.hot_statistics.finance_trend
                },
                this.news_info[10] = {
                    name: 'Comment评论',
                    type: 'bar',
                    stack: '总量',
                    // label: {
                    //     show: true,
                    //     position: 'right'
                    // },
                    data: this.hot_statistics.comment_trend.map((item, index, arr)=> item * -1 )
                },
                this.news_info[11] = {
                    name: 'Other其他',
                    type: 'bar',
                    stack: '总量',
                    // label: {
                    //     show: true,
                    //     position: 'right'
                    // },
                    data: this.hot_statistics.other_trend
                },
                this.getDay();
                this.drawTrend("hot_trend",this.one_week_time.reverse(),this.news_info);
                //词云1
                this.freq_words = this.hotspotRes.hot_freq_words;
                // var freq_words1 = this.freq_words.today;
                // var freq_words2 = this.freq_words.nearly_three_days;
                var freq_words3 = this.freq_words.nearly_one_week;
                // this.getFreqWords("hot_freq_words1",freq_words1,'今日新闻高频词分布词云');
                // this.getFreqWords("hot_freq_words2",freq_words2,'近三日新闻高频词分布词云');
                this.getFreqWords("hot_freq_words3",freq_words3,'近七日新闻高频词分布词云');

                //词云2
                this.key_words = this.hotspotRes.hot_key_words;
                // var key_words1 = this.key_words.today;
                // var key_words2 = this.key_words.nearly_three_days;
                var key_words3 = this.key_words.nearly_one_week;
                // this.getKeyWords("hot_key_words1",key_words1,'今日新闻高影响力词分布词云');
                // this.getKeyWords("hot_key_words2",key_words2,'近三日新闻高影响力词分布词云');
                this.getKeyWords("hot_key_words3",key_words3,'近七日新闻高影响力词分布词云');
                // for(let i = 0; i < 100; i++){
                //     let obj = {};
                //     obj.name = key_words2[i].word;
                //     obj.value = key_words2[i].influence;
                //     this.key_words2_list[i] = obj;
                // }
                // this.$nextTick(() => {
                //     this.WordCloud("hot_key_words2",this.key_words2_list,'近三日新闻高影响力词分布词云');
                // })



                // }
                // this.recent_half_hour_increase_news = hotspotRes.hot_statistics.nearly_one_week_news_distribution
            })
        },
        //词云
        WordCloud(id,words,title) {
            this.chart = echarts.init(document.getElementById(id));
            const option = {
                colorArr:['#fda67e', '#81cacc', '#cca8ba', "#88cc81", "#82a0c5", '#fddb7e', '#735BA1', '#bda29a', '#6e7074', '#546570', '#c4ccd3'],
                title: {
                    text: title,
                    x: "center",
                    padding:9,
                    top:'0%',//各个方向的内边距，默认是5，可以自行设置
                    textStyle:{//标题内容的样式
                        fontStyle:'normal',//主标题文字字体风格，默认normal，有italic(斜体),oblique(斜体)
                        fontWeight:"normal",//可选normal(正常)，bold(加粗)，bolder(加粗)，lighter(变细)，100|200|300|400|500...
                        fontSize:15//主题文字字体大小，默认为18px
                      },

                },
                tooltip: {
                    trigger: 'item',
                },
                backgroundColor: "#fff",
                grid:{
                    left:'5%',
                    right:'8%',
                    bottom:'10%',
                    top:'19%',
                    containLabel:true
                },

                series: [{
                    type: "wordCloud",
                    //用来调整词之间的距离
                    gridSize: 5,
                    //用来调整字的大小范围
                    // Text size range which the value in data will be mapped to.
                    // Default to have minimum 12px and maximum 60px size.
                    sizeRange: [14, 60],
                    // Text rotation range and step in degree. Text will be rotated randomly in range [-90,                                                                             90] by rotationStep 45
                    //用来调整词的旋转方向，，[0,0]--代表着没有角度，也就是词为水平方向，需要设置角度参考注释内容
                    rotationRange: [-40, 0, 45, 90],
                    // rotationRange: [ 0,90],
                    // rotationRange: [0, 0],
                    //随机生成字体颜色
                    // maskImage: maskImage,
                    textStyle: {
                      normal: {
                        color: function() {
                            var colorArr = ['#7db5e2', '#81cacc', '#cca8ba', "#7EBF50", "#82a0c5", '#fddb7e', '#bda29a', '#d2a59a', '#909399', '#c4ccd3','#67C23A'];
                            var flag = parseInt(Math.random() * 10);
                            return (colorArr[flag]);
                                // colorArr[flag]
                            // };
                          // return (
                          //   "rgb(" +
                          //   Math.round(Math.random() * 10) +
                          //   ", " +
                          //   Math.round(Math.random() * 248) +
                          //   ", " +
                          //   Math.round(Math.random() * 255) +
                          //   ")"
                          // );
                        }
                      }
                    },
                    //位置相关设置
                    // Folllowing left/top/width/height/right/bottom are used for positioning the word cloud
                    // Default to be put in the center and has 75% x 80% size.
                    left: "center",
                    top: "center",
                    right: null,
                    bottom: null,
                    width: "200%",
                    height: "200%",
                    //数据
                    data: words
                  }
                ]
            };
            this.chart.setOption(option);
            // window.addEventListener("resize", function() {
            //   this.chart.resize()
            // })
            window.addEventListener("resize", () => {
                this.chart.resize();
            });
        },
        //场景分布柱状图
        drawDistribution(id,data1,date) {
            // 基于准备好的dom，初始化echarts实例
            this.chart = echarts.init(document.getElementById(id));
            // 指定图表的配置项和数据
            var option = {
                // color:['#E47470','#7EBF50','#589EF8'],
                // color:['rgb(210,100,93)','rgb(228,116,79)','rgb(242,176,110)','rgb(249,224,150)','rgb(255,254,198)','rgb(233,244,163)','rgb(181,219,169)','rgb(156,218,174)','rgb(125,191,166)','rgb(93,178,155)','rgb(74,134,183)','rgb(125,169,185)'],
                color:['rgb(227,158,156)','rgb(224,108,146)','rgb(197,151,212)','rgb(175,159,215)','rgb(160,169,214)','rgb(233,244,163)','rgb(181,219,169)','rgb(156,218,174)','rgb(125,191,166)','rgb(93,178,155)','rgb(74,144,173)','rgb(126,180,225)'].reverse(),
                tooltip: {
                    trigger: 'axis',
                    axisPointer: {
                        type: 'shadow'
                    }
                },
                title: {
                    // text: '主题分布图',
                    textAlign: "center",
                    left:'50%',//各个方向的内边距，默认是5，可以自行设置
                },
                dataset: {
                    source: this.source
                },
                grid:{
                    top:'10%',
                    // left:'5%',
                    right:'60%',
                    bottom:'40%',
                    // containLabel:true
                },
                legend: {
                  data:this.source[0],
                    // data: [
                    //     {
                    //         name: '今日',
                    //         icon: '',
                    //         textStyle: {
                    //           fontSize:15,
                    //           // color: 'red',  // 单独设置某一个图列的颜色
                    //           // backgroundColor: '#fff' // 单独设置某一个图列的字体背景色
                    //         }
                    //     },
                    //     {
                    //         name: '近三日',
                    //         icon: '',
                    //         textStyle: {
                    //           fontSize:15,
                    //           // color: 'red',  // 单独设置某一个图列的颜色
                    //           // backgroundColor: '#fff' // 单独设置某一个图列的字体背景色
                    //         }
                    //     },
                    //     {
                    //         name: '近七日',
                    //         icon: '',
                    //         textStyle: {
                    //           fontSize:15,
                    //           // color: 'red',  // 单独设置某一个图列的颜色
                    //           // backgroundColor: '#fff' // 单独设置某一个图列的字体背景色
                    //         }
                    //     },
                    // ],
                    // textStyle: {
                    //
                    //     fontSize:15
                    // },
                    // right: 100,
                },

                yAxis: {
                    type: 'category',
                    name: '主题',
                    nameTextStyle:{
                        fontSize:'10',
                    },
                    axisLabel: {
                        interval:0,
                        fontSize:'10',
                        fontFamily:'微软雅黑',
                    },
                    data:['Comment评论', 'Domestic国内', 'Education教育', 'Entertainment娱乐', 'Finance经济','Government政府', 'History历史', 'Military军事', 'Other其他', 'Society社会', 'Sports体育', 'World世界']
                },
                xAxis: {
                    type: 'value',
                    name: '数量',
                    nameTextStyle:{
                        fontSize:'10',
                    },
                    axisLabel: {
                        fontSize:'10',
                        fontFamily:'微软雅黑',
                        marginTop:'35px',
                        show:true,
                    },
                },
                series: [
                    {
                        name: date,
                        type: "bar",
                        data: Object.values(data1),
                    },
                    {
                        type: 'pie',
                        id: 'pie',
                        radius: [20, 110],
                        //
                        // roseType: 'radius',
                        roseType: 'area',
                        left:'40%',
                        bottom:'30%',
                        label: {
                            formatter: '{@date}'+':'+ '{@今日}({d}%)'
                        },
                        // data: [Object.keys(data1),Object.values(data1)],
                        encode: {
                            itemName: date,
                            value: '今日',
                            tooltip: '今日'
                        }


                    }
                ]
            };
            this.chart.on('updateAxisPointer', function (event) {
                var xAxisInfo = event.axesInfo[0];
                if (xAxisInfo) {
                    var dimension = xAxisInfo.value + 1;
                    this.chart.setOption({
                        series: {
                            id: 'pie',
                            label: {
                                formatter: '{b}: {@[' + dimension + ']} ({d}%)'
                            },
                            encode: {
                                value: dimension,
                                tooltip: dimension
                            }
                        }
                    });
                }
            });
            this.chart.setOption(option);
            // window.addEventListener("resize", function() {
            //   this.chart.resize()
            // })
            // setTimeout(function () {
            //     var width = $('#aside').width();
            //     if(width=='100'|| width=='60'){ //一定要加定时器，然后判断宽度是展开或者收起的时候再去调用echarts提供的resize()方法
            //         this.chart.resize();
            //     }
            //  },200);
             window.addEventListener("resize", function() {
                this.chart.resize();
            });
        },
        //获取近七日日期 step_1
        getBeforeDate(n) {
            var n = n;
            var d = new Date();
            var year = d.getFullYear();
            var mon = d.getMonth() + 1;
            var day = d.getDate();
            if(day >= n) {
                if(mon > 1) {
                    mon = mon - 1;
                } else {
                    year = year - 1;
                    mon = 12;
                }
            }
            d.setDate(d.getDate() + n); //很重要，+n取得是前一天的时间
            year = d.getFullYear();
            mon = d.getMonth() + 1;
            day = d.getDate();
            var s = (mon < 10 ? ('0' + mon) : mon) + "-" + (day < 10 ? ('0' + day) : day);
            return s;
        },
        //获取近七日日期 step_2
        getDay(){
            for(var i = 0; i > -7; i--){
                this.one_week_time.push(this.getBeforeDate(i));
            }
        },
        //近七日主题新闻每日增长数
        drawTrend(id,date_arr,news_info){
            // 基于准备好的dom，初始化echarts实例
            this.chart = echarts.init(document.getElementById(id));
            // 指定图表的配置项和数据
            var option = {
                // color : ['#7db5e2', '#81cacc', '#cca8ba', "#7EBF50", "#82a0c5", '#fddb7e', '#bda29a', '#d2a59a', '#7f9979', '#c4ccd3','#5F9EA0','#a498d6'],
                color:['rgb(210,100,93)','rgb(228,116,79)','rgb(242,176,110)','rgb(249,224,150)','rgb(255,254,198)','rgb(233,244,163)','rgb(181,219,169)','rgb(156,218,174)','rgb(125,191,166)','rgb(93,178,155)','rgb(74,134,183)','rgb(125,169,185)'].reverse(),
                // color:['rgb(215,121,118)','rgb(224,108,146)','rgb(175,110,195)','rgb(249,224,150)','rgb(255,254,198)','rgb(233,244,163)','rgb(181,219,169)','rgb(156,218,174)','rgb(125,191,166)','rgb(93,178,155)','rgb(74,134,183)','rgb(125,169,185)'].reverse(),
                // color:['rgb(227,158,156)','rgb(224,108,146)','rgb(197,151,212)','rgb(175,159,215)','rgb(160,169,214)','rgb(233,244,163)','rgb(181,219,169)','rgb(156,218,174)','rgb(125,191,166)','rgb(93,178,155)','rgb(74,144,173)','rgb(126,180,225)'].reverse(),
                // color:['#DC143C','#FFB6C1','#BA55D3','#483D8B','#1E90FF','#5F9EA0','#90EE90','#556B2F','#808000','#FFD700','#FFA500','#8B4513'],
                //标题
                tooltip: {
                      trigger: 'item',
                      axisPointer: {            // 坐标轴指示器，坐标轴触发有效
                        type: 'shadow'        // 默认为直线，可选为：'line' | 'shadow'
                      },
                      formatter: function (params, ticket, callback) {
                          var res = params.name+'</br>'+params.marker+params.seriesName+' : '+Math.abs(params.value)
                          return res;
                         // console.log(params)
                         // var res = params[0].name ;
                         //
                         // for (var i = 0, l = params.length; i < l; i++) {
                         //     res += '<br/>' + params[i].marker+params[i].seriesName + ' : ' + Math.abs(params[i].value) ;
                         //
                         // }
                         // setTimeout(function () {
                         //     // 仅为了模拟异步回调
                         //     callback(ticket, res);
                         // }, 10)
                         // return res;
                      },

                },
                grid: {
                    top:'10%',
                    left: '3%',
                    right: '12%',
                    bottom: '3%',
                    containLabel: true
                },
                //工具箱
                //保存图片
                toolbox:{
                    show:true,
                    feature:{
                        saveAsImage:{
                            show:true
                        }
                    }
                },
                //图例-每一条数据的名字叫销量
                legend:{
                    data:this.name,
                    textStyle: {
                      //legend字体颜色
                    },
                    orient: 'vertical',
                    right: '-0%',
                    top: '8%',
                    bottom: 20,
                },
                //x轴没有显式设置，根据值自动生成x轴
                xAxis:{
                    type: 'value',
                    name: '增长数量',
                    nameTextStyle:{
                        fontSize:'15',
                        padding:10
                    },
                    axisLabel: {
                        formatter:function(value)
                        {
                            return Math.abs(value)
                        },
                        fontSize: '15',
                        fontFamily: '微软雅黑',
                        marginTop: '35px',
                        show: true,
                    },
                },
                //y轴
                yAxis:{
                    type: 'category',
                    name: '日期',
                    nameTextStyle:{
                        fontSize:'15',
                    },
                    data: date_arr,
                    axisLabel: {

                        fontSize:'15',
                        fontFamily:'微软雅黑',
                        marginTop:'35px',
                        show:true,
                    },
                },

                //数据-data是最终要显示的数据

                /*  [+] Here I need Initial the series arr */
                series: news_info
            };
            this.chart.setOption(option);
            // window.addEventListener("resize", () => {
            //     this.chart.resize();
            // });
            window.onresize = () => {
                this.chart.resize();
                // this.percentCharts.resize();
            }
        },

        init() {
           const self = this;//因为箭头函数会改变this指向，指向windows。所以先把this保存
           setTimeout(() => {
              window.addEventListener('resize', function() {
                  self.chart = self.$echarts.init(self.$refs.Echart);
                  self.chart.resize();
              })
           },10)
         },
        // tableRowClassName({row, rowIndex}) {
        //     if (rowIndex === 0) {
        //       return 'warning-row';
        //     } else if (rowIndex === 1) {
        //       return 'warning-row';
        //     }else if (rowIndex === 2) {
        //       return 'warning-row';
        //     }
        //     return '';
        // }
    }
};
</script>

<style scoped type="text/css">
    @import url("//unpkg.com/element-ui@2.13.2/lib/theme-chalk/index.css");
    @import '../../assets/css/icon.css';

    .el-header, .el-footer {
        font-size: 20px;
        color: black;
        text-align: center;
        line-height: 60px;
    }
    .res-textarea/deep/ {
        color: black; margin-top: 30px;box-shadow: 0 2px 4px rgba(0, 0, 0, .12), 0 0 6px rgba(0, 0, 0, .04)
    }
    .el-card/deep/ {
        box-shadow: 0 8px 12px 0 rgba(0,0,0,.1);
    }
    .el-table/deep/.tableStyle/deep/{
        background-color: #1989fa!important;
        color:#fff;
        font-weight:300;
    }
    .buttonText{
        color: #303133;
        text-align:left;
    }
    /*.clearfix{*/
        /*display: flex;*/
        /*justify-content: center;*/
        /*align:middle;*/
    /*}*/
    .wrap{
        display: flex;
        height: 100%;
        justify-content: center;
        align:middle;
    }
    a:link {color:#000000;}      /* 未访问链接*/
    a:visited {color:#000000;}  /* 已访问链接 */
    a:hover {color: #589ef8;}  /* 鼠标移动到链接上 */
    a:active {color: #589ef8;}  /* 鼠标点击时 */
    .chartsClass {
      padding-left: 1.2rem;
    }
</style>

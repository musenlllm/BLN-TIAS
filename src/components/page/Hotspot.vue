<template>
    <div>
        <el-container>
            <el-header style="height: max-content;text-align: center">
                <h1 style="color: gray">热点挖掘</h1>
                <!--<el-row style="margin-top: 30px; display: flex; justify-content: center">-->
                    <!--<el-button v-on:click="getData" type="primary" style="background: #242f42; border: 0px">开始分析</el-button>-->
                    <!--<el-button >随机样例</el-button>-->
                <!--</el-row>-->
            </el-header>
            <el-main  style="margin-left: 1px; margin-top: 10px; text-align: center">
                <el-row :gutter="20" >
                    <el-col :span="8">
                        <el-card shadow="hover" class="box-card" :body-style="{padding: '0px'}" style="min-height: 458px;">
                        <div slot="header" class="clearfix">
                            <span>热点新闻</span>
                        </div>
                        <div class="tag-group" style=" display: flex; justify-content: center; flex-direction: row; flex-wrap: wrap;">
                            <el-table
                                    :data="this.hotspotRes.hot_event"
                                    style="width: 100%; text-align: center"
                                    stripe
                                    :row-class-name="tableRowClassName"
                                    @sort-change="changeSort"
                                    :default-sort="{prop: 'rank', order: 'ascending'}"
                                    :show-overflow-tooltip=true
                                    max-height="400px"
                            >
                                <el-table-column align='center'
                                    prop="rank"
                                    label="排序"
                                    sortable
                                    :sort-orders="['ascending', 'descending']"
                                    width="100%"
                                >
                                </el-table-column>
                                <el-table-column align='center'
                                    prop="event"
                                    label="链接和话题"
                                    :show-overflow-tooltip=true
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
                        <el-card shadow="hover" :body-style="{padding: '0px'}" style="min-height: 458px;">
                        <div slot="header" class="clearfix">
                            <span>热烈讨论话题</span>
                        </div>
                        <div class="tag-group" style=" display: flex; justify-content: center; flex-direction: row; flex-wrap: wrap;">
                            <el-table
                                    :data="hotspotRes.hot_topic"
                                    style="width: 100%; text-align: center"
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
                                    width="100%">

                                  </el-table-column>
                                  <el-table-column align='center'
                                    prop="topic"
                                    label="话题和链接"
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
                        <el-card shadow="hover" :body-style="{padding: '0px'}" style="min-height: 458px;">
                            <div slot="header" class="clearfix">
                                <span>最近半小时增长新闻</span>
                            </div>
                            <el-table
                                    :data="this.recent_half_hour_increase_news"
                                    style="width: 100%; text-align: center"
                                    stripe
                                    @sort-change="changeSort"
                                    :default-sort="{prop: 'publish_time', order: 'ascending'}"
                                    :row-class-name="tableRowClassName"
                                    :show-overflow-tooltip=true
                                    max-height="400px"
                            >
                                <el-table-column align='center'
                                    prop="news"
                                    label="链接和话题"
                                     :show-overflow-tooltip=true
                                >
                                    <template slot-scope="scope">
                                      <a :href="scope.row.url" target="_blank" class="buttonText" >【{{scope.row.news_type}}】{{scope.row.news}}</a>
                                    </template>
                                </el-table-column>
                                <el-table-column align='center'
                                    prop="publish_time"
                                    label="发布时间"
                                    sortable
                                    :sort-orders="['ascending', 'descending']"
                                >
                                    <template slot-scope="scope">
                                          <span >发布时间：{{scope.row.publish_time}}</span>
                                    </template>
                                </el-table-column>
                            </el-table>
                        </el-card>
                    </el-col>
                </el-row>
                              <!--<el-table-column align='center'-->
                                <!--prop="url"-->
                                <!--label="链接和话题"-->
                              <!--&gt;-->
                                  <!--<template slot-scope="scope">-->
                                    <!--<a :href="scope.row.url" target="_blank" class="buttonText">{{scope.row.event}}</a>-->
                                  <!--</template>-->
                              <!--</el-table-column>-->
                                <!--{{ item.label }}-->
                        <!--<div>{{hotspotRes}}</div>-->
                        <!--<div class="tag-group" style="margin-top: 0; display: flex; flex-direction: row; flex-wrap: wrap;">-->
                            <!--<span class="tag-group__title">Dark</span>-->
                            <!--<el-tag style="margin-bottom: 10px; margin-right: 5px; border-radius: 4px; font-size: 15px; border: 0"-->
                                    <!--v-for="item in items"-->
                                    <!--:key="item.label"-->
                                    <!--:type="item.type"-->
                                    <!--:color="item.color"-->
                                    <!--size="medium"-->
                                    <!--effect="dark">-->
                                <!--{{ item.label }}-->
                            <!--</el-tag>-->
                        <!--</div>-->
                <el-card class="box-card" style="min-height:200px; margin-top: 20px;text-align: center">
                    <!--<div slot="header" class="clearfix">-->
                        <!--<span>新闻高频词</span>-->
                    <!--</div>-->
                    <el-tabs v-model="activeName" @tab-click="handleClick">
                        <el-tab-pane label="今日" name="first" lazy>
                            今日
                            <div class="wrap">
                                <div id = "hot_freq_words1" style="margin: 4%">新闻高频词</div>
                                <div id = "hot_key_words1" style="margin: 4%">新闻高影响力词</div>
                                <!--<div>{{this.freq_words2_list}}</div>-->
                            </div>
                        </el-tab-pane>
                        <el-tab-pane label="近三日" name="second">
                            <div class="wrap">
                                <div id = "hot_freq_words2" style="width:100%;min-height:400px;" ></div>
                                <!--<div id="hot_distribution" style="width:100%;min-height:400px;"></div>-->
                                <div id = "hot_key_words2" style="width:100%;min-height:400px;" ></div>
                                <!--<div>{{this.key_words2_list}}</div>-->
                            </div>
                        </el-tab-pane>
                        <el-tab-pane label="近七日" name="third" lazy>
                            近七日
                            <div class="wrap">
                                <div id = "hot_freq_words3" style="width:100%;min-height:400px;" v-if="'third' === activeName"></div>
                                <div id = "hot_key_words3" style="width:100%;min-height:400px;"></div>
                                <!--<div>{{this.key_words2_list}}</div>-->

                            </div>
                        </el-tab-pane>
                    </el-tabs>
                    <!--<div :id="id" :class="className" :style="{ height:height,width:width }" />-->
                     <!--<el-table-->
                            <!--:data="hotspotRes.hot_key_words.today"-->
                            <!--style="width: 100%; text-align: center"-->
                            <!--@sort-change="changeSort"-->
                            <!--:default-sort="{prop: 'rank', order: 'ascending'}"-->
                            <!--:row-class-name="tableRowClassName"-->
                            <!--border-->
                            <!--max-height="500px"-->
                     <!--&gt;-->
                          <!--<el-table-column align='center'-->
                            <!--prop="rank"-->
                            <!--label="排序"-->
                            <!--sortable-->
                            <!--:sort-orders="['ascending', 'descending']"-->
                            <!--&gt;-->
                          <!--</el-table-column>-->
                          <!--<el-table-column align='center'-->
                            <!--prop="word"-->
                            <!--label="关键词"-->
                            <!--&gt;-->
                          <!--</el-table-column>-->
                          <!--<el-table-column align='center'-->
                            <!--prop="influence"-->
                            <!--label="影响力"-->
                          <!--&gt;-->
                          <!--</el-table-column>-->
                          <!--&lt;!&ndash;<el-table-column&ndash;&gt;-->
                            <!--&lt;!&ndash;prop="url"&ndash;&gt;-->
                            <!--&lt;!&ndash;label="链接"&ndash;&gt;-->
                            <!--&lt;!&ndash;sortable="custom">&ndash;&gt;-->
                          <!--&lt;!&ndash;</el-table-column>&ndash;&gt;-->
                            <!--&lt;!&ndash;{{ item.label }}&ndash;&gt;-->
                        <!--</el-table>-->
                </el-card>
            <!--</el-main>-->
            <!--<el-main style="text-align: center; margin-top: 10px; ">-->
                <el-card class="box-card" style="min-height: 400px;margin-top: 20px;text-align: center">
                    <div slot="header" class="clearfix">
                        <span>新闻主题分布图</span>
                    </div>
                    <div id="hot_distribution" style="width:100%;min-height:400px;"></div>
                </el-card>
                <el-card class="box-card" style="min-height: 50px; margin-top: 20px">
                    <div slot="header" class="clearfix">
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
            hotspotRes:{
                // hot_event: [],  // 热点新闻,每一项item均为{"rank": int, "event": string, "popularity": int, "url": string}形式
                // hot_topic: [],  // 热烈讨论话题, 每一项item均为{"rank": int, "topic": string, "view_number": string, "url": string}, "view_number"表示阅读和讨论量
                // hot_freq_words: {
                //     today: [], // 今日新闻高频词, 每一项均为{"rank": int, "word": str, "frequency": int}形式
                //     nearly_three_days: [], // 近三日新闻高频词, 每一项均为{"rank": int, "word": str, "frequency": int}形式
                //     nearly_one_week: [], //近一周新闻高频词, 每一项均为{"rank": int, "word": str, "frequency": int}形式
                // },
                // hot_key_words: {
                //     today: [], // 今日新闻高影响力关键词, 每一项均为{"rank": int, "word": str, "influence": float}形式
                //     nearly_three_days: [], // 近三日新闻高影响力关键词, 每一项均为{"rank": int, "word": str, "influence": float}形式
                //     nearly_one_week: [], //近一周新闻高影响力关键词, 每一项均为{"rank": int, "word": str, "influence": float}形式
                // },
                // // hot_statistics: {
                // //     "today_news_number": int, // 今日新增新闻数
                // //     "nearly_three_days_news_number": int, // 近三日新增新闻数
                // //     "nearly_one_week_news_number": int, // 近一周新增新闻数
                // //     "today_news_distribution": {
                // //         "domestic": int, "world": int, "sports": int, "society": int, "other": int, "history": int,"entertainment": int,
                // //         "military": int, "government": int, "education": int, "finance": int, "comment": int
                // //     },  // 今日新闻的主题(场景)分布;
                // //     "nearly_three_days_news_distribution": {
                // //         "domestic": int, "world": int, "sports": int, "society": int, "other": int, "history": int, "entertainment": int,
                // //         "military": int, "government": int, "education": int, "finance": int, "comment": int
                // //     }, // 近三日新闻的主题(场景)分布;
                // //     "nearly_one_week_news_distribution": {
                // //         "domestic": int, "world": int, "sports": int, "society": int, "other": int, "history": int, "entertainment": int,
                // //         "military": int, "government": int, "education": int, "finance": int, "comment": int
                // //     }, // 近一周新闻的主题(场景)分布
                // //     // 下面十二个列表为近7日各主题新闻的每天增长数(7个整数值)
                // //     "domestic_trend": [],
                // //     "world_trend": [],
                // //     "sports_trend": [],
                // //     "society_trend": [],
                // //     "other_trend": [],
                // //     "history_trend": [],
                // //     "entertainment_trend": [],
                // //     "military_trend": [],
                // //     "government_trend": [],
                // //     "education_trend": [],
                // //     "finance_trend": [],
                // //     "comment_trend": [],
                // //     "recent_half_hour_increase_news": []  //每个列表项{"news": str, "news_type": str, "publish_time": str, "url": str}  // 按时间先后, 最近发布的在前面
                // // }
            },
            items: [
                // { type: '', label: '标签一' },
                // { type: 'success', label: '标签二' },
            ],
            // 柱状图
            charts: "",
            view_number: "",
            hot_event:[
                // { rank: 1, topic: '新冠' ,view_number: 1000000, url:"http://baidu.com"},
                // { rank: 2, topic: '中国' ,view_number: 950101,url:"http://baidu.com"},
                // { rank: 3, topic: '奥运' ,view_number: 905100,url:"http://baidu.com"},
                // { rank: 4, topic: '国庆' ,view_number: 904100, url:"http://baidu.com"},
                // { rank: 5, topic: 'IPHONE' ,view_number: 850101,url:"http://baidu.com"},
                // { rank: 6, topic: '出轨' ,view_number: 805100,url:"http://baidu.com"},
            ],
            hot_topic:[],
            freq_words:[],
            freq_words_list:[],
            freq_words1_list:[],
            freq_words2_list:[],
            freq_words3_list:[],
            key_words:[],
            key_words1_list:[],
            key_words2_list:[],
            entData:[],
            activeName: 'second',
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
     // charts: '',
            // opinion:['直接访问','邮件营销','联盟广告','视频广告','搜索引擎'],
            // opinionData:[
            //     {value:335, name:'直接访问'},
            //     {value:310, name:'邮件营销'},
            //     {value:234, name:'联盟广告'},
            //     {value:135, name:'视频广告'},
            //     {value:1548, name:'搜索引擎'}
            // ]
        };
    },
    created() {
    },
    mounted() {
        // this.WordCloud('hot_freq_words');
        this.ResultofHospot();
        // this.WordCloud("hot_freq_words2",this.freq_words2_list);
        // this.WordCloud("hot_freq_words3",this.freq_words3_list);
        // this.getDay();
        // this.drawDistribution("hot_distribution");
        // this.drawEChart();
        // this.drawChart();
        this.init()
    },
    methods: {
        // 获取词列表
        getFreqWords(id,freq_words,title){
            for(let i = 0; i < 100; i++){
                let obj = {};
                obj.name = freq_words[i].word;
                obj.value = freq_words[i].frequency;
                this.freq_words_list[i] = obj;
            }
            this.WordCloud(id,this.freq_words_list,title);
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
                this.nearly_three_days_news_distribution = this.hotspotRes.hot_statistics.nearly_three_days_news_distribution;
                this.nearly_three_days_news_dis = Object.values(this.nearly_three_days_news_distribution);
                this.nearly_one_week_news_distribution = this.hotspotRes.hot_statistics.nearly_one_week_news_distribution;
                this.nearly_one_week_news_dis = Object.values(this.nearly_one_week_news_distribution);
                // console.log(this.today_news_dis);
                //柱状图
                this.drawDistribution("hot_distribution",this.today_news_dis,this.nearly_three_days_news_dis,this.nearly_one_week_news_dis);
                console.log("success")
                //折线图
                this.hot_statistics = this.hotspotRes.hot_statistics;
                this.news_info[0] = {
                    name: 'Domestic家庭',
                    type: 'line',
                    data: this.hot_statistics.domestic_trend
                },
                this.news_info[1] = {
                    name: 'World世界',
                    type: 'line',
                    data: this.hot_statistics.world_trend
                },
                this.news_info[2] = {
                    name: 'Sports体育',
                    type: 'line',
                    data: this.hot_statistics.sports_trend
                },
                this.news_info[3] = {
                    name: 'Society社会',
                    type: 'line',
                    data: this.hot_statistics.society_trend
                }
                this.news_info[4] = {
                    name: 'History历史',
                    type: 'line',
                    data: this.hot_statistics.history_trend
                },
                this.news_info[5] = {
                    name: 'Entertainment娱乐',
                    type: 'line',
                    data: this.hot_statistics.entertainment_trend
                },
                this.news_info[6] = {
                    name: 'Military军事',
                    type: 'line',
                    data: this.hot_statistics.military_trend
                },
                this.news_info[7] = {
                    name: 'Government政府',
                    type: 'line',
                    data: this.hot_statistics.government_trend
                },
                this.news_info[8] = {
                    name: 'Education教育',
                    type: 'line',
                    data: this.hot_statistics.education_trend
                },
                this.news_info[9] = {
                    name: 'Finance经济',
                    type: 'line',
                    data: this.hot_statistics.finance_trend
                },
                this.news_info[10] = {
                    name: 'Comment评论',
                    type: 'line',
                    data: this.hot_statistics.comment_trend
                },
                this.news_info[11] = {
                    name: 'Other其他',
                    type: 'line',
                    data: this.hot_statistics.other_trend
                },
                this.getDay();
                this.drawTrend("hot_trend",this.one_week_time.reverse(),this.news_info);
                //词云1
                this.freq_words = this.hotspotRes.hot_freq_words;
                var freq_words1 = this.freq_words.today;
                var freq_words2 = this.freq_words.nearly_three_days;
                var freq_words3 = this.freq_words.nearly_one_week;
                this.getFreqWords("hot_freq_words2",freq_words2,'新闻高频词分布词云');
                // if(this.activeName=="third"){
                //     for(let j = 0; j < 100; j++){
                //         let obj = {};
                //         obj.name = freq_words3[j].word;
                //         obj.value = freq_words3[j].frequency;
                //         this.freq_words3_list[j] = obj;
                //     }
                //     this.WordCloud("hot_freq_words3",this.freq_words3_list);
                // }else if(this.activeName=="second"){
                //     for(let i = 0; i < 100; i++){
                //     let obj = {};
                //     obj.name = freq_words2[i].word;
                //     obj.value = freq_words2[i].frequency;
                //     this.freq_words2_list[i] = obj;
                //     this.WordCloud("hot_freq_words2",this.freq_words2_list);
                // }

                // for(let i = 0; i < 100; i++){
                //     let obj = {};
                //     obj.name = freq_words2[i].word;
                //     obj.value = freq_words2[i].frequency;
                //     this.freq_words2_list[i] = obj;
                // }
                // this.WordCloud("hot_freq_words2",this.freq_words2_list);
                //
                // for(let j = 0; j < 100; j++){
                //     let obj = {};
                //     obj.name = freq_words3[j].word;
                //     obj.value = freq_words3[j].frequency;
                //     this.freq_words3_list[j] = obj;
                // }
                // this.getFreqWords("hot_freq_words3",freq_words3);
                // this.WordCloud("hot_freq_words3",this.freq_words3_list);
                //词云2
                this.key_words = this.hotspotRes.hot_key_words;
                var key_words1 = this.freq_words.today;
                var key_words2 = this.key_words.nearly_three_days;
                for(let i = 0; i < 100; i++){
                    let obj = {};
                    obj.name = key_words2[i].word;
                    obj.value = key_words2[i].influence;
                    this.key_words2_list[i] = obj;
                }
                this.WordCloud("hot_key_words2",this.key_words2_list,'新闻高影响力词分布词云');


                // }
                // this.recent_half_hour_increase_news = hotspotRes.hot_statistics.nearly_one_week_news_distribution
            })
            //词云
            // this.freq_words = this.hotspotRes.hot_freq_words;
            // var freq_words1 = this.freq_words.today;
            // var freq_words2 = this.freq_words.nearly_three_days;
            // var freq_words3 = this.freq_words.nearly_one_week;
            // // this.getFreqWords("hot_freq_words2",freq_words2);
            // for(let i = 0; i < 100; i++){
            //     let obj = {};
            //     obj.name = freq_words2[i].word;
            //     obj.value = freq_words2[i].frequency;
            //     this.freq_words2_list[i] = obj;
            // }
            // this.WordCloud("hot_freq_words2",this.freq_words2_list);
            // // this.getFreqWords("hot_freq_words3",freq_words3);
            // for(let j = 0; j < 100; j++){
            //     let obj = {};
            //     obj.name = freq_words3[j].word;
            //     obj.value = freq_words3[j].frequency;
            //     this.freq_words3_list[j] = obj;
            // }
            // this.WordCloud("hot_freq_words3",this.freq_words3_list);

            // var data1 = this.today_news_dis;
            // console.log(Object.values(this.today_news_distribution));
            // this.drawDistribution("hot_distribution",data1,data1,data1);
            // this.$message.success(this.hotspotRes);

        },
        //词云
        WordCloud(id,words,title) {
            this.chart = echarts.init(document.getElementById(id));
            const option = {
                colorArr:['#fda67e', '#81cacc', '#cca8ba', "#88cc81", "#82a0c5", '#fddb7e', '#735ba1', '#bda29a', '#6e7074', '#546570', '#c4ccd3'],
                title: {
                    text: title,
                    x: "center"
                },
                backgroundColor: "#fff",

                series: [{
                    type: "wordCloud",
                    //用来调整词之间的距离
                    gridSize: 10,
                    //用来调整字的大小范围
                    // Text size range which the value in data will be mapped to.
                    // Default to have minimum 12px and maximum 60px size.
                    sizeRange: [14, 60],
                    // Text rotation range and step in degree. Text will be rotated randomly in range [-90,                                                                             90] by rotationStep 45
                    //用来调整词的旋转方向，，[0,0]--代表着没有角度，也就是词为水平方向，需要设置角度参考注释内容
                    // rotationRange: [-45, 0, 45, 90],
                    // rotationRange: [ 0,90],
                    rotationRange: [0, 0],
                    //随机生成字体颜色
                    // maskImage: maskImage,
                    textStyle: {
                      normal: {
                        color: function() {
                            var colorArr = ['#fda67e', '#81cacc', '#cca8ba', "#88cc81", "#82a0c5", '#fddb7e', '#735ba1', '#bda29a', '#6e7074', '#546570', '#c4ccd3'];
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
        },
        //场景分布柱状图
        drawDistribution(id,data1,data2,data3) {
            // 基于准备好的dom，初始化echarts实例
            this.chart = echarts.init(document.getElementById(id));
            // 指定图表的配置项和数据
            var option = {
                color:['#E47470','#7EBF50','#589EF8'],
                tooltip: {
                    trigger: 'axis',
                    axisPointer: {
                        type: 'shadow'
                    }
                },
                grid:{
                    left:'5%',
                    right:'8%',
                    bottom:'10%',
                    containLabel:true
                },
                legend: {
                    data: [
                        {
                            name: '今日',
                            icon: 'circle',
                            textStyle: {
                              // color: 'red',  // 单独设置某一个图列的颜色
                              // backgroundColor: '#fff' // 单独设置某一个图列的字体背景色
                            }
                        },
                        {
                            name: '近三日',
                            icon: 'circle',
                            textStyle: {
                              // color: 'red',  // 单独设置某一个图列的颜色
                              // backgroundColor: '#fff' // 单独设置某一个图列的字体背景色
                            }
                        },
                        {
                            name: '近七日',
                            icon: 'circle',
                            textStyle: {
                              // color: 'red',  // 单独设置某一个图列的颜色
                              // backgroundColor: '#fff' // 单独设置某一个图列的字体背景色
                            }
                        },
                    ]
                },
                title: {
                    text: ""
                },

                xAxis: {
                    type: 'category',
                    name: '新闻主题',
                    axisLabel: {
                        interval:0,
                        rotate:40
                    },
                    data:['Comment评论', 'Domestic家庭', 'Education教育', 'Entertainment娱乐', 'Finance经济','Government政府', 'History历史', 'Military军事', 'Other其他', 'Society社会', 'Sports体育', 'World世界']
                },
                yAxis: {
                    type: 'value',
                    name: '新闻主题数量',
                },
                series: [
                    {
                        name: "今日",
                        type: "bar",
                        data: data1,
                    },
                    {
                        name: "近三日",
                        type: "bar",
                        data: data2,
                    },
                    {
                        name: "近七日",
                        type: "bar",
                        data: data3,
                    }
                ]
            };
            this.chart.setOption(option);
            window.addEventListener("resize", function() {
              this.charts.resize()
            })
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
                // color:['#E47470','#7EBF50','#589EF8'],
                //标题
                title:{
                  // text: `各主题新闻每日增长数`  /*  [+] 折线图叫啥名字 */
                },
                tooltip: {
                    trigger: 'axis'
                },
                grid: {
                    top:'15%',
                    left: '3%',
                    right: '4%',
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
                    data:["Domestic家庭","World世界","Sports体育","Society社会","History历史","Entertainment娱乐",
                        "Military军事","Government政府","Education教育","Finance经济","Comment评论","Other其他"]
                },
                //x轴
                xAxis:{
                    type: 'category',
                    name: '近七日',
                    data: date_arr,
                },
                //y轴没有显式设置，根据值自动生成y轴
                yAxis:{
                    type: 'value',
                    name: '各新闻主题增长数量',
                },
                //数据-data是最终要显示的数据

                /*  [+] Here I need Initial the series arr */
                series: news_info
            };
            this.chart.setOption(option);
            window.addEventListener("resize", function(){
                this.charts.resize()
            })
        },

        init() {
           const self = this;//因为箭头函数会改变this指向，指向windows。所以先把this保存
           setTimeout(() => {
              window.onresize = function() {
                  self.chart = echarts.init(self.$refs.myEchart);
                  self.chart.resize();
              }
           },20)
         },
        // 修改table header的背景色
        tableHeaderColor() {
            return 'tableStyle'
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

<style>
    @import url("//unpkg.com/element-ui@2.13.2/lib/theme-chalk/index.css");
    .el-header/deep/, .el-footer {
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
        font-weight:400;
    }
    .buttonText{
        color: #303133;
        font-weight: bold;
    }
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

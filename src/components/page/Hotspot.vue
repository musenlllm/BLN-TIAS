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
            <el-container>
                <el-aside width="800px" style="margin-left: 20px; margin-top: 30px; text-align: center">
                    <el-card class="box-card" style="min-height: 500px">
                        <div slot="header" class="clearfix">
                            <span>热点新闻</span>
                        </div>
                        <el-table
                                :data="hotspotRes.hot_event"
                                style="width: 100%; text-align: center; background-color: #2d8cf0"
                                @sort-change="changeSort"
                                :default-sort="{prop: 'rank', order: 'ascending'}"
                                border
                                :row-class-name="tableRowClassName"
                                max-height="500px"
                        >
                              <el-table-column align='center'
                                prop="rank"
                                label="排序"
                                sortable
                                :sort-orders="['ascending', 'descending']"
                                width="100%">
                              </el-table-column>
                              <el-table-column align='center'
                                prop="event"
                                label="话题"
                                width="100%">
                              </el-table-column>
                              <el-table-column align='center'
                                prop="popularity"
                                label="阅读量"
                                               width="100%"
                              >
                              </el-table-column>
                              <el-table-column align='center'
                                prop="url"
                                label="链接"
                              >
                              </el-table-column>

                                <!--{{ item.label }}-->
                        </el-table>
                        <!--<div>{{hotspotRes}}</div>-->
                        <div class="tag-group" style="margin-top: 0; display: flex; flex-direction: row; flex-wrap: wrap;">
                            <!--<span class="tag-group__title">Dark</span>-->

                            <el-tag style="margin-bottom: 10px; margin-right: 5px; border-radius: 4px; font-size: 15px; border: 0"
                                    v-for="item in items"
                                    :key="item.label"
                                    :type="item.type"
                                    :color="item.color"
                                    size="medium"
                                    effect="dark">
                                {{ item.label }}
                            </el-tag>
                        </div>
                    </el-card>

                    <el-card class="box-card" style="min-height:200px; margin-top: 20px">
                        <div slot="header" class="clearfix">
                            <span>新闻高影响力关键词排序</span>
                        </div>
                         <el-table
                                :data="hotspotRes.hot_key_words.today"
                                style="width: 100%; text-align: center"
                                @sort-change="changeSort"
                                :default-sort="{prop: 'rank', order: 'ascending'}"
                                :row-class-name="tableRowClassName"
                                border
                                max-height="500px"
                         >
                              <el-table-column align='center'
                                prop="rank"
                                label="排序"
                                sortable
                                :sort-orders="['ascending', 'descending']"
                                >
                              </el-table-column>
                              <el-table-column align='center'
                                prop="word"
                                label="关键词"
                                >
                              </el-table-column>
                              <el-table-column align='center'
                                prop="influence"
                                label="影响力"
                              >
                              </el-table-column>
                              <!--<el-table-column-->
                                <!--prop="url"-->
                                <!--label="链接"-->
                                <!--sortable="custom">-->
                              <!--</el-table-column>-->

                                <!--{{ item.label }}-->
                            </el-table>
                    </el-card>

                </el-aside>


                <el-main style="text-align: center; margin-top: 10px; ">
                    <el-card class="box-card">
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
                                    border
                                    max-height="500px"
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
                                    label="话题"
                                  >
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

                            <!--柱状图-->
                            <div id="hottopic" style="width: 900px; height:400px "></div>

                        </div>
                    </el-card>
                    <el-card class="box-card" style="min-height: 50px; margin-top: 20px">
                        <div slot="header" class="clearfix">
                            <span>新增新闻数</span>
                        </div>
                            <!--柱状图-->
                            <div id="hot_statistics" style="width: 900px; height:400px "></div>



                        <div id="number" style="width: 600px;height: 100px;"></div>
                    </el-card>

                    <el-card class="box-card" style="min-height: 174px; margin-top: 20px">
                        <div slot="header" class="clearfix">
                            <span>新闻主题分布</span>
                        </div>
                        <div id="percent" style="width: 600px; height: 100px;"></div>
                    </el-card>

            </el-main>
            </el-container>
            <el-footer>
                <el-container>
                    <!--<el-aside style="width: 700px">-->
                        <!--<el-card class="box-card" style="min-height: 174px">-->
                            <!--<div slot="header" class="clearfix">-->
                                <!--<span>实体分类树</span>-->
                            <!--</div>-->
                            <!--<div id="tree" style="width: 600px;height: 600px;"></div>-->
                        <!--</el-card>-->
                    <!--</el-aside>-->
                    <el-main>

                    </el-main>
                </el-container>


            </el-footer>
            <!--<el-footer>Footer</el-footer>-->
        </el-container>
    </div>


</template>
<script>
import echarts from 'echarts'
import { fetchData } from '../../api/index';
const hotspoturl = "http://49.234.217.110:5000/api/hotspot";
export default {
    name: 'basetable',
    data() {
        return {
            text: '',
            summaryText: '',
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
            hot_key_words:[],
            entData:[],
            treeCharts: '',
            percentCharts: '',
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
         // this.getData();
    },
    mounted() {
        this.ResultofHospot();
        this.drawEChart();
        this.drawChart();
        this.init()
    },
    methods: {
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
                this.hot_event = hotspotRes.hot_event;
                this.hot_topic = hotspotRes.hot_topic;
                this.hot_key_words = response
            })
            // this.drawDashboard("emotionLevel",this.sentimentscore);
            //this.$message.success("提交成功！");

        },
        // 画柱状图
        drawChart() {
            // 基于准备好的dom，初始化echarts实例
            let myChart = this.$echarts.init(document.getElementById("hottopic"));
            // 指定图表的配置项和数据
            let option = {
                color:['#93bee2'],
                title: {
                    text: "热门话题排序"
                },
                tooltip: {},
                xAxis: {
                    data:this.hot_topic.topic
                },
                yAxis: {},
                series: [
                    {
                        name: "阅读量",
                        type: "bar",
                        data: this.hot_topic.view_number
                    }
                ]
            };
            // 使用刚指定的配置项和数据显示图表。
            myChart.setOption(option);
        },
        drawEChart() {
            // 基于准备好的dom，初始化echarts实例
            let myChart = this.$echarts.init(document.getElementById("hot_statistics"));
            // 指定图表的配置项和数据
            let option = {
                color:['#93bee2'],
                title: {
                    text: ""
                },
                tooltip: {},
                xAxis: {
                    data:['周一', '周二', '周三', '周四', '周五', '周六', '周日']
                },
                yAxis: {},
                series: [
                    {
                        name: "阅读量",
                        type: "bar",
                        data: [100, 95, 90, 88, 85, 80]
                    }
                ]
            };
            // 使用刚指定的配置项和数据显示图表。
            myChart.setOption(option);
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
        tableRowClassName({row, rowIndex}) {
            if (rowIndex === 0) {
              return 'warning-row';
            } else if (rowIndex === 1) {
              return 'warning-row';
            }else if (rowIndex === 2) {
              return 'warning-row';
            }
            return '';
        }
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
    .el-table/deep/.warning-row {
        background: #f0f9eb;
    }
</style>

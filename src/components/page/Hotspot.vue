<template>
    <!--<link rel="stylesheet" type="text/css" href="http://at.alicdn.com/t/font_2015036_ral7di9rm4.css">-->
    <div>
        <el-container>
            <el-header style="height: max-content;text-align: center">
              <el-card class="noBorderInput"style="border: 0px; margin-top: 15px;border-radius: 0;
      background-color: #fff;
      box-shadow: 0 0px 0px 0 rgba(0,0,0,.1);">

                <div slot="header" class="diyCardHead" style="margin-bottom: -1%;margin-top: -1.5%">
                  <h1 style="color: black; letter-spacing: 10px; font-weight: normal; font-size: 25px; "> 热点挖掘</h1>
                </div>

                <div class="diyCardBody" style="margin-top: 0px">
                  <el-row :gutter="20" >
                    <el-col :span="8">
                      <!--<el-card shadow="always" class="box-card" :body-style="{padding: '0px'}" style="min-height: 458px;font-size: 18px">-->
                      <el-card class="noBorderInput" :body-style="{padding: '0px'}" style="min-height: 466px;border: 0px;border-radius: 0;background-color: #fff;box-shadow: 0 0px 0px 0 rgba(0,0,0,.1);">
                        <div slot="header" class="clearfix" style="font-size: 18px;height: 30px; margin-top: -25px; margin-bottom: 20px">

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
                        <div slot="header" class="clearfix" style="font-size: 18px;height: 30px;margin-top: -25px; margin-bottom: 20px">
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
                        <div slot="header" class="clearfix" style="font-size: 18px;height: 30px;margin-top: -25px; margin-bottom: 20px">
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
                </div>
              </el-card>
            </el-header>
            <el-main  style="margin-left: 0px; margin-top: -30px; text-align: center">

                <!--<el-card class="box-card" style="min-height:200px; margin-top: 20px;text-align: center">-->
                <el-card class="noBorderInput" :body-style="{padding: '0px'}" style="text-align: center;margin-top: 30px;min-height: 200px;border: 0px;border-radius: 0;background-color: #fff;box-shadow: 0 0px 0px 0 rgba(0,0,0,.1);">
                    <el-tabs type="card" v-model="activeName" @tab-click="handleClick" style="border: 0px;border-radius: 0">
                        <el-tab-pane label="今日" name="first">

                            <div class="wrap" v-if="isChildUpdate1" style="display: flex; justify-content: space-around">
                                <div id = "hot_key_words1" style="width:30%;min-height:400px;" ></div>
                                <div id="hot_freq_words1" style="width:30%;height:400px;"></div>
                                <div id="today_hot_distribution1" style="width:30%;height:400px;"></div>


                                <!--<div>{{this.freq_words2_list}}</div>-->
                            </div>
                        </el-tab-pane>
                        <el-tab-pane label="近七日" name="third">
                            <div class="wrap" v-if="isChildUpdate3" style="display: flex; justify-content: space-around">
                                <div id = "hot_key_words3" style="width:30%;min-height:400px;" ></div>
                                <div id = "hot_freq_words3" style="width:30%;min-height:400px;" ></div>
                                <div id="today_hot_distribution3" style="width:30%;height:400px;"></div>
                                <!--<div>{{this.key_words2_list}}</div>-->
                            </div>
                        </el-tab-pane>
                    </el-tabs>

                </el-card>
            <!--</el-main>-->
            <!--<el-main style="text-align: center; margin-top: 10px; ">-->
                <!--<el-card class="box-card" style="min-height: 400px;margin-top: 20px;text-align: center">-->
                <!--<el-card class="noBorderInput" :body-style="{padding: '0px'}" style="text-align: center;margin-top: 30px;min-height: 200px;border: 0px;border-radius: 0;background-color: #fff;box-shadow: 0 0px 0px 0 rgba(0,0,0,.1);">-->
                    <!--<div slot="header" class="clearfix" style="font-size: 18px">-->
                        <!--<span>新闻主题分布图</span>-->
                    <!--</div>-->
                    <!--<div id="today_hot_distribution" style="width:100%;height:600px;"></div>-->
                    <!--<div id="week_hot_distribution" style="width:100%;height:600px;">近七日</div>-->
                  <!--&lt;!&ndash;{{this.recent_half_hour_increase_news}}&ndash;&gt;-->
                  <!--&lt;!&ndash;{{this.nearly_one_week_news_dis}}&ndash;&gt;-->
                  <!--&lt;!&ndash;{{this.nearly_three_days_news_dis}}&ndash;&gt;-->
                  <!--&lt;!&ndash;{{this.today_news_dis}}&ndash;&gt;-->
                <!--</el-card>-->
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
        hotspotRes: {},
        items: [],
        // 柱状图
        charts: "",
        view_number: "",
        hot_event: [],
        hot_topic: [],
        freq_words: [],
        freq_words_list: [],
        freq_words1_list: [],
        freq_words2_list: [],
        freq_words3_list: [],
        key_words: [],
        key_words_list: [],
        key_words1_list: [],
        key_words2_list: [],
        entData: [],
        activeName: 'third',
        isChildUpdate1: false,
        isChildUpdate2: false,
        isChildUpdate3: true,
        recent_half_hour_increase_news: [],
        test: {"name": "Liza", "password": "123"},
        hot_statistics: {},
        today_news_distribution: {},
        today_news_dis: [],
        nearly_three_days_news_distribution: {},
        nearly_three_days_news_dis: [],
        nearly_one_week_news_distribution: {},
        nearly_one_week_news_dis: [],

        one_week_time: [],
        news_info: [],
// <<<<<<< Updated upstream
        name: ["国内", "世界", "体育", "社会", "历史", "娱乐",
          "军事", "政府", "教育", "经济", "评论", "其他"],
        source: [['topic', '今日', '近七日'], ['评论'], ['国内'], ['教育'], ['娱乐'], ['经济'], ['政府'],
          ['历史'], ['军事'], ['其他'], ['社会'], ['体育'], ['世界']],

        //高频词的热力图数据
        heatmap_x_axis: [],
        today_freq_heat_data: [],
        one_week_freq_heat_data: [],
        heatmap: '',
        image1: "data:image/png;base64,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",

// =======
//             name:["Domestic国内","World世界","Sports体育","Society社会","History历史","Entertainment娱乐",
//                         "Military军事","Government政府","Education教育","Finance经济","Comment评论","Other其他"],
//             source:[['topic','今日','近七日'],['Comment评论'],['Domestic国内'], ['Education教育'], ['Entertainment娱乐'], ['Finance经济'],['Government政府'],
//               ['History历史'], ['Military军事'], ['Other其他'], ['Society社会'], ['Sports体育'], ['World世界']],
        image2:"data:image/png;base64,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",
        image3:"data:image/png;base64,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",
        image4:"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAABU0lEQVQ4T6WTsUsCYRjGf9/daXfnFu1N1RoFESQJLf0DBU39Bw5KChY0OHgStdTQ1iAELo2NDhYZtBXhEm0RlNGUnEl3X5yinJJ60jd9vB/83ud93ucTUkqVfxwxLmD5nMjjO9NfCape37EBSo47CQt6iFU7RaUHED5g23FYUVVummkK/ZMZeWINl1KnLqDcBfgfFUHWyZDtB5iHLNlNKp16WGNT6JZc+3Y5kjALmH66oZOoJ3mInmHevrHjSvZ90GrEYKulQOT4GbKIDwEvEuZbpkHZNIh7d8/IFkDJUZIQC7pNuYvWVeoBJvJsNF2KQQFmiMV6ivueNY4DUQTHTobkwByoVtusPtO6AhXBqZNp+zAwSEMU1aZ0orUkzyOTqFgUBbxKyZyEdQEXYY1CI81lj4mjzAtZ7Gkq13aaK288f8gC/YWZEyaf4nz+1SgQYJjCXzBWkv34rjyaAAAAAElFTkSuQmCC",
      }
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
                this.getHotTopic("today_hot_distribution1",this.today_news_distribution,'今日新闻主题分类')
                this.getKeyWords("hot_key_words1",this.key_words.today,'今日新闻高影响力词分布词云');
                this.getFreqWords("hot_freq_words1",this.freq_words.today,'今日新闻高频词分布');
                // this.isChildUpdate2 = false;
                this.isChildUpdate3 = false;
            } else if(tab.name == "third") {
                this.isChildUpdate1 = false;
                // this.isChildUpdate2 = false;
                this.isChildUpdate3 = true;
                this.getHotTopic("today_hot_distribution3",this.nearly_one_week_news_distribution,'近七日新闻主题分类')
                this.getKeyWords("hot_key_words3",this.key_words.nearly_one_week,'近七日新闻高影响力词分布词云');
                this.getFreqWords("hot_freq_words3",this.freq_words.nearly_one_week,'近七日新闻高频词分布');
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
                this.drawRose(id,this.freq_words_list,title);

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
      getHotTopic(id,today_news_distribution,title){
        this.$nextTick(() => {
          this.drawDistribution(id,today_news_distribution,title);
        })
      },

      drawRose(id,data,title){
          data = data.slice(0,20);
        // 基于准备好的dom，初始化echarts实例
        this.chart = echarts.init(document.getElementById(id));
        // 指定图表的配置项和数据


        var option = {
          title: {
            text: title,
            x: "center",
            top:'1%',//各个方向的内边距，默认是5，可以自行设置
            textStyle:{//标题内容的样式
              fontStyle:'normal',//主标题文字字体风格，默认normal，有italic(斜体),oblique(斜体)
              fontWeight:"normal",//可选normal(正常)，bold(加粗)，bolder(加粗)，lighter(变细)，100|200|300|400|500...
              fontSize:15//主题文字字体大小，默认为18px

            },
            left: 'center'
          },
          tooltip: {
            trigger: 'item',
            formatter: '{a} <br/>{b} : {c} ({d}%)'
          },

          series: [

            {
              name: '面积模式',
              type: 'pie',
              radius: [30, 110],
              roseType: 'area',
              data: data,
            }
          ]
        }


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
        // window.addEventListener("resize", function() {
        //   this.chart.resize();
        // });
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

                //获取高频词热力图所需要的数据
                var today_freq_heat = this.hotspotRes.hot_freq_words.today;
                //测试接受数据是否正确
                for(let i=0;i<10;i++){
                  this.today_freq_heat_data.push({
                    'name':today_freq_heat[i].word,
                    'value':today_freq_heat[i].frequency
                  });
                }
                //柱状图
                var i = 1

                for(i;i < 13;i++){
                     this.source[i].push(this.today_news_dis[i-1]);
                       // .push(this.nearly_three_days_news_dis[i-1]).push(this.nearly_one_week_news_dis[i-1])
                     this.source[i].push(this.nearly_one_week_news_dis[i-1]);
                     console.log(i)
                     // this.source = a.concat(b);
                }

                // setTimeout(()=>{
                //     this.drawDistribution("today_hot_distribution",this.today_news_distribution,'今日');
                //     // this.drawDistribution("today_hot_distribution",this.nearly_one_week_news_dis,'近七日');
                // })
                console.log("success")

                //词云
                this.key_words = this.hotspotRes.hot_key_words;
                // var key_words1 = this.key_words.today;
                // var key_words2 = this.key_words.nearly_three_days;
                // var key_words3 = this.key_words.nearly_one_week;
                // this.getKeyWords("hot_key_words1",key_words1,'今日新闻高影响力词分布词云');
                // this.getKeyWords("hot_key_words2",key_words2,'近三日新闻高影响力词分布词云');
                this.getKeyWords("hot_key_words3",this.key_words.nearly_one_week,'近七日新闻高影响力词分布词云');



                //折线图
                this.hot_statistics = this.hotspotRes.hot_statistics;
                this.news_info[0] = {
                    name: '国内',
                    type: 'bar',
                    stack: '总量',
                    // label: {
                    //     show: true,
                    //     position: 'right'
                    // },
                    data: this.hot_statistics.domestic_trend
                },
                this.news_info[1] = {
                    name: '世界',
                    type: 'bar',
                    stack: '总量',
                    // label: {
                    //     show: true,
                    //     position: 'right'
                    // },
                    data: this.hot_statistics.world_trend
                },
                this.news_info[2] = {
                    name: '体育',
                    type: 'bar',
                    stack: '总量',
                    // label: {
                    //     show: true,
                    //     position: 'right'
                    // },
                    data: this.hot_statistics.sports_trend.map((item, index, arr)=> item * -1 )
                },
                this.news_info[3] = {
                    name: '社会',
                    type: 'bar',
                    stack: '总量',
                    // label: {
                    //     show: true,
                    //     position: 'right'
                    // },
                    data: this.hot_statistics.society_trend
                },
                this.news_info[4] = {
                    name: '历史',
                    type: 'bar',
                    stack: '总量',
                    // label: {
                    //     show: true,
                    //     position: 'right'
                    // },
                    data: this.hot_statistics.history_trend.map((item, index, arr)=> item * -1 )
                },
                this.news_info[5] = {
                    name: '娱乐',
                    type: 'bar',
                    stack: '总量',
                    // label: {
                    //     show: true,
                    //     position: 'right'
                    // },
                    data: this.hot_statistics.entertainment_trend.map((item, index, arr)=> item * -1 )
                },
                this.news_info[6] = {
                    name: '军事',
                    type: 'bar',
                    stack: '总量',
                    // label: {
                    //     show: true,
                    //     position: 'right'
                    // },
                    data: this.hot_statistics.military_trend.map((item, index, arr)=> item * -1 )
                },
                this.news_info[7] = {
                    name: '政府',
                    type: 'bar',
                    stack: '总量',
                    // label: {
                    //     show: true,
                    //     position: 'right'
                    // },
                    data: this.hot_statistics.government_trend.map((item, index, arr)=> item * -1 )
                },
                this.news_info[8] = {
                    name: '教育',
                    type: 'bar',
                    stack: '总量',
                    // label: {
                    //     show: true,
                    //     position: 'right'
                    // },
                    data: this.hot_statistics.education_trend.map((item, index, arr)=> item * -1 )
                },
                this.news_info[9] = {
                    name: '经济',
                    type: 'bar',
                    stack: '总量',
                    // label: {
                    //     show: true,
                    //     position: 'right'
                    // },
                    data: this.hot_statistics.finance_trend
                },
                this.news_info[10] = {
                    name: '评论',
                    type: 'bar',
                    stack: '总量',
                    // label: {
                    //     show: true,
                    //     position: 'right'
                    // },
                    data: this.hot_statistics.comment_trend.map((item, index, arr)=> item * -1 )
                },
                this.news_info[11] = {
                    name: '其他',
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



                //近七天的话题柱状图
                this.getHotTopic("today_hot_distribution3",this.nearly_one_week_news_distribution,'近七日新闻主题分类')
            })
        },
        //词云
        WordCloud(id,words,title) {
            this.chart = echarts.init(document.getElementById(id));
            var maskImage = new Image();
            maskImage.src = this.image2;
            maskImage.style.width='100px';
            maskImage.style.height='100px';

            var option = {
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
                    left:'',
                    right:'0%',
                    bottom:'5%',
                    top:'19%',
                    containLabel:true
                },

                series: [{
                    type: "wordCloud",
                    //用来调整词之间的距离
                    gridSize: 0,
                    //用来调整字的大小范围
                    // Text size range which the value in data will be mapped to.
                    // Default to have minimum 12px and maximum 60px size.
                    sizeRange: [9, 30],
                    // Text rotation range and step in degree. Text will be rotated randomly in range [-90,                                                                             90] by rotationStep 45
                    //用来调整词的旋转方向，，[0,0]--代表着没有角度，也就是词为水平方向，需要设置角度参考注释内容
                    rotationRange: [-40, 0, 45, 90],
                    // rotationRange: [ 0,90],
                    // rotationRange: [0, 0],
                    //随机生成字体颜色
                    maskImage: maskImage,
                    drawOutOfBound:true,
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
                    width: "100%",
                    height: "100%",
                    //数据
                    // data: words.slice(0,words.length-40),
                    data:words
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
            var option1 = {
              title: {
                text: date,
                x: "center",
                padding:9,
                top:'0%',//各个方向的内边距，默认是5，可以自行设置
                textStyle:{//标题内容的样式
                  fontStyle:'normal',//主标题文字字体风格，默认normal，有italic(斜体),oblique(斜体)
                  fontWeight:"normal",//可选normal(正常)，bold(加粗)，bolder(加粗)，lighter(变细)，100|200|300|400|500...
                  fontSize:15//主题文字字体大小，默认为18px
                },

              },
              color: ['#3398DB'],
              tooltip: {
                trigger: 'axis',
                axisPointer: {            // 坐标轴指示器，坐标轴触发有效
                  type: 'shadow'        // 默认为直线，可选为：'line' | 'shadow'
                }
              },
              dataset: {
                source: this.source
              },
              grid: {
                left: '3%',
                right: '4%',
                bottom: '10%',
                containLabel: true
              },
              xAxis: [
                {
                  type: 'value',
                }

              ],
              yAxis: [
                {
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
                  data:['评论', '国内', '教育', '娱乐', '经济','政府', '历史', '军事', '其他', '社会', '体育', '世界'],

                  axisTick: {
                    alignWithLabel: true
                  }
                }
              ],
              series: [
                {
                  name: date,
                  type: "bar",
                  data: Object.values(data1),
                  // name: '直接访问',
                  // type: 'bar',
                  barWidth: '60%',
                  // data: [10, 52, 200, 334, 390, 330, 220]
                }
              ]
            }
            var option = {
                // color:['#E47470','#7EBF50','#589EF8'],
                // color:['rgb(210,100,93)','rgb(228,116,79)','rgb(242,176,110)','rgb(249,224,150)','rgb(255,254,198)','rgb(233,244,163)','rgb(181,219,169)','rgb(156,218,174)','rgb(125,191,166)','rgb(93,178,155)','rgb(74,134,183)','rgb(125,169,185)'],
                color:['rgb(227,158,156)','rgb(224,108,146)','rgb(197,151,212)','rgb(175,159,215)','rgb(160,169,214)','rgb(233,244,163)','rgb(181,219,169)','rgb(156,218,174)','rgb(125,191,166)','rgb(93,178,155)','rgb(74,144,173)','rgb(126,180,225)'].reverse(),
                // tooltip: {
                //     trigger: 'axis',
                //     axisPointer: {
                //         type: 'shadow'
                //     }
                // },
                title: {
                    text: '今日主题分布图',
                    textAlign: "center",
                    left:'50%',//各个方向的内边距，默认是5，可以自行设置
                },
                dataset: {
                    source: this.source
                },
                // grid:{
                //     top:'10%',
                //     // left:'5%',
                //     right:'0%',
                //     bottom:'10%',
                //     // containLabel:true
                // },
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
                    data:['评论', '国内', '教育', '娱乐', '经济','政府', '历史', '军事', '其他', '社会', '体育', '世界']
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
                ]
            };
            // this.chart.on('updateAxisPointer', function (event) {
            //     var xAxisInfo = event.axesInfo[0];
            //     if (xAxisInfo) {
            //         var dimension = xAxisInfo.value + 1;
            //         this.chart.setOption({
            //             series: {
            //                 id: 'pie',
            //                 label: {
            //                     formatter: '{b}: {@[' + dimension + ']} ({d}%)'
            //                 },
            //                 encode: {
            //                     value: dimension,
            //                     tooltip: dimension
            //                 }
            //             }
            //         });
            //     }
            // });
            this.chart.setOption(option1);
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
        //画出热力图
        init() {
           const self = this;//因为箭头函数会改变this指向，指向windows。所以先把this保存
           setTimeout(() => {
              window.addEventListener('resize', function() {
                  self.chart = self.$echarts.init(self.$refs.Echart);
                  self.chart.resize();
              })
           },10)
         },
    }
}
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

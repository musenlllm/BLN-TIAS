<template>
    <div>
        <el-container>
            <el-header style="height: max-content;text-align: center;">
                <!--<h1 style="color: gray">情感分析</h1>-->

              <el-card class="noBorderInput" style="border: 0px; margin-top: 20px;border-radius: 0;max-height: 275px;
        background-color: #fff;
        box-shadow: 0 0px 0px 0 rgba(0,0,0,.1);">
                      <h1 style=" letter-spacing: 10px; font-weight: normal; font-size: 25px; margin-top: -20px">情感分析</h1>
                  <!--<el-card style="text-align: center;">-->
                      <el-input
                              type="textarea"
                              placeholder="请输入文本"
                              v-model="summaryText"
                              maxlength="400"
                              show-word-limit='false'
                              :autosize="{ minRows: 6, maxRows: 6}"
                              clearable
                              style="box-shadow: 0 2px 4px rgba(0, 0, 0, .12), 0 0 6px rgba(0, 0, 0, .04); font-size: 15px;"
                      >
                      </el-input>
                      <el-row style="margin-top: 17px; display: flex; justify-content: center">
                          <el-button v-on:click="ResultofSentiment" type="primary" style="background: #242f42; border: 0px;font-size: 15px; letter-spacing: 5px">开始分析</el-button>
                      </el-row>
              </el-card>
           </el-header>
            <el-main
              ref = "mainContainer"
              style="text-align: center;margin-top: 20px;height: 100%;padding: 0 20px"
              >
              <el-row style="max-height: 480px;max-width: 100%">
                    <el-card class="box-card" style="height: 240px;background-color: #fff;
      box-shadow: 0 0px 0px 0 rgba(0,0,0,.1);" v-loading="resloading">
                        <div slot="header" class="clearfix" style="font-size: 18px">
                            <span>本次分析结果</span>
                        </div>
                        <el-row>
                          <span :style=style_sen > {{this.classification}} </span>
                          <div id="wrap" align="middle" style="width: 100%;justify-content: center;margin-top: -60px">
                              <div id = "pos_emoji" style="margin-top: 45px" align="bottom">
                                  <span style="font-size:15px;color:#909399;text-align:center;display:block;position:relative;top:40px;margin-right: 15px;letter-spacing: 5px">正面情绪</span>
                                  <img src="../../assets/img/pos2.png" width="100px"/>
                              </div>

                              <div align="middle" id="emotionLevel" style="width:500px;height:400px;margin-top: -90px"></div>

                              <div id = "neg_emoji" style="margin-left:8px;margin-top: 45px">
                                  <img src="../../assets/img/neg2.png" width="100px"/>
                                  <span style="font-size:15px;color:#909399;text-align:center;display:block;position:relative;top:40px;margin-left: 15px;letter-spacing: 5px">负面情绪</span>
                              </div>
                          </div>
                        </el-row>
                    </el-card>
              </el-row>

              <el-row style="max-width: 100%;margin-top: 20px">
                    <el-card class="box-card" style="height:520px;box-shadow: 0 0px 0px 0 rgba(0,0,0,.1);" v-loading="resloading">
                        <div slot="header" class="clearfix">
                            <span style="color: black;font-size: 18px">今日新闻分析结果</span>
                            <div class="showupdatetime">更新时间：{{lastupdatetime}}</div>
                        </div>

                        <el-container style="margin: -20px;margin-right: -9px">
                            <el-aside width="50%" style="margin-top:-1px;margin-right: 10px;margin-left: 11px;height:100%">
                                <el-row :gutter="0" >
                                    <el-col :span="24" style="padding: 0px;margin-top:-2px;margin-left: -1px;margin-right: 1px">
                                        <el-card :body-style="{padding: '0px',shadow:'never'}" style="border-radius: 0;" shadow="never">
                                            <div class="grid-content grid-con-1" style="color:#E47470 ">
                                                <div class="grid-con-text">
                                                    <div class="grid-num">今日检测总数</div>
                                                    <div class="grid-num">{{today_num = today_negative_count+today_positive_count}} 条</div>
                                                </div>

                                                <el-divider direction="vertical" class="el-div"></el-divider>
                                                <div class="grid-cont-right1">
                                                    <div class="right-text">
                                                        <span class="grid-text">正面</span>
                                                        <span class="grid-num">{{today_positive_count}} 条</span>
                                                    </div>
                                                    <div class="right-text">
                                                        <span class="grid-text">负面</span>
                                                        <span class="grid-num">{{today_negative_count}} 条</span>
                                                    </div>
                                                </div>
                                            </div>
                                        </el-card>
                                    </el-col>
                                </el-row>
                                <!--今日小时曲线图-->
                                <div id="today_emotionLevel" style="width:100%;height:390px;margin-top: -2%"></div>
                            </el-aside>
                            <el-main style="margin: -20px;margin-bottom: -20px;margin-right: 0px" >

                                <el-tabs type="border-card" stretch=true style="padding:-10%;margin-right:-16px;margin-left: -2px;margin-top:-1px;border-radius: 0;">
                                    <el-tab-pane>
                                      <span slot="label" >正面新闻</span>
                                      <!--<el-card class="box-card" :body-style="{padding: '0px'}">-->
                                      <div
                                        class="tag-group"
                                        style=" display: flex; justify-content: center; flex-direction: row; flex-wrap: wrap;"
                                      >
                                        <el-table
                                            :data="pos_news"
                                            stripe
                                            :height="tableHeight"
                                            style="width: 100%;text-align: center;fontSize:13px;margin-bottom: -10px"
                                            :show-header=false
                                            :show-overflow-tooltip=true
                                            @sort-change="changeSort"
                                            :default-sort="{prop: 'rank', order: 'ascending'}"
                                            max-height="377px"
                                        >
                                            <el-table-column align='center'
                                                    type="index"
                                                    :show-overflow-tooltip=true
                                                    :sort-orders="['ascending', 'descending']"
                                            >
                                            </el-table-column>
                                            <el-table-column
                                              prop="news"
                                              label="主题和链接"
                                              :show-overflow-tooltip=true
                                            >
                                                <template slot-scope="scope">
                                                    <a :href="scope.row.url" target="_blank" class="buttonText" >{{scope.row.news}}</a>
                                                </template>
                                            </el-table-column>
                                            <!--<el-table-column-->
                                                    <!--prop="score"-->
                                                    <!--width="80%"-->
                                                    <!--label="置信度"-->
                                                    <!--sortable-->
                                                    <!--:show-overflow-tooltip=true-->
                                            <!--&gt;-->
                                                <!--<template slot-scope="scope">-->
                                                    <!--<span >{{scope.row.score.toFixed(4)}}</span>-->
                                                <!--</template>-->
                                            <!--</el-table-column>-->
                                            <el-table-column
                                                    prop="publish_time"
                                                    sortable
                                                    label="日期"
                                                    :show-overflow-tooltip=true
                                                    width="200%"
                                            >
                                                <template slot-scope="scope">
                                                    <span >发布时间：{{scope.row.publish_time}}</span>
                                                </template>
                                            </el-table-column>
                                       </el-table>
                                     </div>
                                   <!--</el-card>-->
                                    </el-tab-pane>
                                    <el-tab-pane label="负面新闻">
                                      <span slot="label" >负面新闻</span>
                                        <el-table
                                            :data="neg_news"
                                            stripe
                                            style="width: 100%;text-align: center;fontSize:13px;margin-bottom: -10px"
                                            :show-header=false
                                            :show-overflow-tooltip=true
                                            max-height="377px"
                                        >
                                            <el-table-column align='center'
                                                     type="index"
                                                    :show-overflow-tooltip=true
                                                    sortable
                                                    :sort-orders="['ascending', 'descending']"

                                                             margin-right = "-10%"
                                            >
                                            </el-table-column>
                                            <el-table-column
                                                    prop="news"
                                                    :show-overflow-tooltip=true
                                            >
                                                <template slot-scope="scope">
                                                    <a :href="scope.row.url" target="_blank" class="buttonText" >{{scope.row.news}}</a>
                                                </template>
                                            </el-table-column>
                                            <!--<el-table-column-->
                                                    <!--prop="score"-->
                                                    <!--width="80%"-->
                                                    <!--:show-overflow-tooltip=true-->
                                            <!--&gt;-->
                                                <!--<template slot-scope="scope">-->
                                                    <!--<span >{{scope.row.score}}</span>-->
                                                <!--</template>-->
                                            <!--</el-table-column>-->
                                            <el-table-column prop="publish_time"
                                                            :show-overflow-tooltip=true
                                                             width="200%"
                                            >
                                                <template slot-scope="scope">
                                                    <span >发布时间：{{scope.row.publish_time}}</span>
                                                </template>
                                            </el-table-column>
                                      </el-table>
                                    </el-tab-pane>
                                </el-tabs>



                            </el-main>
                        </el-container>
                    </el-card>
              </el-row>

              <el-row style="margin-bottom:20px">
                  <el-card class="box-card" style="height:520px;box-shadow: 0 0px 0px 0 rgba(0,0,0,.1);align-items: center" v-loading="resloading">
                      <div slot="header" class="clearfix" style="color: black;font-size: 18px">
                          <span>
                            <i class="iconfont iconxinwen"></i>
                            历史新闻分析结果
                          </span>
                          <div class="showupdatetime">更新时间：{{lastupdatetime}}</div>
                      </div>
                      <el-row :gutter="10" style="width: 100%;margin-top: -10px;margin-left: 0.1px">
                          <el-col :span="8" style="">
                              <el-card :body-style="{padding: '0px',shadow:'never'}" style="box-shadow: 0 0px 0px 0 rgba(0,0,0,.1);">
                                  <div class="grid-content grid-con-1" style="height:90px;color:#E47470;background-color: white ">
                                      <div class="grid-con-text" style="">
                                          <div class="iconof1" style="margin-left:10%;border-radius:15px;align-items: center">
                                            <span style="color: #ffffff">
                                              <i class="el-icon-s-data" style="font-size: 45px;margin-top: 15%;"></i>
                                            </span>
                                          </div>
                                      </div>
                                      <!--<el-divider direction="vertical" class="el-div"></el-divider>-->
                                      <div class="grid-cont-right1" style="margin-left: -140px;width:70%;">
                                          <!--<div class="right-text" style="color: #35363b;margin: 0px">-->
                                          <div class="right-text">
                                            <span class="grid-num" style="font-size: 28px;font-weight: bold;color: #35363b;">{{today_num = history_pos_count+history_neg_count}} 条</span>
                                          </div>
                                        <!--<div class="right-text" style="color: #35363b;margin: 0px">-->
                                          <div class="right-text">
                                            <!--<span class="grid-num">{{today_num = today_negative_count+today_positive_count}} 条</span>-->
                                            <span class="grid-text" style="font-size: 15px;font-weight:normal ;color: #35363b;margin-left: 10%;margin: 10%;">历史检测新闻总数</span>
                                          </div>
                                          <!--<div class="grid-num"></div>-->
                                      </div>
                                  </div>
                              </el-card>
                          </el-col>
                        <!--<el-col :span="8" style="padding: 0px;margin-top:-2px;margin-left: -1%;margin-right: -1%;">-->
                          <el-col :span="8" style="">
                              <el-card :body-style="{padding: '0px',shadow:'never'}" style="border-radius: 0;box-shadow: 0 0px 0px 0 rgba(0,0,0,.1);" >
                                  <div class="grid-content grid-con-1" style="height:90px;color:#E47470;background-color: white ">
                                      <div class="grid-con-text">
                                          <div class="iconof1" style="margin-left:10%;background-color: #e47470;align-items: center;border-radius:15px;">
                                            <span style="color: #ffffff">
                                              <i class="el-icon-top" style="font-size: 45px;margin-top: 15%;"></i>
                                            </span>

                                          </div>
                                      </div>

                                      <!--<el-divider direction="vertical" class="el-div"></el-divider>-->
                                      <div class="grid-cont-right1" style="margin-left: -140px;width:50px;">
                                          <div class="right-text">

                                              <span class="grid-num" style="font-size: 28px;color: #35363b;">{{history_pos_count}} 条</span>
                                          </div>
                                          <div class="right-text" >
                                              <span class="grid-text" style="font-size: 15px;font-weight:normal ;color: #35363b;margin-left: 10%;margin: 10%;">历史检测正面新闻总数</span>
                                              <!--<span class="grid-num">{{today_negative_count}} 条</span>-->
                                          </div>

                                      </div>
                                  </div>
                              </el-card>
                          </el-col>
                        <!--<el-col :span="8" style="padding: 0px;margin-top:-2px;margin-left: -1%;margin-right: -1%;">-->
                          <el-col :span="8" style="">
                              <el-card :body-style="{padding: '0px',shadow:'never'}" style="border-radius: 0;box-shadow: 0 0px 0px 0 rgba(0,0,0,.1);" shadow="never">
                                  <div class="grid-content grid-con-1" style="height:90px;color:#E47470;background-color: white ">
                                      <div class="grid-con-text">
                                          <div class="iconof1" style="margin-left:10%;background-color: #8dbf6a;border-radius:15px;">
                                            <span style="color: #ffffff">
                                              <i class="el-icon-bottom" style="font-size: 45px;margin-top: 15%;"></i>
                                            </span>

                                          </div>
                                      </div>

                                      <!--<el-divider direction="vertical" class="el-div"></el-divider>-->
                                      <div class="grid-cont-right1" style="margin-left: -140px;width:50px;">
                                          <div class="right-text">

                                              <span class="grid-num" style="align: left;font-size: 28px;color: #35363b;">{{history_neg_count}} 条</span>
                                          </div>
                                          <div class="right-text">
                                              <span class="grid-text" style="font-size: 15px;font-weight:normal ;color: #35363b;margin-left: 10%;margin: 10%">历史检测负面新闻总数</span>

                                          </div>

                                      </div>
                                  </div>
                              </el-card>
                          </el-col>
                      </el-row>
                      <el-row :gutter="20" >
                          <!--<el-col :span="4">-->
                            <!--<div id="history_sum" style="width:300px;height:400px;">-->
                            <!--</div>-->
                          <!--</el-col>-->
                          <el-col :span="10">
                            <div id="history_trend" style="width:800px;height:400px;"></div>
                          </el-col>
                          <el-col :span="14">
                            <div id="hot_theme_sen_dis" style="width:800px;min-height:400px;"></div>
                          </el-col>
                      </el-row>
                    </el-card>
              </el-row>

            </el-main>
        </el-container>
    </div>


</template>
<script>
import "echarts/dist/extension/dataTool";
import echarts from 'echarts'
Date.prototype.Format = function (fmt) {
  // author: meizz
  var o = {
    "M+": this.getMonth() + 1, // 月份
    "d+": this.getDate(), // 日
    "h+": this.getHours(), // 小时
    "m+": this.getMinutes(), // 分
    "s+": this.getSeconds(), // 秒
    "q+": Math.floor((this.getMonth() + 3) / 3), // 季度
    S: this.getMilliseconds(), // 毫秒
  };
  if (/(y+)/.test(fmt))
    fmt = fmt.replace(
      RegExp.$1,
      (this.getFullYear() + "").substr(4 - RegExp.$1.length)
    );
  for (var k in o)
    if (new RegExp("(" + k + ")").test(fmt))
      fmt = fmt.replace(
        RegExp.$1,
        RegExp.$1.length == 1 ? o[k] : ("00" + o[k]).substr(("" + o[k]).length)
      );
  return fmt;
};
import { fetchData } from '../../api/index';
const sentimenturl = "http://115.236.52.123:6012/api/sentiment";
const realurl = "http://115.236.52.123:6012/api/getRealTimeSentimentInfo";
// const score = 0.5;
export default {
    name: 'basetable',
    data() {
        return {
            text: '',
            summaryText: '9月8日上午，全国抗击新冠肺炎疫情表彰大会在北京人民大会堂隆重举行。已84岁高龄的中国工程院院士、广州医科大学附属第一医院国家呼吸系统疾病临床医学研究中心主任钟南山获颁“共和国勋章”。',
            sentimentscore:0,
            history:{},

            today_positive_count: 0,
            today_negative_count: 0,

            pos_news: [],
            neg_news:[],
            today_pos_trend:[],
            today_neg_trend:[],
            news: {
                news: '',
                url: '',
                score: '',
                publish_time: ''
            },
            one_week_time : [],
            history_pos_count:0,
            history_neg_count:0,
            history_pos_trend:[],
            history_neg_trend:[],
            hot_theme_dis:{},
            classification:'',
            style_sen:"",
            source_pos:[],
            source_neg:[],
            source:['education教育','entertainment娱乐','finance经济','politics','society','sports','technology'],
            // todaydatatest: [[1,2,3,4,5,6,7,8,9,10,11, 12, 13, 14, 15,16,17],[150, 232, 201, 154, 190, 330, 410]]
            lastupdatetime: new Date().Format("yyyy-MM-dd hh:mm:ss"),

            // "positive_news": [],  //列表每个item为字典形式, {"news": str, "url": str, "score": float, "publish_time": str}, 每个列表最多包含20条
            // "negative_news": []   //列表每个item为字典形式, {"news": str, "url": str, "score": float, "publish_time": str}, 每个列表最多包含20条

        };

    },
    created() {
         // this.getData();
    },
    mounted() {

        // this.drawProgress("emotionLevel",this.sentimentscore);

        // this.getRealTimeSentimentInfo();
        this.ResultofSentiment();

        const refreshTime = 5 * 60 * 1000;
        var that = this;
        this.getDay();
        var func = function () {
          that.lastupdatetime = new Date().Format("yyyy-MM-dd hh:mm:ss");
          that.getRealTimeSentimentInfo();
        };
        func();
        setInterval(func, refreshTime);
        // setTimeout(()=>{
        //   this.drawSum('history_sum',this.history_pos_count,this.history_neg_count);
        // })
        // this.drawToday('today_emotionLevel',this.todaydatatest);
        // this.drawHistory('historyChart');
        // this.getDay();
        // this.$nextTick(function() {
        //   this.drawHistory("lineChart");
        // });
        // this.$nextTick(function() {
        // });
        // this.init()
    },
    methods: {
        ResultofSentiment() {
            fetch(sentimenturl, {
                method: "POST",
                body: JSON.stringify({
                  docs: [{
                        "id":0,
                        "doc":this.summaryText,
                  }]
                }),
                headers: {
                  "Content-Type": "application/json",
                },
            })
            .then((res) => res.json())
            .catch((error) => console.error("Error:", error))
            .then((response) => {
                this.classification = response.results[0].data;
                if (this.classification == '负面')
                {
                  this.sentimentscore = -parseFloat(response.results[0].score).toFixed(2);
                  this.classification = '情感偏'+this.classification+'('+this.sentimentscore*(-100)+'%)';
                  this.style_sen = "color: #6B2A4A;font-size: 20px;";
                }else {
                  this.sentimentscore =  parseFloat(response.results[0].score).toFixed(2);
                  this.classification = '情感偏'+this.classification+'('+ this.sentimentscore*100 +'%)';
                  this.style_sen = "color: #E47470;font-size: 20px;";
                }

                // this.drawDashboard("emotionLevel",this.sentimentscore,this.classification);
                this.drawProgress("emotionLevel",this.sentimentscore)
            })
            // this.drawDashboard("emotionLevel",this.sentimentscore);
            //this.$message.success("提交成功！");
        },
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
        getDay(){
            for(var i = 0; i > -7; i--){
                this.one_week_time.push(this.getBeforeDate(i));
            }
        },
        getRealTimeSentimentInfo() {
            // 获取实时新闻列表
            fetch(realurl, {
            method: "GET",
            headers: {
              "Content-Type": "application/json",
            },
            })
            .then((res) => res.json())
            .catch((error) => console.error("Error:", error))
            .then((response) => {
                // console.log(response);
                this.today_positive_count = response.results.today_positive_count;
                this.today_negative_count = response.results.today_negative_count;
                this.history_pos_count = response.results.nearly_one_week_positive_count;
                this.history_neg_count = response.results.nearly_one_week_negative_count;
                this.pos_news = response.results.positive_news;
                this.neg_news = response.results.negative_news;
                this.today_pos_trend = response.results.today_positive_news_increase_trend;//,  //每个item为{"timestamp": str, "count": int}
                this.today_neg_trend = response.results.today_negative_news_increase_trend;//": [],  //每个item为{"timestamp": str, "count": int}
                this.history_pos_trend = response.results.nearly_one_week_positive_news_increase_trend; // int列表
                this.history_neg_trend = response.results.nearly_one_week_negative_news_increase_trend;
              // "nearly_one_week_negative_news_increase_trend": []
                this.hot_theme_dis = response.results.hot_theme_sentiment_distribution;
                //一天每小时增长图
                var pos_count = [];
                var neg_count = [];
                var each_hour = [];
                for (let i = 0; i < 24; i++) {
                    pos_count.push(this.today_pos_trend[i].count);
                    neg_count.push(this.today_neg_trend[i].count);
                    each_hour.push(this.today_pos_trend[i].timestamp);
                }
                //热门主题情感分布

                this.source_pos.push(this.hot_theme_dis.education.positive_count);
                this.source_pos.push(this.hot_theme_dis.entertainment.positive_count);
                this.source_pos.push(this.hot_theme_dis.finance.positive_count);
                this.source_pos.push(this.hot_theme_dis.politics.positive_count);
                this.source_pos.push(this.hot_theme_dis.society.positive_count);
                this.source_pos.push(this.hot_theme_dis.sports.positive_count);
                this.source_pos.push(this.hot_theme_dis.technology.positive_count);
                this.source_neg.push(-this.hot_theme_dis.education.negative_count);
                this.source_neg.push(-this.hot_theme_dis.entertainment.negative_count);
                this.source_neg.push(-this.hot_theme_dis.finance.negative_count);
                this.source_neg.push(-this.hot_theme_dis.politics.negative_count);
                this.source_neg.push(-this.hot_theme_dis.society.negative_count);
                this.source_neg.push(-this.hot_theme_dis.sports.negative_count);
                this.source_neg.push(-this.hot_theme_dis.technology.negative_count);
                // this.source[1]=this.hot_theme_dis.entertainment;
                // this.source[2]=this.hot_theme_dis.finance;
                // this.source[3]=this.hot_theme_dis.politics;
                // this.source[4]=this.hot_theme_dis.society;
                // this.source[5]=this.hot_theme_dis.sports;
                // this.source[6]=(this.hot_theme_dis.technology;

                     // this.source = a.concat(b);


                this.drawToday('today_emotionLevel',pos_count,neg_count,each_hour);
                // this.drawSum('history_sum',this.history_pos_count,this.history_neg_count);
                this.drawTrend('history_trend',this.history_pos_trend,this.history_neg_trend,this.one_week_time.reverse());

                this.drawHotDis('hot_theme_sen_dis',this.source_pos,this.source_neg);
                console.log(this.source_pos)
                console.log(this.source_neg)

                //
            });
        },
        drawHistory(id){
            // 基于准备好的dom，初始化echarts实例
            this.charts = echarts.init(document.getElementById(id));
            // 初始化数据 && 设置窗口自适应大小
            // this.lineChart.setOption(this.echartOption, window.onresize = this.lineChart.resize);
            var option = {
              color:['#E47470','#7EBF50', '#589EF8'],
              legend: {},
              tooltip: {
                  trigger: 'axis',
                  showContent: false
              },
              dataset: {
                  source: [
                      ['sentiment', '周一', '周二', '周三', '周四', '周五', '周六','周日'],
                      ['积极', 41.1, 30.4, 65.1, 53.3, 83.8, 98.7, 90],
                      ['消极', 86.5, 92.1, 85.7, 83.1, 73.4, 55.1, 10],

                      // ['未知', 55.2, 67.1, 69.2, 72.4, 53.9, 39.1]
                  ]
              },
              xAxis: {type: 'category'},
              yAxis: {
                  gridIndex: 0,
                  // type: 'value',
                  //   name: '元/币',
                  //   splitLine: {
                  //       show: false//是否显示分隔线。默认数值轴显示，类目轴不显示。
                  //   },
                  //   nameGap: 15,
                  //   axisTick: {
                  //       inside: true
                  //   }

              },
              grid: {top: '55%'},
              series: [
                  {type: 'line', smooth: true, seriesLayoutBy: 'row'},
                  {type: 'line', smooth: true, seriesLayoutBy: 'row'},
                  {type: 'line', smooth: true, seriesLayoutBy: 'row'},
                  {
                      type: 'pie',
                      id: 'pie',
                      radius: '30%',
                      center: ['50%', '25%'],
                      label: {
                          formatter: '{b}: {@周一} ({d}%)'
                      },
                      encode: {
                          itemName: 'sentiment',
                          value: '周一',
                          tooltip: '周一'
                      }
                  }
              ]
            }
            this.charts.on('updateAxisPointer', event =>  {
                var xAxisInfo = event.axesInfo[0];
                if (xAxisInfo) {
                    var dimension = xAxisInfo.value + 1;
                    this.charts.setOption({
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
            // var option = {
            //     title: {
            //         text: '近期币值走势'
            //     },
            //     tooltip: {
            //         trigger: 'axis', //坐标轴触发，主要在柱状图，折线图等会使用类目轴的图表中使用。
            //     },
            //     xAxis: {
            //         type: 'category',//类目轴，适用于离散的类目数据，为该类型时必须通过 data 设置类目数据。
            //         name: '日期',//坐标轴名称
            //         boundaryGap: false,
            //         data: one_week_time.reverse(),
            //         nameGap: 7,//坐标轴名称与轴线之间的距离。
            //         axisTick: {//是否显示坐标轴刻度。
            //             inside: true//坐标轴刻度是否朝内，默认朝外。
            //         }
            //     },
            //     yAxis: {
            //         type: 'value',
            //         name: '元/币',
            //         splitLine: {
            //             show: false//是否显示分隔线。默认数值轴显示，类目轴不显示。
            //         },
            //         nameGap: 15,
            //         axisTick: {
            //             inside: true
            //         }
            //     },
            //     series: [{
            //         type: 'line',//线条
            //         name: '币值',//系列名称，用于tooltip的显示
            //         data: [0.2, 0.5, 0.8, 1, 1.5, 2],
            //         symbol: 'circle',//标记的类型：圆圈
            //         itemStyle: {
            //             normal: {
            //                 shadowBlur: 50,//文字块的背景阴影长度。
            //                 shadowColor: 'red',//文字块的背景阴影颜色。
            //                 color: 'red',//图形的颜色
            //                 lineStyle: {
            //                     color: '#4d6dfd',//线的颜色
            //                     width: 1//线的宽度
            //                 }
            //             }
            //         }
            //     }],
            // };
            this.charts.setOption(option);
            window.addEventListener("resize", function() {
              this.charts.resize()
            })
        },
        // drawPie(id) {
        //   this.charts = echarts.init(document.getElementById(id));
        //   var option = {
        //       legend: {},
        //       tooltip: {
        //           trigger: 'axis',
        //           showContent: false
        //       },
        //       dataset: {
        //           source: [
        //               ['product', '2012', '2013', '2014', '2015', '2016', '2017'],
        //               ['Matcha Latte', 41.1, 30.4, 65.1, 53.3, 83.8, 98.7],
        //               ['Milk Tea', 86.5, 92.1, 85.7, 83.1, 73.4, 55.1],
        //               ['Cheese Cocoa', 24.1, 67.2, 79.5, 86.4, 65.2, 82.5],
        //               ['Walnut Brownie', 55.2, 67.1, 69.2, 72.4, 53.9, 39.1]
        //           ]
        //       },
        //       xAxis: {type: 'category'},
        //       yAxis: {gridIndex: 0},
        //       grid: {top: '55%'},
        //       series: [
        //           {type: 'line', smooth: true, seriesLayoutBy: 'row'},
        //           {type: 'line', smooth: true, seriesLayoutBy: 'row'},
        //           {type: 'line', smooth: true, seriesLayoutBy: 'row'},
        //           {type: 'line', smooth: true, seriesLayoutBy: 'row'},
        //           {
        //               type: 'pie',
        //               id: 'pie',
        //               radius: '30%',
        //               center: ['50%', '25%'],
        //               label: {
        //                   formatter: '{b}: {@2012} ({d}%)'
        //               },
        //               encode: {
        //                   itemName: 'product',
        //                   value: '2012',
        //                   tooltip: '2012'
        //               }
        //           }
        //       ]
        //     }
        //   this.charts.on('updateAxisPointer', event =>  {
        //         var xAxisInfo = event.axesInfo[0];
        //         if (xAxisInfo) {
        //             var dimension = xAxisInfo.value + 1;
        //             this.charts.setOption({
        //                 series: {
        //                     id: 'pie',
        //                     label: {
        //                         formatter: '{b}: {@[' + dimension + ']} ({d}%)'
        //                     },
        //                     encode: {
        //                         value: dimension,
        //                         tooltip: dimension
        //                     }
        //                 }
        //             });
        //         }
        //   });
        //   this.charts.setOption(option);
        //   window.addEventListener("resize", function() {
        //       this.charts.resize()
        //   })
        //
        //   // this.charts.setOption({
        //   //   tooltip: {
        //   //     trigger: "item",
        //   //     formatter: "{a}<br/>{b}:{c} ({d}%)"
        //   //   },
        //   //   legend: {
        //   //     bottom: 10,
        //   //     left: "center",
        //   //     data: this.opinion
        //   //   },
        //   //   series: [
        //   //     {
        //   //       name: "状态",
        //   //       type: "pie",
        //   //       radius: "65%",
        //   //       center: ["50%", "50%"],
        //   //       avoidLabelOverlap: false,
        //   //       itemStyle: {
        //   //         emphasis: {
        //   //           shadowBlur: 10,
        //   //           shadowOffsetX: 0,
        //   //           shadowColor: "rgba(0, 0, 0, 0.5)"
        //   //         },
        //   //         color: function(params) {
        //   //           //自定义颜色
        //   //           var colorList = ["#4bb375", "#d24c47"];
        //   //           return colorList[params.dataIndex];
        //   //         }
        //   //       },
        //   //       data: this.opinionData
        //   //     }
        //   //   ]
        //   // });
        // },
        drawDashboard(id,score,classf){
            // this.charts = echarts.init(document.getElementById(id));
            // if (classf == '负面'){
            //     score = -score
            // };
            // var option = {
            //     // color:['#E47470','#7EBF50', '#589EF8'],
            //     tooltip: {
            //         formatter: '{a} <br/>{b} : {c}%'
            //     },
            //     toolbox: {
            //         feature: {
            //             restore: {},
            //             saveAsImage: {}
            //         }
            //     },
            //     series: [
            //         {
            //             name: '分类置信度',
            //             type: 'gauge',
            //             min: -1,
            //             max: 1,
            //             startAngle: 180,
            //             endAngle: 0,
            //             detail: {
            //                 // formatter: Math.abs(score)*100+'%',
            //                 formatter: Math.abs(score)*100+'%',
            //                 textStyle:{
            //                     fontSize:20
            //                 },
            //                 fontWeight: 'bolder'
            //             },
            //             data: [{
            //                 value: score,
            //                 name: '置信度',
            //
            //             }],
            //             title : {
            //                 textStyle: {       // 其余属性默认使用全局文本样式，详见TEXTSTYLE
            //                     fontWeight: 'bolder',
            //                     fontSize: 20,
            //                     fontStyle: 'italic',
            //                     color:'gray'
            //                 }
            //             },
            //             axisLine: {            // 坐标轴线
            //                  lineStyle: {       // 属性lineStyle控制线条样式
            //                      color: [[0.5, '#E47470'], [1, '#7EBF50']],
            //                      width:20
            //                  },
            //
            //
            //             },
            //             axisLabel:{
            //                 formatter: function (v){
            //                     switch (v + '') {
            //                         case '-1' : return '100';
            //                         case '0' : return '0';
            //                         case '1' : return '100';
            //                     }
            //                 },
            //
            //                 distance:-65,
            //                 textStyle:{
            //                     fontSize:15
            //                 }
            //             }
            //
            //         }
            //
            //     ]
            // };
            // this.charts.setOption(option);
            //
            // // setInterval(event =>  {
            // //     option.series[0].data[0].value = (Math.random() * 100).toFixed(2) - 0;
            // //     this.charts.setOption(option, true);
            // // },2000);
            // window.addEventListener("resize", () =>
            // {
            //     this.charts.resize();
            // });

        },
        drawProgress(id,score){
          this.charts = echarts.init(document.getElementById(id));
          // if (classf == '负面'){
          //     score_pos = 0
          // }else if(classf == '正面'){
          //   score_neg = 0
          // };
          var origindata = [100];
          if(score<0)
          {
            origindata = [-100];
          }
          var option = {
              // backgroundColor: '#0a1d53',
              grid: {
                left: '2%',
                top: '2%',
                right: '2%',
                bottom: '2%',
                containLabel: true
              },
              tooltip: {
                trigger: 'item',
                axisPointer: {
                  // 坐标轴指示器，坐标轴触发有效
                  type: 'shadow' // 默认为直线，可选为：'line' | 'shadow'
                }
              },
              // textStyle: {
              //   color: '#35363b'
              // },
              title: {
                    text: '情感偏',
                    x: "center",
                    top:'-50%',
                    textStyle:{//标题内容的样式
                        fontStyle:'normal',//主标题文字字体风格，默认normal，有italic(斜体),oblique(斜体)
                        fontWeight:"normal",//可选normal(正常)，bold(加粗)，bolder(加粗)，lighter(变细)，100|200|300|400|500...
                        fontSize:15//主题文字字体大小，默认为18px
                    },
                    color: '#000',
              },
              xAxis: {
                show: false,
                type: 'value',
                // inverse: true,
                splitLine: {
                  show: false
                },
              },
              yAxis: {
                show: true,
                type: 'category',
                data: [
                  ''
                ],
                axisTick: { show: false },
                axisLine: {
                  show: false,
                  lineStyle: {
                    color: '#bb7e43',
                  }
                },
                splitLine: {
                  show: false
                },
                inside: true,
                textStyle: {
                  color: '#000c45'
                }
              },
              series: [
                  {
                      type: 'bar',
                      itemStyle: {
                      normal: {
                          color: function (param){
                                if(param.value < 0)
                                {
                                  return '#E47470';
                                }else{
                                  return '#6B2A4A';
                                }

                            } ,
                          // color: '#6B2A4A', // 定义柱形的背景色
                          barBorderRadius: [15, 15, 15, 15] // 定义背景柱形的圆角
                      }
                    },
                    barGap: '-100%', // 设置柱形重合的重要步骤
                    data: origindata,
                    z: 0,
                    silent: true,
                    animation: false, // 关闭动画效果
                    barWidth: '20px' // 设置柱形宽度
                  },
                  {
                      type: 'bar',
                      data: [score*100],
                      barWidth: '20px',
                      barGap: '-100%', // 设置柱形重合的重要步骤
                      // label: {
                      //     normal: {
                      //     show: true, //是否显现，不显示的话设置成false
                      //     position: "bottom", //显示的位置
                      //
                      //     // formatter: function(param) {
                      //     //     return Math.abs(param.value)+'%';
                      //     // },
                      //     textStyle: {
                      //       //这个地方颜色是支持回调函数的这种的，如果是一种颜色则可以写成： color :'#1089E7'
                      //         color: '#000',
                      //         fontSize: "16",
                      //
                      //     }
                      //   }
                      // },
                      itemStyle:{
                            color: function (param){
                                if(param.value < 0)
                                {
                                  return '#6B2A4A';
                                }else{
                                  return '#E47470';
                                }

                            } ,
                            barBorderRadius: [15, 15,15, 15] // 定义柱形的圆角
                      },
                      animation: false, // 关闭动画效果
                  },

              ]
          }
          this.charts.setOption(option);

            // setInterval(event =>  {
            //     option.series[0].data[0].value = (Math.random() * 100).toFixed(2) - 0;
            //     this.charts.setOption(option, true);
            // },2000);
          window.addEventListener("resize", () =>
          {
              this.charts.resize();
          });

        },
        drawToday(id,pos,neg,hour){
          this.charts = echarts.init(document.getElementById(id));
          window.onresize = this.charts.resize;
          // window.onresize = this.percentCharts.resiz
          var option = {
            // color:['#8dbf6a','#eb7777'],
            // color:['#E9E9E9','#9EBACB'],
            color:['#9EBACB','#E9E9E9'],
            // color:['#E47470','#6B2A4A'],
            // title: {
            //     text: '近24小时增长图',
            //     textAlign: 'center',
            //     left:'260px'
            // },
            tooltip: {
                trigger: 'axis',
                formatter:function (params, ticket, callback) {
                  var res = '时间：'+params[0].name+':00'+'</br>'+params[0].marker+params[0].seriesName+':'+params[0].value+'</br>'+params[1].marker+params[1].seriesName+':'+params[1].value;
                  console.log("pare:",params);
                  return res;
                },
                textStyle:{
                        align:'left'
                },
                confine:true,
                position: function(point, params, dom, rect, size){
                  //其中params为当前鼠标的位置
                  return [point+20,'40%'];

                }
            },
            grid:{
                  x:50,
                  y:30,
                  x2:40,
                  y2:80,
                  borderWidth:10
	          },
            legend: {
                data: ['正面新闻', '负面新闻'],

                // orient: 'vertical',
                right: '6%',
            },
            xAxis: {
                  type: 'category',
                  name: '时间',
                  data: hour,
                  boundaryGap: false,
                  axisLabel: {
                        interval:0,
                        // rotate:90,
                        formatter:function(value) {
                            if (Math.abs(value) % 2 == 0) {
                              return value+':00';
                          }
                        },
                        //     if(parseInt(param.value) % 2 ==0)
                        //     {
                        //       return '{a}:00';
                        //     }else {
                        //       return "1";
                        //     }
                        // },
                        fontSize: '13',
                        fontFamily: '微软雅黑',
                        marginleft: '15px',
                        show: true,
                  },

            },
            yAxis: {
                // splitLine: {
                //     show: false
                // }
                type: 'value',
                name: '增长数量',
                splitLine:{
                      show:true,
                      lineStyle:{
                        width:0.35

                      }
                },
              // nameTextStyle:{
              //     fontSize:14,
              //     fontWeight: 700,
              // }
            },
            series: [
                {
                    name: '正面新闻',
                    type: 'line',
                    data: pos,
                    smooth: true,
                    areaStyle: {}
                },
                {
                    name: '负面新闻',
                    type: 'line',
                    data: neg,
                    smooth: true,
                    areaStyle: {}
                },
            ]
          }
          //防止越界，重绘canvas
          // window.onresize = this.charts.resize;
          this.charts.setOption(option);
          window.onresize = () => {
                  this.charts.resize();
                // this.percentCharts.resize();

                // let height = this.$refs.asideContainer.offsetHeight;
                // this.$refs.mainContainer.offsetHeight = height;

                //如果有多个表变动在下方依次写下去就可以了
              }
          // window.addEventListener("resize", () =>
          // {
          //     this.charts.resize();
          // });
        },
        drawWeek(id,pos,neg,week){
          this.charts = echarts.init(document.getElementById(id));
          var option = {
            color:['#8dbf6a','#eb7777'],
            title: {
                text: '近七天增长图',
                textAlign: 'center',
                left:'260px'
            },
            tooltip: {
                trigger: 'axis'
            },
            legend: {
                data: ['正面新闻', '负面新闻'],
                orient: 'vertical',
                right: '10%',
            },
            toolbox: {
              feature: {
                  saveAsImage: {}
              }
            },
            xAxis: {
                  type: 'category',
                  name: '日期',
                  data: hour,
                  axisLabel: {
                        interval:0,
                        rotate:90,
                        formatter:'{value}:00',
                        fontSize: '14',
                        fontFamily: '微软雅黑',
                        marginleft: '15px',
                        show: true,
                  },

            },
            yAxis: {
                // splitLine: {
                //     show: false
                // }
                type: 'value',
                name: '增长数量',
            },
            series: [
                {
                    name: '正面新闻',
                    type: 'line',
                    data: pos,
                    smooth: true
                },
                {
                    name: '负面新闻',
                    type: 'line',
                    data: neg,
                    smooth: true
                },
            ]
          }
          this.charts.setOption(option);
          window.addEventListener("resize", () =>
          {
              this.charts.resize();
          });

        },
        drawSum(id,pos,neg){
          this.charts = echarts.init(document.getElementById(id));
          var option = {
              color:['#8dbf6a','#eb7777'],
              title: {
                  text: '历史分析总数',
                  left: 'center'
              },
              grid: {
                    width:'200px',
                    left: '6%',
                    right: '10%',
                    top: '30%',
                    containLabel: true
                },
              tooltip: {
                  trigger: 'item',
                  formatter: '<br/>{b} : {c} ({d}%)'
              },
              // legend: {
              //     orient: 'vertical',
              //     left: 'left',
              //     top: '15%',
              //     data: ['正面新闻', '负面新闻']
              // },
              series: [
                  {
                      type: 'pie',
                      radius: ['20%', '70%'],
                      center: ['50%', '60%'],
                      roseType: 'radius',
                      // roseType: 'area',
                      data: [
                          {value: pos, name: '正面新闻'},
                          {value: neg, name: '负面新闻'},
                      ],
                      emphasis: {
                          itemStyle: {
                              shadowBlur: 10,
                              shadowOffsetX: 0,
                              shadowColor: 'rgba(0, 0, 0, 0.5)'
                          }
                      }
                  }
              ]
          };
          this.charts.setOption(option);
          window.onresize = () => {
            this.charts.resize();
          }

        },
        drawSum_TWO(id){
          this.charts = echarts.init(document.getElementById(id));
          var option = {
                legend: {},
                tooltip: {
                    trigger: 'axis',
                    showContent: false
                },
                dataset: {
                    source: [
                        ['product', '2012', '2013', '2014', '2015', '2016', '2017'],
                        ['Matcha Latte', 41.1, 30.4, 65.1, 53.3, 83.8, 98.7],
                        ['Milk Tea', 86.5, 92.1, 85.7, 83.1, 73.4, 55.1],
                        ['Cheese Cocoa', 24.1, 67.2, 79.5, 86.4, 65.2, 82.5],
                        ['Walnut Brownie', 55.2, 67.1, 69.2, 72.4, 53.9, 39.1]
                    ]
                },
                xAxis: {type: 'category'},
                yAxis: {gridIndex: 0},
                grid: {top: '55%'},
                series: [
                    {type: 'line', smooth: true, seriesLayoutBy: 'row'},
                    {type: 'line', smooth: true, seriesLayoutBy: 'row'},
                    {type: 'line', smooth: true, seriesLayoutBy: 'row'},
                    {type: 'line', smooth: true, seriesLayoutBy: 'row'},
                    {
                        type: 'pie',
                        id: 'pie',
                        radius: '30%',
                        center: ['50%', '25%'],
                        label: {
                            formatter: '{b}: {@2012} ({d}%)'
                        },
                        encode: {
                            itemName: 'product',
                            value: '2012',
                            tooltip: '2012'
                        }
                    }
                ]
          };
          this.charts.on('updateAxisPointer', function (event) {
              var xAxisInfo = event.axesInfo[2];
              if (xAxisInfo) {
                  var dimension = xAxisInfo.value + 1;
                  this.charts.setOption({
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
          this.charts.setOption(option);
          window.addEventListener("resize", () =>
          {
              this.charts.resize();
          });

        },
        drawTrend(id,pos,neg,date_arr) {
          this.charts = echarts.init(document.getElementById(id));

          window.onresize = this.charts.resize;
          var option = {
            color:['#86c1f5','#E9E9E9'],
            // color: ['#7bbf67', '#e39fa1'].reverse(),
            // title: {
            //   text: '近七日增长图',
            //   textAlign: 'center',
            //   left: '190px'
            // },
            tooltip: {
              trigger: 'axis',
              axisPointer: {

              },
              formatter:function (params, ticket, callback) {
                  var res = '日期：'+params[0].name+'</br>'+params[0].marker+params[0].seriesName+':'+params[0].value+'</br>'+params[1].marker+params[1].seriesName+':'+params[1].value;
                  console.log("pare:",params);
                  return res;
                },
              textStyle:{
                        align:'left'
                },
                // confine:true,
               position: function(point, params, dom, rect, size){
                  //其中params为当前鼠标的位置
                  return [point+30,'40%'];

                }
            },
            legend: {
              data: ['正面新闻', '负面新闻'],
              left:'50%',

            },
            // toolbox: {
            //   feature: {
            //     saveAsImage: {}
            //   }
            // },

            grid:{
                  x:50,
                  y:30,
                  x2:260,
                  y2:115,
                  borderWidth:10
            },
            xAxis: {
              type: 'category',
              name: '时间',
              data: date_arr,
              boundaryGap: false,
              nameTextStyle:{
                  fontSize:14,
                  fontWeight: 700,
              }

            },
            yAxis: {
              // splitLine: {
              //     show: false
              // }
              type: 'value',
              name: '增长数量',
              splitLine:{
                  show:true,
                  lineStyle:{
                    width:0.35

                  }
              },
              nameTextStyle:{
                  fontSize:14,
                  fontWeight: 700,
              }
            },
            series: [
              {
                name: '正面新闻',
                type: 'line',
                data: pos,
                smooth: true,
                areaStyle: {}
              },
              {
                name: '负面新闻',
                type: 'line',
                data: neg,
                smooth: true,
                areaStyle: {}
              },
            ]

          };
          //防止越界，重绘canvas
          // window.onresize = this.charts.resize;
          this.charts.setOption(option);
          window.onresize = () => {
                this.charts.resize();
                // this.percentCharts.resize();

                // let height = this.$refs.asideContainer.offsetHeight;
                // this.$refs.mainContainer.offsetHeight = height;

                //如果有多个表变动在下方依次写下去就可以了
          }

          // window.addEventListener("resize", () =>
          // {
          //     this.charts.resize();
          // });
        },
        drawHotDis(id,pos,neg) {
           this.chart = echarts.init(document.getElementById(id));
           window.onresize = this.chart.resize;
           var option = {
                color:['#6eb4f8','#d2e2eb'],
                // color: ['#eb7777','#8dbf6a'],
                // color : ['#7db5e2', '#81cacc', '#cca8ba', "#7EBF50", "#82a0c5", '#fddb7e', '#bda29a', '#d2a59a', '#7f9979', '#c4ccd3','#5F9EA0','#a498d6'],
                // color:['rgb(210,100,93)','rgb(228,116,79)','rgb(242,176,110)','rgb(249,224,150)','rgb(255,254,198)','rgb(233,244,163)','rgb(181,219,169)','rgb(156,218,174)','rgb(125,191,166)','rgb(93,178,155)','rgb(74,134,183)','rgb(125,169,185)'].reverse(),
                // color:['rgb(215,121,118)','rgb(224,108,146)','rgb(175,110,195)','rgb(249,224,150)','rgb(255,254,198)','rgb(233,244,163)','rgb(181,219,169)','rgb(156,218,174)','rgb(125,191,166)','rgb(93,178,155)','rgb(74,134,183)','rgb(125,169,185)'].reverse(),
                // color:['rgb(227,158,156)','rgb(224,108,146)','rgb(197,151,212)','rgb(175,159,215)','rgb(160,169,214)','rgb(233,244,163)','rgb(181,219,169)','rgb(156,218,174)','rgb(125,191,166)','rgb(93,178,155)','rgb(74,144,173)','rgb(126,180,225)'].reverse(),
                // color:['#DC143C','#FFB6C1','#BA55D3','#483D8B','#1E90FF','#5F9EA0','#90EE90','#556B2F','#808000','#FFD700','#FFA500','#8B4513'],
                //标题
                tooltip: {
                      trigger: 'axis',
                      axisPointer: {            // 坐标轴指示器，坐标轴触发有效
                        type: 'shadow'        // 默认为直线，可选为：'line' | 'shadow'
                      },
                      axisLabel:{
                        fontColor:'#000',
                      },
                      confine:true,
                      formatter:function (params, ticket, callback) {
                        var res = '主题：'+params[0].name+'</br>'+params[0].marker+params[0].seriesName+':'+Math.abs(-params[0].value)+'</br>'+params[1].marker+params[1].seriesName+':'+Math.abs(params[1].value);
                        console.log("pare:",params);
                        return res;
                      },
                      fontColor:'#000',

                },
                // dataset: {data},
                grid: {
                    x:180,
                    y:30,
                    x2:175,
                    y2:115,
                    borderWidth:10
                },
                //工具箱
                //保存图片
                // toolbox:{
                //     show:true,
                //     feature:{
                //         saveAsImage:{
                //             show:true
                //         }
                //     }
                // },
                //图例-每一条数据的名字叫销量
                legend:{
                    data:['正面','负面'],
                    left:'63%',

                },
                //x轴没有显式设置，根据值自动生成x轴
                xAxis:[{
                    type: 'value',
                    name: '数量',
                    // nameTextStyle:{
                    //     fontSize:'15',
                    //     padding:10
                    // },
                    axisLabel: {
                        formatter:function(value)
                        {
                            return Math.abs(value)
                        },
                        fontColor:'#000',
                        fontFamily: '微软雅黑',
                        show: true,
                    },
                    nameTextStyle:{
                        fontSize:14,
                        fontWeight: 700,
                        fontColor:'#000',
                    }
                }],
                //y轴
                yAxis:[{
                    type: 'category',
                    name: '主题',
                    axisTick: {
                        show: false
                    },
                    data: ['教育','娱乐','经济','政治','社会','体育','科技'],
                    splitLine:{
                      show:true,
                      lineStyle:{
                        width:0.25

                      }

                    },
                    nameTextStyle:{
                        fontSize:14,
                        fontWeight: 700,
                    }
                    // seriesLayoutBy: 'column',
                    // axisLine: {
                    //
                    // },
                }],

                //数据-data是最终要显示的数据

                /*  [+] Here I need Initial the series arr */
                series:[
                  {
                      name: '正面',
                      type: 'bar',
                      // barWidth : 30,//柱图宽度
                      label: {
                          show: true,
                          position: 'right',
                          color:'#000',

                      },
                      data: pos
                  },
                  {
                      name: '负面',
                      type: 'bar',
                      data: neg,
                      // barWidth : 30,//柱图宽度

                      label: {
                        normal: {
                            show: true,
                            position: 'left',
                            color:'#000',
                            formatter:function(v)
                            {
                              return Math.abs(v.data)
                            }
                        }
                          // formatter:function(data)
                          // {
                          //     return Math.abs(data)
                          // },
                          // show: true,
                          // position: 'left'
                      },

                  }
                ]
          };
          // var option = {
          //       tooltip: {
          //           trigger: 'axis',
          //           axisPointer: {            // 坐标轴指示器，坐标轴触发有效
          //               type: 'shadow'        // 默认为直线，可选为：'line' | 'shadow'
          //           }
          //       },
          //       legend: {
          //           data: ['利润', '支出', '收入']
          //       },
          //       grid: {
          //           left: '3%',
          //           right: '4%',
          //           bottom: '3%',
          //           containLabel: true
          //       },
          //       xAxis: [
          //           {
          //               type: 'value'
          //           }
          //       ],
          //       yAxis: [
          //           {
          //               type: 'category',
          //               axisTick: {
          //                   show: false
          //               },
          //               data: ['周一', '周二', '周三', '周四', '周五', '周六', '周日']
          //           }
          //       ],
          //       series: [
          //           {
          //               name: '利润',
          //               type: 'bar',
          //               label: {
          //                   show: true,
          //                   position: 'inside'
          //               },
          //               data: [200, 170, 240, 244, 200, 220, 210]
          //           },
          //           {
          //               name: '收入',
          //               type: 'bar',
          //               stack: '总量',
          //               label: {
          //                   show: true
          //               },
          //               data: [320, 302, 341, 374, 390, 450, 420]
          //           },
          //           {
          //               name: '支出',
          //               type: 'bar',
          //               stack: '总量',
          //               label: {
          //                   show: true,
          //                   position: 'left'
          //               },
          //               data: [-120, -132, -101, -134, -190, -230, -210]
          //           }
          //       ]
          //   };
          //防止越界，重绘canvas
          // window.onresize = this.chart.resize;
          this.chart.setOption(option);
          window.onresize = () => {
                this.chart.resize();
                // this.percentCharts.resize();

                // let height = this.$refs.asideContainer.offsetHeight;
                // this.$refs.mainContainer.offsetHeight = height;

                //如果有多个表变动在下方依次写下去就可以了
              }
          // window.addEventListener("resize", () =>
          // {
          //     this.chart.resize();
          // });
        },


        init() {
           const self = this;//因为箭头函数会改变this指向，指向windows。所以先把this保存
           setTimeout(() => {
              window.onresize = function() {
                  self.chart = echarts.init(self.$refs.myEchart);
                  self.chart.resize();
              }
           },20)
         }


    },
    watch: {
    echartOption(newVal, oldVal) {
        let newOption = JSON.stringify(newVal);
        let oldOption = JSON.stringify(oldVal);
        // newVal ，oldVal无function类型，故转化为string来深层对比
        if (newOption !== oldOption) {
            // 数据更改时更新echart
            // console.log('updateEchart');
            this.lineChart.setOption(this.echartOption);
        }
    }
},
    computed: {
        tableHeight: function () {
            var width = window.innerWidth * 0.5;
            var height = parseInt(width * 0.39);
            return height + 770;
        },
        echartOption() {
            let seriesArr = []
            this.echartData.forEach((item) => {
                seriesArr.push({
                    name: item.text,
                    type: 'line',
                    smooth: true, // 平滑
                    itemStyle: {
                        normal: {
                            color: item.color, // 设置折线折点颜色
                            lineStyle: {
                                color: item.color  // 设置折线线条颜色
                            }
                        }
                    },
                    data: item.dataLsit
                });
            });

            return {
                tooltip: {
                    trigger: 'axis'
                },
                legend: {
                    // x: '0px',图标位置
                    y: '400px',
                    data: this.echartData.map(item => item.text) // 图标名字
                },
                grid: {  // echart四边距离
                    top: '20px',
                    left: '8%',
                    right: '2%',
                    bottom: '30px',
                    containLabel: true

                },
                toolbox: {
                    feature: {
                        saveAsImage: {}
                    }
                },
                xAxis: {
                    type: 'category',
                    boundaryGap: false,
                    data: this.echartData[0].getXAxis // 横坐标都一样。故取默认第一个
                },
                yAxis: {
                    type: 'value'
                },
                series: seriesArr
            }
        }
    }


};
</script>

<style scoped>
    @import url("//unpkg.com/element-ui@2.13.2/lib/theme-chalk/index.css");
    .el-header/deep/, .el-footer/deep/ {
        font-size: 20px;
        color: black;
        text-align: center;
        line-height: 60px;
    }
    .res-textarea/deep/ {
        color: black; margin-top: 30px;box-shadow: 0 2px 4px rgba(0, 0, 0, .12), 0 0 6px rgba(0, 0, 0, .04)
    }
    .el-card {
        box-shadow: 0 8px 12px 0 rgba(0,0,0,.1);
    }

    .line-echarts-ii {
        width: 100%;
        height: 420px;
        margin-left: 20px;
        /*align : center;*/
    }
    .el-row {
        margin-bottom: 20px
    }
    .el-col {
        border-radius: 4px;
    }
    .bg-purple-dark {
        background: #99a9bf;
    }
    .bg-purple {
        background: #589ef8;
    }
    .iconof1{
      width: 80px;
      height: 70px;
      background-color: #589ef8;
      text-align: center;
    }
    .grid-cont-right1 {
        flex: 1;
        text-align: left;
        font-size: 14px;
        color: #f3fbf8;
        /*color: #35363b;*/
    }
    .right-text{
        margin-bottom: 5%;
        margin-top: 5%;
    }

    .right-text .grid-text {
        font-size: 22px;
        font-weight: bold;
        margin-left: 10%;
        margin: 10%;
    }
    .right-text .grid-num {
        /*font-size: 30px;*/
        /*font-weight: bold;*/
        /*margin-left: 10%;*/
        /*!*margin: 10%;*!*/
        /*color: white;*/
        font-size: 20px;
        font-weight: bold;
        margin-left: 10%;

    }

    .grid-con-1 .grid-con-text {
        flex: 1;
        /*width: 30px;*/

        /*flex-direction: row;*/
        font-weight: bold;
        font-size: 20px;
        /*width: 50%;*/
        /*height: 100%;*/
        text-align: center;
        /*color: #35363b;*/

        /*line-height: 100%;*/
        /*justify-content: center;*/
        /*color: #fff;*/
    }
    .grid-con-text .grid-num {
        font-size: 20px;
        font-weight:bolder;
        margin-left: 5%;
        margin: 5%;
    }

    .grid-con-text {
        /*width: 30px;*/
        /*flex: 1;*/
        /*!*flex-direction: row;*!*/
        /*!*font-weight:bolder;*!*/
        /*font-size:10px;*/
        /*!*width: 50%;*!*/
        /*!*height: 100%;*!*/
        /*text-align: center;*/
        /*!*line-height: 100%;*!*/
        /*!*justify-content: center;*!*/
        /*color: #35363b;*/
        flex: 1;
        /*flex-direction: row;*/
        /*font-weight:bolder;*/
        font-size:10px;
        /*width: 50%;*/
        /*height: 100%;*/
        text-align: center;
        /*line-height: 100%;*/
        /*justify-content: center;*/
        color: #fff;
    }
    .el-icon-s-data{
      font-size: 60px;
      margin-top: 10%;
    }
    .grid-text2{
        text-align: left;
        font-weight: bold;
        /*text-align: left;*/
        font-size: 18px;
        text-align: left;
        color: #f3fbf8
    }
    .grid-num2{
        font-size: 18px;
        font-weight: bold;
        text-align: center;
        margin-left:20%;
    }
    .div-text2{
        margin-bottom: 5px;
        margin-left: 10%;
        text-align: left;
    }
    .bg-purple-light {
        background: #e5e9f2;
    }
    .grid-content {
        flex-direction: row;
        display: flex;
        align-items: center;
        height: 100px;
        background: rgb(45, 140, 240);
        /*background-color: #488CE9;*/
    }

    .el-div{
        width: 1px;
        height: 70%;
    }
    .el-div-horizontal{
         margin: 8px 0;
         background: 0 0;
         border-top: 1px dashed #e8eaec;
     }
    #wrap{
        display: flex;
        height: 400px;
        justify-content: flex-start;
    }
    #pos_emoji{
      display: flex;
      height: 100px;
      justify-content: flex-start;
    }
    #neg_emoji{
      display: flex;
      height: 100px;
      justify-content: flex-start;

    }
    .showupdatetime {
      color: gray;
      font-size: 10px;
      text-align: right;
      margin-bottom: -1%;
    }

    a:link {color:#000000;}      /* 未访问链接*/
    a:visited {color:#000000;}  /* 已访问链接 */
    a:hover {color: #589ef8;}  /* 鼠标移动到链接上 */
    a:active {color: #589ef8;}  /* 鼠标点击时 */

</style>
<style>
.el-input__count{
    background-color: transparent !important;
    margin-bottom: -2%;
}
.el-card__body{
  box-shadow: none !important;
}
.el-col el-col-8{
  box-shadow: none !important;
  shadow:'nerver' !important;
}
</style>


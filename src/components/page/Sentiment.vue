<template>
    <div>
        <el-container>
            <el-header style="height: max-content;text-align: center;">
                <h1 style="color: gray">情感分析</h1>
            </el-header>
            <el-container >
                <el-main style="text-align: center;">
                    <el-input
                            type="textarea"
                            placeholder="请输入内容"
                            v-model="summaryText"
                            maxlength="400"
                            show-word-limit
                            :autosize="{ minRows: 5, maxRows: 8}"
                            clearable
                            style="box-shadow: 0 2px 4px rgba(0, 0, 0, .12), 0 0 6px rgba(0, 0, 0, .04); font-size: 15px"
                    >
                    </el-input>
                    <el-row style="margin-top: 30px; display: flex; justify-content: center">
                        <el-button v-on:click="ResultofSentiment" type="primary" style="background: #242f42; border: 0px">开始分析</el-button>
                        <el-button v-on:click="mockData">随机样例</el-button>
                    </el-row>
                    <el-card class="box-card" style="min-height: 250px;margin-top: 20px" align="middle">
                        <div slot="header" class="clearfix">
                            <span style="color: gray">本次分析结果</span>
                        </div>
                        <!--<div>-->
                            <!--{{sentimentscore}}-->
                        <!--</div>-->
                        <!--<div id="wrap">-->
                            <!--<div id="icon_positive">-->
                                <!--<i class="iconfont iconjijiqingxu"></i>-->
                            <!--</div>-->
                        <div align="middle" id="emotionLevel" style="height: 300px"></div>
                        <!--</div>-->
                    </el-card>
                    <el-card class="box-card" style="min-height: 300px;margin-top: 20px" align="middle">
                        <div slot="header" class="clearfix">
                            <span style="color: gray">历史分析结果</span>
                        </div>
                        <el-row :gutter="10" >
                            <el-col :span="12">
                                <el-card shadow="hover" :body-style="{padding: '0px'}">
                                    <div class="grid-content grid-con-1">
                                        <div class="grid-con-text">
                                            <div class="grid-num">历史检测总数</div>
                                            <div class="grid-num">{{history_count.history_negative_count+history_count.history_positive_count}} 条</div>
                                        </div>

                                        <el-divider direction="vertical" class="el-div"></el-divider>
                                        <div class="grid-cont-right1">
                                            <div class="right-text">
                                                <span class="grid-text">积极</span>
                                                <span class="grid-num">{{history_count.history_positive_count}} 条</span>
                                            </div>
                                            <div class="right-text">
                                                <span class="grid-text">消极</span>
                                                <span class="grid-num">{{history_count.history_negative_count}} 条</span>
                                            </div>
                                        </div>
                                    </div>
                                </el-card>
                            </el-col>
                            <el-col :span="4">
                                <el-card shadow="hover" :body-style="{padding: '0px'}">
                                    <div class="grid-content1 grid-con-2">
                                        <div class="grid-con-text">
                                            <div class="grid-text-2">近7日 </div>
                                            <el-divider class="el-div-horizontal"></el-divider>
                                            <div class="div-text2">
                                                <span class="grid-text2">总数</span>
                                                <span class="grid-num2">{{nearly_one_week_num = history_count.nearly_one_week_negative_count+history_count.nearly_one_week_positive_count}} 条</span>
                                            </div>
                                            <div class="div-text2">
                                                <span class="grid-text2">积极</span>
                                                <span class="grid-num2">{{history_count.nearly_one_week_positive_count}} 条</span>
                                            </div>
                                            <div class="div-text2">
                                                <span class="grid-text2">消极</span>
                                                <span class="grid-num2">{{history_count.nearly_one_week_negative_count}} 条</span>
                                            </div>
                                        </div>
                                    </div>
                                </el-card>
                            </el-col>
                            <el-col :span="4">
                                <el-card shadow="hover" :body-style="{padding: '0px'}">
                                    <div class="grid-content2 grid-con-2">
                                        <div class="grid-con-text">
                                            <div class="grid-text-2">近3日</div>
                                            <el-divider class="el-div-horizontal"></el-divider>
                                            <div class="div-text2">
                                                <span class="grid-text2">总数</span>
                                                <span class="grid-num2">{{nearly_three_days_num = history_count.nearly_three_days_negative_count+history_count.nearly_three_days_positive_count}} 条</span>
                                            </div>
                                            <div class="div-text2">
                                                <span class="grid-text2">积极</span>
                                                <span class="grid-num2">{{history_count.nearly_three_days_positive_count}} 条</span>
                                            </div>
                                            <div class="div-text2">
                                                <span class="grid-text2">消极</span>
                                                <span class="grid-num2">{{history_count.nearly_three_days_negative_count}} 条</span>
                                            </div>
                                        </div>
                                    </div>
                                </el-card>
                            </el-col>
                            <el-col :span="4">
                                <el-card shadow="hover" :body-style="{padding: '0px'}">
                                    <div class="grid-content3 grid-con-2">
                                        <div class="grid-con-text">
                                            <div class="grid-text-2">今日</div>
                                            <el-divider class="el-div-horizontal"></el-divider>
                                            <div class="div-text2">
                                                <span class="grid-text2">总数</span>
                                                <span class="grid-num2">{{today_num = history_count.today_negative_count+history_count.today_positive_count}} 条</span>
                                            </div>
                                            <div class="div-text2">
                                                <span class="grid-text2">积极</span>
                                                <span class="grid-num2">{{history_count.today_negative_count}} 条</span>
                                            </div>
                                            <div class="div-text2">
                                                <span class="grid-text2">消极</span>
                                                <span class="grid-num2">{{history_count.today_positive_count}} 条</span>
                                            </div>
                                        </div>
                                    </div>
                                </el-card>
                            </el-col>

                        </el-row>
                        <!--<el-col :span="16">-->
                            <!--<div class="grid-content grid-con-1">-->
                                <!--<i class="el-icon-lx-people grid-con-icon"></i>-->
                                <!--<div class="grid-cont-right">-->
                                    <!--<div class="grid-num">1234</div>-->
                                    <!--<div>历史信息</div>-->
                                <!--</div>-->
                            <!--</div>-->
                        <!--</el-col>-->
                        <!--<el-col :span="8">-->
                            <!--<el-card shadow="hover" :body-style="{padding: '0px'}">-->
                                <!--<div class="grid-content grid-con-2">-->
                                    <!--<i class="el-icon-lx-notice grid-con-icon"></i>-->
                                    <!--<div class="grid-cont-right">-->
                                        <!--<div class="grid-num">321</div>-->
                                        <!--<div>系统消息</div>-->
                                    <!--</div>-->
                                <!--</div>-->
                            <!--</el-card>-->
                        <!--</el-col>-->
                        <!--<el-col :span="8">-->
                            <!--<el-card shadow="hover" :body-style="{padding: '0px'}">-->
                                <!--<div class="grid-content grid-con-3">-->
                                    <!--<i class="el-icon-lx-goods grid-con-icon"></i>-->
                                    <!--<div class="grid-cont-right">-->
                                        <!--<div class="grid-num">5000</div>-->
                                        <!--<div>数量</div>-->
                                    <!--</div>-->
                                <!--</div>-->
                            <!--</el-card>-->
                        <!--</el-col>-->
                        <!--<div class="line-echarts" style="text-align: center;">-->
                        <div id="historyChart" style="min-height: 600px"></div>
                        <!--{{pos_news}}-->
                        <!--{{neg_news}}-->
                        {{one_week_time}}

                        <!--</div>-->
                    </el-card>
                </el-main>>
        </el-container>
        </el-container>
    </div>


</template>
<script>
import echarts from 'echarts'
import { fetchData } from '../../api/index';
const sentimenturl = "http://49.234.217.110:5000/api/sentiment";
const realurl = "http://49.234.217.110:5000/api/getRealTimeSentimentInfo";
export default {
    name: 'basetable',
    data() {
        return {
            text: '',
            summaryText: '',
            sentimentscore:0,
            history:{},
            history_count :{
                history_positive_count: 0,
                history_negative_count: 0,
                nearly_one_week_positive_count: 0,
                nearly_one_week_negative_count: 0,
                nearly_three_days_positive_count: 0,
                nearly_three_days_negative_count: 0,
                today_positive_count: 0,
                today_negative_count: 0,
                positive_news:[],
                negative_news:[]
            },
            pos_news: [],
            neg_news:[],
            news: {
                news: '',
                url: '',
                score: '',
                publish_time: ''
            },
            one_week_time : [],


            // "positive_news": [],  //列表每个item为字典形式, {"news": str, "url": str, "score": float, "publish_time": str}, 每个列表最多包含20条
            // "negative_news": []   //列表每个item为字典形式, {"news": str, "url": str, "score": float, "publish_time": str}, 每个列表最多包含20条

        };

    },
    created() {
         // this.getData();
    },
    mounted() {

        this.drawDashboard("emotionLevel",0);
        this.getRealTimeSentimentInfo();
        this.getDay();
        this.drawHistory('historyChart');
        // this.getDay();
        // this.$nextTick(function() {
        //   this.drawHistory("lineChart");
        // });
        // this.$nextTick(function() {
        // });
        this.init()
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
                this.sentimentscore = parseFloat(response.results[0].score*100).toFixed(2);
                this.drawDashboard("emotionLevel",this.sentimentscore);
            })
            // this.drawDashboard("emotionLevel",this.sentimentscore);
            //this.$message.success("提交成功！");
        },
        mockData(){
            this.summaryText='印度军方说，解放军的重型坦克和轻型坦克部署位置处在印度驻军的火力范围以内。印度驻军全副武装，拥有坦克和火炮的支援。据《今日印度》9月1日报道，印度陆军已经在斯潘古尔湖和楚舒勒之间的平原上部署了一个坦克团，这里也是8月底印度侵犯中国领土、与解放军发生冲突的位置附近。'
            this.ResultofSentiment()
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
                console.log(response);
                this.history_count = response.results;

                this.pos_news = response.results.positive_news;
                this.neg_news = response.results.negative_news;
                // this.positive_news = [
                //     positive_news.news,
                //     positive_news.url,
                //     positive_news.score,
                //     positive_news.publish_time,
                // ];

                // var news = response.results;
                // delete news.theme_count;
                //
                // this.newslist = [];
                // for (var key in news) {
                //
                //     this.newslist.push({
                //       kind: eng2cn[key],
                //       events: news[key],
                //     });
                // }
                // this.drawHistory();
                // this.drawPieChart();
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
                      ['中性', 24.1, 67.2, 79.5, 86.4, 65.2, 82.5, 0]
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
        drawDashboard(id,score){
            this.charts = echarts.init(document.getElementById(id));
            var option = {
                // color:['#E47470','#7EBF50', '#589EF8'],
                tooltip: {
                    formatter: '{a} <br/>{b} : {c}%'
                },
                toolbox: {
                    feature: {
                        restore: {},
                        saveAsImage: {}
                    }
                },
                series: [
                    {
                        name: '情感程度',
                        type: 'gauge',
                        detail: {
                            formatter: '{value}%',
                            textStyle:{
                                fontSize:20
                            }
                        },
                        data: [{
                            value: score,
                            name: '情感程度',

                        }],
                        title : {
                            textStyle: {       // 其余属性默认使用全局文本样式，详见TEXTSTYLE
                                fontWeight: 'bolder',
                                fontSize: 20,
                                fontStyle: 'italic',
                                color:'gray'
                            }
                        },
                        axisLine: {            // 坐标轴线
                             lineStyle: {       // 属性lineStyle控制线条样式
                                 color: [[0.2, '#E47470'], [0.8, '#DDA450'], [1, '#7EBF50']],
                                 // width:50
                             },


                        },
                        axisLabel:{

                            distance:-60,
                            textStyle:{
                                fontSize:15
                            }
                        }

                    }
                ]
            };
            this.charts.setOption(option);

            // setInterval(event =>  {
            //     option.series[0].data[0].value = (Math.random() * 100).toFixed(2) - 0;
            //     this.charts.setOption(option, true);
            // },2000);

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
            console.log('updateEchart');
            this.lineChart.setOption(this.echartOption);
        }
    }
},
    computed: {
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
    .el-header, .el-footer {
        font-size: 20px;
        color: black;
        text-align: center;
        line-height: 60px;
    }
    .res-textarea {
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
        margin-bottom: 20px;

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
    .grid-cont-right1 {
        flex: 1;
        text-align: left;
        font-size: 14px;
        color: #f3fbf8;

    }
    .right-text{
        margin-bottom: 10%;
        margin-top: 10%;
    }

    .right-text .grid-text {
        font-size: 28px;
        font-weight: bold;
        margin-left: 10%;
        margin: 10%;
    }
    .right-text .grid-num {
        font-size: 25px;
        font-weight: bold;
        margin-left: 10%;
        margin: 10%;
    }

    .grid-con-1 .grid-con-text {
        flex: 1;
        /*flex-direction: row;*/
        font-size: 30px;
        /*width: 50%;*/
        /*height: 100%;*/
        text-align: center;
        /*line-height: 100%;*/
        /*justify-content: center;*/
        color: #fff;
    }
    .grid-con-text .grid-num {
        font-size: 30px;
        font-weight: bold;
        margin-left: 10%;
        margin: 10%;
    }

    .grid-con-text {
        flex: 1;
        /*flex-direction: row;*/
        font-size:10px;
        /*width: 50%;*/
        /*height: 100%;*/
        text-align: center;
        /*line-height: 100%;*/
        /*justify-content: center;*/
        color: #fff;
    }
    .grid-text-2{
        font-size: 20px;
        font-weight: bold;
        text-align: center;
        /*justify-content: center;*/
        /*align-items: center;*/
    }
    .grid-text2{
        text-align: left;
        /*text-align: left;*/
        font-size: 20px;
        text-align: left;
        color: #f3fbf8
    }
    .grid-num2{
        font-size: 20px;
        /*font-weight: bold;*/
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
        height: 150px;
        background: rgb(45, 140, 240);
    }
    .grid-content1 {
        flex-direction: row;
        display: flex;
        align-items: center;
        height: 150px;
        background: #E47470;
    }
    .grid-content2 {
        flex-direction: row;
        display: flex;
        align-items: center;
        height: 150px;
        background: #DDA450;
    }
    .grid-content3 {
        flex-direction: row;
        display: flex;
        align-items: center;
        height: 150px;
        background: #7EBF50;
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
    }

</style>

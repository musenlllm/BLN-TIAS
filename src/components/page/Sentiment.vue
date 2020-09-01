<template>
    <div>
        <el-container>
            <el-header style="height: max-content">
                <h1 style="color: gray">情感分析</h1>
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
                    <el-button v-on:click="getData" type="primary" style="background: #242f42; border: 0px">开始分析</el-button>
                    <el-button >随机样例</el-button>
                </el-row>
            </el-header>
            <el-container >
                <el-aside style="margin-left: 20px; margin-top: 30px; text-align: center; width: 100%">
                    <el-card class="box-card" style="min-height: 300px">
                        <div slot="header" class="clearfix">
                            <span>本次分析结果</span>
                        </div>
                        <div id="pieReport" style="width: 400px;height: 300px;margin-left: 35%"></div>
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
                    </el-card>

                    <el-card class="box-card" style="min-height: 300px; margin-top: 20px">
                        <div slot="header" class="clearfix">
                            <span>历史分析结果</span>
                        </div>
                        <div class="line-echarts" style="margin-top: 20px">
                              <div class="line-echarts-ii" id="lineChart"></div>
                         </div>
                    </el-card>

                </el-aside>


                <!--<el-main style="text-align: center; margin-top: 10px">-->
                    <!--<el-card class="box-card">-->
                        <!--<div slot="header" class="clearfix">-->
                            <!--<span>可识别实体类别</span>-->
                        <!--</div>-->
                        <!--<div class="tag-group" style=" display: flex; justify-content: center; flex-direction: row; flex-wrap: wrap;">-->
                            <!--<el-tag style="width: 100px; margin-right: 10px;margin-bottom: 10px; border-radius: 4px; font-size: 15px; border: 0px;-->
                             <!--box-shadow: 0 2px 4px rgba(0, 0, 0, .12), 0 0 6px rgba(0, 0, 0, .04);"-->
                                    <!--v-for="item in itemtypes"-->
                                    <!--:key="item.label"-->
                                    <!--:type="item.type"-->
                                    <!--:color="item.color"-->
                                    <!--size="medium"-->
                                    <!--effect="dark">-->
                                <!--{{ item.label }}-->
                            <!--</el-tag>-->
                        <!--</div>-->
                    <!--</el-card>-->
                    <!--<el-card class="box-card" style="min-height: 174px; margin-top: 20px">-->
                        <!--<div slot="header" class="clearfix">-->
                            <!--<span>实体比例图</span>-->
                        <!--</div>-->
                        <!--<div id="percent" style="width: 600px;height: 600px;"></div>-->
                    <!--</el-card>-->

            <!--</el-main>-->
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
    export default {
        name: 'basetable',
        props: {
          echartData: { // 折线名
              type: Array,
              default: () => [
                  // {
                  //     text: '自定义1',
                  //     color: '#456ef4', // 折线图颜色
                  //     dataLsit: [120, 132, 101, 134, 90, 230, 210, 123], // 折线图数值
                  //     getXAxis: ['周一','周二','周三','周四','周五','周六','周日','周八'] // 目前只支持一条横坐标
                  // },
                  {
                      text: '消极',
                      color: '#63e0bb',
                      dataLsit: [91, 94, 70, 34, 90, 23, 11, 5],
                      getXAxis: ['周一','周二','周三','周四','周五','周六','周日']
                  },
                  {
                      text: '积极',
                      color: 'red',
                      dataLsit: [9, 6, 30, 66, 10, 77, 89, 95],
                      getXAxis: ['周一','周二','周三','周四','周五','周六','周日']
                  }
              ]
            }
         },

        data() {
            return {
                lineChart: {},
                summaryText: '',
                charts: "",
                  opinion: ["消极", "积极"],
                  opinionData: [
                    { value:40 , name: "消极", itemStyle: "#4bb375" },
                    { value:60 , name: "积极", itemStyle: "#d24c47" }
                  ]
            }
        },
        // data() {
        //     return {
        //         text: '',
        //         summaryText: '',
        //         summaryRes:'分析结果',
        //         queryURL:'http://61.135.242.193:5000/api/summarization',
        //         items: [
        //             // { type: '', label: '标签一' },
        //             // { type: 'success', label: '标签二' },
        //         ],
        //         // itemtypes:[
        //         //     { label: '人名', type: '' ,color: '#F56C6C'},
        //         //     { label: '地名', type: '' ,color:'#E6A23C'},
        //         //     { label: '组织机构名', type: '',color:'#409EFF' },
        //         //     { label: '时间', type: '' ,color: '#67C23A'},
        //         //     { label: '公司', type: '',color:'#242f42' },
        //         //     { label: '产品', type: '' ,color:'pink'},
        //         // ],
        //         treeData:{
        //         },
        //         percentData:[
        //         ],
        //         entData:[],
        //         treeCharts: '',
        //         percentCharts: '',
        //         // charts: '',
        //         // opinion:['直接访问','邮件营销','联盟广告','视频广告','搜索引擎'],
        //         // opinionData:[
        //         //     {value:335, name:'直接访问'},
        //         //     {value:310, name:'邮件营销'},
        //         //     {value:234, name:'联盟广告'},
        //         //     {value:135, name:'视频广告'},
        //         //     {value:1548, name:'搜索引擎'}
        //         // ]
        //     };
        // },
        created() {
             // this.getData();
        },
        mounted() {
            this.drawLine();
            this.$nextTick(function() {
              this.drawPie("pieReport");
            });
            this.init()
        },
        methods: {
            // 获取 easy-mock 的模拟数据
            getData() {
                // for(let j=0; j<this.items.length; j++){
                //     this.items.pop();
                // }
                this.items=[];
                this.percentData=[];
                this.entData=[];
                // this.treeData=[];
                // mock data
                var resStr = '[{"start":6,"end":7,"content":"中国","ent":"地点"},{"start":14,"end":15,"content":"宝马","ent":"组织"},{"start":41,"end":42,"content":"宝马","ent":"组织"},{"start":45,"end":47,"content":"瞿云涛","ent":"人名"},{"start":50,"end":51,"content":"宝马","ent":"组织"},{"start":55,"end":56,"content":"中国","ent":"地点"}]'
                // evel 转化为 数组
                var resArray=eval("("+resStr+")");
                // console.log(resArray)
                //无意义文字开头结尾位置
                var plainStart=0;
                var plainEnd=0;
                var resStart;
                var resEnd;
                var resEnt;
                var colorTemp;
                for (var i=0; i<resArray.length; i++){
                     resStart = Number(resArray[i].start);
                    resEnd = Number(resArray[i].end);
                    resEnt = resArray[i].ent;
                    //
                    // console.log(resArray[i])
                    // console.log("plainStart: "+plainStart)
                    // console.log("plainEnd:"+plainEnd)
                    // console.log("resStart: "+resStart)
                    // console.log("resEnd:"+resEnd)
                    plainEnd = resStart;
                    // console.log("plainEnd=resStart:"+plainEnd)
                    if(plainStart!==plainEnd){
                        // console.log("push无意义词")
                        // console.log("无意义词语： "+this.summaryText.slice(plainStart,plainEnd))
                        this.items.push({
                            label: this.summaryText.slice(plainStart,plainEnd),
                            color: 'gray',
                            type:'',
                            ent: '普通',
                            value:'1'
                        })
                    }
                    plainStart = resEnd+1;
                    plainEnd = resEnd+1;
                    if(resEnt=="地点"){
                        colorTemp = '#E6A23C'
                    }
                    else if(resEnt == "人名"){
                        console.log("人名检测！！！！")
                        colorTemp =  '#F56C6C'
                    }
                    else if(resEnt == "组织"){
                        colorTemp = '#409EFF'
                    }
                    else if(resEnt == "时间"){
                        colorTemp =  '#67C23A'
                    }
                    else if(resEnt == "公司"){
                        colorTemp = '#242f42'
                    }
                    else if(resEnt == "产品"){
                        colorTemp = 'pink'
                    }
                    // console.log("push意义词");
                    // console.log("意义词语: "+this.summaryText.slice(resStart,resEnd+1));
                    // console.log("颜色: "+colorTemp);
                    this.items.push({
                        label: this.summaryText.slice(resStart,resEnd+1),
                        color: colorTemp,
                        type: '',
                        ent: resEnt,
                        value:'1'
                    })
                }
                if ((resEnd+1)!=this.summaryText.length) {
                    this.items.push({
                        label: this.summaryText.slice(resEnd,this.summaryText.length),
                        color: 'gray',
                        type: '',
                        ent: '普通',
                        value:'1'
                    })
                }
                this.treeData.name="实体分类树";
                this.treeData.children=[];
                var addedEnt = [];
                for(let k=0;k<this.items.length;k++){
                    var entTemp = this.items[k].ent;
                    if(addedEnt.indexOf(entTemp)==-1 && entTemp!='普通'){
                        var treeDataItemTemp={};
                        treeDataItemTemp.name = entTemp;
                        treeDataItemTemp.children = [];
                        treeDataItemTemp.children.push({
                            name:this.items[k].label,
                            value:this.items[k].value
                        })
                        this.treeData.children.push(treeDataItemTemp);
                        addedEnt.push(entTemp);
                        continue
                    }
                    for(let h=0; h<this.treeData.children.length;h++){
                        if(this.treeData.children[h].name==entTemp){
                            this.treeData.children[h].children.push({
                                name:this.items[k].label,
                                value:this.items[k].value
                            })
                        }
                    }
                }
                // 准备数量比例饼图片
                this.entData = addedEnt;
                for(let i=0; i<this.treeData.children.length; i++){
                    let colorTemp;
                    let resEnt = this.treeData.children[i].name;
                    if(resEnt=="地点"){
                        colorTemp = '#E6A23C'
                    }
                    else if(resEnt == "人名"){
                        console.log("人名检测！！！！")
                        colorTemp =  '#F56C6C'
                    }
                    else if(resEnt == "组织"){
                        colorTemp = '#409EFF'
                    }
                    else if(resEnt == "时间"){
                        colorTemp =  '#67C23A'
                    }
                    else if(resEnt == "公司"){
                        colorTemp = '#242f42'
                    }
                    else if(resEnt == "产品"){
                        colorTemp = 'pink'
                    }
                    this.percentData.push({
                        name:this.treeData.children[i].name,
                        value: this.treeData.children[i].children.length,
                        itemStyle:{
                            color: colorTemp
                        }
                    })
                }
                console.log(this.treeData)
                // this.option.series[0].data=this.treeData
                this.drawTree()
                // console.log(this.items)
                // console.log(resData)
                // fetch(this.queryURL, {
                //     method: "POST",
                //     body: JSON.stringify({
                //         docs: [{
                //             "id":123,
                //             "doc":this.summaryText,
                //         }]
                //     }),
                //     headers: {
                //         "Content-Type": "application/json"
                //     },
                //
                // }).then(res => res.json())
                //     .catch(error => console.error('Error:', error))
                //     .then(response => this.summaryRes =  response.data[0].summary);
            },
            drawTree(){
                // const chart = this.$refs.chart
                // if (chart) {
                //     const myChart = this.$echarts.init(chart)
                //     console.log(this.option)
                //     myChart.setOption(this.option)
                //     window.addEventListener("resize", function() {
                //         myChart.resize()
                //     })
                // }
                this.treeCharts = echarts.init(document.getElementById('tree'));
                this.percentCharts = echarts.init(document.getElementById('percent'));
                // this.charts = echarts.init(document.getElementById('tree'))
                this.treeCharts.setOption({
                    tooltip: {
                        trigger: 'item',
                            triggerOn: 'mousemove'
                    },
                    series: [
                        {
                            type: 'tree',
                            data: [this.treeData],
                            top: '1%',
                            left: '7%',
                            bottom: '1%',
                            right: '20%',
                            symbolSize: 7,
                            label: {
                                position: 'left',
                                verticalAlign: 'middle',
                                align: 'right',
                                fontSize: 9
                            },
                            leaves: {
                                label: {
                                    position: 'right',
                                    verticalAlign: 'middle',
                                    align: 'left'
                                }
                            },
                            expandAndCollapse: true,
                            animationDuration: 550,
                            animationDurationUpdate: 750
                        }
                    ]
                },);
                this.percentCharts.setOption({
                    tooltip: {
                        trigger: 'item',
                        formatter: '{a} <br/>{b}: {c} ({d}%)'
                    },
                    legend: {
                        orient: 'vertical',
                        left: 5,
                        data: this.entData
                    },
                    series: [
                        {
                            name: '实体数量比例图',
                            type: 'pie',
                            radius: ['50%', '70%'],
                            avoidLabelOverlap: false,
                            label: {
                                show: false,
                                position: 'center'
                            },
                            emphasis: {
                                label: {
                                    show: true,
                                    fontSize: '30',
                                    fontWeight: 'bold'
                                }
                            },
                            labelLine: {
                                show: false
                            },
                            data: this.percentData
                        }
                    ]
                })
                window.addEventListener("resize", function() {
                            this.charts.resize()
                        })
            },
            drawLine(){
                // 基于准备好的dom，初始化echarts实例
              this.lineChart = echarts.init(document.getElementById('lineChart'));
              // 初始化数据 && 设置窗口自适应大小
              this.lineChart.setOption(this.echartOption, window.onresize = this.lineChart.resize);
            },
            drawPie(id) {
              this.charts = this.$echarts.init(document.getElementById(id));
              this.charts.setOption({
                tooltip: {
                  trigger: "item",
                  formatter: "{a}<br/>{b}:{c} ({d}%)"
                },
                legend: {
                  bottom: 10,
                  left: "center",
                  data: this.opinion
                },
                series: [
                  {
                    name: "状态",
                    type: "pie",
                    radius: "65%",
                    center: ["50%", "50%"],
                    avoidLabelOverlap: false,
                    itemStyle: {
                      emphasis: {
                        shadowBlur: 10,
                        shadowOffsetX: 0,
                        shadowColor: "rgba(0, 0, 0, 0.5)"
                      },
                      color: function(params) {
                        //自定义颜色
                        var colorList = ["#4bb375", "#d24c47"];
                        return colorList[params.dataIndex];
                      }
                    },
                    data: this.opinionData
                  }
                ]
              });
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
                        left: '1%',
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
</style>

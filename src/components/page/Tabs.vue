<template>
    <div>
        <el-container>
            <el-header style="height: max-content">
                <h1 style="color: gray">实体识别</h1>
                <el-input
                        type="textarea"
                        placeholder="请输入内容"
                        v-model="nerText"
                        maxlength="200"
                        show-word-limit
                        :autosize="{ minRows: 5, maxRows: 8}"
                        clearable
                        style="box-shadow: 0 2px 4px rgba(0, 0, 0, .12), 0 0 6px rgba(0, 0, 0, .04); font-size: 15px"
                >
                </el-input>
                <el-row style="margin-top: 30px; display: flex; justify-content: center">
                    <el-button v-on:click="getData" type="primary" style="background: #242f42; border: 0px">开始识别</el-button>
                    <!--<el-button v-on:click="mockData">随机样例</el-button>-->
                </el-row>
            </el-header>
            <el-container>
                <el-aside width="700px" style="margin-left: 20px; margin-top: 30px; text-align: center">
                    <el-card class="box-card" style="min-height: 174px" v-loading="resloading">
                        <div slot="header" class="clearfix">
                            <span style="font-size: 18px">识别结果</span>
                        </div>
                        <div class="tag-group" style="margin-top: 0; display: flex; flex-direction: row; flex-wrap: wrap;" v-loading="restypeloading">
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

                    <el-card class="box-card" style="min-height: 174px; margin-top: 20px">
                        <div slot="header" class="clearfix">
                            <span style="font-size: 18px">实体分类树</span>
                        </div>
                        <div id="tree" style="width: 600px;height: 600px;"></div>
                    </el-card>

                </el-aside>


                <el-main style="text-align: center; margin-top: 10px">
                    <el-card class="box-card">
                        <div slot="header" class="clearfix">
                            <span style="font-size: 18px">可识别实体类别</span>
                        </div>
                        <div class="tag-group" style=" display: flex; justify-content: center; flex-direction: row; flex-wrap: wrap;">
                            <el-tag style="width: 100px; margin-right: 10px;margin-bottom: 10px; border-radius: 4px; font-size: 15px; border: 0px;
                             box-shadow: 0 2px 4px rgba(0, 0, 0, .12), 0 0 6px rgba(0, 0, 0, .04);"
                                    v-for="item in itemtypes"
                                    :key="item.label"
                                    :type="item.type"
                                    :color="item.color"
                                    size="medium"
                                    effect="dark">
                                {{ item.label }}
                            </el-tag>
                        </div>
                    </el-card>
                    <el-card class="box-card" style="min-height: 174px; margin-top: 20px">
                        <div slot="header" class="clearfix">
                            <span style="font-size: 18px">实体比例图</span>
                        </div>
                        <div id="percent" style="width: 600px;height: 600px;"></div>
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
    export default {
        name: 'basetable',
        data() {
            return {
                text: '',
                nerText: '',
                nerRes:'实体命名识别结果',
                queryURL:'http://49.234.217.110:5000/api/ner',
                resloading: false,
                restypeloading: false,

                items: [
                    // { type: '', label: '标签一' },
                    // { type: 'success', label: '标签二' },

                ],
                itemtypes:[
                    { label: '人名', type: '' ,color: '#F56C6C'},
                    { label: '地名', type: '' ,color:'#E6A23C'},
                    { label: '组织机构名', type: '',color:'#409EFF' },
                    { label: '时间', type: '' ,color: '#67C23A'},
                    { label: '公司', type: '',color:'#242f42' },
                    { label: '产品', type: '' ,color:'pink'},
                ],
                treeData:{

                },
                percentData:[

                ],
                entData:[],

                treeCharts: '',
                percentCharts: '',
                resStr: '',
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
            this.mockData()
        },
        methods: {
            // 获取 easy-mock 的模拟数据
            getData() {
                this.resloading = true;
                this.restypeloading = true;
                this.items=[];
                this.percentData=[];
                this.entData=[];

                //clear the input text
                var tempText = this.clearText(this.nerText);
                // this.nerText = tempText;

                // mock data
                fetch(this.queryURL, {
                    method: "POST",
                    body: JSON.stringify({
                        docs: [{
                            "id":0,
                            "doc":tempText,
                        }]
                    }),
                    headers: {
                        "Content-Type": "application/json"
                    },

                }).then(res => res.json())
                    .catch(error => console.error('Error:', error))
                    .then( (responseJson) => {
                            this.resStr = JSON.stringify(responseJson.results[0].result)
                            console.log("resStr: "+this.resStr)
                            console.log("resStrType: "+typeof this.resStr)

                        var resArray=eval("("+this.resStr+")");
                        // var resArray=resStr
                        console.log("resArray: "+resArray)
                        console.log("resArrayType: "+ typeof resArray)
                        //无意义文字开头结尾位置
                        var plainStart=0;
                        var plainEnd=0;
                        var resStart;
                        var resEnd;
                        var resEnt;
                        var colorTemp;
                        var plainTextCharNum = 10
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
                                var numCuts = Math.floor((plainEnd - plainStart)/plainTextCharNum)
                                // var lastChar = (plainEnd - plainStart)%plainTextCharNum
                                for(let p=0;p<numCuts;p++){
                                    this.items.push({
                                        // label: this.nerText.slice(plainStart,plainStart+plainTextCharNum),
                                        label: tempText.slice(plainStart,plainStart+plainTextCharNum),
                                        color: 'gray',
                                        type:'',
                                        ent: '普通',
                                        value:'1'
                                    });
                                    plainStart = plainStart+plainTextCharNum;
                                }
                                this.items.push({
                                    // label: this.nerText.slice(plainStart,plainEnd),
                                    label: tempText.slice(plainStart,plainEnd),
                                    color: 'gray',
                                    type:'',
                                    ent: '普通',
                                    value:'1'
                                })
                                // console.log("push无意义词")
                                // console.log("无意义词语： "+this.nerText.slice(plainStart,plainEnd))
                                // this.items.push({
                                //     label: this.nerText.slice(plainStart,plainEnd),
                                //     color: 'gray',
                                //     type:'',
                                //     ent: '普通',
                                //     value:'1'
                                // })
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
                            // console.log("意义词语: "+this.nerText.slice(resStart,resEnd+1));
                            // console.log("颜色: "+colorTemp);
                            this.items.push({
                                // label: this.nerText.slice(resStart,resEnd+1),
                                label: tempText.slice(resStart,resEnd+1),
                                color: colorTemp,
                                type: '',
                                ent: resEnt,
                                value:'1'

                            })
                        }
                        // if ((resEnd+1)!=this.nerText.length) {
                        if ((resEnd+1)!=tempText.length) {

                            // var numCuts = Math.floor((this.nerText.length-plainEnd)/plainTextCharNum)
                            var numCuts = Math.floor((tempText.length-plainEnd)/plainTextCharNum)
                            // var lastChar = (plainEnd - plainStart)%6
                            for(let p=0;p<numCuts;p++){
                                this.items.push({
                                    // label: this.nerText.slice(plainEnd,plainEnd+plainTextCharNum),
                                    label: tempText.slice(plainEnd,plainEnd+plainTextCharNum),
                                    color: 'gray',
                                    type:'',
                                    ent: '普通',
                                    value:'1'
                                });
                                plainEnd = plainEnd+plainTextCharNum;
                            }
                            this.items.push({
                                // label: this.nerText.slice(plainEnd,this.nerText.length),
                                label: tempText.slice(plainEnd,tempText.length),
                                color: 'gray',
                                type:'',
                                ent: '普通',
                                value:'1'
                            })



                            //////////
                            // this.items.push({
                            //     label: this.nerText.slice(resEnd+1,this.nerText.length),
                            //     color: 'gray',
                            //     type: '',
                            //     ent: '普通',
                            //     value:'1'
                            // })
                        }

                        this.treeData.name="实体分类树";
                        this.treeData.children=[];
                        var addedEnt = [];

                        //构建实体分类树图的数据treeData,O(n^2)复杂度
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
                        // 准备实体数量比例数据
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
                        this.resloading = false;
                        this.restypeloading = false;

                        console.log(this.treeData)
                        // this.option.series[0].data=this.treeData
                        //画图
                        this.drawGraph()
                        }
                    )
                // var resStr = '[{"start":6,"end":7,"content":"中国","ent":"地点"},{"start":14,"end":15,"content":"宝马","ent":"组织"},{"start":41,"end":42,"content":"宝马","ent":"组织"},{"start":45,"end":47,"content":"瞿云涛","ent":"人名"},{"start":50,"end":51,"content":"宝马","ent":"组织"},{"start":55,"end":56,"content":"中国","ent":"地点"}]'
                // evel 转化为 数组


                // console.log(this.items)


                // console.log(resData)
                // fetch(this.queryURL, {
                //     method: "POST",
                //     body: JSON.stringify({
                //         docs: [{
                //             "id":123,
                //             "doc":this.nerText,
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
            drawGraph(){

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

                this.treeCharts.showLoading();
                this.percentCharts.showLoading();

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

                            symbolSize: 10,

                            label: {
                                position: 'left',
                                verticalAlign: 'middle',
                                align: 'right',
                                fontSize: 15
                            },

                            leaves: {
                                label: {
                                    position: 'right',
                                    verticalAlign: 'middle',
                                    align: 'left'
                                }
                            },

                            expandAndCollapse: true,
                            animationDuration: 1000,
                            animationDurationUpdate: 1000
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
                            right: "20%",
                            data: this.percentData
                        }
                    ]
                })
                this.treeCharts.hideLoading()
                this.percentCharts.hideLoading();
                window.addEventListener("resize", function() {
                            this.treeCharts.resize()
                            this.percentCharts.resize()
                        })

            },
            mockData(){
                this.nerText ='10月25日在北京的小米新品发布会上，雷军发布了一款概念手机小米MIX。该手机的设计师是当代著名的设计大师、民主设计和极简设计的倡导者菲利普·斯塔克。(请输入文本)'
                this.getData()
            },
            clearText(testStr) {
                var resultStr = testStr.replace(/\ +/g, "");
                resultStr = resultStr.replace(/\s+/g, "");
                resultStr = resultStr.replace(/[ ]/g, "");    //去掉空格
                resultStr = resultStr.replace(/[\r\n]/g, ""); //去掉回车换行
                if(this.nerText.indexOf("(请输入文本)")!=-1){
                    resultStr = resultStr.slice(0,resultStr.length-7)
                }

                return resultStr;
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






</style>


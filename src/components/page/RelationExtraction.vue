<template>
    <div>
        <el-container>
            <el-header>
                <h1 style="color: gray">关系抽取</h1>
            </el-header>
            <el-main style="text-align: center">
                <span style="font-size: 15px; color: gray">
                    关系抽取能够自动识别文本中实体之间所隐含的语义关系，如人物关系、从属关系、目的关系等。
                </span>
                
                <el-row style="margin-top: 20px">
                    <el-col :span="16">
                        <el-input
                        type="textarea"
                        placeholder="请输入内容"
                        v-model="content"
                        maxlength="800"
                        show-word-limit
                        :rows=16
                        clearable
                        style="box-shadow: 0 2px 4px rgba(0, 0, 0, .12), 0 0 6px rgba(0, 0, 0, .04)"
                        >
                        </el-input>
                        
                    </el-col>
                    
                    <el-col :span="8" style="padding-left:10px;max-height:200px;height:200px;overflow: auto;">
                        <el-card shadow="hover">
                                            
                    <template v-for="item in items">
                        <el-tag style="margin: 2px; border-radius: 0px; font-size: 15px"
                                :key="item.person1+item.id"
                                type="warning"
                                size="medium"
                                effect="dark">
                            {{ item.person1 }}
                        </el-tag>
                        ----
                        <el-tag style="margin: 2px; border-radius: 0px; font-size: 15px"
                                :key="item.relation+item.id"
                                type="danger"
                                size="medium"
                                effect="plain">
                            {{ item.relation }}
                        </el-tag>
                        ----
                        <el-tag style="margin: 2px; border-radius: 0px; font-size: 15px"
                                :key="item.person2+item.id"
                                type="warning"
                                size="medium"
                                effect="dark">
                            {{ item.person2 }}
                        </el-tag>
                    </template>
                        </el-card>
                    </el-col>
                </el-row>
                
                <el-row style="margin-top: 30px; display: flex; justify-content: center">
                    <el-button v-on:click="getData" type="primary">开始提取</el-button>
                </el-row>
                
            </el-main>
            <!--<el-footer>Footer</el-footer>-->
        </el-container>
        <div>
            <div id="showRelation" :style="{width: '1200px', height: '600px'}"></div>
        </div>
    </div>
</template>

<script>
import { fetchData } from '../../api/index';
import echarts from 'echarts/lib/echarts'
import 'echarts/dist/extension/dataTool'

export default {
    name: 'basetable',
    data() {
        return {
            text: '',
            content: '',
            queryURL:'http://61.135.242.193:5000/api/summarization',
            
            items: [
                // { type: '', label: '标签一' },
                // { type: 'success', label: '标签二' },
                {person1: '曹操', person2: '曹丕', relation: '父子', id:'1'}
            ]
        };
    },
    created() {
        // this.getData();
    },
    methods: {
        drawChart() {
            // 初始化echarts实例
            let myChart = echarts.init(document.getElementById('showRelation'));
            
            var theData = {    
                nodes:[{
                name: '曹丕', //	彰显节点
				x: 300,
                y: 300,
                category: 1,
                label: {
                show: true
            },
            }, {
                name: '曹操2', //	被覆盖节点
                x: 800,
                y: 300,
                symbolSize: 100,
                color: 'blue',
                category: 2,
                label: {
                show: false
            },
            },{
                name: '曹操',  
                x: 800,
                y: 300,
                symbolSize: 100,
                category: 2,
                color: 'blue'
            }, {
                name: '曹植',  
                x: 400,
                y: 400,
                category: 3
            }],
                links:[{
                source: 1,
                target: 0,
                value:'父子',
                lineStyle: {
                    width: 1,
                    curveness: 0.1
                }
            },{
                source: 1,
                target: 0,
                value:'父子',
                lineStyle: {
                    width: 1,
                    curveness: 0.2
                }
            },{
                source: 0,
                target: 3,
                value:'兄弟',
                lineStyle: {
                    width: 1,
                }
            },{
                source: 1,
                target: 3,
                value:'父子',
                lineStyle: {
                    width: 1,
                }
            }
            ]}
            
            var categories = [];
            for (var i = 0; i < 9; i++) {
                categories[i] = {
                    name: '类目' + i
                };
            }
            
            // 绘制图表
            var option = {
                title: {
                    text: '同方向多种联系'
                },
                series: [
                    {
                        type: 'graph',
                        layout: 'none',
                        symbolSize: 60,
                        label: {
                            show: true,
                            fontSize: 26
                        },
                        roam: true,
                        categories: categories,
                        itemStyle: {
                            borderColor: '#fff',
                            borderWidth: 1,
                            shadowBlur: 10,
                            shadowColor: 'rgba(0, 0, 0, 0.3)'
                        },
                        lineStyle: {
                            color: 'source',
                            curveness: 0.3
                        },
                        edgeSymbol: ['', 'arrow'],
                        edgeLabel: { 		// 连接两个关系对象的线上的标签
                            normal: {
                            show: true,
                            textStyle: {
                            fontSize: 18
                                },
                            formatter: function(param) { // 关系标签内容
                            return param.data.value;
                                            }
                                    }
                                },
                        data: theData.nodes,
                        links: theData.links,
                    }
                ]
            }
            //防止越界，重绘canvas
            window.onresize = myChart.resize;
            myChart.setOption(option);//设置option
        },
        // 获取 easy-mock 的模拟数据
        getData() {
            fetch(this.queryURL, {
                method: "POST",
                body: JSON.stringify({
                    docs: [{
                        "id":123,
                        "doc":this.content,
                    }]
                }),
                headers: {
                    "Content-Type": "application/json"
                },

            }).then(res => res.json())
                .catch(error => console.error('Error:', error))
                .then(response => console.log(response.data[0].summary));
        }

    },
    
    mounted() {
        this.drawChart();
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





</style>

<template>
    <div>
        <el-container>
          <el-header style="height: max-content;padding:0">
              <el-card class="noBorderInput" style="border: 0px;border-radius: 0;
          background-color: #fff;
          box-shadow: 0 0px 0px 0 rgba(0,0,0,.1);">

                <!--<div slot="header" class="diyCardHead" >-->
                <h1 style="color: black; letter-spacing: 10px; font-weight: normal; font-size: 25px; margin-top: -20px">文本摘要</h1>
                <!--<el-divider style="width: 30px"></el-divider>-->
                <!--</div>-->
                <!--<h1 style="color: gray">实体识别</h1>-->
                <el-input
                  type="textarea"
                  placeholder="请输入内容"
                  v-model="summaryText"
                  maxlength="400"
                  show-word-limit
                  :autosize="{ minRows: 5, maxRows: 8}"
                  clearable
                  style="box-shadow: 0 2px 4px rgba(0, 0, 0, .12), 0 0 6px rgba(0, 0, 0, .04); font-size: 15px;"
                >
                </el-input>

                <el-row style="margin-top: 17px; display: flex; justify-content: center">
                  <el-button v-on:click="getData" type="primary" style="background: #242f42; border: 0px; font-size: 15px; letter-spacing: 5px">开始摘要</el-button>
                  <!--<el-button v-on:click="mockData">随机样例</el-button>-->
                </el-row>
              </el-card>
          </el-header>
            <!--<el-container>-->
                <!--<el-aside width="200px">Aside</el-aside>-->
                <el-main style="padding:0;margin-top:20px">
                    <!--</span>-->

                    <el-card class="box-card" style="font-size:18px; text-align: center;min-height: 250px" v-loading="loading">
                        <div slot="header" class="clearfix">
                            <span>摘要结果</span>
                        </div>
                        <div style="line-height: 1.5;-webkit-box-sizing: border-box;box-sizing: border-box;width: 100%;font-size: 15px;color: #606266;font-family: monospace;letter-spacing: normal;line-height: normal;">
                            {{summaryRes}}
                        </div>
                        <!--<el-input-->
                                <!--type="textarea"-->
                                <!--placeholder=""-->
                                <!--v-model="summaryRes"-->
                                <!--maxlength="400"-->
                                <!--:autosize="{ minRows: 5, maxRows: 5 }"-->
                                <!--clearable-->
                                <!--class="res-textarea"-->
                        <!--&gt;-->
                        <!--</el-input>-->
                    </el-card>

                </el-main>
            <!--</el-container>-->
        </el-container>

        <!--<el-container>-->
            <!--<el-header>-->
                <!--<h1 style="color: gray">自动摘要</h1>-->
            <!--</el-header>-->
            <!--<el-main style="text-align: center">-->
                <!--&lt;!&ndash;<span style="font-size: 15px; color: gray;">&ndash;&gt;-->
                    <!--&lt;!&ndash;文本摘要生成能够实现文本内容的理解、精简提炼，生成简短、准确、流畅的摘要，并能根据需求灵活控制生成的摘要长度。文本摘要生成可用于文本内容理解、新闻自动生成、冗余文档检测、智能写作等，是智能媒体行业必备的AI能力之一。&ndash;&gt;-->
                <!--&lt;!&ndash;</span>&ndash;&gt;-->
                <!--&lt;!&ndash;<span style="font-size: 15px; color: gray;">&ndash;&gt;-->

                <!--&lt;!&ndash;</span>&ndash;&gt;-->
                <!--<el-input-->
                        <!--type="textarea"-->
                        <!--placeholder="请输入内容"-->
                        <!--v-model="summaryText"-->
                        <!--maxlength="400"-->
                        <!--show-word-limit-->
                        <!--:autosize="{ minRows: 5, maxRows: 8}"-->
                        <!--clearable-->
                        <!--style="box-shadow: 0 2px 4px rgba(0, 0, 0, .12), 0 0 6px rgba(0, 0, 0, .04)"-->
                <!--&gt;-->
                <!--</el-input>-->
                <!--<el-row style="margin-top: 30px; display: flex; justify-content: center">-->
                    <!--<el-button v-on:click="getData" type="primary">开始摘要</el-button>-->
                    <!--<el-button type="success">随便试试</el-button>-->
                <!--</el-row>-->
                <!--<el-input-->
                        <!--type="textarea"-->
                        <!--placeholder="摘要生成结果"-->
                        <!--v-model="summaryRes"-->
                        <!--maxlength="400"-->
                        <!--disabled-->
                        <!--:autosize="{ minRows: 5, maxRows: 5 }"-->
                        <!--clearable-->
                        <!--class="res-textarea"-->
                <!--&gt;-->
                <!--</el-input>-->

            <!--</el-main>-->
            <!--&lt;!&ndash;<el-footer>Footer</el-footer>&ndash;&gt;-->
        <!--</el-container>-->
    </div>
</template>

<script>

import { fetchData } from '../../api/index';
export default {
    name: 'summarization',
    data() {
        return {
            text: '',
            summaryText: '',
            summaryRes:'',
            queryURL:'http://115.236.52.123:6012/api/summarization',
            loading: false
        };
    },
    created() {
        // this.getData();
    },
    mounted(){
      this.mockData()
    },
    methods: {
        // 获取 easy-mock 的模拟数据
        getData() {
            var tempText = this.clearText(this.summaryText)
            // this.summaryText = this.clearText(this.summaryText)
            this.loading=true;
            var tempRes;
            // this.summaryRes = this.summaryText
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
                    this.summaryRes = responseJson.results[0].result.summary
                    this.loading=false
                    // console.log(tempRes)
                    }
                )
            // console.log(tempRes)
            // this.summaryRes = tempRes;
        },
        mockData(){
            this.summaryText='日前，方舟子发文直指林志颖旗下爱碧丽推销假保健品，引起哗然。调查发现，爱碧丽没有自己的生产加工厂,其胶原蛋白饮品无核心研发，全部代工生产。号称有“逆生长”功效的爱碧丽“梦幻奇迹限量组”售价高达1080元，实际成本仅为每瓶4元！（请输入文本）'
            this.getData()
        },
        clearText(testStr) {
            var resultStr = testStr.replace(/\ +/g, "");
            resultStr = resultStr.replace(/\s+/g, "");
            resultStr = resultStr.replace(/[ ]/g, "");    //去掉空格
            resultStr = resultStr.replace(/[\r\n]/g, ""); //去掉回车换行
            if(this.summaryText.indexOf("(请输入文本)")!=-1){
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






</style>

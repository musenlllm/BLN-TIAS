<template>
  <div>
    <el-container>
      <el-header style="height: max-content;padding:0">
        <el-card
          class="noBorderInput"
          style="border: 0px;border-radius: 0;
      background-color: #fff;
      box-shadow: 0 0px 0px 0 rgba(0,0,0,.1);"
        >
          <!--<div slot="header" class="diyCardHead" >-->
          <h1
            style="color: black; letter-spacing: 10px; font-weight: normal; font-size: 25px; margin-top: -20px"
          >实体识别</h1>
          <!--<el-divider style="width: 30px"></el-divider>-->
          <!--</div>-->
          <!--<h1 style="color: gray">实体识别</h1>-->
          <el-input
            type="textarea"
            placeholder="请输入内容"
            v-model="nerText"
            maxlength="200"
            show-word-limit
            :autosize="{ minRows: 5, maxRows: 5}"
            clearable
            style="font-size: 15px; box-shadow: rgba(0, 0, 0, 0.12) 0px 2px 4px, rgba(0, 0, 0, 0.04) 0px 0px 6px"
          >
            <!--style=" font-size: 15px; margin-top: 0px;border-radius: 0;-->
            <!--background-color: #fff;-->
            <!--box-shadow: 0 0px 0px 0 rgba(0,0,0,.1);"-->
            >
          </el-input>
          <el-row style="margin-top: 17px; display: flex; justify-content: center">
            <el-button
              v-on:click="getData"
              type="primary"
              style="background: #242f42; border: 0px; font-size: 15px; letter-spacing: 5px"
            >开始识别</el-button>
            <!--<el-button v-on:click="mockData">随机样例</el-button>-->
          </el-row>
        </el-card>
      </el-header>
      <el-container style="width: 100%">
        <div ref="asideContainer" style="width: 100%;margin-top: 20px">
          <el-aside width="100%" style=" text-align: center">
            <el-card
              class="box-card"
              style="min-height: 170px;border-radius: 0;
      background-color: #fff;
      box-shadow: 0 0px 0px 0 rgba(0,0,0,.1);"
              v-loading="resloading"
            >
              <div slot="header" class="clearfix">
                <span style="font-size: 18px">识别结果</span>
              </div>

              <el-scrollbar style="width: 100%;">
                <div
                  class="tag-group"
                  style="margin-top: 0; display: flex; flex-direction: row; flex-wrap: wrap;"
                  v-loading="restypeloading"
                >
                  <el-tag
                    ref="nerResRef"
                    style="margin-right: 10px;margin-bottom: 10px; border-radius: 4px; font-size: 15px; border: 0px;
                              padding: 5px; padding-top: 1px; "
                    v-for="item in items"
                    :key="item.label"
                    :type="item.type"
                    :color="item.color"
                    size="medium"
                    effect="plain"
                    :effect="item.effect"
                  >{{ item.label }}</el-tag>
                </div>
              </el-scrollbar>
              <el-scrollbar>
                <div class="tag-group">
                  <el-row
                    style="display:flex;justify-content:center;flex-direction:row; flex-wrap:wrap;max-width:100%;margin-top:20px"
                  >
                    <div
                      style="display:flex;justify-content:center;flex-direction:row; flex-wrap:wrap;max-width:100%"
                    >
                      <template v-for="(color, key) in type2color">
                        <div
                          :key="key"
                          style="display: flex; justify-content: center; flex-direction: row; flex-wrap: wrap;margin:5px 5px;"
                        >
                          <div
                            style="box-shadow: 0 2px 4px rgba(0, 0, 0, .12), 0 0 6px rgba(0, 0, 0, .04);
                    border-radius: 4px;border: 0px;margin:3px 5px;width:25px;height:15px;"
                            :style="{'background-color':color}"
                          ></div>
                          <div style="font-size:15px;min-width:25px;height:15px;padding:0 0">{{key}}</div>
                        </div>
                      </template>
                    </div>
                  </el-row>
                </div>
              </el-scrollbar>
              <!--<span class="tag-group__title">Dark</span>-->

              <!--{ label: '人名', type: '' ,color: '#F56C6C'},-->
              <!--{ label: '地名', type: '' ,color:'#E6A23C'},-->
              <!--{ label: '组织机构名', type: '',color:'#409EFF' },-->
              <!--{ label: '时间', type: '' ,color: '#67C23A'},-->
              <!--{ label: '公司', type: '',color:'#242f42' },-->
              <!--{ label: '产品', type: '' ,color:'pink'},-->
            </el-card>

            <el-card
              class="box-card"
              style=" margin-top:20px;margin-bottom:20px;border-radius: 0;background-color: #fff;box-shadow: 0 0px 0px 0 rgba(0,0,0,.1)"
            >
              <div slot="header" class="clearfix">
                <span style="font-size: 18px">实体分类树</span>
              </div>
              <el-scrollbar style="width: 100%">
                <div id="tree" ref="treePic" style="margin-left:2%; width: 100%;height: 50vh"></div>
              </el-scrollbar>
            </el-card>
          </el-aside>
        </div>

        <!--<div ref="mainContainer" style="width: 40%; margin-top: 20px; margin-left: 20px;margin-right: 20px;">-->
        <!--<el-main   style="text-align: center; margin-top: 0px; height: 100%; padding: 0px; ">-->
        <!--<el-card class="box-card" style="height: 100%; margin-top: 0px;border-radius: 0;-->
        <!--background-color: #fff;-->
        <!--box-shadow: 0 0px 0px 0 rgba(0,0,0,.1);">-->
        <!--<div slot="header" class="clearfix">-->
        <!--<span style="font-size: 18px">实体比例图</span>-->
        <!--</div>-->
        <!--<div id="percent" style="width: 100%;height: 60vh;"></div>-->
        <!--</el-card>-->
        <!--&lt;!&ndash;<el-card class="box-card" style="visibility: hidden">&ndash;&gt;-->
        <!--&lt;!&ndash;<div slot="header" class="clearfix">&ndash;&gt;-->
        <!--&lt;!&ndash;<span style="font-size: 18px">可识别实体类别</span>&ndash;&gt;-->
        <!--&lt;!&ndash;</div>&ndash;&gt;-->
        <!--&lt;!&ndash;<div class="tag-group" style=" display: flex; justify-content: center; flex-direction: row; flex-wrap: wrap;">&ndash;&gt;-->
        <!--&lt;!&ndash;<el-tag style="width: 100px; margin-right: 10px;margin-bottom: 10px; border-radius: 4px; font-size: 15px; border: 0px;&ndash;&gt;-->
        <!--&lt;!&ndash;box-shadow: 0 2px 4px rgba(0, 0, 0, .12), 0 0 6px rgba(0, 0, 0, .04); padding-top: 1px;"&ndash;&gt;-->
        <!--&lt;!&ndash;v-for="item in itemtypes"&ndash;&gt;-->
        <!--&lt;!&ndash;:key="item.label"&ndash;&gt;-->
        <!--&lt;!&ndash;:type="item.type"&ndash;&gt;-->
        <!--&lt;!&ndash;:color="item.color"&ndash;&gt;-->
        <!--&lt;!&ndash;size="medium"&ndash;&gt;-->
        <!--&lt;!&ndash;effect="dark">&ndash;&gt;-->
        <!--&lt;!&ndash;{{ item.label }}&ndash;&gt;-->
        <!--&lt;!&ndash;</el-tag>&ndash;&gt;-->
        <!--&lt;!&ndash;</div>&ndash;&gt;-->
        <!--&lt;!&ndash;</el-card>&ndash;&gt;-->

        <!--</el-main>-->
        <!--</div>-->
      </el-container>
      <!--<el-footer>Footer</el-footer>-->
    </el-container>
  </div>
</template>
<script>
import echarts from "echarts";
import { fetchData } from "../../api/index";
export default {
  name: "basetable",
  data() {
    return {
      text: "",
      nerText: "",
      nerRes: "实体命名识别结果",
      queryURL: "http://115.236.52.123:6012/api/ner",
      resloading: false,
      restypeloading: false,
      isDiyCardHead: true,
      type2color: type2color,

      items: [
        // { type: '', label: '标签一' },
        // { type: 'success', label: '标签二' },
      ],
      itemtypes: [
        { label: "人名", type: "", color: "#F56C6C" },
        { label: "地名", type: "", color: "#E6A23C" },
        { label: "组织机构名", type: "", color: "#409EFF" },
        { label: "时间", type: "", color: "#67C23A" },
        { label: "公司", type: "", color: "#242f42" },
        { label: "产品", type: "", color: "pink" },
      ],
      treeData: {},
      percentData: [],
      entData: [],

      treeCharts: "",
      percentCharts: "",
      resStr: "",
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
    this.mockData();
    // var tabH = this.$refs.asideContainer.style.height;
    // this.$refs.mainContainer.style.height = tabH+'px';
    // console.log('hhhh'+tabH);
  },
  methods: {
    // 获取 easy-mock 的模拟数据
    getData() {
      this.resloading = true;
      this.restypeloading = true;
      this.items = [];
      this.percentData = [];
      this.entData = [];

      //clear the input text
      var tempText = this.clearText(this.nerText);
      // this.nerText = tempText;

      // mock data
      fetch(this.queryURL, {
        method: "POST",
        body: JSON.stringify({
          docs: [
            {
              id: 0,
              doc: tempText,
            },
          ],
        }),
        headers: {
          "Content-Type": "application/json",
        },
      })
        .then((res) => res.json())
        .catch((error) => console.error("Error:", error))
        .then((responseJson) => {
          this.resStr = JSON.stringify(responseJson.results[0].result);
          console.log("resStr: " + this.resStr);
          console.log("resStrType: " + typeof this.resStr);

          var resArray = eval("(" + this.resStr + ")");
          // var resArray=resStr
          console.log("resArray: " + resArray);
          console.log("resArrayType: " + typeof resArray);
          //无意义文字开头结尾位置
          var plainStart = 0;
          var plainEnd = 0;
          var resStart;
          var resEnd;
          var resEnt;
          var colorTemp;
          var plainTextCharNum = 200;
          for (var i = 0; i < resArray.length; i++) {
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
            if (plainStart !== plainEnd) {
              var numCuts = Math.floor(
                (plainEnd - plainStart) / plainTextCharNum
              );
              // var lastChar = (plainEnd - plainStart)%plainTextCharNum
              for (let p = 0; p < numCuts; p++) {
                this.items.push({
                  // label: this.nerText.slice(plainStart,plainStart+plainTextCharNum),
                  label: tempText.slice(
                    plainStart,
                    plainStart + plainTextCharNum
                  ),
                  color: "#cccccc",
                  effect: "dark",
                  type: "info",
                  ent: "普通",
                  textColor: "gray",
                  value: "1",
                });
                plainStart = plainStart + plainTextCharNum;
              }
              this.items.push({
                // label: this.nerText.slice(plainStart,plainEnd),
                label: tempText.slice(plainStart, plainEnd),
                color: "#cccccc",
                type: "info",
                ent: "普通",
                effect: "dark",
                textColor: "gray",
                value: "1",
              });
            }
            plainStart = resEnd + 1;
            plainEnd = resEnd + 1;

            if (resEnt == "地点") {
              colorTemp = "#E6A23C";
            } else if (resEnt == "人名") {
              console.log("人名检测！！！！");
              colorTemp = "#F56C6C";
            } else if (resEnt == "组织") {
              colorTemp = "#409EFF";
            } else if (resEnt == "时间") {
              colorTemp = "#67C23A";
            } else if (resEnt == "公司") {
              colorTemp = "#242f42";
            } else if (resEnt == "产品") {
              colorTemp = "pink";
            }
            // console.log("push意义词");
            // console.log("意义词语: "+this.nerText.slice(resStart,resEnd+1));
            // console.log("颜色: "+colorTemp);
            this.items.push({
              // label: this.nerText.slice(resStart,resEnd+1),
              label: tempText.slice(resStart, resEnd + 1),
              color: colorTemp,
              effect: "dark",
              type: "",
              ent: resEnt,
              value: "1",
            });
          }
          // if ((resEnd+1)!=this.nerText.length) {
          if (resEnd + 1 != tempText.length) {
            // var numCuts = Math.floor((this.nerText.length-plainEnd)/plainTextCharNum)
            var numCuts = Math.floor(
              (tempText.length - plainEnd) / plainTextCharNum
            );
            // var lastChar = (plainEnd - plainStart)%6
            for (let p = 0; p < numCuts; p++) {
              this.items.push({
                // label: this.nerText.slice(plainEnd,plainEnd+plainTextCharNum),
                label: tempText.slice(plainEnd, plainEnd + plainTextCharNum),
                color: "#cccccc",
                type: "info",
                ent: "普通",
                effect: "dark",
                textColor: "gray",
                value: "1",
              });
              plainEnd = plainEnd + plainTextCharNum;
            }
            this.items.push({
              // label: this.nerText.slice(plainEnd,this.nerText.length),
              label: tempText.slice(plainEnd, tempText.length),
              color: "#cccccc",
              type: "info",
              ent: "普通",
              effect: "dark",
              textColor: "gray",
              value: "1",
            });

            //////////
            // this.items.push({
            //     label: this.nerText.slice(resEnd+1,this.nerText.length),
            //     color: 'gray',
            //     type: '',
            //     ent: '普通',
            //     value:'1'
            // })
          }

          this.treeData.name = "实体分类树";
          this.treeData.children = [];
          var addedEnt = [];

          //构建实体分类树图的数据treeData,O(n^2)复杂度
          for (let k = 0; k < this.items.length; k++) {
            var entTemp = this.items[k].ent;

            if (addedEnt.indexOf(entTemp) == -1 && entTemp != "普通") {
              var treeDataItemTemp = {};
              treeDataItemTemp.name = entTemp;
              treeDataItemTemp.children = [];
              treeDataItemTemp.children.push({
                name: this.items[k].label,
                value: this.items[k].value,
              });
              this.treeData.children.push(treeDataItemTemp);
              addedEnt.push(entTemp);
              continue;
            }
            for (let h = 0; h < this.treeData.children.length; h++) {
              if (this.treeData.children[h].name == entTemp) {
                this.treeData.children[h].children.push({
                  name: this.items[k].label,
                  value: this.items[k].value,
                });
              }
            }
          }
          // 准备实体数量比例数据
          // this.entData = addedEnt;
          this.entData = ["人名", "组织", "时间", "公司", "产品", "地点"];

          for (let i = 0; i < this.treeData.children.length; i++) {
            let colorTemp;
            let resEnt = this.treeData.children[i].name;
            if (resEnt == "地点") {
              colorTemp = "#E6A23C";
            } else if (resEnt == "人名") {
              console.log("人名检测！！！！");
              colorTemp = "#F56C6C";
            } else if (resEnt == "组织") {
              colorTemp = "#409EFF";
            } else if (resEnt == "时间") {
              colorTemp = "#67C23A";
            } else if (resEnt == "公司") {
              colorTemp = "#242f42";
            } else if (resEnt == "产品") {
              colorTemp = "pink";
            }
            this.percentData.push({
              name: this.treeData.children[i].name,
              value: this.treeData.children[i].children.length,
              itemStyle: {
                color: colorTemp,
              },
            });
          }
          //填充没有识别到的实体
          var targetAddEnt = ["人名", "组织", "时间", "公司", "产品", "地点"];
          for (let i = 0; i < targetAddEnt.length; i++) {
            let temp = targetAddEnt[i];
            if (addedEnt.indexOf(temp) == -1) {
              let colorTemp = this.getColor(temp);
              this.percentData.push({
                name: temp,
                value: 0,
                itemStyle: {
                  color: colorTemp,
                },
              });
            }
          }
          console.log(this.percentData);
          this.resloading = false;
          this.restypeloading = false;

          // this.changeNerResStyle()

          console.log(this.treeData);
          // this.option.series[0].data=this.treeData
          //画图
          this.drawGraph();

          // let tabH = this.$refs.asideContainer.style.height;
          // this.$refs.mainContainer.style.height = tabH+'px';
          // console.log("hhhhhhhhh"+tabH)
        });
      // var resStr = '[{"start":6,"end":7,"content":"中国","ent":"地点"},{"start":14,"end":15,"content":"宝马","ent":"组织"},{"start":41,"end":42,"content":"宝马","ent":"组织"},{"start":45,"end":47,"content":"瞿云涛","ent":"人名"},{"start":50,"end":51,"content":"宝马","ent":"组织"},{"start":55,"end":56,"content":"中国","ent":"地点"}]'
      // evel 转化为 数组
    },
    drawGraph() {
      // this.treeCharts = echarts.init(document.getElementById('tree'));
      this.treeCharts = echarts.init(this.$refs.treePic);
      // this.percentCharts = echarts.init(document.getElementById('percent'));

      window.onresize = this.treeCharts.resize;
      // window.onresize = this.percentCharts.resize;

      this.treeCharts.showLoading();
      // this.percentCharts.showLoading();

      this.treeCharts.setOption({
        tooltip: {
          trigger: "item",
          triggerOn: "mousemove",
        },
        series: [
          {
            type: "tree",

            data: [this.treeData],

            top: "1%",
            left: "15%",
            bottom: "1%",
            right: "30%",

            symbolSize: 10,

            label: {
              position: "left",
              verticalAlign: "middle",
              align: "right",
              fontSize: 15,
            },

            leaves: {
              label: {
                position: "right",
                verticalAlign: "middle",
                align: "left",
              },
            },

            expandAndCollapse: true,
            animationDuration: 1000,
            animationDurationUpdate: 1000,
          },
        ],
      });

      // this.percentCharts.setOption({
      //     tooltip: {
      //         trigger: 'item',
      //         formatter: '{a} <br/>{b}: {c} ({d}%)'
      //     },
      //     legend: {
      //       //
      //         type: "scroll",
      //         orient: "vertical",
      //         left: 0,
      //         top: 0,
      //         bottom: 0,
      //
      //         textStyle:{
      //           fontSize:15,
      //         },
      //         // data: dataset.legendData,
      //         // selected: dataset.selected,
      //       //
      //       //   orient: 'vertical',
      //       //   left: 5,
      //         data: this.entData
      //     },
      //     series: [
      //         {
      //           left: 0,
      //           top: 100,
      //           bottom: 0,
      //           //
      //           // name: "主题",
      //           // type: "pie",
      //           // radius: "55%",
      //           // center: ["40%", "50%"],
      //           // data: this.percentData,
      //           // emphasis: {
      //           //   itemStyle: {
      //           //     shadowBlur: 10,
      //           //     shadowOffsetX: 0,
      //           //     shadowColor: "rgba(0, 0, 0, 0.5)",
      //           //   },
      //           // },
      //           //
      //             name: '实体数量比例图',
      //             type: 'pie',
      //             radius: ['50%', '70%'],
      //             avoidLabelOverlap: false,
      //             label: {
      //                 show: false,
      //                 position: 'center'
      //             },
      //             emphasis: {
      //                 label: {
      //                     show: true,
      //                     fontSize: '20',
      //                     fontWeight: 'bold'
      //                 }
      //             },
      //             labelLine: {
      //                 show: false
      //             },
      //             right: 0,
      //             data: this.percentData
      //         }
      //     ]
      // })
      this.treeCharts.hideLoading();
      // this.percentCharts.hideLoading();

      // window.onresize = this.$refs.treePic.resize;
      window.onresize = () => {
        this.treeCharts.resize();
        // this.percentCharts.resize();

        // let height = this.$refs.asideContainer.offsetHeight;
        // this.$refs.mainContainer.offsetHeight = height;

        //如果有多个表变动在下方依次写下去就可以了
      };
      // window.onresize = this.percentCharts.resize;
      // window.addEventListener("resize", function() {
      //             this.treeCharts.resize();
      //             this.percentCharts.resize();
      //         })
      // window.onresize = function () {
      //   //重置容器高宽
      //   this.treeCharts.resize()
      //   this.percentCharts.resize()
      // };
    },
    mockData() {
      // this.nerText ='10月25日在北京的小米新品发布会上，雷军发布了一款概念手机小米MIX。该手机的设计师是当代著名的设计大师、民主设计和极简设计的倡导者菲利普·斯塔克。(请输入文本)'
      this.nerText =
        "全球化竞争日益激烈的今天，中国已把科技作为战略博弈的核心。以芯片为例，X86的江湖地位已大不如从前，基于ARM架构芯片的崛起正在撬动英特尔一统天下的格局，比如去年，华为总裁余承东宣布推出了首款基于ARM架构的服务器芯片鲲鹏920，强势闯入服务器市场。(请输入文本)";
      this.getData();
    },
    clearText(testStr) {
      var resultStr = testStr.replace(/\ +/g, "");
      resultStr = resultStr.replace(/\s+/g, "");
      resultStr = resultStr.replace(/[ ]/g, ""); //去掉空格
      resultStr = resultStr.replace(/[\r\n]/g, ""); //去掉回车换行
      if (this.nerText.indexOf("(请输入文本)") != -1) {
        resultStr = resultStr.slice(0, resultStr.length - 7);
      }

      return resultStr;
    },
    getColor(resEnt) {
      var colorTemp;
      if (resEnt == "地点") {
        colorTemp = "#E6A23C";
      } else if (resEnt == "人名") {
        console.log("人名检测！！！！");
        colorTemp = "#F56C6C";
      } else if (resEnt == "组织") {
        colorTemp = "#409EFF";
      } else if (resEnt == "时间") {
        colorTemp = "#67C23A";
      } else if (resEnt == "公司") {
        colorTemp = "#242f42";
      } else if (resEnt == "产品") {
        colorTemp = "pink";
      }
      return colorTemp;
    },
  },
};
const type2color = {
  地点: "#E6A23C",
  人名: "#F56C6C",
  组织: "#409EFF",
  时间: "#67C23A",
  公司: "#242f42",
  产品: "pink",
};
</script>

<style scoped>
@import url("//unpkg.com/element-ui@2.13.2/lib/theme-chalk/index.css");
.el-header,
.el-footer {
  font-size: 20px;
  color: black;
  text-align: center;
  line-height: 60px;
}
.res-textarea {
  color: black;
  margin-top: 30px;
  box-shadow: 0 0px 0px rgba(0, 0, 0, 0.12), 0 0 6px rgba(0, 0, 0, 0.04);
}
.el-card {
  border-radius: 0;
  background-color: #fff;
  box-shadow: 0 0px 0px 0 rgba(0, 0, 0, 0.1);
}
/*.el-input__inner:focus {*/
/*border-color: black;*/
/*box-shadow: none;*/
/*transition-duration: .5s;*/
/*}*/
>>> .el-input__inner {
  border-radius: 0px;
}

/*input:focus{*/
/*outline: none;*/
/*border: 1px solid #fff;*/
/*}*/
</style>


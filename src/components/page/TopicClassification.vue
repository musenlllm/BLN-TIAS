<template>
  <div>
    <el-container>
      <el-header style="height: max-content">
        <h1 style="color: gray">文本主题分类</h1>
      </el-header>

      <el-main style="text-align: center">
        <el-row style="margin:20px 0">
          <el-col :span="13">
            <el-input
              type="textarea"
              placeholder="请输入文本"
              v-model="content"
              maxlength="800"
              show-word-limit
              :autosize="{ minRows: 11, maxRows: 16}"
              clearable
              style="box-shadow: 0 2px 4px rgba(0, 0, 0, .12), 0 0 6px rgba(0, 0, 0, .04)"
            />
          </el-col>
          <el-col :span="3">
            <el-button @click="submit" type="primary" style="background: #242f42; border: 0px">开始分析</el-button>
          </el-col>
          <el-col :span="8">
            <el-card shadow="always" style="height:240px;max-height:230px">
              <div slot="header" class="clearfix">
                <span style="font-size: 18px">本次主题分类结果</span>
              </div>
              <el-row>
                <div v-if="form.type.length > 0" style="text-align:center;height:26px">
                  <p
                    style="font-size:24px;font-weight:bold"
                    :style="{color:form.color}"
                  >{{form.type}}</p>
                  <!--<el-tag
                    effect="dark"
                    size="default"
                    :color="form.color"
                    style="border-radius: 4px;border: 0px;text-align:center;width:60px;font-size:18px;height:30px;
                             box-shadow: 0 2px 4px rgba(0, 0, 0, .12), 0 0 6px rgba(0, 0, 0, .04);"
                  >{{form.type}}</el-tag>-->
                </div>
                <div v-else style="min-height:26px"></div>
              </el-row>
              <!-- <el-row>
                <div align="middle" id="tpChart" style="height: 300px"></div>
              </el-row>-->
              <el-row style="margin-top:36px">
                <div
                  class="tag-group"
                  style=" display: flex; justify-content: center; flex-direction: row; flex-wrap: wrap;"
                >
                  <el-tag
                    style="border-radius: 4px;border: 0px;margin:5px 5px;
                             box-shadow: 0 2px 4px rgba(0, 0, 0, .12), 0 0 6px rgba(0, 0, 0, .04);"
                    v-for="(value, key) in type2color"
                    :key="key"
                    :color="value"
                    effect="dark"
                  >{{ key }}</el-tag>
                </div>
              </el-row>
            </el-card>
          </el-col>
        </el-row>

        <el-row style="margin:3em 0;max-width:100%;max-height:480px">
          <el-card>
            <div slot="header" class="clearfix">
              <span style="font-size: 18px">实时主题新闻分类结果</span>
            </div>
            <el-row style="text-align:left">
              <el-carousel
                :interval="12000"
                direction="vertical"
                arrow="never"
                indicator-position="none"
                height="378px"
                :loop="true"
              >
                <el-carousel-item v-for="(news, index) in newslist" :key="index">
                  <template v-for="i in 2">
                    <el-col :span="12" :key="i">
                      <el-table
                        :show-header="false"
                        :data="news.slice(i*6-6,i*6)"
                        style="height:380px"
                        max-height="380"
                      >
                        <el-table-column :show-overflow-tooltip="true">
                          <template slot-scope="scope">
                            <el-row>
                              <a :href="scope.row.url" style="color:black">{{scope.row.event}}</a>
                            </el-row>
                            <el-row>
                              <el-col :span="16">发布时间：{{scope.row.publish_time}}</el-col>
                              <el-col :span="4">
                                类别：
                                <el-tag
                                  effect="dark"
                                  :color="scope.row.color"
                                  style="border-radius: 4px;border: 0px;
                             box-shadow: 0 2px 4px rgba(0, 0, 0, .12), 0 0 6px rgba(0, 0, 0, .04);"
                                >{{scope.row.type}}</el-tag>
                              </el-col>
                              <el-col :span="4">概率：{{scope.row.score}}</el-col>
                            </el-row>
                          </template>
                        </el-table-column>
                      </el-table>
                    </el-col>
                  </template>
                </el-carousel-item>
              </el-carousel>
            </el-row>
          </el-card>
        </el-row>

        <el-row style="margin-top:30px">
          <el-col :span="12">
            <el-card>
              <div slot="header" class="clearfix">
                <span style="font-size: 18px">实时主题新闻数量统计</span>
              </div>
              <div id="showBarChart" :style="{width: '100%', height: '300px'}"></div>
            </el-card>
          </el-col>

          <el-col :span="12" style="padding-left:20px">
            <el-card>
              <div slot="header" class="clearfix">
                <span style="font-size: 18px">实时主题新闻比例统计</span>
              </div>
              <div id="showPieChart" :style="{width: '100%', height: '300px'}"></div>
            </el-card>
          </el-col>
        </el-row>
      </el-main>
    </el-container>
  </div>
</template>

<script>
import { fetchData } from "../../api/index";
import echarts from "echarts/lib/echarts";
import "echarts/dist/extension/dataTool";

const childtypelist = ["教育", "娱乐", "财经", "时政", "社会", "体育", "科技"];
/*const type2value = {
  体育: 0,
  娱乐: 10,
  家居: 20,
  彩票: 30,
  房产: 40,
  教育: 50,
  时尚: 60,
  时政: 70,
  星座: 80,
  游戏: 90,
  社会: 100,
  科技: 110,
  股票: 120,
  财经: 130,
};*/
const type2color = {
  体育: "#F56C6C",
  娱乐: "pink",
  家居: "#A39391",
  彩票: "#D45246",
  房产: "#FFCC99",
  教育: "#9999CC",
  时尚: "#3366CC",
  时政: "#E6A23C",
  星座: "#E3E1C8",
  游戏: "#FB3C3C",
  科技: "#203643",
  社会: "#74C2E1",
  股票: "#84CF96",
  财经: "#67C23A",
};
const colorList = [
  "#9999CC",
  "pink",
  "#67C23A",
  "#E6A23C",
  "#74C2E1",
  "#F56C6C",
  "#203643",
];
/*
const colorList = [
  "pink",
  "#67C23A",
  "#E6A23C",
  "#409EFF",
  "#242f42",
  "#F56C6C",
  "#7B7BC7",
];
*/
const tpclassurl = "http://49.234.217.110:5000/api/tpclassification";
const carouselurl = "http://49.234.217.110:5000/api/getRealTimeThemeInfo";

export default {
  name: "markdown",
  data: function () {
    return {
      form: {
        type: "科技",
        score: 0.985,
        color: "#203643",
      },
      content:
        "【字节跳动或已拿下支付牌照】8月28日，武汉合众易宝科技有限公司股东中发实业（集团）有限公司退出，天津同融电子商务有限公司接盘100%股份。" +
        "天津同融电子商务有限公司是北京石贝科技有限公司全资子公司，穿透以后，字节跳动创始人张一鸣是实际控制人。合众支付官网显" +
        "示，该公司2014年获得由中国人民银行颁发的《支付业务许可证》，成为湖北省首家持牌互联网支付企业。（请输入文本）",
      cnt: [],
      colorSt: {
        "background-color": "#99a9bf",
      },
      newslist: [],
      type2color: type2color,
    };
  },
  methods: {
    drawDashboard() {
      var theChart = echarts.init(document.getElementById("tpChart"));
      var thisVal = 50;

      var option = {
        // color:['#E47470','#7EBF50', '#589EF8'],
        tooltip: {
          formatter: "{a} <br/>{b} : {c}%",
        },
        series: [
          {
            name: "置信度",
            type: "gauge",
            detail: {
              formatter: "{value}%",
              textStyle: {
                fontSize: 20,
              },
            },
            data: [
              {
                value: Math.floor(this.form.score * 100),
                name: "置信度",
              },
            ],
            title: {
              textStyle: {
                // 其余属性默认使用全局文本样式，详见TEXTSTYLE
                fontWeight: "bolder",
                fontSize: 20,
                fontStyle: "italic",
                color: "gray",
              },
            },
            axisLine: {
              // 坐标轴线
              lineStyle: {
                // 属性lineStyle控制线条样式
                color: [
                  [0.2, "#E47470"],
                  [0.8, "#DDA450"],
                  [1, "#7EBF50"],
                ],
                // width:50
              },
            },
            axisLabel: {
              distance: -60,
              textStyle: {
                fontSize: 15,
              },
            },
          },
        ],
      };
      /*var option2 = {
        tooltip: {
          formatter: "文本主题 : " + typelist[thisVal / 10],
        },
        series: [
          {
            name: "文本主题",
            type: "gauge",
            detail: {
              formatter: function (value) {
                console.log("value");
                console.log(value);
                return typelist[value / 10];
              },
              textStyle: {
                fontSize: 20,
              },
            },
            min: 0,
            max: 130,
            splitNumber: 13,
            data: [
              {
                value: thisVal,
                name: "文本主题",
              },
            ],
            title: {
              textStyle: {
                // 其余属性默认使用全局文本样式，详见TEXTSTYLE
                fontWeight: "bolder",
                fontSize: 20,
                fontStyle: "italic",
                color: "gray",
              },
            },
            axisLine: {
              // 坐标轴线
              lineStyle: {
                // 属性lineStyle控制线条样式
                color: [[1, "#F56C6C"]],
                // width:50
              },
            },
            axisLabel: {
              distance: -60,
              textStyle: {
                fontSize: 15,
              },
              formatter: function (value) {
                for (var key in type2value) {
                  if (type2value[key] == value) {
                    return key;
                  }
                }
                return "error";
              },
            },
            axisTick: {
              show: false,
            },
          },
        ],
      };*/
      theChart.setOption(option);
    },
    drawBarChart() {
      let myChart = echarts.init(document.getElementById("showBarChart"));
      // 绘制图表
      var option = {
        tooltip: {
          trigger: "item",
          formatter: "{b} : {c}",
        },
        grid: {
          top: "5%",
          bottom: "10%",
          left: "15%",
          right: "5%",
        },
        xAxis: {
          type: "category",
          data: childtypelist,
        },
        yAxis: {
          type: "value",
        },
        series: [
          {
            data: this.cnt,
            type: "bar",
            showBackground: false,
            backgroundStyle: {
              color: "rgba(220, 220, 220, 0.8)",
            },
            label: {
              show: true,
              position: "top",
            },
            barWidth: "30",
          },
        ],
      };
      //防止越界，重绘canvas
      window.onresize = myChart.resize;
      myChart.setOption(option); //设置option
    },
    drawPieChart() {
      let myChart = echarts.init(document.getElementById("showPieChart"));

      var seriesData = [];
      var selected = {};
      for (var i = 0; i < childtypelist.length; i++) {
        seriesData.push({
          name: childtypelist[i],
          value: this.cnt[i],
          itemStyle: {
            color: colorList[i],
          },
          label: {
            fontSize: "14",
          },
        });
        selected[childtypelist[i]] = true;
      }
      var dataset = {
        legendData: childtypelist,
        seriesData: seriesData,
        selected: selected,
      };
      //console.log(dataset);
      // 绘制图表
      var option = {
        tooltip: {
          trigger: "item",
          formatter: "{a} <br/>{b} : {c} ({d}%)",
        },
        legend: {
          type: "scroll",
          orient: "vertical",
          right: 10,
          top: 20,
          bottom: 20,
          data: dataset.legendData,
          selected: dataset.selected,
        },
        series: [
          {
            name: "主题",
            type: "pie",
            radius: "55%",
            center: ["40%", "50%"],
            data: dataset.seriesData,
            emphasis: {
              itemStyle: {
                shadowBlur: 10,
                shadowOffsetX: 0,
                shadowColor: "rgba(0, 0, 0, 0.5)",
              },
            },
          },
        ],
      };
      //防止越界，重绘canvas
      window.onresize = myChart.resize;
      myChart.setOption(option); //设置option
    },
    onClick(value) {
      //alert("你点击了 " + value);
    },
    submit() {
      this.form.type = "";
      fetch(tpclassurl, {
        method: "POST",
        body: JSON.stringify({
          docs: [
            {
              id: 123,
              doc: this.content,
            },
          ],
        }),
        headers: {
          "Content-Type": "application/json",
        },
      })
        .then((res) => res.json())
        .catch((error) => console.error("Error:", error))
        .then((response) => {
          this.form.type = response.results[0].data;
          this.form.score = response.results[0].score;
          this.form.color = type2color[response.results[0].data];
          console.log(this.form.score);
          //this.drawDashboard();
        });

      //this.$message.success("提交成功！");
    },
    getRealTimeThemeInfo() {
      // 获取实时新闻列表
      fetch(carouselurl, {
        method: "GET",
        headers: {
          "Content-Type": "application/json",
        },
      })
        .then((res) => res.json())
        .catch((error) => console.error("Error:", error))
        .then((response) => {
          var theme_count = response.results.theme_count;
          this.cnt = [
            theme_count.education,
            theme_count.entertainment,
            theme_count.finance,
            theme_count.politics,
            theme_count.society,
            theme_count.sports,
            theme_count.technology,
          ];
          var tnewslist = response.results.news_list;
          var max_size = parseInt(tnewslist.length / 12);
          var tnews = [];
          tnewslist.forEach(function (news) {
            news.color = type2color[news.type];
            news.score = Math.floor(news.score * 100) / 100;
          });
          for (var i = 0; i < max_size; i++) {
            tnews.push(tnewslist.slice(i * 12, i * 12 + 12));
          }
          this.newslist = tnews;
          this.drawBarChart();
          this.drawPieChart();
        });
    },
  },
  mounted() {
    this.getRealTimeThemeInfo();
    //this.drawDashboard();
  },
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
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.12), 0 0 6px rgba(0, 0, 0, 0.04);
}
</style>


<template>
  <div class="unifiedldmc">
    <el-container>
      <el-header style="height: max-content;padding:0">
        <el-card class="noBorderInput">
          <h1 class="pageheader">文本主题分类</h1>
          <el-row>
            <el-input
              type="textarea"
              placeholder="请输入内容"
              v-model="content"
              maxlength="800"
              show-word-limit
              :autosize="{ minRows: 5, maxRows: 8}"
              clearable
              style="box-shadow: 0 2px 4px rgba(0, 0, 0, .12), 0 0 6px rgba(0, 0, 0, .04); font-size: 15px;"
            />
          </el-row>
          <el-row style="margin-top: 17px; display: flex; justify-content: center">
            <el-button
              v-on:click="submit"
              type="primary"
              style="background: #242f42; border: 0px; font-size: 15px; letter-spacing: 5px"
            >开始分析</el-button>
            <!--<el-button v-on:click="mockData">随机样例</el-button>-->
          </el-row>
        </el-card>
      </el-header>
      <el-main
        ref="mainContainer"
        style="text-align:center;margin-top: 20px;height: 100%;padding:0"
      >
        <el-row style="max-width:100%;max-height:480px">
          <el-card class="box-card">
            <div slot="header" class="clearfix" style="font-size: 18px">
              <span>本次主题分类结果</span>
            </div>
            <el-row>
              <div
                v-if="form.type.length > 0"
                style="text-align:center;height:26px;margin-top:5px;margin-bottom:20px"
              >
                <p style="font-size:26px;font-weight:bold" :style="{color:form.color}">{{form.type}}</p>
              </div>
              <div v-else style="min-height:26px;margin-top:5px;margin-bottom:20px"></div>
            </el-row>
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
          </el-card>
        </el-row>

        <el-row style="max-width:100%;margin-top:20px">
          <el-card class="box-card">
            <div slot="header" class="clearfix" style="color: black;font-size: 18px">
              <el-row>
                <el-col :span="8"><div style="min-height:10px"></div></el-col>
                <el-col :span="8">
                  <span style="max-width:210px">
                    <i class="iconfont iconxinwen"></i>
                    实时主题新闻分类结果
                  </span>
                </el-col>
                <el-col :span="8"><div style="min-height:10px"></div></el-col>
              </el-row>
              <div class="showupdatetime">更新时间：{{lastupdatetime}}</div>
            </div>
            <el-row style="text-align:left">
              <el-carousel
                :interval="12000"
                direction="vertical"
                arrow="never"
                indicator-position="none"
                height="400px"
                :loop="true"
              >
                <el-carousel-item v-for="(news, index) in newslist" :key="index">
                  <template v-for="i in 2">
                    <el-col :span="12" :key="i">
                      <el-table
                        :show-header="false"
                        :data="news.slice(i*6-6,i*6)"
                        style="fontSize:13px"
                      >
                        <el-table-column :show-overflow-tooltip="true">
                          <template slot-scope="scope">
                            <el-row>
                              <a
                                :href="scope.row.url"
                                target="_blank"
                                style="color:black"
                              >{{scope.row.event}}</a>
                            </el-row>
                            <el-row>
                              <el-col :span="15">发布时间：{{scope.row.publish_time}}</el-col>
                              <el-col :span="5">
                                类别：
                                <el-tag
                                  effect="dark"
                                  :color="scope.row.color"
                                  style="border-radius: 4px;border-color:rgba(255,255,255,0.01);box-shadow: 0 2px 4px rgba(0, 0, 0, .12), 0 0 6px rgba(0, 0, 0, .04);"
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

        <el-row style="margin:20px 0">
          <el-col :span="12">
            <el-card class="box-card">
              <div slot="header" class="clearfix" style="font-size: 18px;height: 28px;">
                <span>实时主题新闻数量统计</span>
                <div class="showupdatetime">更新时间：{{lastupdatetime}}</div>
              </div>
              <div id="showBarChart" :style="{width: '100%', height: '250px'}"></div>
            </el-card>
          </el-col>

          <el-col :span="12" style="padding-left:20px">
            <el-card class="box-card">
              <div slot="header" class="clearfix" style="font-size: 18px;height: 28px;">
                <span>实时主题新闻比例统计</span>
                <div class="showupdatetime">更新时间：{{lastupdatetime}}</div>
              </div>
              <div id="showPieChart" :style="{width: '100%', height: '250px'}"></div>
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

// 对Date的扩展，将 Date 转化为指定格式的String
// 月(M)、日(d)、小时(h)、分(m)、秒(s)、季度(q) 可以用 1-2 个占位符，
// 年(y)可以用 1-4 个占位符，毫秒(S)只能用 1 个占位符(是 1-3 位的数字)
// 例子：
// (new Date()).Format("yyyy-MM-dd hh:mm:ss.S") ==> 2006-07-02 08:09:04.423
// (new Date()).Format("yyyy-M-d h:m:s.S") ==> 2006-7-2 8:9:4.18
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

const childtypelist = ["教育", "娱乐", "财经", "时政", "社会", "体育", "科技"];
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
const tpclassurl = "http://115.236.52.123:6012/api/tpclassification";
const carouselurl = "http://115.236.52.123:6012/api/getRealTimeThemeInfo";

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
      lastupdatetime: new Date().Format("yyyy-MM-dd hh:mm:ss"),
      newslist: [],
      type2color: type2color,
      currentIndex: 0,
    };
  },
  methods: {
    drawBarChart() {
      let myChart = echarts.init(document.getElementById("showBarChart"));
      var dataset = [];
      childtypelist.forEach(function (item) {
        dataset.push({
          value: item,
          textStyle: {
            fontSize: "15",
          },
        });
      });
      // 绘制图表
      var option = {
        tooltip: {
          trigger: "item",
          formatter: "{b} : {c}",
        },
        grid: {
          top: "5%",
          bottom: "10%",
          left: "10%",
          right: "5%",
        },
        xAxis: {
          type: "category",
          data: dataset,
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
              fontSize: "15",
            },
            barWidth: "40%",
          },
        ],
      };
      //防止越界，重绘canvas
      window.onresize = myChart.resize;
      myChart.setOption(option);
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
            color: type2color[childtypelist[i]],
          },
          label: {
            fontSize: "15",
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
          textStyle: {
            fontSize: 15,
          },
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
            top: "-20%",
            bottom: "-20%",
          },
        ],
      };
      //防止越界，重绘canvas
      window.onresize = myChart.resize;
      myChart.setOption(option);

      let self = this;

      setInterval(function () {
        var dataLen = option.series[0].data.length;
        // 取消之前高亮的图形
        myChart.dispatchAction({
          type: "downplay",
          seriesIndex: 0,
          dataIndex: self.currentIndex,
        });
        self.currentIndex = (self.currentIndex + 1) % dataLen;
        // 高亮当前图形
        myChart.dispatchAction({
          type: "highlight",
          seriesIndex: 0,
          dataIndex: self.currentIndex,
        });
        // 显示 tooltip
        myChart.dispatchAction({
          type: "showTip",
          seriesIndex: 0,
          dataIndex: self.currentIndex,
        });
      }, 1000);
    },
    onClick(value) {
      //alert("你点击了 " + value);
    },
    clearText(testStr) {
        var resultStr = testStr.replace(/\ +/g, "");
        resultStr = resultStr.replace(/\s+/g, "");
        resultStr = resultStr.replace(/[ ]/g, "");    //去掉空格
        resultStr = resultStr.replace(/[\r\n]/g, ""); //去掉回车换行
        if(this.content.indexOf("（请输入文本）")!=-1){
          resultStr = resultStr.slice(0,resultStr.length-7)
        }
        return resultStr;
    },
    submit() {
      this.form.type = "";
      let textData = this.clearText(this.content);
      fetch(tpclassurl, {
        method: "POST",
        body: JSON.stringify({
          docs: [
            {
              id: 123,
              doc: textData,
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
    const refreshTime = 5 * 60 * 1000;
    var that = this;
    var func = function () {
      that.lastupdatetime = new Date().Format("yyyy-MM-dd hh:mm:ss");
      that.getRealTimeThemeInfo();
    };
    func();
    setInterval(func, refreshTime);
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
.unifiedldmc .el-card {
  border-radius: 0;
  background-color: #fff;
  box-shadow: 0 0px 0px 0 rgba(0, 0, 0, 0.1);
}
.unifiedldmc h1.pageheader {
  color: black;
  letter-spacing: 10px;
  font-weight: normal;
  font-size: 25px;
  margin-top: -20px;
}
.unifiedldmc .showupdatetime {
  color: gray;
  font-size: 10px;
  text-align: right;
  margin-bottom: -1%;
}
</style>


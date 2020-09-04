<template>
  <div>
    <el-container>
      <el-header>
        <h1 style="color: gray;text-align: center">文本主题分类</h1>
      </el-header>

      <el-main style="text-align: center">
        <el-row style="margin:20px 0">
          <el-input
            type="textarea"
            placeholder="【字节跳动或已拿下支付牌照】8月28日，武汉合众易宝科技有限公司股东中发实业（集团）有限公司退出，天津同融电子商务有限公司接盘100%股份。天津同融电子商务有限公司是北京石贝科技有限公司全资子公司，穿透以后，字节跳动创始人张一鸣是实际控制人。合众支付官网显示，该公司2014年获得由中国人民银行颁发的《支付业务许可证》，成为湖北省首家持牌互联网支付企业。（21财经）"
            v-model="content"
            maxlength="800"
            show-word-limit
            :rows="6"
            clearable
            style="box-shadow: 0 2px 4px rgba(0, 0, 0, .12), 0 0 6px rgba(0, 0, 0, .04)"
          />
        </el-row>

        <el-row style="margin-top: 30px">
          <el-button @click="submit" type="primary" style="background: #242f42; border: 0px">开始分析</el-button>
          <el-button>随机样例</el-button>
        </el-row>

        <el-row style="margin: 20px 0">
          <el-card shadow="always">
            <div slot="header" class="clearfix">
              <span>文本分类结果</span>
            </div>
            <el-button-group>
              <template v-for="type in types">
                <el-button
                  type="success"
                  size="medium"
                  :key="type"
                  v-if="form.type.indexOf(type)>=0"
                  @click="onClick(type)"
                >{{type}}</el-button>
                <el-button type="info" size="medium" :key="type" v-else disabled>{{type}}</el-button>
              </template>
            </el-button-group>
          </el-card>
        </el-row>

        <el-row style="margin:10px 0;max-width:100%;max-height:200px">
          <el-carousel
            :interval="10000"
            arrow="never"
            indicator-position="none"
            width="200px"
            height="200px"
            :loop="true"
            @change="changePage"
          >
            <el-carousel-item v-for="(news, index) in newslist" :key="index">
              <el-card :body-style="{ padding: '5px'}">
                <el-row>要闻</el-row>
                <el-row>
                  <el-col :span="6">
                    <el-table
                      :show-header="false"
                      :data="news.events.slice(0,4)"
                      style="height:180px;max-height:180px;margin-top:5px"
                    >
                      <el-table-column align="left" :show-overflow-tooltip="true">
                        <template slot-scope="scope">
                          <a :href="scope.row.url">[{{news.kind}}]{{scope.row.event}}</a>
                        </template>
                      </el-table-column>
                    </el-table>
                  </el-col>
                  <el-col :span="6">
                    <el-table
                      :show-header="false"
                      :data="news.events.slice(4,8)"
                      style="height:180px;max-height:180px;margin-top:5px"
                    >
                      <el-table-column align="left" :show-overflow-tooltip="true">
                        <template slot-scope="scope">
                          <a :href="scope.row.url">[{{news.kind}}]{{scope.row.event}}</a>
                        </template>
                      </el-table-column>
                    </el-table>
                  </el-col>
                  <el-col :span="6">
                    <el-table
                      :show-header="false"
                      :data="news.events.slice(8,12)"
                      style="height:180px;max-height:180px;margin-top:5px"
                    >
                      <el-table-column align="left" :show-overflow-tooltip="true">
                        <template slot-scope="scope">
                          <a :href="scope.row.url">[{{news.kind}}]{{scope.row.event}}</a>
                        </template>
                      </el-table-column>
                    </el-table>
                  </el-col>
                  <el-col :span="6">
                    <el-table
                      :show-header="false"
                      :data="news.events.slice(12,16)"
                      style="height:180px;max-height:180px;margin-top:5px"
                    >
                      <el-table-column align="left" :show-overflow-tooltip="true">
                        <template slot-scope="scope">
                          <a :href="scope.row.url">[{{news.kind}}]{{scope.row.event}}</a>
                        </template>
                      </el-table-column>
                    </el-table>
                  </el-col>
                </el-row>
              </el-card>
            </el-carousel-item>
          </el-carousel>
        </el-row>

        <el-row style="margin-top:26px">
          <el-col :span="12">
            <el-card>
              <div slot="header" class="clearfix">
                <span>实时主题新闻数量统计</span>
              </div>
              <div id="showBarChart" :style="{width: '100%', height: '400px'}"></div>
            </el-card>
          </el-col>

          <el-col :span="12" style="padding-left:20px">
            <el-card>
              <div slot="header" class="clearfix">
                <span>实时主题新闻比例统计</span>
              </div>
              <div id="showPieChart" :style="{width: '100%', height: '400px'}"></div>
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

const typelist = [
  "体育",
  "娱乐",
  "家居",
  "彩票",
  "房产",
  "教育",
  "时尚",
  "时政",
  "星座",
  "游戏",
  "社会",
  "科技",
  "股票",
  "财经",
];

const tpclassurl = "http://49.234.217.110:5000/api/tpclassification";
const carouselurl = "http://49.234.217.110:5000/api/getRealTimeThemeInfo";
const eng2cn = {
  education_news: "教育",
  entertainment_news: "娱乐",
  finance_news: "财经",
  politics_news: "时政",
  society_news: "社会",
  sports_news: "体育",
  technology_news: "科技",
};

export default {
  name: "markdown",
  data: function () {
    return {
      form: {
        type: [],
      },
      content: "【字节跳动或已拿下支付牌照】8月28日，武汉合众易宝科技有限公司股东中发实业（集团）有限公司退出，天津同融电子商务有限公司接盘100%股份。天津同融电子商务有限公司是北京石贝科技有限公司全资子公司，穿透以后，字节跳动创始人张一鸣是实际控制人。合众支付官网显示，该公司2014年获得由中国人民银行颁发的《支付业务许可证》，成为湖北省首家持牌互联网支付企业。（21财经）",
      editorOption: {
        placeholder: "请在这里输入待分类的文本",
      },
      types: typelist,
      cnt: [],
      colorSt: {
        "background-color": "#99a9bf",
      },
      newslist: [],
    };
  },
  methods: {
    drawBarChart() {
      let myChart = echarts.init(document.getElementById("showBarChart"));
      // 绘制图表
      var option = {
        tooltip: {
          trigger: "item",
          formatter: "{b} : {c}",
        },
        grid: {
          left: "10%",
          right: "10%",
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
            showBackground: true,
            backgroundStyle: {
              color: "rgba(220, 220, 220, 0.8)",
            },
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
        seriesData.push({ name: childtypelist[i], value: this.cnt[i] });
        selected[childtypelist[i]] = true;
      }
      var dataset = {
        legendData: childtypelist,
        seriesData: seriesData,
        selected: selected,
      };
      console.log(dataset);
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
    initType() {
      this.form.type = [];
    },
    changePage() {
      console.log("change-page");
    },
    onClick(value) {
      //alert("你点击了 " + value);
    },
    submit() {
      this.form.type = [];
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
        .then((response) => (this.form.type = response.results[0].data));

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
          console.log(response);
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
          var news = response.results;
          delete news.theme_count;
          
          this.newslist = [];
          for (var key in news) {
            
            this.newslist.push({
              kind: eng2cn[key],
              events: news[key],
            });
          }
          this.drawBarChart();
          this.drawPieChart();
        });
    },
  },
  mounted() {
    this.getRealTimeThemeInfo();
  },
};
</script>
<style scoped>
/*
.el-carousel__item:nth-child(2n){
  background-color: #99a9bf;
}
.el-carousel__item:nth-child(2n + 1){
  background-color: #d3dce6;
}*/
</style>
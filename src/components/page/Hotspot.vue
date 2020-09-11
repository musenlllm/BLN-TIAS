<template>
  <!--<link rel="stylesheet" type="text/css" href="http://at.alicdn.com/t/font_2015036_ral7di9rm4.css">-->
  <div>
    <el-container>
      <el-header style="height: max-content;text-align: center">
        <el-card
          class="noBorderInput"
          style="margin-top:20px;border-radius: 0;background-color: #fff;box-shadow: 0 0px 0px 0 rgba(0, 0, 0, 0.1);"
        >
          <h1
            class="pageheader"
            style="
  color: black;
  letter-spacing: 10px;
  font-weight: normal;
  font-size: 25px"
          >热点挖掘</h1>

          <div class="diyCardBody">
            <el-row :gutter="20">
              <el-col :span="8">
                <!--<el-card shadow="always" class="box-card" :body-style="{padding: '0px'}" style="min-height: 458px;font-size: 18px">-->
                <el-card
                  class="noBorderInput"
                  :body-style="{padding: '0px'}"
                  style="min-height: 466px;border: 0px;border-radius: 0;background-color: #fff;box-shadow: 0 0px 0px 0 rgba(0,0,0,.1);"
                >
                  <div slot="header" class="clearfix" style="font-size: 18px;height: 30px;">
                    <span>
                      <!--<link rel="icon" href="../../assets/icon/news.icon" type="image/x-icon">-->
                      <!--<svg class="icon" aria-hidden="true">-->
                      <!--<use xlink:href="#iconxinwen"></use>-->
                      <!--</svg>-->
                      <i class="iconfont iconxinwen"></i>
                      <!--<i class="ldmcxinwen" style="font-size: 21px;"></i>-->
                      热点新闻
                    </span>
                  </div>
                  <div
                    class="tag-group"
                    style=" display: flex; justify-content: center; flex-direction: row; flex-wrap: wrap;"
                  >
                    <el-table
                      :data="this.hotspotRes.hot_event"
                      style="width: 100%; text-align: center; "
                      stripe
                      :row-class-name="tableRowClassName"
                      @sort-change="changeSort"
                      :default-sort="{prop: 'rank', order: 'ascending'}"
                      :show-overflow-tooltip="true"
                      max-height="400px"
                      :header-row-style="{height: '30px'}"
                    >
                      <el-table-column
                        align="center"
                        header-align="center"
                        prop="rank"
                        label="排序"
                        sortable
                        :sort-orders="['ascending', 'descending']"
                        width="80%"
                      >
                        <div slot-scope="scope" v-if="scope.row.rank<4">
                          <i class="iconfont iconmingcheng-huobao-t"></i>
                        </div>
                        <div slot-scope="scope" v-else>{{scope.row.rank}}</div>
                      </el-table-column>
                      <el-table-column
                        align="left"
                        header-align="center"
                        prop="event"
                        label="新闻话题"
                        :show-overflow-tooltip="true"
                        width="200%"
                      >
                        <template slot-scope="scope">
                          <a
                            :href="scope.row.url"
                            target="_blank"
                            class="buttonText"
                          >{{scope.row.event}}</a>
                        </template>
                      </el-table-column>
                      <el-table-column
                        align="center"
                        prop="popularity"
                        label="阅读量"
                        :show-overflow-tooltip="true"
                      ></el-table-column>
                    </el-table>
                  </div>
                </el-card>
              </el-col>
              <el-col :span="8">
                <!--<el-card shadow="always" :body-style="{padding: '0px'}" style="min-height: 458px;">-->
                <el-card
                  class="noBorderInput"
                  :body-style="{padding: '0px'}"
                  style="min-height: 466px;border: 0px;border-radius: 0;background-color: #fff;box-shadow: 0 0px 0px 0 rgba(0,0,0,.1);"
                >
                  <div slot="header" class="clearfix" style="font-size: 18px;height: 30px;">
                    <span>
                      <i class="el-icon-chat-line-square" style="font-size: 21px"></i>

                      <!--<i class="iconfont iconhuati"></i>-->
                      热点话题
                    </span>
                  </div>
                  <div
                    class="tag-group"
                    style=" display: flex; justify-content: center; flex-direction: row; flex-wrap: wrap;"
                  >
                    <el-table
                      :data="hotspotRes.hot_topic"
                      style="width: 100%; text-align: center;"
                      header-cell-style="font-weight:500"
                      @sort-change="changeSort"
                      :default-sort="{prop: 'rank', order: 'ascending'}"
                      :row-class-name="tableRowClassName"
                      stripe
                      :show-overflow-tooltip="true"
                      max-height="400px"
                    >
                      <el-table-column
                        align="center"
                        prop="rank"
                        label="排序"
                        sortable
                        :sort-orders="['ascending', 'descending']"
                        width="80%"
                      >
                        <div slot-scope="scope" v-if="scope.row.rank<4">
                          <i class="iconfont iconmingcheng-huobao-t"></i>
                        </div>
                        <div slot-scope="scope" v-else>{{scope.row.rank}}</div>
                      </el-table-column>
                      <el-table-column
                        align="left"
                        header-align="center"
                        prop="topic"
                        label="新闻话题"
                        :show-overflow-tooltip="true"
                      >
                        <template slot-scope="scope">
                          <a
                            :href="scope.row.url"
                            target="_blank"
                            class="buttonText"
                          >{{scope.row.topic}}</a>
                        </template>
                      </el-table-column>
                      <el-table-column align="center" prop="view_number" label="阅读量" width="100%"></el-table-column>
                      <!--<el-table-column-->
                      <!--prop="url"-->
                      <!--label="链接"-->
                      <!--sortable="custom">-->
                      <!--</el-table-column>-->

                      <!--{{ item.label }}-->
                    </el-table>
                  </div>
                </el-card>
              </el-col>
              <el-col :span="8">
                <!--<el-card shadow="always" :body-style="{padding: '0px'}" style="min-height: 458px;">-->
                <el-card
                  class="noBorderInput"
                  :body-style="{padding: '0px'}"
                  style="min-height: 466px;border: 0px;border-radius: 0;background-color: #fff;box-shadow: 0 0px 0px 0 rgba(0,0,0,.1);"
                >
                  <div slot="header" class="clearfix" style="font-size: 18px;height: 30px;">
                    <span>
                      <i class="iconfont iconzengchang1"></i>
                      <!--</div>-->
                      最近半小时增长新闻
                    </span>
                  </div>
                  <el-table
                    :data="this.recent_half_hour_increase_news"
                    style="width: 100%; text-align: center;"
                    stripe
                    @sort-change="changeSort"
                    :default-sort="{prop: 'publish_time', order: 'descending'}"
                    :row-class-name="tableRowClassName"
                    :show-overflow-tooltip="true"
                    max-height="400px"
                  >
                    <el-table-column
                      align="left"
                      type="index"
                      header-align="center"
                      prop="news"
                      label="新闻话题"
                      :show-overflow-tooltip="true"
                      width="220%"
                    >
                      <template slot-scope="scope" v-if="scope.row.url">
                        <i :href="scope.row.url" class="iconfont iconzuixin"></i>
                        <a
                          :href="scope.row.url"
                          target="_blank"
                          class="buttonText"
                        >【{{scope.row.news_type}}】{{scope.row.news}}</a>
                      </template>
                    </el-table-column>
                    <el-table-column
                      align="center"
                      prop="publish_time"
                      label="发布时间"
                      sortable
                      :sort-orders="['ascending', 'descending']"
                      :show-overflow-tooltip="true"
                    >
                      <template slot-scope="scope">
                        <span>{{scope.row.publish_time}}</span>
                      </template>
                    </el-table-column>
                  </el-table>
                </el-card>
              </el-col>
            </el-row>
          </div>
        </el-card>
      </el-header>
      <el-main style="margin-left: 0px; margin-top: -30px; text-align: center">
        <!--<el-card class="box-card" style="min-height:200px; margin-top: 20px;text-align: center">-->
        <el-card
          class="noBorderInput"
          :body-style="{padding: '0px'}"
          style="text-align: center;margin-top: 30px;min-height: 200px;border: 0px;border-radius: 0;background-color: #fff;box-shadow: 0 0px 0px 0 rgba(0,0,0,.1);"
        >
          <el-tabs
            type="card"
            v-model="activeName"
            @tab-click="handleClick"
            style="border: 0px;border-radius: 0"
          >
            <el-tab-pane label="今日" name="first">
              <div
                class="wrap"
                v-if="isChildUpdate1"
                style="display: flex; justify-content: space-around"
              >
                <div id="hot_key_words1" style="width:30%;min-height:400px;"></div>
                <div id="hot_freq_words1" style="width:30%;height:400px;"></div>
                <div id="today_hot_distribution1" style="width:38%;height:380px;margin-bottom:20px"></div>

                <!--<div>{{this.freq_words2_list}}</div>-->
              </div>
            </el-tab-pane>
            <el-tab-pane label="近七日" name="third">
              <div
                class="wrap"
                v-if="isChildUpdate3"
                style="display: flex; justify-content: space-around"
              >
                <div id="hot_key_words3" style="width:30%;min-height:400px;"></div>
                <div id="hot_freq_words3" style="width:30%;min-height:400px;"></div>
                <div id="today_hot_distribution3" style="width:38%;height:380px;margin-bottom:20px"></div>
                <!--<div>{{this.key_words2_list}}</div>-->
              </div>
            </el-tab-pane>
          </el-tabs>
        </el-card>
        <!--</el-main>-->
        <!--<el-main style="text-align: center; margin-top: 10px; ">-->
        <!--<el-card class="box-card" style="min-height: 400px;margin-top: 20px;text-align: center">-->
        <!--<el-card class="noBorderInput" :body-style="{padding: '0px'}" style="text-align: center;margin-top: 30px;min-height: 200px;border: 0px;border-radius: 0;background-color: #fff;box-shadow: 0 0px 0px 0 rgba(0,0,0,.1);">-->
        <!--<div slot="header" class="clearfix" style="font-size: 18px">-->
        <!--<span>新闻主题分布图</span>-->
        <!--</div>-->
        <!--<div id="today_hot_distribution" style="width:100%;height:600px;"></div>-->
        <!--<div id="week_hot_distribution" style="width:100%;height:600px;">近七日</div>-->
        <!--&lt;!&ndash;{{this.recent_half_hour_increase_news}}&ndash;&gt;-->
        <!--&lt;!&ndash;{{this.nearly_one_week_news_dis}}&ndash;&gt;-->
        <!--&lt;!&ndash;{{this.nearly_three_days_news_dis}}&ndash;&gt;-->
        <!--&lt;!&ndash;{{this.today_news_dis}}&ndash;&gt;-->
        <!--</el-card>-->
        <!--<el-card class="box-card" style="min-height: 50px; margin-top: 20px">-->
        <el-card
          class="noBorderInput"
          :body-style="{padding: '0px'}"
          style="text-align: center;margin-top: 30px;min-height: 200px;border: 0px;border-radius: 0;background-color: #fff;box-shadow: 0 0px 0px 0 rgba(0,0,0,.1);"
        >
          <div slot="header" class="clearfix" style="font-size: 18px">
            <span>近7日各主题新闻的每天增长数</span>
          </div>
          <!--折线图-->
          <div class="wrap">
            <div id="hot_trend" style="width:100%;min-height: 600px;"></div>
          </div>

          <!--<div>{{this.hot_statistics}}</div>-->
        </el-card>
      </el-main>
    </el-container>
  </div>
</template>
<script>
import echarts from "echarts";
import { fetchData } from "../../api/index";
// import resize from "./mixins/resize";
import "echarts-wordcloud/dist/echarts-wordcloud";
import "echarts-wordcloud/dist/echarts-wordcloud.min";
const hotspoturl = "http://115.236.52.123:6012/api/hotspot";
// const maskImage = new Image();

const type2color = [
  "rgb(151, 94, 109)",
  "rgb(224, 113, 156 )",
  "rgb( 221, 76, 81)",
  "rgb(201, 74, 68 )",
  "rgb(221, 76, 81 )",
  "rgb(247, 161, 40 )",
  "rgb(225, 195, 21 )",
  "rgb(176, 151, 51 )",
  "rgb(162, 176, 41 )",
  "rgb(113, 137, 51 )",
  "rgb(58, 162, 85 )",
  "rgb(94, 154, 128 )",
  "rgb(157, 178, 183 )",
  "rgb( 118, 192, 203)",
  "rgb(202, 164, 101 )",
  "rgb(223, 189, 126 )",
  "rgb(190, 134, 99 )",
  "rgb(221, 175, 97 )",
  "rgb(121, 71, 82 )",
  "rgb(204, 61, 65 )",
  "rgb(177, 77, 87 )",
  "rgb(199, 136, 105 )",
  "rgb(187, 118, 76 )",
  "rgb( )",
  "rgb( )",
  "rgb( )",
  "rgb( )",
];
const cloudcolor = [
  "#F56C6C",
  "pink",
  "#A39391",
  "#D45246",
  "#FFCC99",
  "#9999CC",
  "#3366CC",
  "#E6A23C",
  "#FB3C3C",
  "#203643",
  "#74C2E1",
  "#84CF96",
  "#67C23A",
];

export default {
  name: "basetable",
  data() {
    return {
      hotspotRes: {},
      items: [],
      // 柱状图
      charts: "",
      view_number: "",
      hot_event: [],
      hot_topic: [],
      freq_words: [],
      freq_words_list: [],
      freq_words1_list: [],
      freq_words2_list: [],
      freq_words3_list: [],
      key_words: [],
      key_words_list: [],
      key_words1_list: [],
      key_words2_list: [],
      entData: [],
      activeName: "third",
      isChildUpdate1: false,
      isChildUpdate2: false,
      isChildUpdate3: true,
      recent_half_hour_increase_news: [],
      test: { name: "Liza", password: "123" },
      hot_statistics: {},
      today_news_distribution: {},
      today_news_dis: [],
      nearly_three_days_news_distribution: {},
      nearly_three_days_news_dis: [],
      nearly_one_week_news_distribution: {},
      nearly_one_week_news_dis: [],
      // var maskImage = new Image();
      // maskImage.src = this.image2;

      one_week_time: [],
      news_info: [],
      dataTrend: {},
      // <<<<<<< Updated upstream
      name: [
        "国内",
        "世界",
        "体育",
        "社会",
        "历史",
        "娱乐",
        "军事",
        "政府",
        "教育",
        "经济",
        "评论",
        "其他",
      ],
      source: [
        ["topic", "今日", "近七日"],
        ["评论"],
        ["国内"],
        ["教育"],
        ["娱乐"],
        ["经济"],
        ["政府"],
        ["历史"],
        ["军事"],
        ["其他"],
        ["社会"],
        ["体育"],
        ["世界"],
      ],

      //高频词的热力图数据
      heatmap_x_axis: [],
      today_freq_heat_data: [],
      one_week_freq_heat_data: [],
      heatmap: "",
      image1:
        "data:image/png;base64,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",

      // =======
      //             name:["Domestic国内","World世界","Sports体育","Society社会","History历史","Entertainment娱乐",
      //                         "Military军事","Government政府","Education教育","Finance经济","Comment评论","Other其他"],
      //             source:[['topic','今日','近七日'],['Comment评论'],['Domestic国内'], ['Education教育'], ['Entertainment娱乐'], ['Finance经济'],['Government政府'],
      //               ['History历史'], ['Military军事'], ['Other其他'], ['Society社会'], ['Sports体育'], ['World世界']],
      image2:
        "data:image/png;base64,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",
      image3:
        "data:image/png;base64,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",
      image4:
        "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAABU0lEQVQ4T6WTsUsCYRjGf9/daXfnFu1N1RoFESQJLf0DBU39Bw5KChY0OHgStdTQ1iAELo2NDhYZtBXhEm0RlNGUnEl3X5yinJJ60jd9vB/83ud93ucTUkqVfxwxLmD5nMjjO9NfCape37EBSo47CQt6iFU7RaUHED5g23FYUVVummkK/ZMZeWINl1KnLqDcBfgfFUHWyZDtB5iHLNlNKp16WGNT6JZc+3Y5kjALmH66oZOoJ3mInmHevrHjSvZ90GrEYKulQOT4GbKIDwEvEuZbpkHZNIh7d8/IFkDJUZIQC7pNuYvWVeoBJvJsNF2KQQFmiMV6ivueNY4DUQTHTobkwByoVtusPtO6AhXBqZNp+zAwSEMU1aZ0orUkzyOTqFgUBbxKyZyEdQEXYY1CI81lj4mjzAtZ7Gkq13aaK288f8gC/YWZEyaf4nz+1SgQYJjCXzBWkv34rjyaAAAAAElFTkSuQmCC",
      image5:
        "data:image/png;base64,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",
    };
  },
  created() {},
  mounted() {
    // this.WordCloud('hot_freq_words');
    // this.drawTest('hot_trend_test');
    this.ResultofHospot();
    this.init();
  },
  methods: {
    handleClick(tab) {
      if (tab.name == "first") {
        this.isChildUpdate1 = true;
        this.getHotTopic(
          "today_hot_distribution1",
          this.today_news_distribution,
          "今日新闻主题分类"
        );
        this.getKeyWords(
          "hot_key_words1",
          this.key_words.today,
          "今日新闻高影响力词分布词云"
        );
        this.getFreqWords(
          "hot_freq_words1",
          this.freq_words.today,
          "今日新闻高频词分布"
        );
        // this.isChildUpdate2 = false;
        this.isChildUpdate3 = false;
      } else if (tab.name == "third") {
        this.isChildUpdate1 = false;
        // this.isChildUpdate2 = false;
        this.isChildUpdate3 = true;
        this.getHotTopic(
          "today_hot_distribution3",
          this.nearly_one_week_news_distribution,
          "近七日新闻主题分类"
        );
        this.getKeyWords(
          "hot_key_words3",
          this.key_words.nearly_one_week,
          "近七日新闻高影响力词分布词云"
        );
        this.getFreqWords(
          "hot_freq_words3",
          this.freq_words.nearly_one_week,
          "近七日新闻高频词分布"
        );
      }
    },
    // 获取高频词列表
    getFreqWords(id, freq_words, title) {
      for (let i = 0; i < 100; i++) {
        let obj = {};
        obj.name = freq_words[i].word;
        obj.value = freq_words[i].frequency;
        obj.itemStyle = {
          color: type2color[i % 20],
        };
        this.freq_words_list[i] = obj;
      }
      this.$nextTick(() => {
        this.drawRose(id, this.freq_words_list, title);
      });
    },
    // 获取关键词列表
    getKeyWords(id, key_words, title) {
      for (let i = 0; i < 100; i++) {
        let obj = {};
        obj.name = key_words[i].word;
        obj.value = key_words[i].influence;
        this.key_words_list[i] = obj;
      }
      this.$nextTick(() => {
        this.WordCloud(id, this.key_words_list, title);
      });
    },
    getHotTopic(id, today_news_distribution, title) {
      this.$nextTick(() => {
        this.drawDistribution(id, today_news_distribution, title);
      });
    },
    //玫瑰图
    drawRose(id, data, title) {
      data = data.slice(0, 20);
      // 基于准备好的dom，初始化echarts实例
      this.chart = echarts.init(document.getElementById(id));
      // 指定图表的配置项和数据
      var option = {
        title: {
          text: title,
          x: "center",
          top: "1%", //各个方向的内边距，默认是5，可以自行设置
          textStyle: {
            //标题内容的样式
            fontStyle: "normal", //主标题文字字体风格，默认normal，有italic(斜体),oblique(斜体)
            fontWeight: "normal", //可选normal(正常)，bold(加粗)，bolder(加粗)，lighter(变细)，100|200|300|400|500...
            fontSize: 15, //主题文字字体大小，默认为18px
          },
          left: "center",
        },
        tooltip: {
          trigger: "item",
          formatter: "{a} <br/>{b} : {c} ({d}%)",
        },

        series: [
          {
            name: "面积模式",
            type: "pie",
            radius: [30, 110],
            roseType: "area",
            data: data,
          },
        ],
      };
      this.chart.setOption(option);
      // window.addEventListener("resize", function() {
      //   this.chart.resize()
      // })
      // setTimeout(function () {
      //     var width = $('#aside').width();
      //     if(width=='100'|| width=='60'){ //一定要加定时器，然后判断宽度是展开或者收起的时候再去调用echarts提供的resize()方法
      //         this.chart.resize();
      //     }
      //  },200);
      // window.addEventListener("resize", function() {
      //   this.chart.resize();
      // });
    },
    //词云
    WordCloud(id, words, title) {
      this.chart = echarts.init(document.getElementById(id));
      var maskImage = new Image();

      maskImage.src = this.image5;
      //maskImage.src = this.image2;

      var option = {
        /*colorArr: [
          "#fda67e",
          "#81cacc",
          "#cca8ba",
          "#88cc81",
          "#82a0c5",
          "#fddb7e",
          "#735BA1",
          "#bda29a",
          "#6e7074",
          "#546570",
          "#c4ccd3",
        ],*/
        title: {
          text: title,
          x: "center",
          padding: 9,
          top: "0%", //各个方向的内边距，默认是5，可以自行设置
          textStyle: {
            //标题内容的样式
            fontStyle: "normal", //主标题文字字体风格，默认normal，有italic(斜体),oblique(斜体)
            fontWeight: "normal", //可选normal(正常)，bold(加粗)，bolder(加粗)，lighter(变细)，100|200|300|400|500...
            fontSize: 15, //主题文字字体大小，默认为18px
          },
        },
        tooltip: {
          trigger: "item",
        },
        backgroundColor: "#fff",
        grid: {
          left: "",
          right: "0%",
          bottom: "5%",
          top: "19%",
          containLabel: true,
        },

        series: [
          {
            type: "wordCloud",
            //用来调整词之间的距离
            gridSize: 0,
            //用来调整字的大小范围
            // Text size range which the value in data will be mapped to.
            // Default to have minimum 12px and maximum 60px size.
            sizeRange: [9, 38],
            // Text rotation range and step in degree. Text will be rotated randomly in range [-90,                                                                             90] by rotationStep 45
            //用来调整词的旋转方向，，[0,0]--代表着没有角度，也就是词为水平方向，需要设置角度参考注释内容
            rotationRange: [-40, 0, 45, 90],
            // rotationRange: [ 0,90],
            // rotationRange: [0, 0],
            //随机生成字体颜色

            maskImage: maskImage,
            textStyle: {
              normal: {
                color: function () {
                  var colorArr = cloudcolor.slice(
                    0,
                    10
                  ); /*[
                    "#7db5e2",
                    "#81cacc",
                    "#cca8ba",
                    "#7EBF50",
                    "#82a0c5",
                    "#fddb7e",
                    "#bda29a",
                    "#d2a59a",
                    "#909399",
                    "#c4ccd3",
                    "#67C23A",
                  ]*/
                  var flag = parseInt(Math.random() * 10);
                  return colorArr[flag];
                },
              },
            },
            //位置相关设置
            // Folllowing left/top/width/height/right/bottom are used for positioning the word cloud
            // Default to be put in the center and has 75% x 80% size.
            left: "center",
            top: "center",
            right: null,
            bottom: null,
            width: "90%",
            height: "90%",
            //数据
            // data: words.slice(0,words.length-40),
            data: words,
          },
        ],
      };
      // maskImage.onload=function(){
      //
      //     this.chart.setOption(option);
      //
      // };
      this.chart.setOption(option);
      window.addEventListener("resize", function() {
        this.chart.resize()
      })
    },
    // 获取热点挖掘的数据
    ResultofHospot() {
      fetch(hotspoturl, {
        method: "POST",
        body: JSON.stringify({
          // docs: [{
          //       "id":0,
          //       "doc":this.summaryText,
          // }]
        }),
        headers: {
          "Content-Type": "application/json",
        },
      })
        .then((res) => res.json())
        .catch((error) => console.error("Error:", error))
        .then((response) => {
          this.hotspotRes = response.results;
          // console.log("success")
          // this.hot_event = hotspotRes.hot_event;
          // this.hot_topic = hotspotRes.hot_topic;
          // this.hot_freq_words = hotspotRes.hot_freq_words;
          // this.hot_key_words = hotspotRes.hot_key_words;
          // this.hot_statistics = hotspotRes.hot_statistics;
          this.recent_half_hour_increase_news = this.hotspotRes.hot_statistics.recent_half_hour_increase_news;

          this.today_news_distribution = this.hotspotRes.hot_statistics.today_news_distribution;
          console.log("success3");
          this.today_news_dis = Object.values(this.today_news_distribution);
          console.log("success5");
          this.nearly_one_week_news_distribution = this.hotspotRes.hot_statistics.nearly_one_week_news_distribution;
          this.nearly_one_week_news_dis = Object.values(
            this.nearly_one_week_news_distribution
          );

          /****Part 2****/
          //词云
          this.key_words = this.hotspotRes.hot_key_words;
          // var key_words1 = this.key_words.today;
          // var key_words2 = this.key_words.nearly_three_days;
          var key_words3 = this.key_words.nearly_one_week;
          // this.getKeyWords("hot_key_words1",key_words1,'今日新闻高影响力词分布词云');
          // this.getKeyWords("hot_key_words2",key_words2,'近三日新闻高影响力词分布词云');
          // setTimeout(()=>{
          //     this.getKeyWords("hot_key_words3",this.key_words.nearly_one_week,'近七日新闻高影响力词分布词云');
          //     // this.drawDistribution("today_hot_distribution",this.nearly_one_week_news_dis,'近七日');
          // })
          console.log("success draw ciyun");
          this.getKeyWords(
            "hot_key_words3",
            key_words3,
            "近七日新闻高影响力词分布词云"
          );
          //玫瑰图
          this.freq_words = this.hotspotRes.hot_freq_words;
          // var freq_words1 = this.freq_words.today;
          // var freq_words2 = this.freq_words.nearly_three_days;
          var freq_words3 = this.freq_words.nearly_one_week;
          // this.getFreqWords("hot_freq_words1",freq_words1,'今日新闻高频词分布词云');
          // this.getFreqWords("hot_freq_words2",freq_words2,'近三日新闻高频词分布词云');
          this.getFreqWords(
            "hot_freq_words3",
            freq_words3,
            "近七日新闻高频词分布"
          );
          //近七天的话题柱状图
          this.getHotTopic(
            "today_hot_distribution3",
            this.nearly_one_week_news_distribution,
            "近七日新闻主题分类"
          );
          // //获取高频词热力图所需要的数据
          // var today_freq_heat = this.hotspotRes.hot_freq_words.today;
          // //测试接受数据是否正确
          // for(let i=0;i<10;i++){
          //   this.today_freq_heat_data.push({
          //     'name':today_freq_heat[i].word,
          //     'value':today_freq_heat[i].frequency
          //   });
          // }
          //柱状图
          var i = 1;

          for (i; i < 13; i++) {
            this.source[i].push(this.today_news_dis[i - 1]);
            // .push(this.nearly_three_days_news_dis[i-1]).push(this.nearly_one_week_news_dis[i-1])
            this.source[i].push(this.nearly_one_week_news_dis[i - 1]);
            console.log(i);
            // this.source = a.concat(b);
          }
          // setTimeout(()=>{
          //     this.drawDistribution("today_hot_distribution",this.today_news_distribution,'今日');
          //     // this.drawDistribution("today_hot_distribution",this.nearly_one_week_news_dis,'近七日');
          // })
          console.log("success");
          //折线图
          this.hot_statistics = this.hotspotRes.hot_statistics;
          this.getDay();
          for (let i = 0; i < 7; i++) {
            let key = this.one_week_time[i];
            this.dataTrend[key] = [
              this.hot_statistics.domestic_trend[i],
              this.hot_statistics.world_trend[i],
              this.hot_statistics.sports_trend[i],
              this.hot_statistics.society_trend[i],
              this.hot_statistics.history_trend[i],
              this.hot_statistics.entertainment_trend[i],
              this.hot_statistics.military_trend[i],
              this.hot_statistics.government_trend[i],
              this.hot_statistics.education_trend[i],
              this.hot_statistics.finance_trend[i],
              this.hot_statistics.comment_trend[i],
              this.hot_statistics.other_trend[i],
            ];
          }
          this.drawDTrend(
            "hot_trend",
            this.one_week_time.reverse(),
            this.dataTrend,
            this
          );
        });
    },

    //场景分布柱状图
    drawDistribution(id, data1, date) {
      // 基于准备好的dom，初始化echarts实例
      this.chart = echarts.init(document.getElementById(id));
      // 指定图表的配置项和数据
      var option1 = {
        title: {
          text: date,
          x: "center",
          padding: 9,
          top: "0%", //各个方向的内边距，默认是5，可以自行设置
          textStyle: {
            //标题内容的样式
            fontStyle: "normal", //主标题文字字体风格，默认normal，有italic(斜体),oblique(斜体)
            fontWeight: "normal", //可选normal(正常)，bold(加粗)，bolder(加粗)，lighter(变细)，100|200|300|400|500...
            fontSize: 15, //主题文字字体大小，默认为18px
          },
        },
        color: ["rgb(218, 29, 35)"],
        tooltip: {
          trigger: "axis",
          axisPointer: {
            // 坐标轴指示器，坐标轴触发有效
            type: "shadow", // 默认为直线，可选为：'line' | 'shadow'
          },
        },
        dataset: {
          source: this.source,
        },
        grid: {
          left: "3%",
          right: "4%",
          bottom: "10%",
          containLabel: true,
        },
        xAxis: [
          {
            type: "value",
          },
        ],
        yAxis: [
          {
            type: "category",
            nameTextStyle: {
              fontSize: "10",
            },
            axisLabel: {
              interval: 0,
              fontSize: "10",
              fontFamily: "微软雅黑",
            },
            data: [
              "评论",
              "国内",
              "教育",
              "娱乐",
              "经济",
              "政府",
              "历史",
              "军事",
              "其他",
              "社会",
              "体育",
              "世界",
            ],

            axisTick: {
              alignWithLabel: true,
            },
          },
        ],
        series: [
          {
            name: date,
            type: "bar",
            data: Object.values(data1),
            // name: '直接访问',
            // type: 'bar',
            barWidth: "60%",
            // data: [10, 52, 200, 334, 390, 330, 220]
          },
        ],
      };
      var option = {
        // color:['#E47470','#7EBF50','#589EF8'],
        // color:['rgb(210,100,93)','rgb(228,116,79)','rgb(242,176,110)','rgb(249,224,150)','rgb(255,254,198)','rgb(233,244,163)','rgb(181,219,169)','rgb(156,218,174)','rgb(125,191,166)','rgb(93,178,155)','rgb(74,134,183)','rgb(125,169,185)'],
        color: [
          "rgb(227,158,156)",
          "rgb(224,108,146)",
          "rgb(197,151,212)",
          "rgb(175,159,215)",
          "rgb(160,169,214)",
          "rgb(233,244,163)",
          "rgb(181,219,169)",
          "rgb(156,218,174)",
          "rgb(125,191,166)",
          "rgb(93,178,155)",
          "rgb(74,144,173)",
          "rgb(126,180,225)",
        ].reverse(),
        // tooltip: {
        //     trigger: 'axis',
        //     axisPointer: {
        //         type: 'shadow'
        //     }
        // },
        title: {
          text: "今日主题分布图",
          textAlign: "center",
          left: "50%", //各个方向的内边距，默认是5，可以自行设置
        },
        dataset: {
          source: this.source,
        },
        // grid:{
        //     top:'10%',
        //     // left:'5%',
        //     right:'0%',
        //     bottom:'10%',
        //     // containLabel:true
        // },
        legend: {
          data: this.source[0],
          // data: [
          //     {
          //         name: '今日',
          //         icon: '',
          //         textStyle: {
          //           fontSize:15,
          //           // color: 'red',  // 单独设置某一个图列的颜色
          //           // backgroundColor: '#fff' // 单独设置某一个图列的字体背景色
          //         }
          //     },
          //     {
          //         name: '近三日',
          //         icon: '',
          //         textStyle: {
          //           fontSize:15,
          //           // color: 'red',  // 单独设置某一个图列的颜色
          //           // backgroundColor: '#fff' // 单独设置某一个图列的字体背景色
          //         }
          //     },
          //     {
          //         name: '近七日',
          //         icon: '',
          //         textStyle: {
          //           fontSize:15,
          //           // color: 'red',  // 单独设置某一个图列的颜色
          //           // backgroundColor: '#fff' // 单独设置某一个图列的字体背景色
          //         }
          //     },
          // ],
          // textStyle: {
          //
          //     fontSize:15
          // },
          // right: 100,
        },

        yAxis: {
          type: "category",
          name: "主题",
          nameTextStyle: {
            fontSize: "10",
          },
          axisLabel: {
            interval: 0,
            fontSize: "10",
            fontFamily: "微软雅黑",
          },
          data: [
            "评论",
            "国内",
            "教育",
            "娱乐",
            "经济",
            "政府",
            "历史",
            "军事",
            "其他",
            "社会",
            "体育",
            "世界",
          ],
        },
        xAxis: {
          type: "value",
          name: "数量",
          nameTextStyle: {
            fontSize: "10",
          },
          axisLabel: {
            fontSize: "10",
            fontFamily: "微软雅黑",
            marginTop: "35px",
            show: true,
          },
        },
        series: [
          {
            name: date,
            type: "bar",
            data: Object.values(data1),
          },
        ],
      };
      // this.chart.on('updateAxisPointer', function (event) {
      //     var xAxisInfo = event.axesInfo[0];
      //     if (xAxisInfo) {
      //         var dimension = xAxisInfo.value + 1;
      //         this.chart.setOption({
      //             series: {
      //                 id: 'pie',
      //                 label: {
      //                     formatter: '{b}: {@[' + dimension + ']} ({d}%)'
      //                 },
      //                 encode: {
      //                     value: dimension,
      //                     tooltip: dimension
      //                 }
      //             }
      //         });
      //     }
      // });
      this.chart.setOption(option1);
      // window.addEventListener("resize", function() {
      //   this.chart.resize()
      // })
      // setTimeout(function () {
      //     var width = $('#aside').width();
      //     if(width=='100'|| width=='60'){ //一定要加定时器，然后判断宽度是展开或者收起的时候再去调用echarts提供的resize()方法
      //         this.chart.resize();
      //     }
      //  },200);
      window.addEventListener("resize", function () {
        this.chart.resize();
      });
    },
    //获取近七日日期 step_1
    getBeforeDate(n) {
      var n = n;
      var d = new Date();
      var year = d.getFullYear();
      var mon = d.getMonth() + 1;
      var day = d.getDate();
      if (day >= n) {
        if (mon > 1) {
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
      var s = (mon < 10 ? "0" + mon : mon) + "-" + (day < 10 ? "0" + day : day);
      return s;
    },
    //获取近七日日期 step_2
    getDay() {
      for (var i = 0; i > -7; i--) {
        this.one_week_time.push(this.getBeforeDate(i));
      }
    },
    //近七日主题新闻每日增长数
    drawTrend(id, date_arr, news_info) {
      // 基于准备好的dom，初始化echarts实例
      this.chart = echarts.init(document.getElementById(id));
      // 指定图表的配置项和数据
      var option = {
        // color : ['#7db5e2', '#81cacc', '#cca8ba', "#7EBF50", "#82a0c5", '#fddb7e', '#bda29a', '#d2a59a', '#7f9979', '#c4ccd3','#5F9EA0','#a498d6'],
        color: [
          "rgb(210,100,93)",
          "rgb(228,116,79)",
          "rgb(242,176,110)",
          "rgb(249,224,150)",
          "rgb(255,254,198)",
          "rgb(233,244,163)",
          "rgb(181,219,169)",
          "rgb(156,218,174)",
          "rgb(125,191,166)",
          "rgb(93,178,155)",
          "rgb(74,134,183)",
          "rgb(125,169,185)",
        ].reverse(),
        // color:['rgb(215,121,118)','rgb(224,108,146)','rgb(175,110,195)','rgb(249,224,150)','rgb(255,254,198)','rgb(233,244,163)','rgb(181,219,169)','rgb(156,218,174)','rgb(125,191,166)','rgb(93,178,155)','rgb(74,134,183)','rgb(125,169,185)'].reverse(),
        // color:['rgb(227,158,156)','rgb(224,108,146)','rgb(197,151,212)','rgb(175,159,215)','rgb(160,169,214)','rgb(233,244,163)','rgb(181,219,169)','rgb(156,218,174)','rgb(125,191,166)','rgb(93,178,155)','rgb(74,144,173)','rgb(126,180,225)'].reverse(),
        // color:['#DC143C','#FFB6C1','#BA55D3','#483D8B','#1E90FF','#5F9EA0','#90EE90','#556B2F','#808000','#FFD700','#FFA500','#8B4513'],
        //标题
        tooltip: {
          trigger: "item",
          axisPointer: {
            // 坐标轴指示器，坐标轴触发有效
            type: "shadow", // 默认为直线，可选为：'line' | 'shadow'
          },
          formatter: function (params, ticket, callback) {
            var res =
              params.name +
              "</br>" +
              params.marker +
              params.seriesName +
              " : " +
              Math.abs(params.value);
            return res;
            // console.log(params)
            // var res = params[0].name ;
            //
            // for (var i = 0, l = params.length; i < l; i++) {
            //     res += '<br/>' + params[i].marker+params[i].seriesName + ' : ' + Math.abs(params[i].value) ;
            //
            // }
            // setTimeout(function () {
            //     // 仅为了模拟异步回调
            //     callback(ticket, res);
            // }, 10)
            // return res;
          },
        },
        grid: {
          top: "10%",
          left: "3%",
          right: "12%",
          bottom: "3%",
          containLabel: true,
        },
        //工具箱
        //保存图片
        toolbox: {
          show: true,
          feature: {
            saveAsImage: {
              show: true,
            },
          },
        },
        //图例-每一条数据的名字叫销量
        legend: {
          data: this.name,
          textStyle: {
            //legend字体颜色
          },
          orient: "vertical",
          right: "-0%",
          top: "8%",
          bottom: 20,
        },
        //x轴没有显式设置，根据值自动生成x轴
        xAxis: {
          type: "value",
          name: "增长数量",
          nameTextStyle: {
            fontSize: "15",
            padding: 10,
          },
          axisLabel: {
            formatter: function (value) {
              return Math.abs(value);
            },
            fontSize: "15",
            fontFamily: "微软雅黑",
            marginTop: "35px",
            show: true,
          },
        },
        //y轴
        yAxis: {
          type: "category",
          name: "日期",
          nameTextStyle: {
            fontSize: "15",
          },
          data: date_arr,
          axisLabel: {
            fontSize: "15",
            fontFamily: "微软雅黑",
            marginTop: "35px",
            show: true,
          },
        },

        //数据-data是最终要显示的数据

        /*  [+] Here I need Initial the series arr */
        series: news_info,
      };
      this.chart.setOption(option);
      // window.addEventListener("resize", () => {
      //     this.chart.resize();
      // });
      window.onresize = () => {
        this.chart.resize();
        // this.percentCharts.resize();
      };
    },
    //动态柱状图
    drawDTrend(id, date_arr, news_info) {
      this.chart = echarts.init(document.getElementById(id));
      function dataFormat(obj) {
        // console.log("data formatter suc22:",obj)
        var pList = [
          "国内",
          "世界",
          "体育",
          "社会",
          "历史",
          "娱乐",
          "军事",
          "政府",
          "教育",
          "经济",
          "评论",
          "其他",
        ];
        // console.log("pList:",pList)
        var day = date_arr;
        console.log("day:", day);
        let temp;
        for (var i = 0; i <= 6; i++) {
          var index = day[i];
          temp = obj[index];
          for (var j = 0, l = temp.length; j < l; j++)
            obj[index][j] = {
              name: pList[j],
              value: temp[j],
            };
        }
        return obj;
      }
      console.log("data formatter suc11:", news_info);
      var tempdataTrend = {};
      tempdataTrend = dataFormat(news_info);
      // console.log("data formatter suc22:",tempdataTrend)

      // console.log(this.dataTrend)
      var option = {
        baseOption: {
          color: [
            "rgb(210,100,93)",
            "rgb(228,116,79)",
            "rgb(242,176,110)",
            "#F9CC64",
            "#ffe064",
            "rgb(233,244,163)",
            "rgb(181,219,169)",
            "rgb(156,218,174)",
            "rgb(125,191,166)",
            "rgb(93,178,155)",
            "rgb(74,134,183)",
            "rgb(125,169,185)",
          ].reverse(),
          timeline: {
            axisType: "category",
            // realtime: false,
            // loop: false,
            autoPlay: true,
            // currentIndex: 2,
            playInterval: 1000,
            // controlStyle: {
            //     position: 'left'
            // },
            data: date_arr,
            label: {},
          },
          title: {
            subtext: "数据更新于：" + date_arr[6],
            left: "center",
          },
          tooltip: {},
          // legend: {
          //     left: '50%',
          //     data: ['主题'],
          //     // selected: {
          //     //     'GDP': true, '金融': false, '房地产': false,'第一产业': false, '第二产业': false, '第三产业': false
          //     // }
          // },
          calculable: true,
          grid: {
            x: 90,
            y: 80,
            x2: 60,
            y2: 100,
            tooltip: {
              trigger: "axis",
              axisPointer: {
                type: "shadow",
                label: {
                  show: true,
                  formatter: function (params) {
                    return params.value.replace("\n", "");
                  },
                },
              },
            },
          },
          xAxis: [
            {
              type: "category",
              axisLabel: { interval: 0 },
              data: this.name,
              splitLine: { show: true },
            },
          ],
          yAxis: [
            {
              type: "value",
              name: "增长数量（条）",
            },
          ],
          series: [
            { name: "主题", type: "bar" },
            {
              name: "Trend占比",
              type: "pie",
              center: ["85%", "19%"],
              radius: "28%",
              z: 100,
            },
          ],
        },
        options: [
          {
            title: { text: date_arr[0] + "各个主题增长" },
            series: [
              { data: tempdataTrend[date_arr[0]] },
              {
                data: tempdataTrend[date_arr[0]],
              },
            ],
          },
          {
            title: { text: date_arr[1] + "各个主题增长" },
            series: [
              { data: tempdataTrend[date_arr[1]] },
              { data: tempdataTrend[date_arr[1]] },
            ],
          },
          {
            title: { text: date_arr[2] + "各个主题增长" },
            series: [
              { data: tempdataTrend[date_arr[2]] },
              { data: tempdataTrend[date_arr[2]] },
            ],
          },
          {
            title: { text: date_arr[3] + "各个主题增长" },
            series: [
              { data: tempdataTrend[date_arr[3]] },
              { data: tempdataTrend[date_arr[3]] },
            ],
          },
          {
            title: { text: date_arr[4] + "各个主题增长" },
            series: [
              { data: tempdataTrend[date_arr[4]] },
              { data: tempdataTrend[date_arr[4]] },
            ],
          },
          {
            title: { text: date_arr[5] + "各个主题增长" },
            series: [
              { data: tempdataTrend[date_arr[5]] },
              { data: tempdataTrend[date_arr[6]] },
            ],
          },
          {
            title: { text: date_arr[6] + "各个主题增长" },
            series: [
              { data: tempdataTrend[date_arr[6]] },
              { data: tempdataTrend[date_arr[6]] },
            ],
          },
        ],
      };
      this.chart.setOption(option);
      // window.addEventListener("resize", () => {
      //     this.chart.resize();
      // });
      window.onresize = () => {
        this.chart.resize();
        // this.percentCharts.resize();
      };
    },

    init() {
      const self = this; //因为箭头函数会改变this指向，指向windows。所以先把this保存
      setTimeout(() => {
        window.addEventListener("resize", function () {
          self.chart = self.$echarts.init(self.$refs.Echart);
          self.chart.resize();
        });
      }, 10);
    },
  },
};
</script>

<style scoped type="text/css">
@import url("//unpkg.com/element-ui@2.13.2/lib/theme-chalk/index.css");
@import "../../assets/css/icon.css";

.el-header,
.el-footer {
  font-size: 20px;
  color: black;
  text-align: center;
  line-height: 30px;
}
.res-textarea/deep/ {
  color: black;
  margin-top: 30px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.12), 0 0 6px rgba(0, 0, 0, 0.04);
}
.el-card/deep/ {
  box-shadow: 0 8px 12px 0 rgba(0, 0, 0, 0.1);
}
.el-table/deep/.tableStyle/deep/ {
  background-color: #1989fa !important;
  color: #fff;
  font-weight: 300;
}
.buttonText {
  color: #303133;
  text-align: left;
}
/*.clearfix{*/
/*display: flex;*/
/*justify-content: center;*/
/*align:middle;*/
/*}*/
.wrap {
  display: flex;
  height: 100%;
  justify-content: center;
  align: middle;
}
a:link {
  color: #000000;
} /* 未访问链接*/
a:visited {
  color: #000000;
} /* 已访问链接 */
a:hover {
  color: #589ef8;
} /* 鼠标移动到链接上 */
a:active {
  color: #589ef8;
} /* 鼠标点击时 */
.chartsClass {
  padding-left: 1.2rem;
}
</style>

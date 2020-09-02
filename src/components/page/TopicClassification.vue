<template>
  <div>
    <el-container>
      <el-header>
        <h1 style="color: gray;text-align: center">文本主题分类</h1>
      </el-header>

      <el-main style="text-align: center">
        <el-row v-if="false">
          <el-link type="primary" @click="openTips">使用帮助</el-link>
        </el-row>

        <el-row style="margin:10px 0">
          <el-carousel :interval="4000" type="card" height="200px" :loop="false">
            <el-carousel-item v-for="(news, index) in newslist" :key="index">
              <el-card :body-style="{ padding: '5px'}">
                {{news.kind}}
                <el-table
                  :show-header="false"
                  :data="news.newslist.slice(0,4)"
                  style="height:180px;max-height:180px;margin-top:5px"
                >
                  <el-table-column align="left" :show-overflow-tooltip="true">
                    <template slot-scope="scope">
                      <div>{{scope.row}}</div>
                    </template>
                  </el-table-column>
                </el-table>
              </el-card>
            </el-carousel-item>
          </el-carousel>
        </el-row>

        <el-row style="margin:20px 0">
          <el-input
            type="textarea"
            placeholder="请输入内容"
            v-model="content"
            maxlength="800"
            show-word-limit
            :rows="6"
            clearable
            style="box-shadow: 0 2px 4px rgba(0, 0, 0, .12), 0 0 6px rgba(0, 0, 0, .04)"
          />
        </el-row>

        <el-row style="margin: 20px 0">
          <el-button class="editor-btn" type="primary" @click="submit">开始主题分类</el-button>
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
                  size="small"
                  :key="type"
                  v-if="form.type.indexOf(type)>=0"
                  @click="onClick(type)"
                >{{type}}</el-button>
                <el-button type="info" size="medium" :key="type" v-else disabled>{{type}}</el-button>
              </template>
            </el-button-group>
          </el-card>
        </el-row>

        <el-row style="margin-top:30px">
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

export default {
  name: "markdown",
  data: function () {
    return {
      queryURL: "http://61.135.242.193:5000/api/summarization",
      form: {
        type: [],
      },
      content: "",
      editorOption: {
        placeholder: "请在这里输入待分类的文本",
      },
      types: typelist,
      cnt: [120, 200, 150, 80, 70, 110, 130, 602, 23, 256, 445, 56, 92, 13],
      colorSt: {
        "background-color": "#99a9bf",
      },
      newslist: [
        {
          newslist: ["鹿晗关晓彤结婚", "鹿晗关晓彤结婚2", "鹿晗关晓彤结婚3"],
          kind: "娱乐",
        },
        {
          newslist: [
            "今天是国庆节",
            "今天是国庆节2",
            "今天是国庆节3",
            "今天是国庆节4",
            "今天是国庆节5",
            "今天是国庆节6",
            "今天是国庆节7",
          ],
          kind: "生活",
        },
        {
          newslist: [
            "今天是国庆节",
            "今天是国庆节2",
            "今天是国庆节3",
            "今天是国庆节4",
          ],
          kind: "节日",
        },
      ],
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
          data: typelist,
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

      for (var i = 0; i < typelist.length; i++) {
        seriesData.push({ name: typelist[i], value: this.cnt[i] });
        selected[typelist[i]] = true;
      }
      var dataset = {
        legendData: typelist,
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
    openTips() {
      this.$alert(
        "在下方文本框中输入待分类的文本，点击提交后文本的分类结果将在下方“文本类型”后以颜色改变的形式展示。",
        "文本主题分类使用方法",
        {
          confirmButtonText: "确定",
          callback: (action) => {
            /*this.$message({
                    type: 'info',
                    message: `action: ${ action }`
                    });*/
          },
        }
      );
    },
    onClick(value) {
      alert("你点击了 " + value);
    },
    onEditorChange({ editor, html, text }) {
      this.content = html;
    },
    submit() {
      // this.summaryRes = this.summaryText
      fetch(this.queryURL, {
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
        .then((response) => (this.summaryRes = response.data[0].summary));

      console.log(this.content);
      this.form.type = ["娱乐", "教育"];
      this.$message.success("提交成功！");
    },
  },
  mounted() {
    this.drawBarChart();
    this.drawPieChart();
  },
};
</script>
<style scoped>
.editor-btn {
  margin-top: 20px;
}
.el-carousel__item h3 {
  color: #475669;
  font-size: 14px;
  opacity: 0.75;
  line-height: 200px;
  margin: 0;
}
/*
.el-carousel__item:nth-child(2n){
  background-color: #99a9bf;
}
.el-carousel__item:nth-child(2n + 1){
  background-color: #d3dce6;
}*/
</style>
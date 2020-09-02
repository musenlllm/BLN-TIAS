<template>
  <div>
    <el-container>
      <el-header>
        <h1 style="color: gray">关系抽取</h1>
      </el-header>
      <el-main style="text-align: center">
        <el-row style="margin: 10px 0">
          <el-input
            type="textarea"
            placeholder="请输入内容"
            v-model="content"
            maxlength="80"
            show-word-limit
            :rows="6"
            clearable
            style="box-shadow: 0 2px 4px rgba(0, 0, 0, .12), 0 0 6px rgba(0, 0, 0, .04)"
          ></el-input>
        </el-row>

        <el-row style="margin:20px 0; display: flex; justify-content: center">
          <el-button v-on:click="getData" type="primary">开始提取</el-button>
        </el-row>

        <el-row style="margin:20px 0">
          <el-col :span="16">
            <el-card>
              <div slot="header" class="clearfix">
                <span>人物关系图</span>
              </div>
              <div id="showRelation" :style="{width: '1200px', height: '540px'}"></div>
            </el-card>
          </el-col>

          <el-col :span="8" style="padding-left:24px">
            <el-card>
              <div slot="header" class="clearfix">
                <span>人物关系列表</span>
              </div>

              <el-table
                :show-header="true"
                :data="items"
                style="height: 540px;max-height: 540px;overflow: auto"
              >
                <el-table-column prop="person1" align="center" label="人物1"></el-table-column>
                <el-table-column prop="relation" label="关系" align="center" width="50"></el-table-column>
                <el-table-column prop="person2" align="center" label="人物2"></el-table-column>
              </el-table>
            </el-card>
          </el-col>
        </el-row>
      </el-main>
      <!--<el-footer>Footer</el-footer>-->
    </el-container>
  </div>
</template>

<script>
import { fetchData } from "../../api/index";
import echarts from "echarts/lib/echarts";
import "echarts/dist/extension/dataTool";

export default {
  name: "basetable",
  data() {
    return {
      text: "",
      content: "",
      queryURL: "http://61.135.242.193:5000/api/summarization",

      items: [
        // { type: '', label: '标签一' },
        // { type: 'success', label: '标签二' },
        { person1: "曹操", person2: "曹丕", relation: "父子", id: "1" },
        { person1: "曹操", person2: "曹植", relation: "父子", id: "2" },
        { person1: "曹丕", person2: "曹植", relation: "兄弟", id: "3" },
        { person1: "曹操", person2: "曹丕", relation: "父子", id: "4" },
        { person1: "曹操", person2: "曹植", relation: "父子", id: "5" },
        { person1: "曹丕", person2: "曹植", relation: "兄弟", id: "6" },
        { person1: "曹操", person2: "曹丕", relation: "父子", id: "7" },
        { person1: "曹操", person2: "曹植", relation: "父子", id: "8" },
        { person1: "曹丕", person2: "曹植", relation: "兄弟", id: "9" },
        { person1: "曹操", person2: "曹丕", relation: "父子", id: "10" },
        { person1: "曹操", person2: "曹植", relation: "父子", id: "11" },
        { person1: "曹丕", person2: "曹植", relation: "兄弟", id: "12" },
        { person1: "曹操", person2: "曹丕", relation: "父子", id: "13" },
        { person1: "曹操", person2: "曹植", relation: "父子", id: "14" },
        { person1: "曹丕", person2: "曹植", relation: "兄弟", id: "15" },
        { person1: "曹操", person2: "曹丕", relation: "父子", id: "16" },
        { person1: "曹操", person2: "曹植", relation: "父子", id: "17" },
        { person1: "曹丕", person2: "曹植", relation: "兄弟", id: "18" },
      ],
    };
  },
  created() {
    // this.getData();
  },
  methods: {
    drawChart() {
      // 初始化echarts实例
      let myChart = echarts.init(document.getElementById("showRelation"));
      var theData = {
        nodes: [
          {
            name: "曹丕", //	彰显节点
            x: 30,
            y: 30,
            category: 1,
            label: {
              show: true,
            },
          },
          {
            name: "曹操2", //	被覆盖节点
            x: 80,
            y: 30,
            symbolSize: 100,
            color: "blue",
            category: 2,
            label: {
              show: false,
            },
          },
          {
            name: "曹操",
            x: 80,
            y: 30,
            symbolSize: 100,
            category: 2,
            color: "blue",
          },
          {
            name: "曹植",
            x: 40,
            y: 40,
            category: 3,
          },
        ],
        links: [
          {
            source: 1,
            target: 0,
            value: "父子",
            lineStyle: {
              width: 1,
              curveness: 0.1,
            },
          },
          {
            source: 1,
            target: 0,
            value: "父子",
            lineStyle: {
              width: 1,
              curveness: 0.2,
            },
          },
          {
            source: 0,
            target: 3,
            value: "兄弟",
            lineStyle: {
              width: 1,
            },
          },
          {
            source: 1,
            target: 3,
            value: "父子",
            lineStyle: {
              width: 1,
            },
          },
        ],
      };

      var categories = [];
      for (var i = 0; i < 9; i++) {
        categories[i] = {
          name: "类目" + i,
        };
      }

      // 绘制图表
      var option = {
        grid: {
          left: "10%",
          right: "10%",
        },
        series: [
          {
            type: "graph",
            layout: "none",
            symbolSize: 60,
            label: {
              show: true,
              fontSize: 26,
            },
            roam: true,
            categories: categories,
            itemStyle: {
              borderColor: "#fff",
              borderWidth: 1,
              shadowBlur: 10,
              shadowColor: "rgba(0, 0, 0, 0.3)",
            },
            lineStyle: {
              color: "source",
              curveness: 0.3,
            },
            edgeSymbol: ["", "arrow"],
            edgeLabel: {
              // 连接两个关系对象的线上的标签
              normal: {
                show: true,
                textStyle: {
                  fontSize: 18,
                },
                formatter: function (param) {
                  // 关系标签内容
                  return param.data.value;
                },
              },
            },
            data: theData.nodes,
            links: theData.links,
          },
        ],
      };
      //防止越界，重绘canvas
      window.onresize = myChart.resize;
      myChart.setOption(option); //设置option
    },
    // 获取 easy-mock 的模拟数据
    getData() {
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
        .then((response) => console.log(response.data[0].summary));
    },
  },

  mounted() {
    this.drawChart();
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

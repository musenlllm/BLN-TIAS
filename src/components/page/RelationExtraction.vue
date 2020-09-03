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
            placeholder="红楼梦中贾政的五个孩子分别是贾珠、贾元春、贾宝玉、贾探春以及贾环。"
            v-model="content"
            maxlength="80"
            show-word-limit
            :rows="6"
            clearable
            style="box-shadow: 0 2px 4px rgba(0, 0, 0, .12), 0 0 6px rgba(0, 0, 0, .04)"
          ></el-input>
        </el-row>

        <el-row style="margin-top: 30px">
          <el-button @click="getData" type="primary" style="background: #242f42; border: 0px">开始提取</el-button>
          <el-button>随机样例</el-button>
        </el-row>

        <el-row style="margin:20px 0">
          <el-col :span="16">
            <el-card>
              <div slot="header" class="clearfix">
                <span>人物关系图</span>
              </div>
              <el-row>
                <div id="showRelation" :style="{width: '100%', height: '540px'}"></div>
              </el-row>
              <el-row>
                <div id="showRelation2" :style="{width: '100%', height: '540px'}"></div>
              </el-row>
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
                style="height: 1080px;max-height: 1080px;overflow: auto"
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

const typelist = [
  "夫妻",
  "亲子",
  "兄弟姐妹",
  "上下级",
  "师生",
  "好友",
  "同学",
  "合作",
  "同人",
  "情侣",
  "祖孙",
  "同门",
  "亲戚",
];

function getPersonList(links) {
  var personList = [];
  var personDict = {};
  for (var i = 0; i < links.length; ++i) {
    if (personList.indexOf(links[i].person1) < 0) {
      personList.push(links[i].person1);
      personDict[links[i].person1] = 1;
    } else {
      personDict[links[i].person1] += 1;
    }
    if (personList.indexOf(links[i].person2) < 0) {
      personList.push(links[i].person2);
      personDict[links[i].person2] = 1;
    } else {
      personDict[links[i].person2] += 1;
    }
  }
  return [personList, personDict];
}

function shuffle(arr) {
  for (let i = arr.length - 1; i >= 0; i--) {
    let rIndex = Math.floor(Math.random() * (i + 1));
    // 打印交换值
    // console.log(i, rIndex);
    let temp = arr[rIndex];
    arr[rIndex] = arr[i];
    arr[i] = temp;
  }
  return arr;
}

export default {
  name: "basetable",
  data() {
    return {
      content: "",
      queryURL: "http://61.135.242.193:5000/api/summarization",
      items: [
        { person1: "贾政", person2: "贾珠", relation: "亲子" },
        { person1: "贾政", person2: "贾元春", relation: "亲子" },
        { person1: "贾政", person2: "贾宝玉", relation: "亲子" },
        { person1: "贾政", person2: "贾探春", relation: "亲子" },
        { person1: "贾政", person2: "贾环", relation: "亲子" },
        { person1: "贾珠", person2: "贾元春", relation: "兄弟姐妹" },
        { person1: "贾珠", person2: "贾宝玉", relation: "兄弟姐妹" },
        { person1: "贾珠", person2: "贾探春", relation: "兄弟姐妹" },
        { person1: "贾珠", person2: "贾环", relation: "兄弟姐妹" },
        { person1: "贾元春", person2: "贾宝玉", relation: "兄弟姐妹" },
        { person1: "贾元春", person2: "贾探春", relation: "兄弟姐妹" },
        { person1: "贾元春", person2: "贾环", relation: "兄弟姐妹" },
        { person1: "贾宝玉", person2: "贾探春", relation: "兄弟姐妹" },
        { person1: "贾宝玉", person2: "贾环", relation: "兄弟姐妹" },
        { person1: "贾探春", person2: "贾环", relation: "兄弟姐妹" },
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

      var restmp = getPersonList(this.items);
      var personList = restmp[0];
      var personDict = restmp[1];

      var theData = getChartIndex(this.items);
      var categories = [];
      for (var i = 0; i < 8; i++) {
        categories[i] = {
          name: "类目" + i,
        };
      }

      // 绘制图表
      var option = {
        grid: {
          left: "10%",
          right: "10%",
          top: "10%",
          bottom: "10%",
        },
        series: [
          {
            type: "graph",
            layout: "none",
            symbolSize: 60,
            label: {
              show: true,
              fontSize: 16,
            },
            roam: false,
            //categories: categories,
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
                  fontSize: 14,
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
      myChart.setOption(option);

      function getChartIndex(items) {
        var resData = { nodes: [], links: [] };
        let personNum = personList.length;
        var a = 0;
        console.log(personNum);
        console.log(personList);
        personList.forEach(function (p) {
          console.log("a: " + a);
          resData.nodes.push({
            name: p, //	彰显节点
            x: 10 * Math.cos((a * Math.PI) / 180),
            y: 10 * Math.sin((a * Math.PI) / 180),
            category: 1,
            label: {
              show: true,
            },
            symbolSize: p.length * 20 + 6,
          });
          a += 360 / personNum;
        });
        console.log(resData.nodes);
        items.forEach(function (item) {
          resData.links.push({
            source: personList.indexOf(item.person1),
            target: personList.indexOf(item.person2),
            value: item.relation,
            lineStyle: {
              width: 1,
            },
          });
        });
        return resData;
      }
    },
    drawChart2() {
      // 初始化echarts实例
      let myChart = echarts.init(document.getElementById("showRelation2"));

      var restmp = getPersonList(this.items);
      var personList = restmp[0];
      var personDict = restmp[1];
      restmp = getCircular(personList, personDict);
      
      var nodelist = restmp[0];
      var nodedict = restmp[1];
      nodedict = shuffle(nodedict);
      var i = 0;
      nodelist.forEach(function (node) {
        node.label = {
          normal: {
            show: node.symbolSize > 0,
          },
        };
        var val_ = 0;
        if (personDict[nodedict[i]]) {
          val_ = personDict[nodedict[i]];
        }
        node.name = nodedict[i];
        node.tooltip = {
          formatter: personDict[nodedict[i]]
            ? nodedict[i] + " : " + val_
            : "关系 : " + nodedict[i],
        };
        node.category =
          typelist.indexOf(nodedict[i]) < 0
            ? typelist.length
            : typelist.indexOf(nodedict[i]);
        node.symbolSize = 20 + 5 * val_; //10 * Math.log(10 + val_);
        i++;
      });

      var linklist = [];
      var personRelationLabel = {};
      this.items.forEach(function (item) {
        if (personRelationLabel[item.person1 + "-" + item.relation]) {
          personRelationLabel[item.person1 + "-" + item.relation] =
            personRelationLabel[item.person1 + "-" + item.relation] +
            "<br>" +
            item.person1 +
            "-" +
            item.relation +
            "-" +
            item.person2;
        } else {
          personRelationLabel[item.person1 + "-" + item.relation] =
            item.person1 + "-" + item.relation + "-" + item.person2;
        }

        if (personRelationLabel[item.person2 + "-" + item.relation]) {
          personRelationLabel[item.person2 + "-" + item.relation] =
            personRelationLabel[item.person2 + "-" + item.relation] +
            "<br>" +
            item.person1 +
            "-" +
            item.relation +
            "-" +
            item.person2;
        } else {
          personRelationLabel[item.person2 + "-" + item.relation] =
            item.person1 + "-" + item.relation + "-" + item.person2;
        }
      });

      var id = 0;
      this.items.forEach(function (item) {
        id++;
        linklist.push({
          source: nodedict.indexOf(item.person1),
          target: nodedict.indexOf(item.relation),
          id: id,
          tooltip: {
            formatter: personRelationLabel[item.person1 + "-" + item.relation],
          },
        });
        id++;
        linklist.push({
          target: nodedict.indexOf(item.person2),
          source: nodedict.indexOf(item.relation),
          id: id,
          tooltip: {
            formatter: personRelationLabel[item.person2 + "-" + item.relation],
          },
        });
      });

      var categories = [];
      for (var i = 0; i < typelist.length; i++) {
        categories[i] = {
          name: typelist[i],
        };
      }
      categories[typelist.length] = {
        name: "人物",
      };

      // 绘制图表
      var option = {
        grid: {
          left: "10%",
          right: "10%",
          top: "10%",
          bottom: "10%",
        },
        legend: [
          {
            data: categories.map(function (a) {
              return a.name;
            }),
          },
        ],
        tooltip: {},
        animationDurationUpdate: 1500,
        animationEasingUpdate: "quinticInOut",
        series: [
          {
            name: "Les Miserables",
            type: "graph",
            layout: "circular",
            circular: {
              rotateLabel: true,
            },
            data: nodelist,
            links: linklist,
            categories: categories,
            roam: false,
            label: {
              position: "right",
              formatter: "{b}",
            },
            lineStyle: {
              color: "source",
              curveness: 0.3,
            },
            emphasis: {
                lineStyle: {
                    width: 10
                }
            }
          },
        ],
      };
      //防止越界，重绘canvas
      window.onresize = myChart.resize;
      myChart.setOption(option);

      function getCircular(personList, personDict) {
        var nodeNum = typelist.length + personList.length;
        var nodelist = [
          {
            id: 0,
            x: 0,
            y: 100,
            value: 10,
            category: 0,
            name: typelist[0],
            symbolSize: 10,
          },
        ];
        var nodedict = [typelist[0]];

        var a = 0;
        for (var i = 1; i < nodeNum; i++) {
          a += 360 / nodeNum; // Math.sin(2*Math.PI / 360)
          var val_ = 10;
          var category = typelist.length;
          var name;
          if (i < typelist.length) {
            name = typelist[i];
            nodedict.push(name);
            category = i;
          } else {
            name = personList[i - typelist.length];
            nodedict.push(name);
          }
          nodelist.push({
            id: i,
            x: 60 * Math.sin((a * Math.PI) / 180),
            y: 60 * Math.cos((a * Math.PI) / 180),
            value: val_,
            category: category,
            name: name,
            symbolSize: val_,
          });
        }
        return [nodelist, nodedict];
      }
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
    this.drawChart2();
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
